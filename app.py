import streamlit as st
st.markdown("""
<style>
.stApp {
    background-color: #E8A0BF;
}

h1 {
    color: #D63384;
}

.stButton > button {
    background-color: #FF69B4;
    color: white;
    border-radius: 12px;
    border: none;
}

.stButton > button:hover {
    background-color: #D63384;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("Harcama Takipçisi")
st.write("Kişisel bütçeni kolayca takip et.")
if "toplam" not in st.session_state:
    st.session_state.toplam = 0.0
harcama = st.number_input("Harcama miktarı (TL)", min_value=0.0, step=10.0)
if st.button("Harcama ekle"):
    st.session_state.toplam += harcama
    st.write("Harcama eklendi!")
    st.write("Toplam harcama:", st.session_state.toplam, "TL")
if st.button("Harcamaları sıfırla"):
    st.session_state.toplam = 0.0
    st.write("Harcamalar sıfırlandı!")