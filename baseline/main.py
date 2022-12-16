import time
import random
import getch
import os
import pandas as pd

# Keyboard positions based on relative distance from home row and hand
key2position = {
    "a": 0,
    "s": 0,
    "d": 0,
    "f": 0,
    "g": 1,
    "h": 1,
    "j": 0,
    "k": 0,
    "l": 0,
    ";": 0,
    "q": 2,
    "w": 1,
    "e": 1,
    "r": 1,
    "t": 1,
    "y": 1,
    "u": 1,
    "i": 1,
    "o": 1,
    "p": 1,
    "z": 1,
    "x": 1,
    "c": 1,
    "v": 1,
    "b": 2,
    "n": 1,
    "m": 1,
    ",": 1,
    ".": 1,
}
key_times = []

def get_key_times():
    """
    Present the user with a key randomly up to five times and time it.
    """
    times = []
    os.system("clear")
    while True:
        print("Press enter to begin")
        value = getch.getch()
        if value == "\n":
            break
    for _ in range(5):
        iteration = {}
        # Shuffle the key2position dictionary
        keys = list(key2position.keys())
        random.shuffle(keys)
        # Present the user with a key
        for key in keys:
            os.system("clear")
            print(key)
            while True:
                start = time.time()
                value = getch.getch()
                if value == key:
                    end = time.time()
                    break
            iteration[key] = {"time": end - start, "distance": key2position[key]}
        times.append(iteration)
    return times

if __name__ == "__main__":
    times = get_key_times()
    df = pd.DataFrame(columns="key time distance iteration".split())
    for i, iteration in enumerate(times):
        for key, value in iteration.items():
            df = df.append(
                {
                    "key": key,
                    "time": value["time"],
                    "distance": value["distance"],
                    "iteration": i,
                },
                ignore_index=True,
            )
    df.to_csv("key_times.csv", index=False)