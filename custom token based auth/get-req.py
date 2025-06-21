import requests
import time

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdERldmljZTAxIiwiZXhwIjoxNzUwNTI0MTIxfQ.wJK8_ltJJhDcbjoW4nZDuEiUmYyhLSWQg2-d8JbotZg"

headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://r4201x19ib.execute-api.us-east-1.amazonaws.com/dev/device"

start_time = time.time()

response = requests.get(url, headers=headers)

end_time = time.time()
elapsed_time = end_time - start_time

print("Status code:", response.status_code)
print("Response body:", response.text)
print(f"Total authentication + response time: {elapsed_time:.3f} seconds")
