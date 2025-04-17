import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

def data_visualization_tool():
    print("📊 Data Visualization Tool")

    # Embedded CSV data
    csv_data = """
Name,Age,Grade
Alice,20,88
Bob,21,75
Charlie,19,90
David,22,82
    """
    
    # Load dataset from string
    try:
        data = pd.read_csv(StringIO(csv_data))
        print("\n✅ Dataset Loaded Successfully!")
        print("\n🧾 Available Columns:\n", data.columns.tolist())

        # Ask user to pick columns and type of chart
        x_col = input("Enter the column for X-axis: ")
        y_col = input("Enter the column for Y-axis: ")
        chart_type = input("Choose chart type (scatter, line, bar, box): ").lower()

        # Plot based on user choice
        if chart_type == 'scatter':
            sns.scatterplot(data=data, x=x_col, y=y_col)
        elif chart_type == 'line':
            sns.lineplot(data=data, x=x_col, y=y_col)
        elif chart_type == 'bar':
            sns.barplot(data=data, x=x_col, y=y_col)
        elif chart_type == 'box':
            sns.boxplot(data=data, x=x_col, y=y_col)
        else:
            print("❌ Unsupported chart type selected.")
            return

        plt.title(f"{chart_type.title()} Chart: {y_col} vs {x_col}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Error: {e}")

# Run the tool
data_visualization_tool()
