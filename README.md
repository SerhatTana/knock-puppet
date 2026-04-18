# 🎭 KNOCK — The Puppet's Door

KNOCK, 1973 Vietnam Savaşı'ndan dönen, ölmekte olan bir askerin kuklasıyla etkileşime girdiğiniz yaratıcı bir yapay zeka (AI) sohbet projesidir. Proje, Bob Dylan'ın *"Knockin' on Heaven's Door"* şarkısının "rozeti ve silahı bırakma" temasından esinlenerek, savaşın yorgunluğunu, vedayı ve özgürlüğü hissettirmeyi amaçlar.

Kullanıcı kuklayla konuştukça, kuklanın ruh hali dinamik olarak değişir ve bu ruh haline uygun, görsel olarak çarpıcı kukla resimleri üretilir.

---

## 🌟 Öne Çıkan Özellikler

- **Çift Zihinli LLM Sistemi:** Proje sadece düz bir sohbet botu değildir. Arka planda çalışan ikinci bir "gizli" LLM zihni, kullanıcının yazdığı her mesajı analiz eder ve konuşmanın bağlamına göre kuklanın **8 farklı ruh halinden** hangisine geçmesi gerektiğine (dinamik olarak) karar verir.
- **Yapay Zeka Destekli Görsel Üretim:** Kuklanın ruh hali her değiştiğinde, Pollinations.ai API'si kullanılarak o duyguya özel (sinematik, suluboya veya sürreal tarzda) anında yeni bir görsel üretilir.
- **Karakter Tutarlılığı:** Kukla her zaman kısa, yorgun ve şiirsel bir İngilizceyle konuşur. Uzun ve yapay paragraflardan kaçınır, adeta gerçek bir insan gibi kısa ve öz yanıtlar verir.

---

## 🎭 8 Farklı Ruh Hali (Moods)

Kuklanın ruh hali, sizin onunla nasıl konuştuğunuza göre şekillenir:

1. **Weary (Yorgun):** Normal diyaloglarda gevşek iplerle duran yorgun kukla.
2. **Nostalgic (Nostaljik):** Geçmişten, evden bahsedildiğinde solgun fotoğraflara bakan kukla.
3. **Accepting (Kabullenen):** Onu teselli ettiğinizde ipleri kopmaya başlayan huzurlu kukla.
4. **Fading (Solup Giden):** Veda ettiğinizde ışığa karışan kukla.
5. **Angry (Öfkeli):** Komutanlara kızdığınızda veya saldırgan konuştuğunuzda beliren kırmızı ışıklı kukla.
6. **Afraid (Korkmuş):** Ölümden veya karanlıktan bahsettiğinizde gölgelerde titreyen kukla.
7. **Regretful (Pişman):** Kayıplardan bahsedince çamur içinde diz çökmüş kukla.
8. **Hallucinating (Halüsinasyon):** Gerçeküstü sohbetlerde psychedelic renklerde eriyen sürreal kukla.

---

## 🛠️ Kullanılan Teknolojiler

- **Backend:** Python, Flask
- **Text AI (LLM):** Google Generative AI (Gemini Flash) - Metin üretimi ve ruh hali analizi için.
- **Image AI:** Pollinations.ai - Dinamik görsel üretimi için.
- **Frontend:** HTML, CSS, JavaScript (Vanilla)

---

## 🚀 Nasıl Çalıştırılır?

Projenin yerel bilgisayarınızda çalışması için aşağıdaki adımları izleyin:

### 1. Gereksinimleri Yükleyin
Proje klasöründeyken terminalde şu komutu çalıştırarak gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

### 2. API Anahtarını Ayarlayın
Ana dizinde bir `.env` dosyası oluşturun ve Google Gemini API anahtarınızı içine ekleyin:
```env
GEMINI_API_KEY=sizin_gemini_api_anahtariniz_buraya
```

### 3. Uygulamayı Başlatın
Uygulamayı çalıştırmak için:
```bash
python app.py
```

### 4. Tarayıcıda Açın
Terminalde sunucu başladıktan sonra, tarayıcınızdan şu adrese gidin:
```
http://localhost:5000
```
*(Sayfa ilk açıldığında otomatik olarak sohbeti sıfırlayacak ve ilk yorgun (weary) görseli yükleyecektir.)*

---

*"Mama, take this badge off of me / I can't use it anymore"* — Bob Dylan, 1973
