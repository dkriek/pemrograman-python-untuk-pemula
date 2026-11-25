import os
import getpass

import requests


API_URL = "https://api.github.com/user/repos"


def ambil_semua_repository():
    # Gunakan environment variable bila tersedia; jika tidak, minta token
    # secara tersembunyi agar token tidak tersimpan di source code.
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        token = getpass.getpass("Masukkan GitHub token (input tidak terlihat): ").strip()

    if not token:
        raise RuntimeError("GitHub token tidak boleh kosong.")

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2026-03-10",
    }

    url = API_URL
    params = {"per_page": 100, "sort": "updated"}
    nomor_halaman = 1
    jumlah_repository = 0

    while url:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        repository_di_halaman = response.json()

        print(f"\nHalaman {nomor_halaman}: {len(repository_di_halaman)} repository")
        for repository in repository_di_halaman:
            print("-", repository["full_name"])

        jumlah_repository += len(repository_di_halaman)

        # GitHub memberi URL halaman selanjutnya melalui header Link.
        # Response.links adalah cara Requests membaca rel="next".
        url = response.links.get("next", {}).get("url")
        params = None  # URL halaman berikutnya sudah berisi query parameter.
        nomor_halaman += 1

    print(f"\nTotal repository yang dibaca: {jumlah_repository}")


if __name__ == "__main__":
    try:
        ambil_semua_repository()
    except RuntimeError as error:
        print(error)
    except requests.HTTPError as error:
        print("API mengembalikan HTTP error:", error.response.status_code)
        print("Periksa token dan permission yang diperlukan.")
    except requests.RequestException as error:
        print("Terjadi masalah saat menghubungi API:", error)
