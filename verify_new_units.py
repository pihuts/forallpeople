import forallpeople as si
si.environment('structural', top_level=True)
si.environment.auto_prefix = False

import builtins

# Helper to look up unit safely
def get_unit(name):
    if hasattr(si, name):
        return getattr(si, name)
    if hasattr(builtins, name):
        return getattr(builtins, name)
    if name in globals():
        return globals()[name]
    return f"Context missing {name}"

# Check mm (existing but modified)
print(f"mm: {get_unit('mm')} (Factor={get_unit('mm').factor})")

# Check new units
print(f"cm: {get_unit('cm')} (Factor={get_unit('cm').factor})")
print(f"km: {get_unit('km')} (Factor={get_unit('km').factor})")
print(f"day: {get_unit('day')} (Factor={get_unit('day').factor})")
print(f"hour: {get_unit('hour')} (Factor={get_unit('hour').factor})")
print(f"minute: {get_unit('minute')} (Factor={get_unit('minute').factor})")
print(f"kN_m: {get_unit('kN_m')} (Factor={get_unit('kN_m').factor})")
print(f"kN_m2: {get_unit('kN_m2')} (Factor={get_unit('kN_m2').factor})")
print(f"kN_m3: {get_unit('kN_m3')} (Factor={get_unit('kN_m3').factor})")
print(f"mm3: {get_unit('mm3')} (Factor={get_unit('mm3').factor})")
print(f"mm4: {get_unit('mm4')} (Factor={get_unit('mm4').factor})")
print(f"L: {get_unit('L')} (Factor={get_unit('L').factor})")
print(f"mL: {get_unit('mL')} (Factor={get_unit('mL').factor})")

# Verify calculations
print(f"1 km in m: {1 * get_unit('km')}")
print(f"1 day in s: {1 * get_unit('day')}")
