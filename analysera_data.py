import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ladda datasetet
data = pd.read_csv('temperature.csv')

# Visa de första raderna i datasetet och kontrollera data
print(data.head())
print(data.info())
print(data.isnull().sum())

# Rensa datasetet (ta bort rader med saknade värden i Vancouver-kolumnen)
data = data.dropna(subset=['Vancouver'])

# Konvertera datetime till korrekt typ
data['datetime'] = pd.to_datetime(data['datetime'])

# Plot för Vancouver
plt.figure(figsize=(14, 6))
plt.plot(data['datetime'], data['Vancouver'] - 273.15, label='Vancouver (°C)')  # Konvertera Kelvin till Celsius
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation Over Time in Vancouver')
plt.grid(True)
plt.legend()
plt.show()

# Plot för flera städer
plt.figure(figsize=(14, 6))
plt.plot(data['datetime'], data['Vancouver'] - 273.15, label='Vancouver (°C)')
plt.plot(data['datetime'], data['San Francisco'] - 273.15, label='San Francisco (°C)')
plt.plot(data['datetime'], data['New York'] - 273.15, label='New York (°C)')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation Over Time in Multiple Cities')
plt.grid(True)
plt.legend()
plt.show()