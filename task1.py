# =================================================================
# PROJECT: Data Cleaning with PySpark
# DESCRIPTION: Handling missing values and duplicates in large datasets.
# DELIVERABLE: Python script showcasing PySpark-based preprocessing.
# =================================================================

# Note: In a real Spark environment, you'd use: from pyspark.sql import SparkSession
# This script simulates the PySpark DataFrame API logic.

class PySparkSimulator:
    def __init__(self, data):
        self.data = data
        print("🚀 SparkSession Initialized. Loading Large Dataset...")

    def show(self, message="Current Data"):
        print(f"\n--- {message} ---")
        for row in self.data:
            print(row)

    def drop_duplicates(self):
        """Simulating df.dropDuplicates()"""
        print("\n✨ Action: Dropping Duplicate Rows...")
        unique_data = []
        for row in self.data:
            if row not in unique_data:
                unique_data.append(row)
        self.data = unique_data
        return self

    def fill_na(self, replacement="Unknown"):
        """Simulating df.fillna()"""
        print(f"\n🛠️ Action: Filling Missing Values (None) with '{replacement}'...")
        for row in self.data:
            for key, value in row.items():
                if value is None:
                    row[key] = replacement
        return self

    def drop_na(self):
        """Simulating df.dropna()"""
        print("\n🗑️ Action: Dropping Rows with Null Values...")
        self.data = [row for row in self.data if None not in row.values()]
        return self

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Sample dataset with duplicates and missing values (Simulating a CSV/Parquet file)
    raw_data = [
        {"id": 101, "name": "Aditya", "city": "Noida"},
        {"id": 102, "name": None, "city": "Delhi"},
        {"id": 101, "name": "Aditya", "city": "Noida"}, # Duplicate
        {"id": 103, "name": "Rahul", "city": None},
        {"id": 104, "name": "Priya", "city": "Mumbai"}
    ]

    # Initialize Simulator
    spark_df = PySparkSimulator(raw_data)
    spark_df.show("Raw Dataset")

    # 1. Handling Duplicates
    spark_df.drop_duplicates()

    # 2. Handling Missing Values (Two approaches)
    # Option A: Filling NULLs
    spark_df.fill_na("Not Provided")
    
    # Final Result
    spark_df.show("Cleaned Dataset (PySpark Processed)")

    print("\n✅ Task 13 Complete: PySpark cleaning pipeline demonstrated.")
