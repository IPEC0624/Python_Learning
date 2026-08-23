from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlite3
from typing import Optional

DB_PATH = "inventory.db"
# initialize fastapi
app = FastAPI()

# make connection to database
def get_db():
    conn = sqlite3.connect(DB_PATH)
    # 取得結果は sqlite3.Row という特殊なオブジェクトになります。
    conn.row_factory = sqlite3.Row
    return conn

# can not input lower than 0 by Pydantic(validation)
class StockUpdate(BaseModel):
    stock: int = Field(ge=0)

# endpoint 1
@app.get("/products/search")
def search_products(
    # Optional[... = None]: do not need to input
    #le less than, ge greater than
    category: Optional[str] = None,
    stock_le: Optional[int] = None,
    stock_ge: Optional[int] = None,
):
    # WHERE 1=1: just need to add AND in condition, do not need to use IF
    query = "SELECT * FROM products WHERE 1=1"
    # SQLインジェクション対策（プレースホルダー ? 用）のパラメータを入れるリストです。
    params = []

    # 条件をANDで足していく（SQL） 
    if category is not None:
        query += " AND category = ?"
        params.append(category)
    if stock_le is not None:
        query += " AND stock <= ?"
        params.append(stock_le)
    if stock_ge is not None:
        query += " AND stock >= ?"
        params.append(stock_ge)

    conn = get_db()
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(row) for row in rows]

# endpoint 2
@app.put("/products/{product_id}/stock")
def update_stock(product_id: int, body: StockUpdate):
    conn = get_db()
    result = conn.execute(
        "UPDATE products SET stock = ? WHERE id = ?", (body.stock, product_id)
    )
    if result.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")
    conn.commit()
    conn.close()
    return {"id": product_id, "stock": body.stock}