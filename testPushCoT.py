import PushCoT

params = {  # SWX parking lot
    "lat": 27.957261,
    "lon": -82.436587,
    "identity": "friend",
    "dimension": "land-equipment",
    "entity": "military",
    "type": "E-V-A-T"
}

cot_xml = PushCoT.push_atoms(params)

print cot_xml
