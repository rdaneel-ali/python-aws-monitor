import requests

def check_url(url, timeout=5):
    try:
        r = requests.get(url, timeout=timeout)
        return r.status_code == 200, r.status_code
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    urls = ["https://example.com", "https://python.org"]
    for u in urls:
        ok, info = check_url(u)
        print(u, ok, info)
