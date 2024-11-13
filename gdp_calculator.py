import math

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

# Function to ask for user input with error handling
def get_input(prompt):
    while True:
        try:
            # Get input and try to convert it to a float
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Main program to ask for inputs and calculate GDP
def main():
    # Create GDP components for Consumption, Investment, Government Spending, and Net Exports
    consumption = GDPComponent("Consumption")
    investment = GDPComponent("Investment")
    government_spending = GDPComponent("Government Spending")
    net_exports = GDPComponent("Net Exports")

    # Ask the user for values and assign them to the components
    consumption.set_value(get_input("Enter Consumption (C): "))
    investment.set_value(get_input("Enter Investment (I): "))
    government_spending.set_value(get_input("Enter Government Spending (G): "))
    net_exports.set_value(get_input("Enter Net Exports (NX): "))

    # Create a GDPCalculator object and add components to it
    gdp_calculator = GDPCalculator()
    gdp_calculator.add_component(consumption)
    gdp_calculator.add_component(investment)
    gdp_calculator.add_component(government_spending)
    gdp_calculator.add_component(net_exports)

    # Calculate and display the GDP
    total_gdp = gdp_calculator.calculate_gdp()
    print(f"\nTotal GDP is: {total_gdp:.2f}")

if __name__ == "__main__":
    main()
