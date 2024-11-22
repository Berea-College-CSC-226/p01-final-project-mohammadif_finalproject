
#Name: Feda Mohammadi
#Username: mohammadif
########################################################################################################################
#Purpose: This program calculates the GDP using user-provided inputs for its components.

########################################################################################################################
#Acknowledgment: resources and mentors for guidance on GDP and GUI programming.

########################################################################################################################
import tkinter as tk
from tkinter import messagebox

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

        # Welcome message displayed on the same page
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

        # Ranking Button
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

        # Tooltip for guidance
        tooltip = f"Enter the value for {label_text.split(':')[0]}"
        entry_var.bind("<Enter>", lambda e: self.show_tooltip(e, tooltip))
        entry_var.bind("<Leave>", self.hide_tooltip)

        return entry_var

    def show_tooltip(self, event, text):
        self.tooltip = tk.Label(self.root, text=text, bg="yellow", font=("Helvetica", 8))
        self.tooltip.place(x=event.widget.winfo_x() + event.widget.winfo_width() + 10, y=event.widget.winfo_y())

    def hide_tooltip(self, event):
        if hasattr(self, "tooltip"):
            self.tooltip.destroy()

    def format_gdp_value(self, value):
        if value >= 1_000_000_000_000:
            return f"{value / 1_000_000_000_000:,.2f} Trillion"
        elif value >= 1_000_000_000:
            return f"{value / 1_000_000_000:,.2f} Billion"
        elif value >= 1_000_000:
            return f"{value / 1_000_000:,.2f} Million"
        elif value >= 1_000:
            return f"{value / 1_000:,.2f} Thousand"
        else:
            return f"{value:,.2f}"

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
        # List of top 15 countries by GDP (2024)
        countries_gdp = {
            "United States": 25.43,
            "China": 14.72,
            "Japan": 4.25,
            "Germany": 3.85,
            "India": 3.41,
            "United Kingdom": 2.67,
            "France": 2.63,
            "Russia": 2.24,
            "Canada": 2.16,
            "Italy": 2.04,
            "Brazil": 1.92,
            "Australia": 1.69,
            "South Korea": 1.67,
            "Mexico": 1.46,
            "Spain": 1.41,
        }

        # Calculate the user's GDP
        try:
            user_gdp = self.gdp_calculator.calculate_gdp()
            percentile = self.get_gdp_percentile(user_gdp, countries_gdp)
            formatted_gdp = self.format_gdp_value(user_gdp)

            ranking_message = "\nTop 15 countries by GDP in 2024:\n\n"
            for country, gdp in countries_gdp.items():
                ranking_message += f"{country}: ${gdp:.2f} Trillion\n"

            ranking_message += f"\nYour GDP is ${formatted_gdp}, and it ranks in the {percentile} percentile based on these countries."

            messagebox.showinfo("GDP Ranking", ranking_message)
        except ValueError:
            messagebox.showerror("Input Error", "Please calculate GDP before checking the ranking.")

    def get_gdp_percentile(self, user_gdp, countries_gdp):
        sorted_gdps = sorted(countries_gdp.values(), reverse=True)
        rank = 1 + sum(1 for gdp in sorted_gdps if user_gdp < gdp)
        percentile = (rank / len(sorted_gdps)) * 100
        return f"{percentile:.2f}"

if __name__ == "__main__":
    root = tk.Tk()
    app = GDPApp(root)
    root.mainloop()
