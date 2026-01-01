import forallpeople as si
si.environment('structural')
si.environment.auto_prefix = True # Assuming default

try:
    print("--- Test 1: .to('mL') behavior ---")
    mm = si.mm
    vol = mm**3
    print(f"Original: {vol}")
    try:
        converted = vol.to("mL")
        print(f"Converted to mL: {converted}")
    except Exception as e:
        print(f"Conversion failed: {e}")

    print("\n--- Test 2: Auto-conversion behavior ---")
    # V = (70mm)^2 * 1.5m
    v_wood = (70 * si.mm)**2 * (1.5 * si.m)
    print(f"V_wood = {v_wood}")
    
    print("\n--- Test 3: Check units_by_factor for mL ---")
    # mL factor is 1e-6 (approx)
    found_mL = False
    for f in si.environment.units_by_factor:
        if abs(f - 1e-6) < 1e-9:
             units = si.environment.units_by_factor[f]
             print(f"Found units at 1e-6: {units.keys()}")
             if 'mL' in units:
                 found_mL = True
    if not found_mL:
        print("mL NOT found in units_by_factor")

except Exception as e:
    print(e)
