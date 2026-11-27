"""Kalkınmanın Ağacı sitesini ve zihin haritasını Streamlit üzerinde yayımlar."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

KOK = Path(__file__).parent

st.set_page_config(page_title="Kalkınmanın Ağacı", layout="wide")
st.markdown(
    """
    <style>
      .block-container {padding: 0.5rem 0 0 0 !important; max-width: 100% !important;}
      header, footer {visibility: hidden;}
      .stTabs [data-baseweb="tab-list"] {padding-left: 1rem;}
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
