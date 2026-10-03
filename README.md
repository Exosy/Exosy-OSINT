# 🔎 Exosy OSINT

**Türkçe • Basit • Terminal Tabanlı OSINT Aracı**

Açık kaynaklardan temel alan adı, web sunucusu ve güvenlik bilgilerini toplamak için geliştirilmiş Python tabanlı bir OSINT aracıdır.

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
- 🇹🇷 Türkçe terminal çıktısı
- 🐍 Python standart kütüphaneleriyle çalışma

---

## 🛡️ Kontrol Edilen Güvenlik Başlıkları

Araç aşağıdaki HTTP güvenlik başlıklarının bulunup bulunmadığını kontrol eder:

- `Strict-Transport-Security`
- `Content-Security-Policy`
- `X-Content-Type-Options`
- `X-Frame-Options`
- `Referrer-Policy`
- `Permissions-Policy`

Eksik olan güvenlik başlıkları terminal üzerinde kullanıcıya bildirilir.

---

## ⚙️ Gereksinimler

Projeyi çalıştırmak için:

- **Python 3.x**
- **İnternet bağlantısı**

gereklidir.

Proje Python standart kütüphanelerini kullandığından mevcut sürümde ek bir Python paketi yüklemeniz gerekmez.

---

## 🚀 Kurulum

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/Exosy/Exosy-OSINT.git
