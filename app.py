"""Kalkınmanın Ağacı sitesini ve zihin haritasını Streamlit üzerinde yayımlar."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

KOK = Path(__file__).parent

st.set_page_config(page_title="Kalkınmanın Ağacı", layout="wide")
# Streamlit'in kendi başlık ve kenar boşlukları gizlenir; site çerçevesi ekranın
# görünen yüksekliğine uyarlanır. Böylece sayfa telefonda da tam ekran çalışır.
st.markdown(
    """
    <style>
      [data-testid="stHeader"], [data-testid="stToolbar"], footer {display: none !important;}
      [data-testid="stMainBlockContainer"], .block-container {
        padding: 0 !important; max-width: 100% !important;
      }
      [data-testid="stAppViewContainer"] {padding: 0 !important;}
      .stTabs [data-baseweb="tab-list"] {padding-left: 1rem; gap: 1.5rem;}
      .stTabs [data-baseweb="tab-panel"] {padding: 0 !important;}
      iframe {
        display: block; width: 100% !important;
        height: calc(100vh - 52px) !important;
        height: calc(100dvh - 52px) !important;
        border: 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

site = (KOK / "index.html").read_text(encoding="utf-8")
harita = (KOK / "zihin-haritasi.html").read_text(encoding="utf-8")

# Streamlit iframe içinde göreli bağlantıları açamadığı için kapanış kartındaki
# düğme, zihin haritasının üstteki sekmede yer aldığını belirten bir notla değiştirilir.
site = site.replace(
    '<a class="btn" href="zihin-haritasi.html">Ayrıntılı zihin haritasını açın ↗</a>',
    '<p class="turn"><b>Not:</b> Ayrıntılı zihin haritası sayfanın üstündeki '
    '"Zihin haritası" sekmesinde yer almaktadır.</p>',
)

sekme_site, sekme_harita = st.tabs(["Tarihsel gelişim", "Zihin haritası"])
with sekme_site:
    components.html(site, height=900, scrolling=True)
with sekme_harita:
    components.html(harita, height=1000, scrolling=True)
