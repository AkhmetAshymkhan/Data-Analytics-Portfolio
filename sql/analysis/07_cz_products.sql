-- Low-profit and unstable products

SELECT
    p.product_name,
    p.stock,
    SUM(s.profit) AS total_profit
FROM products p
JOIN sales s
    ON p.product_id = s.product_id
WHERE s.abc_class = 'C'
  AND s.xyz_class = 'Z'
GROUP BY
    p.product_id,
    p.product_name,
    p.stock
ORDER BY total_profit DESC
LIMIT 15;