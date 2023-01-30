# Importing libraries
import numpy as np
from scipy import norm

# define variables
r = 0.035
S = 400
K = 410
T = 240 / 365
sigma = 0.25


def blackscholes(r, S, K, T, sigma, type="C"):
    # Calculates the black-Shcoles options price for Call/put
    d1 = (np.log(S / K + (r + sigma ** 2 / 2) / sigma * np.sqrt(T)))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "C":
            price = S * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        elif type == "P":
            price = K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Please enter all parameters")


print("The theoretical options price is: ", round(blackscholes, r, S, K, T, sigma, type="C"), 2)
