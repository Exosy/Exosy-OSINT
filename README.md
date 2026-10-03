# 🔎 Exosy OSINT

/h1 p align="center"> b Türkçe • Basit • Terminal Tabanlı OSINT /b /p p align="center"> Açık kaynaklardan temel alan adı, web sunucusu ve güvenlik bilgilerini toplamak için geliştirilmiş Python tabanlı bir OSINT aracıdır. /p

---

## 🕵️ Exosy OSINT Nedir?

**Exosy OSINT**, siber güvenlik ve OSINT alanında kendimi geliştirmek amacıyla geliştirdiğim terminal tabanlı bir Python projesidir.

Bir alan adı üzerinden erişilebilen temel teknik bilgileri toplar ve sonuçları anlaşılır bir şekilde terminal üzerinde gösterir.

> 🎯 Projenin temel amacı OSINT, web teknolojileri, ağ yapıları ve Python konusunda pratik yapmaktır.

---

## ✨ Özellikler

- 🌐 Alan adı analizi
- 📡 DNS ve IP adresi sorgulama
- 🖥️ Web sunucusu bilgilerinin görüntülenmesi
- 📋 HTTP durum kodunun kontrol edilmesi
- 🛡️ HTTP güvenlik başlıklarının analizi
- 🔒 SSL/TLS sertifika bilgilerinin görüntülenmesi
- 🔐 TLS sürümünün tespit edilmesi
- 🇹🇷 Tamamen Türkçe terminal çıktısı
- 🐍 Ek paket gerektirmeden Python ile çalışma

---

## 🔍 Kontrol Edilen Güvenlik Başlıkları

Araç aşağıdaki HTTP güvenlik başlıklarının bulunup bulunmadığını kontrol eder:

```text
Strict-Transport-Security
Content-Security-Policy
X-Content-Type-Options
X-Frame-Options
Referrer-Policy
Permissions-Policy
```

Eksik olan güvenlik başlıkları terminal üzerinde kullanıcıya bildirilir.

---

## ⚙️ Gereksinimler

Projeyi çalıştırmak için:

```text
Python 3.x
İnternet bağlantısı
```

gereklidir.

Proje Python standart kütüphanelerini kullandığından ek bir paket yüklenmesine ihtiyaç duymaz.

---

## 🚀 Kurulum

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/Exosy/Exosy-OSINT.git
```

Proje klasörüne girin:

```bash
cd Exosy-OSINT
```

Aracı çalıştırın:

```bash
python osint.py
```

Bazı sistemlerde:

```bash
python3 osint.py
```

kullanmanız gerekebilir.

---

## 💻 Kullanım

Program çalıştırıldığında analiz etmek istediğiniz alan adını girin:

```text
[?] İncelenecek alan adını girin: example.com
```

Ardından Exosy OSINT hedef hakkında temel bilgileri toplamaya başlayacaktır.

---

## 📊 Örnek Çıktı

```text
=======================================================
 HEDEF: https://example.com
=======================================================

[+] ALAN ADI BİLGİLERİ
--------------------------------------------------
Alan adı : example.com
IP adresi: xxx.xxx.xxx.xxx

[+] WEB SUNUCUSU BİLGİLERİ
--------------------------------------------------
HTTP Durumu : 200
Son URL     : https://example.com
Sunucu      : Belirtilmemiş

[+] GÜVENLİK BAŞLIKLARI
--------------------------------------------------
[✓] HSTS
[!] Content Security Policy: Bulunamadı
[✓] Content Type Protection
[!] Clickjacking Protection: Bulunamadı

[+] SSL/TLS BİLGİLERİ
--------------------------------------------------
TLS sürümü : TLSv1.3
Sertifika  : example.com

=======================================================
[✓] OSINT analizi tamamlandı.
=======================================================
```

> IP ve diğer bilgiler yalnızca örnek gösterim amacıyla verilmiştir.

---

## 📁 Proje Yapısı

```text
Exosy-OSINT/
│
├── osint.py
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🧠 Bu Projede Neler Öğreniyorum?

Bu proje üzerinde çalışırken özellikle şu alanlarda kendimi geliştirmeyi hedefliyorum:

- OSINT metodolojileri
- Python
- DNS yapısı
- IP ve alan adı analizi
- HTTP protokolü
- HTTP güvenlik başlıkları
- SSL/TLS
- Web güvenliği
- Ağ teknolojileri

---

## 🗺️ Gelecek Planları

Projeye ilerleyen sürümlerde eklenebilecek özellikler:

- [ ] WHOIS sorgulama
- [ ] DNS kayıtlarının detaylı görüntülenmesi
- [ ] Subdomain analizi
- [ ] Sonuçların JSON formatında kaydedilmesi
- [ ] Sonuçların TXT raporu olarak oluşturulması
- [ ] Daha gelişmiş hata yönetimi
- [ ] Terminal arayüzünün geliştirilmesi
- [ ] Modüler proje yapısı

---

## ⚠️ Etik Kullanım

Bu proje **eğitim, OSINT araştırmaları ve siber güvenlik öğrenimi** amacıyla geliştirilmiştir.

Kullanıcı, gerçekleştirdiği işlemlerin yürürlükteki kurallara ve yetkilendirme kapsamına uygun olmasından sorumludur.

Güvenlik testleri yalnızca **size ait olan veya test etme izniniz bulunan sistemlerde** gerçekleştirilmelidir.

---

## 👨‍💻 Geliştirici

**Exosy**

Siber güvenlik, etik hacking, web güvenliği ve OSINT alanlarında kendimi geliştiriyor ve öğrendiklerimi açık kaynak projeler aracılığıyla paylaşıyorum.

---

\<p align="center">
&#x20; \<b>🔎 Araştır • 🧠 Öğren • 🛡️ Güvenliği Anla\</b>
\</p>

\<p align="center">
&#x20; ⭐ Projeyi faydalı bulduysanız yıldız bırakabilirsiniz.
\</p>
