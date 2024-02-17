import json
import sys
import cipheycore

data = ""
for line in sys.stdin:
    data += line

analysis = cipheycore.analyse_string(data)
freqs = {i: j / len(data) for i, j in analysis.freqs.items()}
print(json.dumps(freqs))
