import os
import CoT

ATAK_IP = "192.168.1.160"
if "ATAK_IP" in os.environ:
  ATAK_IP = os.environ["ATAK_IP"]

ATAK_PORT = 4242
if "ATAK_PORT" in os.environ:
  ATAK_PORT = int(os.environ["ATAK_PORT"])

params = {  # SWX parking lot
    "lat": 27.957261,
    "lon": -82.436587,
    "uid": "SWX",
    "identity": "friend",
    "dimension": "land-equipment",
    "entity": "military",
#    "type": "E-V-A"
}

print "Params:\n" + str(params)
cot = CoT.CursorOnTarget()
cot_xml = cot.atoms(params)

print "\nXML message:"
print cot_xml

print "\nPushing to ATAK..."
sent = cot.pushUDP(ATAK_IP, ATAK_PORT, cot_xml)
print str(sent) + " bytes sent to " + ATAK_IP + " on port " + str(ATAK_PORT)
