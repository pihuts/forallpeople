import forallpeople as si
si.environment('structural', top_level=True)
si.environment.auto_prefix = False

try:
    L = si.L
    print(f"L factor: {L.factor}")
    print(f"L dimensions: {L.dimensions}")
    print(f"L repr: {L}")
except:
    print("L not found")

try:
    mm = si.mm
    print(f"mm factor: {mm.factor}")
    print(f"mm repr: {mm}")
except:
    print("mm not found")

from fractions import Fraction
try:
    factors_map = si.environment.units_by_factor()
    key = Fraction(1, 1000)
    print(f"Units for factor {key}: {factors_map.get(key, 'Not Found').keys()}")
except Exception as e:
    print(f"Error checking units_by_factor: {e}")

