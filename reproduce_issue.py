import forallpeople as si
si.environment('structural', top_level=True)
si.environment.auto_prefix = False

# This should now work and be a Factor-based unit
try:
    mm = si.mm
except AttributeError:
    import builtins
    mm = builtins.mm

print(f"mm factor: {mm.factor}")
val = 100000 * mm
print(f"100000 * mm = {val} (Factor={val.factor})")

