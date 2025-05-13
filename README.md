# Marmara Üniversitesi - Test Otomasyon Ödevi

Bu repo, öğrencilere yönelik **Test Otomasyon Araçları** dersi kapsamında verilen uygulamalı ödev içindir.

## 🎯 Ödevin Amacı
Basit bir web login sayfasında, otomasyon testi yazmak. Öğrencilerden beklenen, verilen senaryoyu kodla ifade etmeleri ve sonucu GitHub’a commit etmeleridir.

---

## ✅ Görevler

### 1. Uygulama Senaryosu:
- Tarayıcıyı aç
- Login sayfasına git: `https://the-internet.herokuapp.com/login`
- **Yanlış** kullanıcı adı veya şifre gir
- “Invalid credentials” (veya hata) mesajının görünüp görünmediğini kontrol et
- Testi çalıştır, sonucu gözlemle

### 2. Kullanılabilecek Araçlar:
- Tercihe göre:  
  - Java + Selenium  
  - Python + Selenium  
  - Playwright veya Cypress (isteğe bağlı)

---

## 📁 Dizin Yapısı Örneği

```bash
📁 your-project-folder/
 ┣ 📁 tests/
 ┃ ┗ test_login_invalid.py (veya .java)
 ┣ 📄 README.md
 ┗ 📷 test-sonucu.png (ekran görüntüsü)
