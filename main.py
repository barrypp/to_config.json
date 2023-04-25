import requests
import base64
import re
import json

import sys
sys.path.append(".")
import var

lines = base64.b64decode(requests.get(var.url).text)
j0 = json.loads(open("config.json").read())

for line in lines.splitlines():
    line = line.replace(b"vmess://", b"")
    j = json.loads(base64.b64decode(line+b"==="))
    j0[var.j1][0][var.j2][var.j3][0]['address'] = j['add']
    j0[var.j1][0][var.j2][var.j3][0]['port'] = int(j['port'])
    j0[var.j1][0][var.j2][var.j3][0]['users'][0]['id'] = j['id']
    name = re.compile('s[0-9]+').search(j['add']).group(0)
    open(f"config_{name}.json", "w").write(json.dumps(j0, indent=4))
