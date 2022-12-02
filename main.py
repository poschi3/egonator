import streamlit as st
import vgn
import egon

st.set_page_config(
    page_title="Egonator",
    page_icon="🚇",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

with st.sidebar:
    st.header("Eingaben")
    st.subheader("Herkömmlich")
    tarifstufe = st.selectbox("Tarifstufe", options=vgn.TARIFSTUFEN.keys())
    nbg = st.checkbox("Nürnberg gestreift?", value=True)

    st.subheader("Egon")
    distance = st.number_input("Einfache Distanz in km", value=5.0, step=0.1, min_value=0.1, max_value=200.0, format="%.1f")
    days = st.slider('Anzahl Tage an denen gereist wird', 1, 31, 5)

st.header("Kosten")
st.subheader("Herkömmlich")
vgn_single = vgn.TARIFSTUFEN[tarifstufe].single_online * 2 * days
vgn_day = vgn.TARIFSTUFEN[tarifstufe].day * days

st.markdown("Einzelfahrkarten: " + str(vgn_single) + " €")
st.markdown("Tageskarten: " + str(vgn_day) + " €")

st.subheader("Egon")
egon_price = egon.calc_basic_price(distance * 2 * days)
if nbg:
    egon_price += days * 2
else:
    egon_price += days
egon_price = egon.calc_discount(egon_price)

st.markdown(str(egon_price) + " €")
