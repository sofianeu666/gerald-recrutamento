
import streamlit as st

st.title("🪿 Recrutamento Gansal")
st.subheader("Departamento de RH do Gerald")

st.write(
    "Bem-vindo à entrevista. "
    "O Gerald está a avaliar a tua candidatura."
)

resposta = st.radio(
    "Qual é o dobro da metade de 4?",
    ["2", "4", "8"]
)

if st.button("Submeter resposta"):
    if resposta == "4":
        st.success("Resposta aceite. O Gerald está a observar-te.")
    else:
        st.error("Resposta errada. Vai contar migalhas.")
