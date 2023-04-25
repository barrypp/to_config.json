import requests
import json
import sys
sys.path.append(".")
import var

j = requests.get(var.api).json()

j['bw_counter'] = f"{j['bw_counter_b']/1024**3:.2f}GiB"
j['monthly_bw_limit'] = f"{j['monthly_bw_limit_b']/1024**3:.2f}GiB"
j['bw_percent'] = f"{j['bw_counter_b']/j['monthly_bw_limit_b']*100:.0f}%"
print(json.dumps(j, indent=4))