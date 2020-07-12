# push-cursor-on-target
Send CoT message to mobile TAK device

Sample input data (JSON):
```
{
	"lat": 30.0090027,
	"lon": -85.9578735,
	"identity": "hostile",
	"dimension": "land-unit"
	"entity": "military",
	"type": "E-V-A-T"
}
```

identity may be one of: pending, unknown, friend, neutral, hostile, assumed-friend, suspect

dimension may be one of: unknown, space, air, land-unit, land-equipment, sea-surface, land-installation, subsurface (or sea-subsurface), other

entity may be: military, civilian

type is MIL-STD-2525 function code in CoT format (single letters separated by hyphens), will be appended as-is to CoT Type string 

Sample output data:
```
<?xml version="1.0" standalone="yes"?>
<event
	version="2.0"
	uid="J-01334"
    how="m-g"
	time="2017-10-30T11:43:38.07Z"
	start="2017-10-30T11:43:38.07Z"
	stale="2017-10-30T11:55:38.07Z"
    type="a-h-G">
		<detail></detail>
		<point
			lat="30.0090027"
			lon="-85.9578735"
			hae="1"
			ce="1"
			le="1"/>
</event>
```
