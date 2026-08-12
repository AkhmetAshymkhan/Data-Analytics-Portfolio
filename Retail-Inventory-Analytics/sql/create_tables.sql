CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    purchase_price NUMERIC(12, 2),
    sale_price NUMERIC(12, 2),
    stock INTEGER
);

CREATE TABLE sales (
    product_id INTEGER NOT NULL,
    month TEXT NOT NULL,
    units_sold INTEGER,
    profit NUMERIC(12, 2),
    abc_class CHAR(1),
    xyz_class CHAR(1),
    PRIMARY KEY (product_id, month),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
