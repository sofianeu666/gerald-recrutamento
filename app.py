import random
import streamlit as st

st.set_page_config(page_title="O Número Secreto do Gerald", page_icon="🔢")


def html(texto):
    """Compacta HTML numa linha para o Markdown não o tratar como código."""
    return " ".join(linha.strip() for linha in texto.splitlines() if linha.strip())


# --------------------------------------------------
# VISUAL (as cores do Gerald)
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Source+Serif+4:wght@600;700&display=swap');

:root {
    --bg: #F5F2EC;
    --card: #FFFDFA;
    --accent: #C97852;
    --accent-dark: #8B4F35;
    --text: #29251F;
    --muted: #746B61;
    --border: #E5D7C8;
    --paper: #F0E5D9;
}

.stApp {
    background: var(--bg);
    color: var(--text);
    font-family: 'Plus Jakarta Sans', sans-serif;
}

h1 {
    color: var(--text) !important;
    font-family: 'Source Serif 4', serif !important;
}

.dossier {
    background: var(--card);
    border: 1px solid var(--border);
    border-top: 6px solid var(--accent);
    border-radius: 16px;
    padding: 20px 24px;
    margin: 16px 0;
}

.dossier-label {
    color: var(--accent-dark);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-size: 0.72rem;
    font-weight: 700;
}

.dossier ul {
    margin: 10px 0 0 0;
    padding-left: 20px;
    line-height: 1.8;
}

.dossier li::marker {
    color: var(--accent);
}

div[data-testid="stForm"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
}

div[data-testid="stExpander"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
}

div[data-testid="stAlert"] {
    background: var(--paper);
    border-left: 4px solid var(--accent);
    border-radius: 8px;
    color: var(--text);
}

div.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background: var(--accent);
    color: white;
    border: 1px solid var(--accent);
    border-radius: 10px;
    font-weight: 700;
    transition: 0.2s ease;
}

div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background: var(--accent-dark);
    border-color: var(--accent-dark);
    color: white;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# CONFIGURAÇÃO
# --------------------------------------------------

MINIMO, MAXIMO = 1, 100

# Probabilidade de a pista de um palpite falhado ser absurda (as outras são verdadeiras)
PROB_PISTA_ABSURDA = 0.25


# --------------------------------------------------
# TEXTOS
# --------------------------------------------------

# Pistas absurdas (frases completas, para depois de cada palpite)
PISTAS_ABSURDAS = [
    "O número é um número.",
    "O Gerald garante que o número não é nenhum animal. Exceto, talvez, ele próprio.",
    "O número está algures. O Gerald não pode dizer mais, é confidencial.",
    "Pista oficial: o número tem uma cor. O Gerald não vai dizer qual.",
    "O número é mais ou menos do tamanho de um ganso. Depende do ganso.",
    "O Gerald sonhou com o número, mas acordou antes do fim.",
    "O Gerald diz que o número prefere as terças-feiras.",
    "O número tem medo de formulários. Isto não ajuda ninguém, mas é verdade.",
    "O Gerald escreveu o número num post-it e perdeu o post-it.",
    "HONK. (O Gerald garante que isto é uma pista. Não é.)",
    "O número esteve de baixa médica na semana passada.",
    "A pista de hoje foi cancelada por falta de orçamento.",
    "O número não gosta de ser adivinhado. Tem direito a privacidade.",
    "O Gerald diz que estás «quente». Estava a falar da temperatura da sala.",
    "Pista confidencial: o número é exatamente o número que é.",
    "O Gerald pediu uma segunda opinião ao ganso do departamento ao lado. Também não sabe.",
    "Esta pista está sob análise jurídica.",
    "O número foi visto pela última vez perto da máquina do café.",
    "O Gerald pensou numa pista, mas ficou com fome e comeu-a.",
]

