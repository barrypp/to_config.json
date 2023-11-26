import requests
import base64
import re
import json

import sys
sys.path.append(".")
import var

lines = base64.b64decode(requests.get(var.url).text)
j0 = json.loads(open("config.json").read())

def do(jo,j,i,name):
    jo[var.j1][i][var.j2][var.j3][0]['address'] = j['add']
    jo[var.j1][i][var.j2][var.j3][0]['port'] = int(j['port'])
    jo[var.j1][i][var.j2][var.j3][0]['users'][0]['id'] = j['id']
    jo[var.j1][i]["tag"] = f"vps_{name}"

i = 0
for line in lines.splitlines():

    line = line.replace(b"vmess://", b"")
    j = json.loads(base64.b64decode(line+b"==="))
    name = re.compile('s[0-9]+').search(j['ps']).group(0)

    do(j0,j,i,name)
    i += 1 
    if i >= 4:
        break

open(f"config.json", "w").write(json.dumps(j0, indent=2))
