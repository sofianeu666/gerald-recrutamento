import random
import streamlit as st

st.set_page_config(page_title="O Número Secreto do Gerald", page_icon="🔢")

MINIMO, MAXIMO = 1, 100

# Pistas do Gerald: absurdas, inúteis e sem ajuda nenhuma
PISTAS = [
    "O número é um número.",
    "O Gerald garante que o número não é nenhum animal. Exceto, talvez, ele próprio.",
    "O número está algures. O Gerald não pode dizer mais, é confidencial.",
    "Pista oficial: o número tem uma cor. O Gerald não vai dizer qual.",
    "O número é mais ou menos do tamanho de um ganso. Depende do ganso.",
    "O Gerald sonhou com o número, mas acordou antes do fim.",
    "Segundo o regulamento interno, o número é maior do que zero.",
    "O Gerald diz que o número prefere as terças-feiras.",
    "O número tem medo de formulários. Isto não ajuda ninguém, mas é verdade.",
    "O Gerald escreveu o número num post-it e perdeu o post-it.",
    "HONK. (O Gerald garante que isto é uma pista. Não é.)",
    "O número esteve de baixa médica na semana passada.",
    "O Gerald jura que o número é par, ou ímpar, ou outra coisa. Não tem a certeza.",
    "A pista de hoje foi cancelada por falta de orçamento.",
    "O número não gosta de ser adivinhado. Tem direito a privacidade.",
    "O Gerald diz que estás «quente». Estava a falar da temperatura da sala.",
    "O número já foi mais pequeno. Ou maior. Depende do dia.",
    "Pista confidencial: o número é exatamente o número que é.",
    "O Gerald pediu uma segunda opinião ao ganso do departamento ao lado. Também não sabe.",
    "Esta pista está sob análise jurídica.",
    "O número foi visto pela última vez perto da máquina do café.",
    "O Gerald pensou numa pista, mas ficou com fome e comeu-a.",
]


def novo_jogo():
    st.session_state.segredo = random.randint(MINIMO, MAXIMO)
    st.session_state.palpites = []
    st.session_state.mensagem = None
    st.session_state.ultima_pista = None
    st.session_state.venceu = False


def nova_pista():
    # Evita repetir a mesma pista duas vezes seguidas
    pista = random.choice([p for p in PISTAS if p != st.session_state.ultima_pista])
    st.session_state.ultima_pista = pista
    return pista


def mensagem_vitoria(tentativas):
    if tentativas <= 3:
        return "O Gerald ficou em silêncio. Adivinhaste depressa de mais. Isto vai dar um relatório."
    if tentativas <= 8:
        return "Acertaste! O Gerald aprova, com reservas e um carimbo."
    return "Acertaste, finalmente. O Gerald já ia abrir um processo por demora."


if "segredo" not in st.session_state:
    novo_jogo()

st.title("O Número Secreto do Gerald")
st.caption(
    f"O Gerald escolheu um número entre {MINIMO} e {MAXIMO}. "
    "Vai dar-te pistas. Não vão ajudar."
)

if not st.session_state.venceu:
    with st.form("palpite"):
        palpite = st.number_input(
            "O teu palpite",
            min_value=MINIMO,
            max_value=MAXIMO,
            value=50,
            step=1,
        )
        tentar = st.form_submit_button("Tentar", use_container_width=True)

    if tentar:
        palpite = int(palpite)

        if palpite in st.session_state.palpites:
            st.session_state.mensagem = (
                "aviso",
                f"Já tentaste o {palpite}. O Gerald está a cobrar taxa por repetição.",
            )
        else:
            st.session_state.palpites.append(palpite)

            if palpite == st.session_state.segredo:
                st.session_state.venceu = True
                st.session_state.mensagem = (
                    "sucesso",
                    mensagem_vitoria(len(st.session_state.palpites)),
                )
            else:
                st.session_state.mensagem = (
                    "info",
                    f"**Não é o {palpite}.** {nova_pista()}",
                )

if st.session_state.mensagem:
    tipo, texto = st.session_state.mensagem
    {"info": st.info, "aviso": st.warning, "sucesso": st.success}[tipo](texto)

if st.session_state.palpites:
    st.write(
        f"**Tentativas ({len(st.session_state.palpites)}):** "
        + ", ".join(map(str, st.session_state.palpites))
    )

if st.session_state.venceu:
    st.balloons()
    st.write(f"O número secreto era o **{st.session_state.segredo}**.")

st.button("Novo jogo", on_click=novo_jogo)
