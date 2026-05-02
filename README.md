# 🎭 KNOCK — The Puppet's Door

KNOCK, 1973 Vietnam Savaşı'ndan dönen, ölmekte olan bir askerin kuklasıyla etkileşime girdiğiniz **üst düzey (premium) bir yapay zeka deneyimidir.** Bob Dylan'ın *"Knockin' on Heaven's Door"* şarkısından ilham alan bu proje; savaşın yorgunluğunu, vedayı ve özgürlüğü "Department of Records" estetiğiyle sunar.

Sadece bir sohbet botu değil; ses, görüntü ve atmosferin birleştiği interaktif bir hikaye anlatımıdır.

---

## 🌟 Öne Çıkan Özellikler

- **Gelişmiş LLM Mimarisi (Gemini 2.5 Flash):** Proje, hem ana sohbet hem de arka plandaki "Dinamik Ruh Hali Analizi" için en güncel Gemini modelini kullanır. Kukla, mesajlarınızı analiz ederek **8 farklı duygu durumuna** geçiş yapar.
- **Karakter ve Görsel Tutarlılık:** Stable Diffusion (Pollinations.ai) entegrasyonu; sabit tohum (seed) ve detaylı karakter promptları kullanılarak kuklanın görsel kimliğinin her mesajda korunmasını sağlar.
- **Profesyonel Ses Sentezi (Google Cloud TTS):** Kukla artık sadece yazmıyor, konuşuyor. Ruh haline göre tonlaması değişen, SSML ile zenginleştirilmiş gerçekçi bir "yorgun asker" sesiyle yanıt verir.
- **Sinematik Arayüz:** Tailwind CSS ile tasarlanmış, 1970'lerin askeri kayıt ofisi havasında; film greni, daktilo efektleri ve "Department of Records" temalı premium UI.
- **Atmosferik Ses Deneyimi:** Arka planda çalan Bob Dylan klasiği ve ses seviyesini kontrol edebileceğiniz interaktif slider ile tam bir atmosfer sunar.
- **Bypass Autoplay Policy:** Tarayıcıların ses engelleme politikasını aşan özel "Enter the Archive" giriş ekranı.

---

## 🎭 8 Farklı Ruh Hali (Moods)

Kuklanın dünyası sizin sözlerinizle şekillenir:

1. **Weary (Yorgun):** Varsayılan hali; ipleri gevşek, başı eğik.
2. **Nostalgic (Nostaljik):** Geçmişten veya evden bahsettiğinizde solgun fotoğraflara odaklanır.
3. **Accepting (Kabullenen):** Huzur bulduğunda iplerinin kopmaya başladığı an.
4. **Fading (Solup Giden):** Vedalarda ışığa ve toza karışan silüet.
5. **Angry (Öfkeli):** Çatışma ve öfke anlarında beliren sert, kırmızı ışıklı atmosfer.
6. **Afraid (Korkmuş):** Karanlık ve ölüm karşısında gölgelere sığınan kukla.
7. **Regretful (Pişman):** Yağmur altında, çamurda diz çökmüş hüzünlü hali.
8. **Hallucinating (Halüsinasyon):** Gerçekliğin kaybolduğu, psychedelic renklerin hakim olduğu sürreal anlar.

---

## 🛠️ Teknolojik Altyapı

- **Motor:** Python / Flask
- **Zeka (LLM):** Google Gemini 2.5 Flash
- **Görsel (Image Gen):** Stable Diffusion (via Pollinations API)
- **Ses (Voice):** Google Cloud Text-to-Speech
- **Stil:** HTML5 / Tailwind CSS / Vanilla JS

---

## 🚀 Kurulum ve Çalıştırma

### 1. Ortamı Hazırlayın
```bash
pip install -r requirements.txt
```

### 2. API Anahtarlarını Tanımlayın
`.env` dosyanıza şu anahtarları ekleyin:
```env
GEMINI_API_KEY=sizin_gemini_anahtariniz
GOOGLE_API_KEY=sizin_google_tts_anahtariniz
```

### 3. Arka Plan Müziği
`static/audio/background.mp3` yoluna dilediğiniz atmosferik müziği yerleştirin.

### 4. Başlatın
```bash
python app.py
```
`http://localhost:5000` adresine gidin ve "Enter the Archive" diyerek dosyaları açın.

---

*"Mama, take this badge off of me / I can't use it anymore"* — Bob Dylan, 1973
