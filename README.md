# 🎭 KNOCK — The Puppet's Door

KNOCK, 1973 Vietnam Savaşı'ndan dönen, ölmekte olan bir askerin kuklasıyla etkileşime girdiğiniz sinematik bir yapay zeka (AI) deneyimidir. Proje, Bob Dylan'ın *"Knockin' on Heaven's Door"* şarkısının "rozeti ve silahı bırakma" temasından esinlenerek; savaşın yorgunluğunu, vedayı ve özgürlüğü hissettirmeyi amaçlar.

Kullanıcı kuklayla konuştukça, kuklanın ruh hali dinamik olarak değişir, bu ruh haline uygun seslendirmeler yapılır ve görsel olarak tutarlı kukla resimleri üretilir.

---

## 🌟 Öne Çıkan Özellikler

- **Çift Zihinli LLM Sistemi:** Arka planda çalışan ikinci bir "gizli" LLM zihni (Gemini 2.5 Flash), kullanıcının mesajlarını analiz ederek kuklanın **8 farklı ruh halinden** hangisine geçmesi gerektiğine karar verir.
- **Yapay Zeka Destekli Görsel Üretim & Karakter Tutarlılığı:** Pollinations.ai API'si kullanılarak, her ruh hali için özel görseller üretilir. Sabit tohum (seed) ve detaylı karakter bazlı promptlar sayesinde kuklanın görsel kimliği tüm konuşma boyunca korunur.
- **Profesyonel Seslendirme (TTS):** Google Cloud Text-to-Speech API kullanılarak, kuklanın ruh haline göre değişen, SSML ile zenginleştirilmiş ("yorgun asker" tonunda) sesli yanıtlar üretilir.
- **Sinematik Tasarım:** "Department of Records" estetiğine sahip, Tailwind CSS ile modernleştirilmiş, daktilo efektleri ve film greni içeren premium bir arayüz.
- **Atmosferik Arka Plan Müziği:** Bob Dylan'ın klasiği eşliğinde, kullanıcıyı 1973'ün melankolik havasına sokan entegre ses sistemi.

---

## 🎭 8 Farklı Ruh Hali (Moods)

Kuklanın ruh hali, sizin onunla nasıl konuştuğunuza göre şekillenir:

1. **Weary (Yorgun):** Normal diyaloglarda gevşek iplerle duran yorgun kukla.
2. **Nostalgic (Nostaljik):** Geçmişten bahsedildiğinde solgun fotoğraflara bakan kukla.
3. **Accepting (Kabullenen):** Onu teselli ettiğinizde huzur bulan, ipleri kopmaya başlayan kukla.
4. **Fading (Solup Giden):** Veda ettiğinizde ışığa karışan kukla.
5. **Angry (Öfkeli):** Saldırgan konuşulduğunda beliren kırmızı ışıklı, öfkeli kukla.
6. **Afraid (Korkmuş):** Ölümden veya karanlıktan bahsettiğinizde gölgelerde titreyen kukla.
7. **Regretful (Pişman):** Kayıplardan bahsedince çamur içinde diz çökmüş kukla.
8. **Hallucinating (Halüsinasyon):** Gerçeküstü sohbetlerde psychedelic renklerde eriyen sürreal kukla.

---

## 🛠️ Kullanılan Teknolojiler

- **Backend:** Python, Flask
- **Text AI (LLM):** Google Generative AI (Gemini 2.5 Flash)
- **Image AI:** Pollinations.ai (Stable Diffusion)
- **Voice AI:** Google Cloud Text-to-Speech
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla)

---

## 🚀 Nasıl Çalıştırılır?

### 1. Gereksinimleri Yükleyin
```bash
pip install -r requirements.txt
```

### 2. API Anahtarlarını Ayarlayın
`.env` dosyası oluşturun ve aşağıdaki anahtarları ekleyin:
```env
GEMINI_API_KEY=sizin_gemini_api_anahtariniz
GOOGLE_API_KEY=sizin_google_cloud_tts_api_anahtariniz
```

### 3. Arka Plan Müziği
Proje klasörüne dilediğiniz bir MP3 dosyasını ekleyin (Örn: Bob Dylan).

### 4. Uygulamayı Başlatın
```bash
python app.py
```

### 5. Tarayıcıda Açın
`http://localhost:5000` adresine gidin ve "Enter the Archive" butonuna tıklayarak deneyimi başlatın.

---

*"Mama, take this badge off of me / I can't use it anymore"* — Bob Dylan, 1973