# Pistas absurdas para o dossier inicial (fragmentos que continuam «O número...»)
DOSSIER_ABSURDAS = [
    "é maior do que o infinito em pé",
    "tem a cor do número",
    "nunca foi visto ao pé de uma impressora",
    "é amigo do ganso do departamento ao lado",
    "não gosta de segundas-feiras",
    "é menor do que a paciência do Gerald",
    "assinou o livro de ponto às 9h07",
    "é mais alto do que o ganso do departamento ao lado",
]

# Comentários do Gerald a cada palpite falhado
COMENTARIOS = [
    "O Gerald anotou o teu palpite num formulário que ninguém vai ler.",
    "O Gerald olhou para ti três segundos a mais do que o necessário.",
    "O Gerald está a fingir que não está a gostar disto.",
    "O Gerald pediu um café. Não é para ele, é para a tensão.",
    "O Gerald carimbou o teu palpite. Não sabe porquê.",
    "Ouviu-se um HONK ao longe. Pode ou não ter sido o Gerald.",
    "O Gerald abriu uma ficha de ocorrência só para este palpite.",
    "O Gerald suspirou com a elegância de um funcionário em fim de contrato.",
    "O Gerald está a ajeitar a gravata. É mau sinal. Ou bom. Ele ainda não decidiu.",
    "O Gerald pediu uma reunião de alinhamento sobre este palpite.",
    "Um colega perguntou ao Gerald se estava tudo bem. Ele respondeu «tudo sob controlo» e escondeu a prancheta.",
    "O Gerald tentou parecer impassível. Falhou nas penas.",
    "O Gerald copiou o teu palpite para a ata. Com erros ortográficos.",
    "O Gerald disse «interessante» sem mexer o bico.",
]

# Comentários para palpites específicos
COMENTARIOS_ESPECIAIS = {
    1: "O 1? O Gerald respeita a ambição de quem começa pelo princípio.",
    7: "O 7. O Gerald diz que toda a gente tenta o 7. É estatística.",
    8: "O 8. O Gerald diz que isso é o infinito em pé e pediu que não o mexas.",
    13: "O 13. O Gerald fez uma pausa para uma cerimónia de mau agouro.",
    42: "O 42. O Gerald diz que essa é a resposta de outro jogo.",
    50: "O 50. O Gerald elogia a coragem de quem tenta sempre o meio.",
    69: "O 69. O Gerald corou e pediu que isto não conste da ata.",
    100: "O 100. O Gerald diz que quem começa pelo fim tem pouca paciência.",
}

# Comentários para marcos de tentativas
COMENTARIOS_MARCOS = {
    10: "Já vais em 10 tentativas. O Gerald abriu uma ficha de acompanhamento.",
    20: "20 tentativas. O Gerald começou a apostar com os colegas.",
    30: "30 tentativas. O Gerald trouxe uma cadeira.",
    50: "50 tentativas. O Gerald enviou um email aos Recursos Humanos. Ele é os Recursos Humanos.",
}


# --------------------------------------------------
# LÓGICA
# --------------------------------------------------

def factos(segredo, palpite=None, incluir_final=True):
    """Factos verdadeiros sobre o número, como fragmentos que continuam «O número...»."""
    algarismos = "um algarismo" if segredo < 10 else "dois algarismos" if segredo < 100 else "três algarismos"
    divisor = random.choice([3, 5, 7])
    limite_baixo = max(MINIMO - 1, segredo - random.randint(1, 40))
    limite_alto = min(MAXIMO + 1, segredo + random.randint(1, 40))

    lista = [
        "é par" if segredo % 2 == 0 else "é ímpar",
        f"tem {algarismos}",
        f"é múltiplo de {divisor}" if segredo % divisor == 0 else f"não é múltiplo de {divisor}",
        f"é maior do que {limite_baixo}",
        f"é menor do que {limite_alto}",
    ]

    if incluir_final:
        lista.append(f"termina em {segredo % 10}")

    if palpite is not None:
        # A pista clássica: mais alto ou mais baixo (com peso a dobrar)
        direcao = "é maior do que o teu palpite" if segredo > palpite else "é menor do que o teu palpite"
        lista += [direcao, direcao]

    return lista


