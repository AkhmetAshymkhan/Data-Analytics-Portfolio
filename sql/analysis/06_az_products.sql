SELECT
    p.product_name,
    p.stock,
    s.abc_class,
    s.xyz_class,
    SUM(s.profit) AS total_profit
FROM products p
JOIN sales s
    ON p.product_id = s.product_id
WHERE s.abc_class = 'A'
  AND s.xyz_class = 'Z'
GROUP BY
    p.product_id,
    p.product_name,
    p.stock,
    s.abc_class,
    s.xyz_class
ORDER BY total_profit DESC
LIMIT 15;