import pandas as pd
import numpy as np

# Sample data
data_str = """5,52\t214,2\t214,20\t10744515025\t₺10.744.515.025,20\t203,3\t203,30\t215,4\t215,40\t18:10\t"THYAO\nTURK HAVA YOLLARI\nTURK HAVA YOLLARI"\tTHYAO
5,76\t135,9\t135,90\t7289617493\t₺7.289.617.493,20\t130,8\t130,80\t138,6\t138,60\t18:10\t"TUPRS\nTUPRAS\nTUPRAS"\tTUPRS
0,34\t17,69\t17,69\t6458300402\t₺6.458.300.402,16\t17,24\t17,24\t18,11\t18,11\t18:10\t"YKBNK\nYAPI VE KREDI BANK.\nYAPI VE KREDI BANK."\tYKBNK
0,9\t22,3\t22,30\t6199319283\t₺6.199.319.282,56\t21,46\t21,46\t22,76\t22,76\t18:10\t"ISCTR\nIS BANKASI (C)\nIS BANKASI (C)"\tISCTR
4,09\t142,4\t142,40\t4966408904\t₺4.966.408.904,20\t134,8\t134,80\t142,4\t142,40\t18:10\t"KCHOL\nKOC HOLDING\nKOC HOLDING"\tKCHOL
4,05\t30,8\t30,80\t4935959387\t₺4.935.959.387,14\t29,04\t29,04\t30,86\t30,86\t18:10\t"AKBNK\nAKBANK\nAKBANK"\tAKBNK
-9,43\t36,88\t36,88\t4076291554\t₺4.076.291.554,00\t36,68\t36,68\t44,78\t44,78\t18:10\t"BORLS\nBORLEASE OTOMOTIV\nBORLEASE OTOMOTIV"\tBORLS
2,83\t39,18\t39,18\t3848337050\t₺3.848.337.049,60\t37,86\t37,86\t39,62\t39,62\t18:10\t"EREGL\nEREGLI DEMIR CELIK\nEREGLI DEMIR CELIK"\tEREGL
10\t977,1\t977,10\t3769062486\t₺3.769.062.485,70\t886,1\t886,10\t977,1\t977,10\t18:10\t"BRSAN\nBORUSAN MANNESMANN\nBORUSAN MANNESMANN"\tBRSAN
1,89\t19,43\t19,43\t3340970938\t₺3.340.970.938,19\t18,87\t18,87\t19,82\t19,82\t18:10\t"PETKM\nPETKIM\nPETKIM"\tPETKM
-2,01\t277,7\t277,70\t3227689278\t₺3.227.689.277,50\t277,3\t277,30\t290,8\t290,80\t18:10\t"BIMAS\nBIM MAGAZALAR\nBIM MAGAZALAR"\tBIMAS
"""

# Convert the string data to a list of lines
data_lines = data_str.strip().split('\n')

# Initialize a list to store rows of data
rows = []

# Process each line of data
for line in data_lines:
    # Split the line into columns using tab as the delimiter
    columns = line.split('\t')

    # Extract relevant columns and convert them to appropriate data types
    try:
        rate = float(columns[0].replace(',', '.'))
        lastprice = float(columns[1].replace(',', '.'))
        hacim = float(columns[3].replace(',', '.'))
        # Add more columns as needed

        # Create a row and append it to the list of rows
        row = [rate, lastprice, hacim]  # Add more columns as needed
        rows.append(row)
    except ValueError:
        pass  # Skip rows with non-numeric values

# Create a DataFrame from the list of rows
data = pd.DataFrame(rows, columns=["Rate", "LastPrice", "Hacim"])  # Add more column names as needed

# Parameters (use the same parameters as in your original code)
pn = 20
max_iter = 20000
w_min = 0
w_max = 0.03
yas = data.shape[1]

# Initialize particles and velocities
# Initialize particles and velocities
weights = np.random.uniform(w_min, w_max, size=(pn, yas - 1))
weights = np.column_stack((weights, 1 - np.sum(weights, axis=1)))
velocities = np.zeros_like(weights)

# Convert weights to numeric format
weights = weights.astype(float)

# Diğer kodlar buraya eklenecek


# Initialize best particle and its performance
best_particle_sharpe_ratio = -np.inf
best_particle_weights = None

# Main loop
for iteration in range(max_iter):
    # Calculate expected return and standard deviation
    expected_returns = np.dot(weights, data.mean())
    covariance_matrix = data.cov().values
    standard_deviations = np.sqrt(np.dot(weights, np.dot(covariance_matrix, weights.T)))

    # Calculate fitness (Sharpe ratio)
    sharpe_ratios = expected_returns / standard_deviations

    # Update best particle and its performance
    if np.max(sharpe_ratios) > best_particle_sharpe_ratio:
        best_particle_sharpe_ratio = np.max(sharpe_ratios)
        best_particle_weights = weights[np.argmax(sharpe_ratios)]

    # Update particles based on best and worst performers
    inertia_weight = 0.5
    cognitive_weight = 1.5
    social_weight = 1.5

    for i in range(pn):
        r1, r2 = np.random.rand(), np.random.rand()
        velocity = (inertia_weight * velocities[i] +
                    cognitive_weight * r1 * (best_particle_weights - weights[i]) +
                    social_weight * r2 * (best_particle_weights - weights[i]))
        velocities[i] = velocity
        weights[i] += velocity
        weights[i] = np.clip(weights[i], 0, w_max)
        weights[i] /= np.sum(weights[i])  # Ensure weights sum to 1

# Print results
print(f"Best Sharpe Ratio: {best_particle_sharpe_ratio}")
print(f"Best Portfolio Weights: {best_particle_weights}")
