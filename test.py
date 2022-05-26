import time
import pickle
from pathlib import Path
import yaml
import dvc.api

counter = 0

counter_file = Path("counter.pkl")
if counter_file.exists():
    counter = pickle.load(counter_file.open("rb"))
    print(f"Resuming from {counter}")

steps = yaml.safe_load(open("params.yaml"))["steps"]
while counter < steps:

    counter += 1
    print(f"Counter: {counter}")
    pickle.dump(counter, open("counter.pkl", "wb" ))
    dvc.api.make_checkpoint()
    time.sleep(3)