import yfinance as yf
import pandas as pd
import numpy as np
import cvxpy as cp
from datetime import datetime, timedelta


symbols = ['AKBNK.IS', 'ALARK.IS', 'ARCLK.IS', 'ASELS.IS', 'BIMAS.IS', 'EKGYO.IS', 'ENKAI.IS', 'EREGL.IS', 'FROTO.IS',
           'GARAN.IS', 'GUBRF.IS', 'SAHOL.IS', 'HEKTS.IS', 'KRDMD.IS', 'KCHOL.IS', 'KOZAL.IS', 'KOZAA.IS', 'ODAS.IS',
           'PGSUS.IS', 'PETKM.IS', 'SASA.IS', 'SISE.IS', 'TAVHL.IS', 'THYAO.IS', 'TOASO.IS', 'TUPRS.IS', 'TCELL.IS',
           'ISCTR.IS', 'YKBNK.IS']


end_date = datetime.today()


start_date = end_date - timedelta(days=30)


all_data = yf.download(symbols, start=start_date, end=end_date)['Adj Close']


log_daily_returns = np.log(all_data / all_data.shift(1))


log_daily_returns_df = pd.DataFrame()

for symbol in symbols:
    log_daily_returns_df[symbol] = log_daily_returns[symbol]


last_log_daily_returns = log_daily_returns_df.iloc[-1]


selected_symbols_cumulative_returns = last_log_daily_returns.nsmallest(20).index

print("Kümülatif Log Getirisi En Az Olan 20 Hisse:")
print(selected_symbols_cumulative_returns)


selected_symbols_list = selected_symbols_cumulative_returns.tolist()


start_date_volume = end_date - timedelta(days=7)


volume_increase_last_7_days = {}
for symbol in selected_symbols_list:
    
    df = yf.download(symbol, start=start_date_volume, end=end_date)

    
    daily_volume = df['Volume']
    volume_increase = (daily_volume / daily_volume.shift(1) - 1).iloc[-7:].sum() * 100  
    volume_increase_last_7_days[symbol] = volume_increase


selected_symbols_volume_increase = dict(sorted(volume_increase_last_7_days.items(), key=lambda item: item[1], reverse=True)[:10])

print("Son 7 Günde Kümülatif Volume Artışı En Yüksek 10 Hisse:")
print(selected_symbols_volume_increase)

selected_symbols_volume_increase_positive = {symbol: volume_increase for symbol, volume_increase in selected_symbols_volume_increase.items() if volume_increase > 0}

print("Son 7 Günde Kümülatif Volume Artışı Pozitif Olan Hisse Senetleri:")
print(selected_symbols_volume_increase_positive)


selected_log_returns = log_daily_returns_df[list(selected_symbols_volume_increase_positive.keys())]


portfolio_log_returns = np.dot(selected_log_returns.mean(), equal_weights) * 252


covariance_matrix = selected_log_returns.cov() * 252

n = len(selected_log_returns.columns)  
weights = cp.Variable(n)  


objective = cp.Maximize(cp.sum(portfolio_log_returns * weights))


constraints = [
    cp.sum(weights) == 1,  
    weights >= 0  
]


portfolio_variance = cp.quad_form(weights, covariance_matrix)  
risk_tolerance = 0.1  
constraints.append(portfolio_variance <= risk_tolerance)


problem = cp.Problem(objective, constraints)


problem.solve()


optimal_weights = weights.value


normalized_weights = optimal_weights / optimal_weights.sum()

print("\nOptimal Portföy Ağırlıkları (Normalize Edilmiş):")
for i, symbol in enumerate(selected_log_returns.columns):
    print(f"{symbol}: {normalized_weights[i]:.4f}")


selected_top_5_symbols = selected_log_returns.columns[np.argsort(normalized_weights)[-5:]]

print("\nSadece İlk 5 Hisseden Oluşan Portföy:")
for symbol in selected_top_5_symbols:
    print(symbol)


    
optimal_top_5_weights = normalized_weights[np.argsort(normalized_weights)[-5:]]

total_weight = sum(optimal_top_5_weights)
optimal_top_5_weights /= total_weight

print("\nİlk 5 Hisseden Oluşan Portföyün Optimal Ağırlıkları:")
for i, symbol in enumerate(selected_top_5_symbols):
    print(f"{symbol}: {optimal_top_5_weights[i]:.4f}")