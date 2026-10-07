# Databricks notebook source
# MAGIC %sql
# MAGIC -- Create table
# MAGIC CREATE OR REPLACE TABLE ${var.catalog}.${var.schema}.bakehouse_customers
# MAGIC AS
# MAGIC SELECT * FROM samples.bakehouse.sales_customers

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create MV
# MAGIC CREATE OR REPLACE MATERIALIZED VIEW ${var.catalog}.${var.schema}.agg_orders
# MAGIC TRIGGER ON UPDATE
# MAGIC AS
# MAGIC SELECT
# MAGIC customerID,first_name,last_name,phone_number,city
# MAGIC FROM ${var.catalog}.${var.schema}.bakehouse_customers