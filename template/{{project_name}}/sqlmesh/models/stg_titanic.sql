MODEL (
  name staging.stg_titanic,
  kind FULL,
  grain id
)
WITH stg AS (
  SELECT
    -- Generate a unique ID for each passenger
    ROW_NUMBER() OVER () as id,
    -- Parse the original columns
    "Survived" AS survived,
    "Pclass" AS passenger_class,
    "Name" AS passenger_name,
    "Sex" AS sex,
    "Age" AS age,
    "Siblings/Spouses Aboard" AS siblings_spouses_count,
    "Parents/Children Aboard" AS parents_children_count,
    "Fare" AS fare
  FROM
    raw.titanic
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
  stg
