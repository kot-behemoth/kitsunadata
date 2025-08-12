MODEL (
  name raw.titanic,
  kind SEED (
      path '../seeds/titanic.csv'
  ),
  columns (
      Survived INT,
      Pclass INT,
      Name TEXT,
      Sex TEXT,
      Age INT,
      "Siblings/Spouses Aboard" TEXT,
      "Parents/Children Aboard" TEXT,
      Fare FLOAT
  )
);
