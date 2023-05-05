# Get current world population and growth rate
current_population = 7853000000
growth_rate = 1.05 / 100

# Calculate world population growth each year for the next 75 years
print("Year\tWorld Population\tNumerical Increase")
for year in range(1, 76):
    new_population = current_population * (1 + growth_rate) ** year
    numerical_increase = new_population - current_population
    print(f"{year}\t{int(new_population):,}\t\t{int(numerical_increase):,}")

    # Check if population has doubled
    if new_population >= current_population * 2:
        print(f"The population will be double in {year}.")
        break
