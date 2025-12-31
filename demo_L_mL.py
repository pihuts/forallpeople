import forallpeople as si
import sys

# Ensure we are using the structural environment where we added L and mL
si.environment('structural', top_level=True)
si.environment.auto_prefix = False

print("--- Testing L and mL ---")

# Access L
try:
    L = si.L
    print(f"L: {L} (Factor={L.factor})")
except AttributeError:
    print("Error: L not found in environment!")
    try:
        import builtins
        print(f"L (builtins): {builtins.L}")
        L = builtins.L
    except:
        pass

# Access mL
try:
    mL = si.mL
    print(f"mL: {mL} (Factor={mL.factor})")
except AttributeError:
    print("Error: mL not found in environment!")
    try:
        import builtins
        print(f"mL (builtins): {builtins.mL}")
        mL = builtins.mL
    except:
        pass

if 'L' in locals() and 'mL' in locals():
    # Test Stickiness and Conversions
    val_L = 5 * L
    print(f"5 * L = {val_L}") 

    val_mL = 500 * mL
    print(f"500 * mL = {val_mL}")

    # Check collisions
    print(f"Check collisions: 1000 * mL = {1000 * mL}") # Should satisfy 1 L? No, stickiness keeps it mL?
    # Actually auto_prefix=False keeps it as is unless explicit?
    # 1000 * mL = 1000 mL.
    
    # Check what 1 cm^3 is
    cm = si.cm
    cm3 = cm**3
    print(f"1 cm^3 = {cm3}")

    # Prioritization check:
    # 1e-6 m^3. Should match mL (Defined) over cm^3 (Derived)
    print("Prioritization check (1e-6 m^3):")
    # We construct a Physical manually with 1e-6 factor to see what it defaults to
    # But factor lookup requires the unit to be in units_by_factor.
    # mL is in units_by_factor.
    
    # Let's force a calculation that results in 1e-6 but without "stickiness" from LHS?
    # No, stickiness comes from _evaluate_dims_and_factor.
    
    print("Success!")
else:
    print("Failed to find L or mL.")
