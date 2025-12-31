import forallpeople as si
from forallpeople.dimensions import Dimensions
si.environment('default', top_level=True)

# Define a unit using Value (like mm currently)
# Value = 0.001 means 1 unit = 0.001 base units. Factor defaults to 1.
mm_val_def = si.Physical(0.001, Dimensions(0,1,0,0,0,0,0), factor=1)
print(f"mm (Value): {mm_val_def}, factor={mm_val_def.factor}")

# Define a unit using Factor
# Factor = 0.001 means the unit IS 0.001 base units. Value starts at 1.
mm_fact_def = si.Physical(1, Dimensions(0,1,0,0,0,0,0), factor=0.001)
print(f"mm (Factor): {mm_fact_def}, factor={mm_fact_def.factor}")

# Test multiplication
res_val = 100000 * mm_val_def
print(f"100000 * mm (Value) = {res_val} (Factor={res_val.factor})")

res_fact = 100000 * mm_fact_def
print(f"100000 * mm (Factor) = {res_fact} (Factor={res_fact.factor})")
