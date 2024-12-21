import streamlit as st
import pandas as pd
import vgn
import egon
import plotly.express as px

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
# Egonator der Vergleichsrechner

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
PendlerInnen-Szenario:
"""
    )
    days = 31

    rides_per_day = st.slider("Anzahl Fahrten pro Pendeltag", value=2, min_value=1, max_value=5)

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
Addiere die Kilometer falls sie auf mehrere Rabattstufen aufgeteilt werden.
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

    # st.subheader("Weitere Zeitkarten einblenden")
    # abo = st.checkbox("Abos")
    # mobi = st.checkbox("Mobi-Karte")
    # from_nine = st.checkbox("9 Uhr Abo / Mobi-Karten")


st.title("🚇 Egonator")
st.info(
"""Dieser Rechner ist noch experimentell. Feedback ist willkommen. Der [Quellcode](https://github.com/poschi3/egonator/) ist öffentlich 🙂
""", icon="ℹ️")

st.header("Kosten")

data = []
for day in range(1, days + 1):
    data.append([
        day,
        egon.price_for_days(day, distance, rides_per_day, nbg),
        vgn.single_online(day, tarifstufe, rides_per_day),
        vgn.day(day, tarifstufe),
        # vgn.TARIFSTUFEN[tarifstufe].solo_31,
        # vgn.TARIFSTUFEN[tarifstufe].abo_3,
        # vgn.TARIFSTUFEN[tarifstufe].abo_6,
        # vgn.TARIFSTUFEN[tarifstufe].abo_12,
        # vgn.TARIFSTUFEN[tarifstufe].abo_12_9,
        # vgn.TARIFSTUFEN[tarifstufe].mobi_9,
        # vgn.TARIFSTUFEN[tarifstufe].mobi_31
        58.00 # Deutschlandticket
    ])

chart_data = pd.DataFrame(
    data,
    columns=[
        "Pendeltage",
        "Egon",
        "Einzelfahrkarte",
        "Tagesticket",
        # "Solo 31",
        # "Abo 3",
        # "Abo 6",
        # "Jahres Abo",
        # "9 Uhr Jahres Abo",
        # "9 Uhr MobiCard",
        # "31 Tage MobiCard"
        "Deutschlandticket"
        ]
)

columns=["Pendeltage", "Egon", "Einzelfahrkarte", "Tagesticket", "Deutschlandticket"] #  "Solo 31"
# if abo:
#     columns.extend(["Abo 3", "Abo 6", "Jahres Abo"])
# if mobi:
#     columns.extend(["31 Tage MobiCard"])
# if from_nine:
#     columns.extend(["9 Uhr Jahres Abo", "9 Uhr MobiCard"])

# Create the Plotly figure
fig = px.line(chart_data, height=800, x="Pendeltage", y=columns,
              title="Kosten",
              labels={"value": "Kosten (€)", "variable": "Fahrkarte"},
              markers=True)

fig.update_traces(hovertemplate='%{fullData.name}<br>%{x} Pendeltage %{y:.2f} €<extra></extra>')

st.plotly_chart(fig, use_container_width=True)
