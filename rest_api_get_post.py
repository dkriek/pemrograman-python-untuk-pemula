import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BASE_URL = "https://jsonplaceholder.typicode.com"


def ambil_post(post_id):
    """Mengirim HTTP GET untuk mengambil satu post."""
    url = f"{BASE_URL}/posts/{post_id}"

    request = Request(url, method="GET")
    with urlopen(request, timeout=10) as response:
        print("GET status:", response.status)
        return json.loads(response.read().decode("utf-8"))


def buat_post():
    """Mengirim HTTP POST dengan body JSON untuk membuat post."""
    url = f"{BASE_URL}/posts"
    data_baru = {
        "userId": 1,
        "title": "Belajar REST API",
        "body": "Contoh mengirim data menggunakan HTTP POST.",
    }

    body = json.dumps(data_baru).encode("utf-8")
    request = Request(
        url,
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    with urlopen(request, timeout=10) as response:
        print("\nPOST status:", response.status)
        return json.loads(response.read().decode("utf-8"))


try:
    hasil_get = ambil_post(1)
    print("Data dari GET:")
    print(json.dumps(hasil_get, indent=2, ensure_ascii=False))

    hasil_post = buat_post()
    print("\nRespons dari POST:")
    print(json.dumps(hasil_post, indent=2, ensure_ascii=False))

except HTTPError as error:
    print("Server mengembalikan HTTP error:", error.code, error.reason)
except URLError as error:
    print("Tidak dapat terhubung ke API:", error.reason)
