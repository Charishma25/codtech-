
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, avg, count
import matplotlib.pyplot as plt

# Initialize Spark Session
spark = SparkSession.builder.appName("BigDataAnalysis").getOrCreate()

# Load dataset
df = spark.read.csv("data/sales_data.csv", header=True, inferSchema=True)

# Basic Analysis
df.printSchema()
df.show(5)

# Total transaction amount per category
category_sales = df.groupBy("ProductCategory").agg(
    spark_sum("Amount").alias("TotalSales"),
    avg("Amount").alias("AverageSales"),
    count("*").alias("TransactionCount")
)

# Show aggregated data
category_sales.show()

# Collect for visualization
pandas_df = category_sales.toPandas()

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(pandas_df["ProductCategory"], pandas_df["TotalSales"], color='skyblue')
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/sales_by_category.png")
plt.close()

# Stop Spark session
spark.stop()
