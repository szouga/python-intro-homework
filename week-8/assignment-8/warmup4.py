# certifi==2026.10.23
# charset-normalizer==3.5.2
# idna==3.20
# requests==2.34.2
# urllib3==2.8.0

import requests

with open('requirements.txt', 'r', encoding="utf-16") as file:
    lines = file.readlines()
    number_version = 0
    for i in lines:
        if "requests" in i:
            number_version = i.replace("requests==", "")
                    
    print(f"requests version: {number_version}")
        
with open('requirements.txt', 'w', encoding="utf-8") as file:
    file.write(number_version)