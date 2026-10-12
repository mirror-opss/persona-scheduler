import time

INTERVAL_MIN = 42  # intervalle fixe : le signal que la slide 7 fait détecter

for i in range(5):
    print(f"Publication simulée #{i + 1} (toutes les {INTERVAL_MIN} min)")
    time.sleep(0.1)
