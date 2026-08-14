import requests

url = "https://merolagani.com/LatestMarket.aspx"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("Status Code:", response.status_code)
print("URL:", response.url)
print("Content Length:", len(response.text))

if response.status_code == 200:
    print("✅ Website can be accessed")
else:
    print("❌ Website could not be accessed")

print("\nFirst 500 characters:")
print(response.text[:500])