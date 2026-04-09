# =================================================================
# PROJECT: Distributed Data Processing
# DESCRIPTION: Analyzing large datasets with Filtering, Grouping, and Aggregation.
# DELIVERABLE: A Spark Job script demonstrating high-performance analysis.
# =================================================================

# Simulation of PySpark SQL functions
class SparkDataAnalyzer:
    def __init__(self, data):
        self.df = data
        print("⚡ Spark Job Started: Parallel Processing Initialized...")

    def filter_data(self, column, threshold):
        """Simulating df.filter(col > threshold)"""
        print(f"🔍 Filtering: Keeping records where {column} > {threshold}")
        self.df = [row for row in self.df if row[column] > threshold]
        return self

    def group_and_aggregate(self, group_by_col, agg_col):
        """Simulating df.groupBy().agg(sum())"""
        print(f"📊 Aggregating: Grouping by '{group_by_col}' and summing '{agg_col}'")
        summary = {}
        for row in self.df:
            key = row[group_by_col]
            value = row[agg_col]
            summary[key] = summary.get(key, 0) + value
        
        print("\n--- ANALYSIS RESULT (Aggregated Data) ---")
        for category, total in summary.items():
            print(f"Category: {category:10} | Total {agg_col}: {total}")
        return summary

# --- MAIN SPARK JOB ---
if __name__ == "__main__":
    # Simulated Large Dataset (e.g., Sales Data)
    # Fields: TransactionID, Category, Amount
    sales_data = [
        {"id": 1, "category": "Electronics", "amount": 1200},
        {"id": 2, "category": "Furniture", "amount": 500},
        {"id": 3, "category": "Electronics", "amount": 800},
        {"id": 4, "category": "Clothing", "amount": 150},
        {"id": 5, "category": "Electronics", "amount": 2000},
        {"id": 6, "category": "Furniture", "amount": 300},
        {"id": 7, "category": "Clothing", "amount": 400},
    ]

    # Initialize Spark Analyzer
    spark_job = SparkDataAnalyzer(sales_data)

    # 1. Filter: Remove small transactions (less than 400)
    spark_job.filter_data("amount", 400)

    # 2. Group & Aggregate: Total sales per category
    spark_job.group_and_aggregate("category", "amount")

    print("\n✅ Task 14 Complete: Spark Job executed successfully.")
