f = open("Data/datagdp_data_2.xlsx.csv", "r")
for line in f.readlines():
    data = line.split(",")
    print(data)

for item in data:
    country_name = [0]
    gdp_value = [1]

    print(f"Country: {country_name}, GDP: {gdp_value}")