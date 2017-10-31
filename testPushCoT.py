import PushCoT

params = {  # SWX parking lot
    "lat": 27.957261,
    "lon": -82.436587,
    "identity": "friend",
    "dimension": "land-equipment",
    "entity": "military",
    "type": "E-V-A-T"
}

cot = PushCoT.CursorOnTarget()
cot_xml = cot.push(params)

print cot_xml
