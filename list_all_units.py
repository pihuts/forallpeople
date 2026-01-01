
import json
import os
import glob
from collections import defaultdict
from forallpeople.dimensions import Dimensions

def list_units():
    env_dir = r"c:\Users\peter\OneDrive\Documents\forallpeople\forallpeople\environments"
    json_files = glob.glob(os.path.join(env_dir, "*.json"))
    
    units_by_dim = defaultdict(set)
    
    for json_file in json_files:
        env_name = os.path.basename(json_file).replace(".json", "")
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for unit_name, defs in data.items():
                    if "Dimension" in defs:
                        dim = tuple(defs["Dimension"])
                        units_by_dim[dim].add(unit_name)
        except Exception as e:
            print(f"Error reading {env_name}: {e}")

    # SI Base Units (always available)
    # Mass, Length, Time, Current, Intensity, Temp, Amount
    base_units = {
        "kg": (1, 0, 0, 0, 0, 0, 0),
        "m": (0, 1, 0, 0, 0, 0, 0),
        "s": (0, 0, 1, 0, 0, 0, 0),
        "A": (0, 0, 0, 1, 0, 0, 0),
        "cd": (0, 0, 0, 0, 1, 0, 0),
        "K": (0, 0, 0, 0, 0, 1, 0),
        "mol": (0, 0, 0, 0, 0, 0, 1),
    }
    for name, dim in base_units.items():
        units_by_dim[dim].add(name)

    with open("units_list_final.txt", "w", encoding="utf-8") as f:
        f.write("# All Available Units for Conversion\n\n")
        f.write("Units are grouped by their physical dimension. You can convert between any units in the same group.\n\n")
        
        # Sort by dimension tuple for consistency
        sorted_dims = sorted(units_by_dim.keys())
        
        for dim in sorted_dims:
            units = sorted(list(units_by_dim[dim]))
            # Try to give a hint of what the dimension is based on common units
            hint = ""
            if "m" in units: hint = "(Length)"
            elif "kg" in units: hint = "(Mass)"
            elif "s" in units: hint = "(Time)"
            elif "N" in units: hint = "(Force)"
            elif "Pa" in units: hint = "(Pressure)"
            elif "J" in units: hint = "(Energy)"
            elif "W" in units: hint = "(Power)"
            elif "A" in units: hint = "(Current)"
            elif "V" in units: hint = "(Voltage)"
            elif "C" in units: hint = "(Charge)"
            
            f.write(f"## Dimension {dim} {hint}\n")
            f.write(f"**Units**: {', '.join(units)}\n")
            f.write("\n")

if __name__ == "__main__":
    list_units()
