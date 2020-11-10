import requests
for i in range(100):
    r=requests.get(f"http://10.10.150.152/th1s_1s_h1dd3n/?secret={i}")
    if b"wrong" not in r.content:
        print("Secret is",i)