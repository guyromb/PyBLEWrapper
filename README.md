Scanning Example:

```
from Libraries.Bluetooth.Bluetooth import *
import sys
import json

if len(sys.argv) < 4:
    sys.exit("Usage: %s device-type device-name timeout" % sys.argv[0])

results = "" # JSON
if sys.argv[1] == "ble":
    results = Bluetooth(Bluetooth.M_AUTO, sys.argv[2]).lescan(sys.argv[3], False)
    print(str(json.dumps(results)))
else:
    print("Device type is unknown")
```
