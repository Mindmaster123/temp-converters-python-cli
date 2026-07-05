#!/usr/bin/env python3
import sys
def to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5/9
    print(celsius)
if __name__ == "__main__":
    to_celsius(float(sys.argv[1]))
