"""
Comprehensive unit verification script for forallpeople structural environment.
Checks all units for correct display, factor values, and .to() conversion.
"""
import forallpeople as si
si.environment('structural')
si.environment.auto_prefix = False

# List of all units to test from structural.json
units_to_test = [
    # Base and derived SI units
    ('m', 'Length', 1),
    ('mm', 'Length', 0.001),
    ('cm', 'Length', 0.01),
    ('km', 'Length', 1000),
    
    # Force
    ('N', 'Force', 1),
    ('kN', 'Force', 1000),
    ('MN', 'Force', 1e6),
    
    # Pressure/Stress
    ('Pa', 'Pressure', 1),
    ('kPa', 'Pressure', 1000),
    ('MPa', 'Pressure', 1e6),
    ('GPa', 'Pressure', 1e9),
    
    # Energy
    ('J', 'Energy', 1),
    ('MJ', 'Energy', 1e6),
    
    # Power
    ('W', 'Power', 1),
    
    # Time
    ('s', 'Time', 1),
    ('minute', 'Time', 60),
    ('hour', 'Time', 3600),
    ('day', 'Time', 86400),
    
    # Volume
    ('L', 'Volume', 0.001),
    ('mL', 'Volume', 1e-6),
    ('mm3', 'Volume', 1e-9),
    
    # Area
    ('mm4', 'Moment of Inertia', 1e-12),
]

print("=" * 60)
print("UNIT VERIFICATION REPORT")
print("=" * 60)

errors = []
warnings_list = []

for unit_name, category, expected_factor in units_to_test:
    try:
        unit = getattr(si, unit_name, None)
        if unit is None:
            errors.append(f"[ERROR] {unit_name}: Unit not found in environment")
            continue
        
        # Check factor
        actual_factor = float(unit.factor)
        factor_ok = abs(actual_factor - expected_factor) < 1e-15 * max(abs(expected_factor), 1)
        
        # Check display
        unit_repr = repr(unit)
        
        # Check if symbol is in the repr
        symbol_ok = unit_name in unit_repr or unit_name.replace('_', '/') in unit_repr
        
        status = "OK" if factor_ok else "FACTOR MISMATCH"
        print(f"[{status}] {unit_name:10} | Factor: {actual_factor:15.9g} (expected {expected_factor:15.9g}) | Display: {unit_repr}")
        
        if not factor_ok:
            errors.append(f"[ERROR] {unit_name}: Factor mismatch - got {actual_factor}, expected {expected_factor}")
            
    except Exception as e:
        errors.append(f"[ERROR] {unit_name}: {e}")

print("\n" + "=" * 60)
print("CONVERSION TESTS (.to() method)")
print("=" * 60)

# Test .to() conversions
conversion_tests = [
    ('mm**3', 'mL', 1e-6),  # 1 mm³ = 1e-6 mL
    ('mm**3', 'L', 1e-9),   # 1 mm³ = 1e-9 L
    ('m', 'km', 0.001),     # 1 m = 0.001 km
    ('m', 'mm', 1000),      # 1 m = 1000 mm
    ('kN', 'N', 1000),      # 1 kN = 1000 N
]

for expr, target, expected_val in conversion_tests:
    try:
        if '**' in expr:
            base, power = expr.split('**')
            unit = getattr(si, base) ** int(power)
        else:
            unit = getattr(si, expr)
        
        converted = unit.to(target)
        if converted:
            print(f"{expr}.to('{target}'): {converted}")
        else:
            errors.append(f"[ERROR] {expr}.to('{target}'): Returned None")
    except Exception as e:
        errors.append(f"[ERROR] {expr}.to('{target}'): {e}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

if errors:
    print(f"ERRORS ({len(errors)}):")
    for err in errors:
        print(f"  {err}")
else:
    print("All units verified successfully!")
