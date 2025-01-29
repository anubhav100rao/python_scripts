"""


columns = tile description products
I want to process excell file and load into multiple dimension array


"""


import requests
import pandas as pd

df = pd.read_excel("data.xlsx", sheet_name="Sheet1")


data = {
    "securityImpact": "ElevationOfPrivilege",
    "targetList": [{"product": "Azure", "componentName": "Azure Portal"}],
    "title": "Sample title",
    "description": "sample vul. description1\nsample vul. description2\nsample vul. description3\nsample vul. description4\nsample vul. description5",
    "reproductionSteps": "sample steps to reproduce1\nsample steps to reproduce2",
    "acknowledgements": [{"name": "Harsh vardhan", "emailAddress": "harshvardhan@microsoft.com", "company": "Microsoft", "companyUrl": "", "socialMediaUrl": ""}],
    "uri": "Sample vulnerability URL"
}

bearer_token = ""

url = "https://api.msrc.microsoft.com/portal/v2.0/vulnerabilityReport"

headers = {
    # "Content-Length": "533",
    # "X-Request-Id": "112d8357-4fbf-4803-9307-812527a5a7ed",
    "Authorization": f"Bearer {bearer_token}",
    # "Cache-Control": "no-cache",
    # "Sec-Ch-Ua-Platform": "\"Windows\"",
    # "Pragma": "no-cache",
    # "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    # "Sec-Ch-Ua-Mobile": "?0",
    # "Request-Id": "112d8357-4fbf-4803-9307-812527a5a7ed",
    # "Access-Control-Allow-Origin": "*",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    # "Accept": "application/json, text/plain, /",
    # "Content-Type": "application/json",
    # "Origin": "https://msrc.microsoft.com",
    # "Sec-Fetch-Site": "same-site",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Dest": "empty",
    # "Referer": "https://msrc.microsoft.com/",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "en-US,en;q=0.9",
    # "Priority": "u=1, i"
}




response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
