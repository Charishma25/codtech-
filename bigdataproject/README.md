
# Big Data Analysis - PySpark Project

## Description
This project demonstrates big data analysis using PySpark on a simulated sales transaction dataset containing 500,000 rows.

## Tasks Performed
- Loaded data using PySpark
- Aggregated transaction data by product category
- Visualized total sales per category

## How to Run

1. Ensure you have Python and PySpark installed.
2. Place the dataset in `data/sales_data.csv` (already included).
3. Run the PySpark script:

```bash
spark-submit big_data_analysis.py
```

## Output
A bar chart image will be saved at `output/sales_by_category.png`.
