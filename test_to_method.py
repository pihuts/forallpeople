import forallpeople as si
si.environment('structural')
si.environment.auto_prefix = False

print("--- Test: .to('mL') on mm**3 ---")
mm = si.mm
a = mm**3
print(f"a = {a}")
result = a.to("mL")
print(f"a.to('mL') = {result}")

print("\n--- Test: .to('L') on mm**3 ---")
result2 = a.to("L")
print(f"a.to('L') = {result2}")

print("\n--- Test: V_wood calculation ---")
v_wood = (70 * si.mm)**2 * (1.5 * si.m)
print(f"V_wood = {v_wood}")
v_wood_mL = v_wood.to("mL")
print(f"V_wood.to('mL') = {v_wood_mL}")
