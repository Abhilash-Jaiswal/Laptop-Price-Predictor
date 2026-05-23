import pickle

path = r"c:\Users\ABHILASH JAISWAL\Desktop\hbtu\Krish Naik Udamy\MyCode\Laptop Price Predictor\df.pkl"
with open(path, 'rb') as f:
    data = f.read()
keys = [b'ppi', b'PPI', b'TouchScreen', b'Touchscreen', b'IPS Panel', b'IPS', b'Company', b'TypeName', b'Cpu Brand', b'Gpu Brand', b'os', b'HDD', b'SSD', b'Weight', b'Ram']
print([k.decode() for k in keys if k in data])
strings = []
cur = b''
for b in data:
    if 32 <= b < 127:
        cur += bytes([b])
    else:
        if len(cur) >= 4:
            strings.append(cur.decode('ascii', errors='ignore'))
        cur = b''
if len(cur) >= 4:
    strings.append(cur.decode('ascii', errors='ignore'))
for s in strings:
    if any(x in s for x in ['ppi', 'PPI', 'Touch', 'IPS', 'Company', 'TypeName', 'Cpu', 'Gpu', 'os', 'HDD', 'SSD', 'Weight', 'Ram']):
        print(s)
