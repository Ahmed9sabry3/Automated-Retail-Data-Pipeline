-- SELECT
--       "Store" AS store_id,
--        "Date" AS sales_date,
--         "Weekly_Sales" AS weekly_sales,
--         CASE WHEN "Holiday_Flag" = 1 THEN TRUE ELSE FALSE END AS is_holiday,
--         "Temperature" AS temperature_f,
--         "Fuel_Price" AS fuel_price,
--         "CPI" AS cpi,
--         "Unemployment" AS unemployment_rate
-- FROM {{ source('raw', 'walmart_sales') }}
-- WHERE "Weekly_Sales" > 0

SELECT
    store AS store_id,
    date AS sales_date,
    weekly_sales,
    CASE WHEN holiday_flag = 1 THEN TRUE ELSE FALSE END AS is_holiday,
    temperature AS temperature_f,
    fuel_price,
    cpi,
    unemployment AS unemployment_rate
FROM {{ source('raw', 'walmart_sales') }}
WHERE weekly_sales > 0