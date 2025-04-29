# Databricks notebook source
# MAGIC %md
# MAGIC ## Return Day number to run piepline weekly

# COMMAND ----------

dbutils.widgets.text("weekday", "1")

# COMMAND ----------

var = dbutils.widgets.get("weekday")
try:
    var = int(var)
except ValueError:
    print(f"Error: The value '{var}' is not a valid integer.")

# COMMAND ----------

dbutils.jobs.taskValues.set(key="weekoutput", value=var)

# COMMAND ----------

