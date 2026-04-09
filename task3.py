# =================================================================
# PROJECT: Big Data Visualization Dashboard
# DESCRIPTION: Visualizing insights from large datasets (Tableau/Power BI Logic).
# DELIVERABLE: A script showcasing dashboard-style insights and trends.
# =================================================================

class DashboardSimulator:
    def __init__(self, data):
        self.data = data
        print("📊 Connecting to Big Data Source...")
        print("📉 Generating Interactive Dashboard Insights...")

    def generate_kpi_metrics(self):
        """Calculates Key Performance Indicators (KPIs)."""
        total_sales = sum(item['sales'] for item in self.data)
        avg_order_value = total_sales / len(self.data)
        top_region = max(self.data, key=lambda x: x['sales'])['region']
        
        print("\n" + "="*40)
        print("🏠 DASHBOARD OVERVIEW (KPIs)")
        print("="*40)
        print(f"💰 Total Revenue:       ₹{total_sales:,}")
        print(f"📦 Avg Order Value:    ₹{avg_order_value:,.2f}")
        print(f"🌍 Top Performing Region: {top_region}")
        print("-" * 40)

    def create_visual_bars(self, column):
        """Simulates Bar Charts for regional sales."""
        print(f"\n📊 SALES BY {column.upper()} (Visual Representation)")
        # Grouping data
        regional_data = {}
        for item in self.data:
            reg = item[column]
            regional_data[reg] = regional_data.get(reg, 0) + item['sales']

        # Generating "Charts" using text bars
        for reg, total in regional_data.items():
            bar_length = int(total / 500) # Scaling for display
            bar = "▇" * bar_length
            print(f"{reg:10} | {bar} ₹{total:,}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Simulated Dataset (Big Data Sample)
    big_data_sample = [
        {"id": 1, "region": "North", "sales": 5000, "category": "Tech"},
        {"id": 2, "region": "South", "sales": 7500, "category": "Furniture"},
        {"id": 3, "region": "East", "sales": 3200, "category": "Tech"},
        {"id": 4, "region": "West", "sales": 9000, "category": "Furniture"},
        {"id": 5, "region": "North", "sales": 4500, "category": "Tech"},
        {"id": 6, "region": "South", "sales": 6000, "category": "Tech"},
        {"id": 7, "region": "West", "sales": 12000, "category": "Furniture"},
    ]

    # Initialize Dashboard
    dashboard = DashboardSimulator(big_data_sample)

    # 1. Display KPIs (Summary)
    dashboard.generate_kpi_metrics()

    # 2. Display Bar Charts (Visualization)
    dashboard.create_visual_bars("region")

    print("\n" + "="*40)
    print("✅ Task 15 Complete: Dashboard Insights Generated.")
    print("NOTE: Logic mimics Tableau/Power BI data aggregation.")
    print("="*40)
