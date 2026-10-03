import socket
import ssl
import urllib.request
from urllib.parse import urlparse


BANNER = r"""
███████╗██╗  ██╗ ██████╗ ███████╗██╗   ██╗
██╔════╝╚██╗██╔╝██╔═══██╗██╔════╝╚██╗ ██╔╝
█████╗   ╚███╔╝ ██║   ██║███████╗ ╚████╔╝
██╔══╝   ██╔██╗ ██║   ██║╚════██║  ╚██╔╝
███████╗██╔╝ ██╗╚██████╔╝███████║   ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝

        EXOSY OSINT - Açık Kaynak İstihbarat Aracı
"""


def hedefi_duzenle(hedef):
    """Girilen alan adını geçerli bir URL haline getirir."""
    hedef = hedef.strip()

    if not hedef.startswith(("http://", "https://")):
        hedef = "https://" + hedef

    return hedef


def alan_adi_bilgisi(url):
    """Alan adının temel DNS ve IP bilgilerini toplar."""
    alan_adi = urlparse(url).hostname

    print("\n[+] ALAN ADI BİLGİLERİ")
    print("-" * 50)
    print(f"Alan adı : {alan_adi}")

    try:
        ip = socket.gethostbyname(alan_adi)
        print(f"IP adresi: {ip}")

        bilgiler = socket.getaddrinfo(alan_adi, None)
        ipler = sorted(set(x[4][0] for x in bilgiler))

        print("\nBulunan IP adresleri:")

        for adres in ipler:
            print(f"  [+] {adres}")

    except socket.gaierror:
        print("[!] DNS bilgileri alınamadı.")


def http_bilgisi(url):
    """Web sunucusundan temel HTTP bilgilerini toplar."""
    print("\n[+] WEB SUNUCUSU BİLGİLERİ")
    print("-" * 50)

    try:
        istek = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Exosy-OSINT/1.0"
            }
        )

        with urllib.request.urlopen(istek, timeout=8) as cevap:
            print(f"HTTP Durumu : {cevap.status}")
            print(f"Son URL     : {cevap.geturl()}")

            server = cevap.headers.get("Server")

            if server:
                print(f"Sunucu      : {server}")
            else:
                print("Sunucu      : Belirtilmemiş")

            return cevap.headers

    except Exception as hata:
        print(f"[!] Site bilgileri alınamadı: {hata}")

    return None


def guvenlik_basliklari(headers):
    """Yaygın HTTP güvenlik başlıklarının bulunup bulunmadığını kontrol eder."""
    if not headers:
        return

    print("\n[+] GÜVENLİK BAŞLIKLARI")
    print("-" * 50)

    kontrol = {
        "Strict-Transport-Security": "HSTS",
        "Content-Security-Policy": "Content Security Policy",
        "X-Content-Type-Options": "Content Type Protection",
        "X-Frame-Options": "Clickjacking Protection",
        "Referrer-Policy": "Referrer Policy",
        "Permissions-Policy": "Permissions Policy",
    }

    for header, aciklama in kontrol.items():

        if headers.get(header):
            print(f"[✓] {aciklama}")

        else:
            print(f"[!] {aciklama}: Bulunamadı")


def ssl_bilgisi(url):
    """Hedefin SSL/TLS sertifikası hakkında temel bilgiler gösterir."""
    alan_adi = urlparse(url).hostname

    print("\n[+] SSL/TLS BİLGİLERİ")
    print("-" * 50)

    try:
        context = ssl.create_default_context()

        with socket.create_connection(
            (alan_adi, 443),
            timeout=8
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=alan_adi
            ) as ssock:

                sertifika = ssock.getpeercert()

                print(f"TLS sürümü : {ssock.version()}")

                issuer = dict(
                    x[0] for x in sertifika.get("issuer", [])
                )

                subject = dict(
                    x[0] for x in sertifika.get("subject", [])
                )

                print(
                    f"Sertifika  : "
                    f"{subject.get('commonName', 'Bilinmiyor')}"
                )

                print(
                    f"Sağlayıcı  : "
                    f"{issuer.get('organizationName', 'Bilinmiyor')}"
                )

                print(
                    f"Bitiş       : "
                    f"{sertifika.get('notAfter', 'Bilinmiyor')}"
                )

    except Exception as hata:
        print(f"[!] SSL/TLS bilgileri alınamadı: {hata}")


def main():

    print(BANNER)

    print(
        "[*] Bu araç eğitim ve güvenlik araştırmaları amacıyla "
        "hazırlanmıştır."
    )

    print(
        "[*] Yalnızca size ait veya inceleme izniniz bulunan "
        "sistemlerde kullanın.\n"
    )

    hedef = input(
        "[?] İncelenecek alan adını girin: "
    )

    url = hedefi_duzenle(hedef)

    print("\n" + "=" * 55)
    print(f" HEDEF: {url}")
    print("=" * 55)

    alan_adi_bilgisi(url)

    headers = http_bilgisi(url)

    guvenlik_basliklari(headers)

    ssl_bilgisi(url)

    print("\n" + "=" * 55)
    print("[✓] OSINT analizi tamamlandı.")
    print("=" * 55)


if __name__ == "__main__":
    main()
