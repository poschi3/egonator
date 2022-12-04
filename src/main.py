import streamlit as st
import pandas as pd
import vgn
import egon

st.set_page_config(
    page_title="Egonator",
    page_icon="🚇",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/poschi3/egonator/issues",
        "Report a bug": "https://github.com/poschi3/egonator/issues",
        "About": 
"""
# Kleiner Vergleichsrechner

* [Fork me on GitHub](https://github.com/poschi3/egonator)
* [VGN Preisliste](https://www.vgn.de/media/preistabelle-2022.pdf)
* [Egon Preisliste](https://www.vgn.de/egon/kosten)
"""
    }
)

with st.sidebar:
    st.header("Anleitung")
    st.markdown(
"""
Hier wird der [VGN-Tarif](https://www.vgn.de/media/preistabelle-2022.pdf) mit dem 
[Egon-Tarif](https://www.vgn.de/egon/kosten) verglichen. Wir betrachten ein 
PendlerInnen-Szenario: Jeder Tag entspricht zwei Fahrten.
"""
    )
    days = st.slider("Anzahl Pendeltage", value=10, min_value=2, max_value=31)

    st.subheader("VGN-Tarif")
    st.markdown(
"""
Tarifstufe für die Pendelstrecke. Kann über die [VGN-Auskunft](https://www.vgn.de/verbindungen/)
ermittelt werden.
"""
    )
    tarifstufe = st.selectbox("Tarifstufe", options=vgn.TARIFSTUFEN.keys())

    st.subheader("Egon-Tarif")
    st.markdown(
"""
Gesamtkilometer für eine einfache Fahrt entsprechend der [Egon-Auskunft](https://www.vgn.de/egon/preisinfo).
Addiere die Kilometer falls sie auf mehrere Rabattstufen aufteilt werden.
"""
    )
    distance = st.number_input("Einfache Entfernung in km",
        value=10.0,
        step=0.1,
        min_value=0.1,
        max_value=200.0,
        format="%.1f"
    )
    nbg = st.checkbox("Zone 100 oder 200 (Nürnberg) berührt?", value=True)



st.title("🚇 Egonator")
st.warning(
"""Status: Experimentell. Der neue Tarif ist so kompliziert, dass ich nicht garantieren kann,
dass alle Rabatte komplett richtig berechnet werden.
""",
    icon="⚠️")
st.header("Kosten")

data = []
for day in range(1, days + 1):
    data.append([
        day,
        vgn.single_online(day, tarifstufe),
        vgn.day(day, tarifstufe),
        vgn.TARIFSTUFEN[tarifstufe].solo_31,
        egon.price_for_days(day, distance, nbg)
    ])

chart_data = pd.DataFrame(
    data,
    columns=["Tag", "Einzelfahrkarte", "Tagesticket", "Solo 31", "Egon"]
)

st.line_chart(chart_data, height=800,x="Tag",y=["Einzelfahrkarte", "Tagesticket", "Solo 31", "Egon"])
#st.dataframe(chart_data)
