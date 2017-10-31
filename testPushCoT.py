import PushCoT

ATAK_IP = "192.168.1.150"
ATAK_PORT = 4242

params = {  # SWX parking lot
    "lat": 27.957261,
    "lon": -82.436587,
    "uid": "SWX",
    "identity": "friend",
    "dimension": "land-equipment",
    "entity": "military",
    "type": ""
}

print "Params:\n" + str(params)
cot = PushCoT.CursorOnTarget()
cot_xml = cot.atoms(params)

print "\nXML message:"
print cot_xml

print "\nPushing to ATAK..."
sent = cot.pushUDP(ATAK_IP, ATAK_PORT, cot_xml)
print str(sent) + " bytes sent to " + ATAK_IP + ":" + str(ATAK_PORT)
