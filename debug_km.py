import forallpeople as si
import json
si.environment('structural', top_level=True)
si.environment.auto_prefix = False

try:
    km = si.km
    print(f"km factor: {km.factor}")
    print(f"km repr: {km}")
    
    m = si.m
    print(f"m factor: {m.factor}")
    print(f"km/m result: {km/m}")
except:
    print("km or m not found")

# Check environment definition
try:
    km_def = si.environment.environment.get('km')
    print(f"km definition keys: {list(km_def.keys())}")
    print(f"km Factor raw: {km_def.get('Factor')}")
    print(f"km Factor type: {type(km_def.get('Factor'))}")
except:
    print("km definition not found")

# Check L definition
try:
    L_def = si.environment.environment.get('L')
    print(f"L definition keys: {list(L_def.keys())}")
    print(f"L Factor raw: {L_def.get('Factor')}")
except:
    print("L definition not found")
