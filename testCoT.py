import os
import time
import CoT

ATAK_IP = os.getenv('ATAK_IP', '192.168.1.160')
ATAK_PORT = int(os.getenv('ATAK_PORT', '4242'))
ATAK_PROTO = os.getenv('ATAK_PROTO', 'UDP')

params = {  # SWX parking lot
    "lat": 27.957261,
    "lon": -82.436587,
    "uid": "Nerd Herd",
    "identity": "hostile",
    "dimension": "land-unit",
    "entity": "military",
    "type": "U-C"
#    "type": "U-C-R-H"
}

for i in range(0, 10):
    params["lat"] = params["lat"] + i/10000.0
    params["lon"] = params["lon"] + i/10000.0
    print "Params:\n" + str(params)
    cot = CoT.CursorOnTarget()
    cot_xml = cot.atoms(params)


    print "\nXML message:"
    print cot_xml
    
    print "\nPushing to ATAK..."
    if ATAK_PROTO == "TCP":
      sent = cot.pushTCP(ATAK_IP, ATAK_PORT, cot_xml)
    else
      sent = cot.pushUDP(ATAK_IP, ATAK_PORT, cot_xml)
    print str(sent) + " bytes sent to " + ATAK_IP + " on port " + str(ATAK_PORT)
    time.sleep(2)
