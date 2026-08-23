import httpx
from mcp.server.fastmcp import FastMCP

API_BASE = "http://127.0.0.1:8000"

mcp = FastMCP("在庫管理MCPサーバ")

@mcp.tool()
def search_products(
    category: str | None = None,
    max_stock: int | None = None,
    min_stock: int | None = None,
):

    """
    在庫管理システムの商品を検索する。
    カテゴリ、在庫数の上限、下限で絞り込める。
    """

    params = {}
    if category:
        params["category"] = category
    if max_stock is not None:
        params["stock_le"] = max_stock
    if min_stock is not None:
        params["stock_ge"] = min_stock

    response = httpx.get(f"{API_BASE}/products/search", params=params)
    return response.text


@mcp.tool()
def update_stock(product_id: int, new_stock: int) -> str:
    """
    在庫管理システムの商品の在庫数を更新する。
    """
    response = httpx.put(
        f"{API_BASE}/products/{product_id}/stock",
        json={"stock": new_stock},
    )
    return response.text

if __name__ == "__main__":
    mcp.run(transport="stdio")