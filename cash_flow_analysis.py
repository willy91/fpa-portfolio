import pandas as pd
import matplotlib.pyplot as plt

EXCEL_PATH = r"Cash_FLow_Forecast_Runway_Tech_startup.xlsx"

xls = pd.ExcelFile(EXCEL_PATH)
print("Hojas encontradas:", xls.sheet_names)

# Leer la hoja Monthly_Forecast completa, sin asumir encabezados limpios
df = pd.read_excel(EXCEL_PATH, sheet_name="Monthly_Forecast", header=None)

# Ver las primeras filas para entender la estructura
print(df.head(20))
print("---")
print("Dimensiones (filas, columnas):", df.shape)
# Extraer las filas clave (sin la columna 0 que tiene las etiquetas de texto)
fechas = df.iloc[0, 1:].values          # Fila 0: las fechas
mrr = df.iloc[3, 1:].values             # Fila 3: MRR
total_revenue = df.iloc[12, 1:].values  # Fila 12: Total Revenue
total_costs = df.iloc[13, 1:].values    # Fila 13: Total Costs
net_burn = df.iloc[14, 1:].values       # Fila 14: Net Burn
cash_balance = df.iloc[15, 1:].values   # Fila 15: Cash Balance

# Verificar que extrajimos bien
print("Fechas:", fechas[:3], "...")
print("Cash Balance inicio:", cash_balance[0], "| final:", cash_balance[-1])
print("Net Burn inicio:", net_burn[0])
# === GRÁFICA 1: Cash Balance Over Time ===
plt.figure(figsize=(10, 6))
plt.plot(fechas, cash_balance, color="#1f3a93", linewidth=2.5, marker="o", markersize=3)

# Línea horizontal en cero (el punto crítico)
plt.axhline(y=0, color="red", linestyle="--", linewidth=1, alpha=0.7)

# Títulos y etiquetas
plt.title("Cash Balance Over Time", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Cash Balance ($)")

# Formatear el eje Y en millones para que se lea fácil
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:.0f}M"))

plt.grid(True, alpha=0.3)
plt.tight_layout()

# Guardar como imagen
plt.savefig("cash_balance_chart.png", dpi=150)
print("Gráfica guardada: cash_balance_chart.png")
# === GRÁFICA 2: MRR Over Time ===
plt.figure(figsize=(10, 6))
plt.plot(fechas, mrr, color="#16a085", linewidth=2.5, marker="o", markersize=3)

plt.title("MRR Over Time", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("MRR ($)")
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("mrr_chart.png", dpi=150)
print("Gráfica guardada: mrr_chart.png")
# === GRÁFICA 3: Revenue vs Costs vs Net Burn ===
plt.figure(figsize=(10, 6))
plt.plot(fechas, total_revenue, color="#16a085", linewidth=2.5, label="Total Revenue")
plt.plot(fechas, total_costs, color="#f39c12", linewidth=2.5, label="Total Costs")
plt.plot(fechas, net_burn, color="#c0392b", linewidth=2.5, label="Net Burn")

plt.axhline(y=0, color="gray", linestyle="--", linewidth=1, alpha=0.5)

plt.title("Revenue vs Costs vs Net Burn", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("revenue_costs_burn_chart.png", dpi=150)
print("Gráfica guardada: revenue_costs_burn_chart.png")
