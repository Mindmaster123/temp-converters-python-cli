# Temperature Converter

## ctf.py
Converts Celsius to Fahrenheit.

**Usage:**
python3 ctf.py <celsius>

**Example:**
python3 ctf.py 100
# Output: 212.0

## ftc.py
Converts Fahrenheit to Celsius.

**Usage:**
python3 ftc.py <fahrenheit>

**Example:**
python3 ftc.py 212
# Output: 100.0

## Running as CLI tools (no `python3` prefix)

1. Make executable: `chmod +x ctf.py ftc.py`
2. Optionally, drop the `.py` extension and move to your PATH:
   `mv ctf.py ~/.local/bin/ctf && mv ftc.py ~/.local/bin/ftc`
3. Now call directly: `ctf 100`
