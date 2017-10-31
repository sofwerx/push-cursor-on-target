import time as t
import uuid
import xml.etree.ElementTree as ET

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

class CursorOnTarget:

    def push(unit):
        zulu = t.strftime("%Y-%m-%dT%H:%M:%SZ", t.gmtime())
        unit_id = ID[unit["identity"]] or ID["none"]
    
        cot_type = "a-" + unit_id + "-" + DIM[unit["dimension"]] + "-" + unit["type"]
        cot_id = uuid.uuid4().get_hex()
    
        evt_attr = {
            "version": "2.0",
            "uid": cot_id,
            "time": zulu,
            "start": zulu,
            "stale": zulu,
            "type": cot_type
        }

        pt_attr = {
            "lat": str(unit["lat"]),
            "lon":  str(unit["lon"]),
            "hae": "1",   #unit["hae"],
            "ce": "1",    #unit["ce"],
            "le": "1"     #unit["le"]1
        }
    
        cot = ET.Element('event', attrib=evt_attr)
        ET.SubElement(cot, 'detail')
        ET.SubElement(cot,'point', attrib=pt_attr)
    
        return ET.dump(cot)
