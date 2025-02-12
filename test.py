import time

frames = [
    "(^_^)",
    "(-_-)",
    "(^_^)",
    "(^o^)",
]

while True:
    for frame in frames:
        print("\r" + frame, end="")
        time.sleep(0.5)
