import pandas as pd
import numpy as np

# Excel dosyasından veriyi okuma
excel_file_path = r'C:\Users\app_a\Documents\Python Projects\miniPython\SRC\veri.xlsx'  # Dosya yolunu güncelleyin
df = pd.read_excel(excel_file_path, sheet_name='Sayfa1')  # header=0, ilk satırı sütun isimleri olarak kullanır

# Belirli bir aralıktaki sütunları seçme (Date sütunu ve A:Y aralığındaki sütunlar)
selected_columns = df.loc[:, ['Date', 'S&P/ASX 200 (AXJO)', 'ATX (ATX)', 'BEL 20 (BFX)', 'S&P/TSX (GSPTSE)', 'SWI20 (SSMI)',
                               'DAX (GDAXI)', 'OMXC20', 'IBEX 35 (IBEX)', 'OMX Helsinki 25 (OMXH25)', 'CAC 40 (FCHI)',
                               'FTSE 100 (FTSE)', 'Hang Seng (HSI)', 'ISEQ Overall (ISEQ)', 'FTSE MIB (FTMIB)',
                               'Nikkei 225 (N225)', 'AEX (AEX)', 'Oslo OBX (OBX)', 'S&P/NZX 50', 'PSI (PSI20)',
                               'OMX Stockholm 30 (OMXS30)', 'FTSE Straits Times Singapore (STI)', 'Nasdaq 100 (NDX)',
                               'S&P 500 (SPX)', 'MSCI Dünya (MIWO00000PUS)']]

# Seçilen verileri yazdırma
print("Seçilen Veriler:")
print(selected_columns)

# Seçilen sütunlardaki sayısal verileri numpy dizisine dönüştürme
returns = selected_columns.iloc[:, 1:].replace({',': ''}, regex=True).astype(float).values

# Sütun isimlerini güncelleme
returns_columns = selected_columns.columns[1:]

# Optimizasyon için sınırlar
bounds = np.array([[0, 1]] * len(returns_columns))

# Jaya Algoritması
def portfolio_objective(weights, returns):
    portfolio_return = np.sum(weights * returns.mean(axis=0))
    portfolio_variance = np.dot(weights.T, np.dot(np.cov(returns, rowvar=False), weights))
    return -portfolio_return / np.sqrt(portfolio_variance)

def jaya_algorithm(obj_func, bounds, population_size, max_iterations):
    num_variables = len(bounds)
    population = np.random.uniform(bounds[:, 0], bounds[:, 1], size=(population_size, num_variables))

    for iteration in range(max_iterations):
        fitness_values = [obj_func(individual, returns) for individual in population]
        best_index = np.argmin(fitness_values)
        worst_index = np.argmax(fitness_values)

        for i in range(population_size):
            if i != best_index and i != worst_index:
                r1, r2 = np.random.rand(), np.random.rand()
                population[i] += r1 * (population[best_index] - np.abs(population[i])) - r2 * (population[worst_index] - np.abs(population[i]))

        population = np.clip(population, bounds[:, 0], bounds[:, 1])

    best_solution = population[best_index]
    best_fitness = fitness_values[best_index]
    return best_solution, best_fitness

# Portföy optimizasyonu
best_weights, best_fitness = jaya_algorithm(lambda x, y: portfolio_objective(x, y),
                                             bounds=bounds,
                                             population_size=50,
                                             max_iterations=100)

print("\nEn İyi Ağırlıklar:")
for asset, weight in zip(returns_columns, best_weights):
    print(f"{asset}: {weight:.4f}")

print("\nEn İyi Fitness Değeri:", best_fitness)
