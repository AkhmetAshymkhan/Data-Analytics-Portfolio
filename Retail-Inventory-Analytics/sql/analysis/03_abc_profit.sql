SELECT
    abc_class,
    SUM(profit) AS total_profit,
    COUNT(DISTINCT product_id) AS products_count
FROM sales
GROUP BY abc_class
ORDER BY total_profit DESC;