payload_einsatz = '''<?xml version="1.0" encoding="UTF-8"?>
<fireboardOperation version="1.0.3" test="true"> 
<uniqueId>123456</uniqueId>
<externalId>t01</externalId>
<source>test</source>
<basicData>
<externalNumber>OF120133</externalNumber>
<keyword>Test</keyword>
<announcement>Testeinsatz</announcement>
<location>Ravensburg, Pfannenstiel 31</location>
<geo_location>
<latitude>47.781767011396084</latitude>
<longitude>9.603345390692118</longitude>
</geo_location>
<timestampStarted>
<long>1696349826.8157475</long>
</timestampStarted>
</basicData>
</fireboardOperation>
'''

payload_status = '''<?xml version="1.0" encoding="UTF-8"?>
<fireboardStatus version="1.0">
<statusData>
<status>1</status>
<issi/>
<opta/>
<fms>A2897511</fms> 
<device_id>AK RV 75/11</device_id>
<timestamp>
<long>1458028846582</long>
</timestamp>
</statusData>
</fireboardStatus>
'''

link_e = "https://login.fireboard.net/api?authkey=U2jRwAvqSXU6Atosm2agI824JQ8tV0XO&call=operation_data"
link_s = "https://login.fireboard.net/api?authkey=zKKdXYN9BLTjOt6mBbaYGAY0P1T8GsSr&call=status_data"
headers = {'Content-Type':'xml'}
import requests
print (payload_einsatz)
r = requests.post(link_s, data = payload_status)
result = r.json()
print (result)
r = requests.post(link_e, data = payload_einsatz)
result = r.json()
print (result)