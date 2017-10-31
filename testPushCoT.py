import PushCoT

ATAK_IP = "192.168.1.150"
ATAK_PORT = 4242

params = {  # SWX parking lot
    "lat": 27.957261,
    "lon": -82.436587,
    "identity": "friend",
    "dimension": "land-equipment",
    "entity": "military",
    "type": ""
}

print params
cot = PushCoT.CursorOnTarget()
cot_xml = cot.push(params)

print "\nXML message:"
print cot_xml

print "\nPushing to ATAK..."
cot.push_to_atak(ATAK_IP, ATAK_PORT, cot_xml)
