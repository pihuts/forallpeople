import sys
import os
sys.path.insert(0, os.getcwd())
import forallpeople as si
si.environment('structural')
si.environment.auto_prefix = False

try:
    km = si.km
    m = si.m
    res = km / m
    print(f"km/m = {res}")
    
    L = si.L
    print(f"L value: {L.value}")
    print(f"L factor: {L.factor}")
    print(f"L repr: {L}")
    
    mL = si.mL
    print(f"mL value: {mL.value}")
    print(f"mL factor: {mL.factor}")
    print(f"mL repr: {mL}")
except Exception as e:
    print(e)
