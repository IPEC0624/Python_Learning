CREATE TABLE IF NOT EXISTS products (
    id          INTEGER PRIMARY KEY,
    name        TEXT    NOT NULL,
    category    TEXT    NOT NULL,
    stock       INTEGER NOT NULL
);

INSERT INTO products (name, category, stock) VALUES
    ('りんご', '食品', 5),
    ('バナナ', '食品', 32),
    ('ノート', '文具', 8),
    ('ペン', '文具', 3),
    ('牛乳', '飲料', 12);