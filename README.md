# Kalkınmanın Ağacı

Kalkınma iktisadının düşünsel köklerinden günümüze tarihsel gelişimini anlatan etkileşimli bir web sitesidir. Site her dönemi tarihsel arka plan, ana temalar, modeller ve kuramlar ile eleştiriler başlıkları altında ele almaktadır. Sayfa aşağı kaydırıldıkça dönem pencereleri üst üste kaymakta ve arka plandaki fidan ağaca dönüşmektedir.

## İçerik

| Dosya | Açıklama |
| --- | --- |
| `index.html` | Ana site: kalkınma tanımları, BM Sürdürülebilir Kalkınma Amaçları ve sekiz dönem kartı |
| `zihin-haritasi.html` | Kalkınma iktisadının tarihsel gelişimine ilişkin etkileşimli zihin haritası |
| `app.py` | İki sayfayı sekmeler halinde sunan Streamlit uygulaması |
| `requirements.txt` | Streamlit bağımlılığı |

Her iki HTML dosyası da bağımsız olarak çalışmaktadır. Zihin haritası d3.js kütüphanesini cdnjs üzerinden yüklemektedir.

## Yayımlama

### GitHub Pages (önerilen)

1. Depoda **Settings → Pages** bölümüne gidin.
2. **Source** olarak `Deploy from a branch`, dal olarak `main` ve klasör olarak `/ (root)` seçin.
3. Site birkaç dakika içinde `https://ercumentlaleli.github.io/tarihselkalkinma/` adresinde yayına girer.

Bu yöntemde site tam ekran açılır ve mobil cihazlarda doğru çalışır.

### Streamlit Community Cloud

1. [share.streamlit.io](https://share.streamlit.io) adresinde GitHub hesabınızla oturum açın.
2. Bu depoyu, `main` dalını ve `app.py` dosyasını seçerek uygulamayı oluşturun.

Streamlit siteyi sabit yükseklikte bir çerçeve içinde gösterdiği için mobil cihazlarda deneyim sınırlı kalabilir.

### Yerel çalıştırma

```bash
pip install -r requirements.txt
streamlit run app.py
```

HTML dosyaları doğrudan tarayıcıda da açılabilir.
