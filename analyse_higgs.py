import numpy as np
import matplotlib.pyplot as plt

LHC_ENERGY_GEV = 13000

# Higgs signal peak
SIGNAL_MU = 125.0

def run_cern_analysis():
    print(f"Running analysis at {LHC_ENERGY_GEV} GeV...")
    background = np.random.exponential(scale=50, size=10000)
    mu, sigma = SIGNAL_MU, 2 

    signal = np.random.normal(mu, sigma, size=500)
    data = np.concatenate([background, signal])

    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=100, range=(50, 200), histtype='step', label='LHC Data')
    plt.axvline(125, color='red', linestyle='--', label='125 GeV')
    plt.title("Plot with signal")
    plt.legend()
    plt.show()

    print(f"PEAK_DETECTED_AT: {SIGNAL_MU} GeV")


if __name__ == "__main__":
    run_cern_analysis()
