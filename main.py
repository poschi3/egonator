import streamlit as st
import pandas as pd
import vgn
import egon

st.set_page_config(
    page_title="Egonator",
    page_icon="🚇",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

with st.sidebar:
    st.header("Eingaben")
    days = st.slider(
        "Betrachtungszeitraum",
        min_value=2,
        max_value=31,
        value=10
    )

    st.subheader("Herkömmlich")
    tarifstufe = st.selectbox(
        "Tarifstufe",
        options=vgn.TARIFSTUFEN.keys()
    )

    nbg = st.checkbox(
        "Nürnberg gestreift?",
        value=True
    )

    st.subheader("Egon")
    distance = st.number_input(
        "Einfache Distanz in km",
        value=10.0,
        step=0.1,
        min_value=0.1,
        max_value=200.0,
        format="%.1f"
    )

st.header("Kosten")
st.warning("Status: Experimental", icon="⚠️")

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
st.dataframe(chart_data)
