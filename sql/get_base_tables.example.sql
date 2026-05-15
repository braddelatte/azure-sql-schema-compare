SELECT
    SCHEMA_NAME(t.schema_id) AS schema_name,
    t.name AS table_name
FROM sys.tables t
WHERE t.schema_id = SCHEMA_ID('dbo')
    AND t.is_ms_shipped = 0
ORDER BY t.name;
