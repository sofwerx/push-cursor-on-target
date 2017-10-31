import datetime as dt
import uuid
import xml.etree.ElementTree as ET
import socket
import logging

logger = logging.getLogger("django")

ID = {
    "pending": "p",
    "unknown": "u",
    "assumed-friend": "a",
    "friend": "f",
    "neutral": "n",
    "suspect": "s",
    "hostile": "h",
    "joker": "j",
    "faker": "f",
    "none": "o",
    "other": "x"
}
DIM = {
    "space": "P",
    "air": "A",
    "land-unit": "G",
    "land-equipment": "G",
    "land-installation": "G",
    "sea-surface": "S",
    "sea-subsurface": "U",
    "subsurface": "U",
    "other": "X"
}

DATETIME_FMT = "%Y-%m-%dT%H:%M:%SZ"

class CursorOnTarget:

    def atoms(__self, unit):
        timer = dt.datetime
        now = timer.utcnow()
        zulu = now.strftime(DATETIME_FMT)

        stale_now = now.replace(minute=now.minute + 1)
        stale = stale_now.strftime(DATETIME_FMT)

        unit_id = ID[unit["identity"]] or ID["none"]
    
        cot_type = "a-" + unit_id + "-" + DIM[unit["dimension"]]

        if "type" in unit:
          cot_type = cot_type + "-" + unit["type"]

        if "uid" in unit:
          cot_id = unit["uid"]
        else:
          cot_id = uuid.uuid4().get_hex()

        evt_attr = {
            "version": "2.0",
            "uid": cot_id,
            "time": zulu,
            "start": zulu,
            "stale": stale,
            "type": cot_type
        }

        pt_attr = {
            "lat": str(unit["lat"]),
            "lon":  str(unit["lon"]),
            "hae": "1",   #unit["hae"],
            "ce": "50",    #unit["ce"],
            "le": "50"     #unit["le"]1
        }
    
        cot = ET.Element('event', attrib=evt_attr)
        ET.SubElement(cot, 'detail')
        ET.SubElement(cot,'point', attrib=pt_attr)
    
        cot_xml = '<?xml version="1.0" standalone="yes"?>' + ET.tostring(cot)
        return cot_xml

    def pushUDP(__self, ip_address, port, cot_xml):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sent = sock.sendto(cot_xml, (ip_address, port))
        return sent