def pistas_iniciais(segredo):
    """Dossier inicial: três pistas verdadeiras e uma absurda, por ordem aleatória."""
    dossier = random.sample(factos(segredo, incluir_final=False), 3)
    dossier.append(random.choice(DOSSIER_ABSURDAS))
    random.shuffle(dossier)
    return dossier


def novo_jogo():
    st.session_state.segredo = random.randint(MINIMO, MAXIMO)
    st.session_state.dossier = pistas_iniciais(st.session_state.segredo)
    st.session_state.palpites = []
    st.session_state.mensagem = None
    st.session_state.ultima_pista = None
    st.session_state.ultimo_comentario = None
    st.session_state.venceu = False


def nova_pista(palpite):
    # Evita repetir a mesma pista duas vezes seguidas
    for _ in range(10):
        if random.random() < PROB_PISTA_ABSURDA:
            pista = random.choice(PISTAS_ABSURDAS)
        else:
            abertura = random.choice([
                "O Gerald garante que o número",
                "Segundo o Gerald, o número",
                "O Gerald diz, com ar solene, que o número",
            ])
            pista = f"{abertura} {random.choice(factos(st.session_state.segredo, palpite))}."
        if pista != st.session_state.ultima_pista:
            break
    st.session_state.ultima_pista = pista
    return pista


def novo_comentario(palpite, tentativas):
    if palpite in COMENTARIOS_ESPECIAIS:
        return COMENTARIOS_ESPECIAIS[palpite]
    if tentativas in COMENTARIOS_MARCOS:
        return COMENTARIOS_MARCOS[tentativas]
    comentario = random.choice([c for c in COMENTARIOS if c != st.session_state.ultimo_comentario])
    st.session_state.ultimo_comentario = comentario
    return comentario


def mensagem_vitoria(tentativas):
    if tentativas <= 3:
        return "O Gerald ficou em silêncio. Adivinhaste depressa de mais. Isto vai dar um relatório."
    if tentativas <= 8:
        return "Acertaste! O Gerald aprova, com reservas e um carimbo."
    return "Acertaste, finalmente. O Gerald já ia abrir um processo por demora."


if "segredo" not in st.session_state:
    novo_jogo()


# --------------------------------------------------
# ECRÃ
# --------------------------------------------------

st.title("O Número Secreto do Gerald")
st.caption(
    f"O Gerald escolheu um número entre {MINIMO} e {MAXIMO}. "
    "Vai dar-te pistas. A maioria é séria. Algumas, nem por isso."
)

with st.expander("Instruções", expanded=not st.session_state.palpites):
    st.markdown(
        f"""
1. O Gerald escolheu um **número secreto entre {MINIMO} e {MAXIMO}**.
2. Escreve um palpite e carrega em **Tentar**.
3. O **dossier** já traz umas pistas à vista. Algumas são verdadeiras, outras são disparates do Gerald. Cabe-te a ti perceber quais.
4. Quando falhas, o Gerald dá uma **pista** (quase sempre verdadeira, de vez em quando absurda) e faz um **comentário**.
5. **Não podes repetir palpites.** Se repetires, o Gerald cobra taxa, mas a tentativa não conta.
6. Não há limite de tentativas, mas o Gerald está a contá-las.
7. Quando acertares, o Gerald reage consoante o tempo que demoraste.
"""
    )

itens = "".join(f"<li>{pista}</li>" for pista in st.session_state.dossier)
st.markdown(
    html(f"""
    <div class="dossier">
        <div class="dossier-label">Dossier deixado à vista pelo Gerald</div>
        <div>O número...</div>
        <ul>{itens}</ul>
    </div>
    """),
    unsafe_allow_html=True,
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
            tentativas = len(st.session_state.palpites)

            if palpite == st.session_state.segredo:
                st.session_state.venceu = True
                st.session_state.mensagem = ("sucesso", mensagem_vitoria(tentativas))
            else:
                st.session_state.mensagem = (
                    "info",
                    f"**Não é o {palpite}.** {nova_pista(palpite)}\n\n"
                    f"*{novo_comentario(palpite, tentativas)}*",
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
