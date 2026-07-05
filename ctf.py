#!/usr/bin/env python3
import sys
def to_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)
if __name__ == "__main__":
    to_fahrenheit(float(sys.argv[1]))
