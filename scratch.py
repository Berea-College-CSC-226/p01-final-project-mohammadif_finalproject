import tkinter as tk
from tkinter import messagebox
import wbgapi as wb  # World Bank API library

# Class for individual GDP components
class GDPComponent:
    def __init__(self, name):
        self.component_name = name
        self.value = 0

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

# Class for calculating total GDP
class GDPCalculator:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def calculate_gdp(self):
        total_gdp = sum(component.get_value() for component in self.components)
        return total_gdp

# GUI application class
class GDPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GDP Calculator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.config(bg="#f7f7f7")

        # GDP components
        self.consumption = GDPComponent("Consumption")
        self.investment = GDPComponent("Investment")
        self.government_spending = GDPComponent("Government Spending")
        self.net_exports = GDPComponent("Net Exports")

        self.gdp_calculator = GDPCalculator()
        self.gdp_calculator.add_component(self.consumption)
        self.gdp_calculator.add_component(self.investment)
        self.gdp_calculator.add_component(self.government_spending)
        self.gdp_calculator.add_component(self.net_exports)

        # Title label
        self.title_label = tk.Label(root, text="GDP Calculator", font=("Helvetica", 18, "bold"), bg="#f7f7f7")
        self.title_label.pack(pady=10)

        # Welcome message
        self.create_welcome_message()

        # Input fields
        self.consumption_entry = self.create_input_field("Consumption (C): $")
        self.investment_entry = self.create_input_field("Investment (I): $")
        self.government_entry = self.create_input_field("Government Spending (G): $")
        self.net_exports_entry = self.create_input_field("Net Exports (NX): $")

        # Buttons
        self.calculate_button = tk.Button(root, text="Calculate GDP", command=self.calculate_gdp, bg="#4CAF50", fg="white", width=20)
        self.calculate_button.pack(pady=15)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_inputs, bg="#f44336", fg="white", width=20)
        self.reset_button.pack(pady=5)

        self.ranking_button = tk.Button(root, text="See the Ranking", command=self.show_ranking, bg="#2196F3", fg="white", width=20)
        self.ranking_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(root, text="Overall GDP:$ ", font=("Helvetica", 12, "bold"), bg="#f7f7f7")
        self.result_label.pack(pady=10)

    def create_welcome_message(self):
        message = (
            "Welcome to the GDP Calculator!\n\n"
            "What is GDP?\nGross Domestic Product (GDP) measures the total economic output of a country \n within a year.\n\n"
            "Components of GDP:\n"
            "Consumption (C): Total spending by households.\n"
            "Investment (I): Expenditure on goods used for future production.\n"
            "Government Spending (G): Expenditure by the government on goods and services.\n"
            "Net Exports (NX): Exports minus imports."
        )

        self.welcome_frame = tk.LabelFrame(self.root, text="Welcome", font=("Helvetica", 10, "bold"), bg="#f7f7f7", width=450)
        self.welcome_frame.pack(pady=10)

        self.welcome_label = tk.Label(self.welcome_frame, text=message, font=("Helvetica", 9), bg="#f7f7f7", justify="left", anchor="w")
        self.welcome_label.pack(padx=10, pady=10)

    def create_input_field(self, label_text):
        label = tk.Label(self.root, text=label_text, font=("Helvetica", 10, "bold"), bg="#f7f7f7")
        label.pack()

        entry_var = tk.Entry(self.root, width=30)
        entry_var.pack(pady=5)

        return entry_var

    def calculate_gdp(self):
        try:
            self.consumption.set_value(float(self.consumption_entry.get()))
            self.investment.set_value(float(self.investment_entry.get()))
            self.government_spending.set_value(float(self.government_entry.get()))
            self.net_exports.set_value(float(self.net_exports_entry.get()))

            total_gdp = self.gdp_calculator.calculate_gdp()

            formatted_gdp = self.format_gdp_value(total_gdp)
            self.result_label.config(text=f"Overall GDP: $ {formatted_gdp}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")

    def reset_inputs(self):
        self.consumption_entry.delete(0, tk.END)
        self.investment_entry.delete(0, tk.END)
        self.government_entry.delete(0, tk.END)
        self.net_exports_entry.delete(0, tk.END)
        self.result_label.config(text="Overall GDP:$ ")

    def show_ranking(self):
        try:
            user_gdp = self.gdp_calculator.calculate_gdp()
            gdp_data = self.fetch_real_gdp_data()

            ranked_countries = sorted(gdp_data.items(), key=lambda x: x[1], reverse=True)
            rank = 1 + sum(1 for _, gdp in ranked_countries if user_gdp < gdp)

            ranking_message = "\nTop countries by GDP:\n\n"
            for country, gdp in ranked_countries[:15]:
                ranking_message += f"{country}: ${gdp:,.2f}\n"

            ranking_message += f"\nYour GDP is ranked #{rank} globally."
            messagebox.showinfo("GDP Ranking", ranking_message)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching GDP data: {e}")

    def fetch_real_gdp_data(self):
        gdp_data = {}
        for record in wb.data.fetch('NY.GDP.MKTP.CD', time='2022'):
            gdp_data[wb.economy.info(record['economy'])['name']] = record['value']
        return gdp_data

    def format_gdp_value(self, value):
        if value >= 1_000_000_000_000:
            return f"{value / 1_000_000_000_000:,.2f} Trillion"
        elif value >= 1_000_000_000:
            return f"{value / 1_000_000_000:,.2f} Billion"
        else:
            return f"{value:,.2f}"

if __name__ == "__main__":
    root = tk.Tk()
    app = GDPApp(root)
    root.mainloop()
