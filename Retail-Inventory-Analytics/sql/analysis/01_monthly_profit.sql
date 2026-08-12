SELECT
    month,
    SUM(profit) AS total_profit
FROM sales
GROUP BY month
ORDER BY
    CASE month
        WHEN 'Апрель' THEN 1
        WHEN 'Май' THEN 2
        WHEN 'Июнь' THEN 3
        WHEN 'Июль' THEN 4
    END;