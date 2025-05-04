import time
import logging
from pathlib import Path

class TimerContext:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        logging.info(f"Elapsed: {elapsed:.2f} seconds")

logging.basicConfig(level=logging.INFO)

with TimerContext():
    time.sleep(2)

with TimerContext():
    sum(range(100000000))

with TimerContext():
    for x in range(1, 199999):
        x**5

STORAGE_FILE_NAME = Path(__file__).parent.parent / "storage/students.csv"
with TimerContext():
    with open(STORAGE_FILE_NAME, "r", encoding="utf-8", newline="") as file:
        file.readlines()
