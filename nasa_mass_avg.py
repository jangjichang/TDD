import urllib.request
import json

from simple_calculator.main import SimpleCalculator

URL = "https://data.nasa.gov/resource/y77d-th95.json"

with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())

masses = [float(d["mass"]) for d in data if "mass" in d]

print(masses)

calculator = SimpleCalculator()

avg_mass = calculator.avg(masses)

print(avg_mass)
