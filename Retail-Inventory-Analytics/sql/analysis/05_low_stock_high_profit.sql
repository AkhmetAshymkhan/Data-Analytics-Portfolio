SELECT
    p.product_name,
    p.stock,
    SUM(s.profit) AS total_profit
FROM products p
JOIN sales s
    ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name, p.stock
HAVING p.stock <= 3
ORDER BY total_profit DESC;
LIMIT 15;