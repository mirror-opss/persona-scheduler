import time

INTERVAL_MIN = 42  # intervalle fixe

for i in range(5):
    print(f"Publication simulée #{i + 1} (toutes les {INTERVAL_MIN} min)")
    time.sleep(0.1)
