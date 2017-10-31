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

print "Constructing XML with:"
print params
cot_xml = PushCoT.atoms_xml(params)

print "\nXML message:"
print cot_xml

print "\nPushing to ATAK..."
PushCoT.push_to_atak(ATAK_IP, ATAK_PORT, cot_xml)
