-- models/raw_titanic.sql
MODEL (
  name bronze.raw_titanic,
  kind FULL,
  grain id -- We'll create an ID in the SQL
);

-- This loads the raw Titanic dataset from the CSV
WITH raw_data AS (
  SELECT
    -- Generate a unique ID for each passenger
    ROW_NUMBER() OVER () as id,
    -- Parse the original columns
    CAST("Survived" AS INTEGER) AS survived,
    CAST("Pclass" AS INTEGER) AS passenger_class,
    "Name" AS passenger_name,
    "Sex" AS sex,
    CAST("Age" AS DOUBLE) AS age,
    CAST("Siblings/Spouses Aboard" AS INTEGER) AS siblings_spouses_count,
    CAST("Parents/Children Aboard" AS INTEGER) AS parents_children_count,
    CAST("Fare" AS DOUBLE) AS fare
  FROM
    read_csv('https://raw.githubusercontent.com/techascent/tech.ml.dataset/refs/heads/master/test/data/titanic.csv',
             auto_detect=true,
             header=true)
)

SELECT
  id,
  survived,
  passenger_class,
  passenger_name,
  sex,
  age,
  siblings_spouses_count,
  parents_children_count,
  fare,
  -- Add metadata fields
  CURRENT_TIMESTAMP() AS loaded_at
FROM
  raw_data