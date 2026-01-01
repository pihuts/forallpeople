import forallpeople as si
si.environment('structural')

print("=" * 50)
print("ALL AVAILABLE .to() KEYWORDS BY DIMENSION")
print("=" * 50)

print("\n--- VOLUME (e.g., L, m*mm**2) ---")
si.L.to()

print("\n--- LENGTH (e.g., m, mm, km) ---")
si.m.to()

print("\n--- FORCE (e.g., N, kN) ---")
si.N.to()

print("\n--- PRESSURE/STRESS (e.g., Pa, kPa, MPa) ---")
si.Pa.to()

print("\n--- ENERGY (e.g., J, kJ) ---")
si.J.to()

print("\n--- POWER (e.g., W) ---")
si.W.to()

print("\n--- AREA (e.g., m**2) ---")
(si.m**2).to()

print("\n--- MOMENT OF INERTIA (e.g., m**4) ---")
(si.m**4).to()

print("\n--- TIME (e.g., s) ---")
si.s.to()
