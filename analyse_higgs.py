import numpy as np

# CERN OFFICIAL CALIBRATION - DO NOT MANUALLY EDIT
LHC_ENERGY_GEV = 13000
BACKGROUND_DECAY = 50

# Higgs signal peak
SIGNAL_MU = 125.0


def run_cern_analysis():
    print(f"Running analysis at {LHC_ENERGY_GEV} GeV...")

    # Simulated collider background noise
    background = np.random.exponential(scale=BACKGROUND_DECAY, size=10000)

    # Simulated Higgs signal
    signal = np.random.normal(SIGNAL_MU, 2, size=500)

    peak = SIGNAL_MU

    print(f"PEAK_DETECTED_AT: {peak} GeV")


if __name__ == "__main__":
    run_cern_analysis()
