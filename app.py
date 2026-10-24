
import random
import time
import streamlit as st

st.set_page_config(
    page_title="O Número Secreto do Gerald",
    page_icon="🔢",
    layout="centered",
)


def html(texto):
    return " ".join(
        linha.strip()
        for linha in texto.splitlines()
        if linha.strip()
    )


# --------------------------------------------------
# CONFIGURAÇÃO
# --------------------------------------------------

MINIMO, MAXIMO = 1, 100

PROB_PISTA_ABSURDA = 0.25

PONTOS_INICIAIS = 1000
PENALIZACAO_TENTATIVA = 40
PENALIZACAO_SEGUNDO = 2
PENALIZACAO_REPETICAO = 25


# --------------------------------------------------
# ESTILO
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

h1, h2, h3 {
    color: var(--text) !important;
    font-family: 'Source Serif 4', serif !important;
}

.dossier, .welcome-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-top: 6px solid var(--accent);
    border-radius: 16px;
    padding: 22px 24px;
    margin: 16px 0;
}

.dossier-label, .welcome-label {
    color: var(--accent-dark);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-size: 0.72rem;
    font-weight: 700;
}

.dossier ul {
    margin-top: 12px;
    padding-left: 22px;
    line-height: 1.9;
}

.dossier li::marker {
    color: var(--accent);
}

.welcome-title {
    font-family: 'Source Serif 4', serif;
    font-size: 1.8rem;
    line-height: 1.2;
    margin: 12px 0;
}

.welcome-text {
    color: var(--muted);
    line-height: 1.8;
}

.welcome-note {
    color: var(--accent-dark);
    font-style: italic;
    margin-top: 18px;
}

div[data-testid="stForm"],
div[data-testid="stExpander"],
div[data-testid="stMetric"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
}

div[data-testid="stMetric"] {
    padding: 12px;
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

div[data-testid="stDialog"] > div {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 22px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TEXTOS DO GERALD
# --------------------------------------------------

PISTAS_ABSURDAS = [
    "O número secreto é um número.",
    "O Gerald garante que o número secreto não é nenhum animal. Exceto, talvez, ele próprio.",
    "O número secreto está algures. O Gerald considera a localização confidencial.",
    "Pista oficial: o número secreto tem uma cor. O Gerald não vai dizer qual.",
    "O número secreto é mais ou menos do tamanho de um ganso. Depende do ganso.",
    "O Gerald sonhou com o número, mas acordou antes do fim.",
    "O número secreto prefere as terças-feiras.",
    "O número secreto tem medo de formulários.",
    "O Gerald escreveu o número num post-it e perdeu o post-it.",
    "HONK. O Gerald garante que isto é uma pista. Não é.",
    "O número secreto esteve de baixa médica na semana passada.",
    "A pista foi cancelada por falta de orçamento.",
    "O número secreto tem direito à privacidade.",
    "O Gerald estava a falar da temperatura da sala.",
    "O número secreto é exatamente o número que é.",
    "O Gerald pediu uma segunda opinião a outro ganso. Também não sabe.",
    "Esta pista está sob análise jurídica.",
    "O número secreto foi visto perto da máquina do café.",
    "O Gerald pensou numa pista, mas ficou com fome e comeu-a.",
]

DOSSIER_ABSURDAS = [
    "tem a cor do número",
    "nunca foi visto ao pé de uma impressora",
    "é amigo do ganso do departamento ao lado",
    "não gosta de segundas-feiras",
    "é menor do que a paciência do Gerald",
    "assinou o livro de ponto às 9h07",
    "é mais alto do que o ganso do departamento ao lado",
]

COMENTARIOS = [
    "O Gerald anotou o teu palpite num formulário que ninguém vai ler.",
    "O Gerald olhou para ti três segundos a mais do que o necessário.",
    "O Gerald está a fingir que não está a gostar disto.",
    "O Gerald pediu um café. Não é para ele, é para a tensão.",
    "O Gerald carimbou o teu palpite. Não sabe porquê.",
    "Ouviu-se um HONK ao longe. Pode ou não ter sido o Gerald.",
    "O Gerald abriu uma ficha de ocorrência só para este palpite.",
    "O Gerald suspirou com a elegância de um funcionário em fim de contrato.",
    "O Gerald está a ajeitar a gravata. É mau sinal. Ou bom.",
    "O Gerald pediu uma reunião de alinhamento sobre este palpite.",
    "Um colega perguntou se estava tudo bem. O Gerald escondeu a prancheta.",
    "O Gerald tentou parecer impassível. Falhou nas penas.",
    "O Gerald copiou o teu palpite para a ata. Com erros ortográficos.",
    "O Gerald disse «interessante» sem mexer o bico.",
]

COMENTARIOS_ESPECIAIS = {
    1: "O 1. O Gerald respeita a coragem de quem tenta logo o limite mínimo.",
    7: "O 7. O Gerald diz que toda a gente tenta o 7. É estatística.",
    8: "O 8. O Gerald diz que isso é o infinito em pé.",
    13: "O 13. O Gerald fez uma pausa para uma cerimónia de mau agouro.",
    42: "O 42. O Gerald diz que essa é a resposta de outro jogo.",
    50: "O 50. O Gerald elogia a coragem de quem tenta sempre o meio.",
    69: "O 69. O Gerald corou e pediu que isto não conste da ata.",
    100: "O 100. O Gerald diz que quem tenta o limite máximo tem pouca paciência.",
}

COMENTARIOS_MARCOS = {
    10: "Já vais em 10 tentativas. O Gerald abriu uma ficha de acompanhamento.",
    20: "20 tentativas. O Gerald começou a apostar com os colegas.",
    30: "30 tentativas. O Gerald trouxe uma cadeira.",
    50: "50 tentativas. O Gerald enviou um email aos Recursos Humanos. Ele é os Recursos Humanos.",
}

AVALIACOES = [
    (800, "Desempenho exemplar. O Gerald está desconfiado."),
    (500, "Desempenho aceitável. O Gerald vai arquivar o processo."),
    (250, "Desempenho em análise. O Gerald pede mais dez palpites."),
    (0, "Desempenho a justificar. O Gerald marcou-te uma reunião."),
]


# --------------------------------------------------
# FUNÇÕES DO JOGO
# --------------------------------------------------

def formatar_tempo(segundos):
    segundos = int(segundos)
    return f"{segundos // 60:02d}:{segundos % 60:02d}"


def calcular_pontuacao(tentativas, segundos, repeticoes):
    pontos = (
        PONTOS_INICIAIS
        - PENALIZACAO_TENTATIVA * (tentativas - 1)
        - PENALIZACAO_SEGUNDO * int(segundos)
        - PENALIZACAO_REPETICAO * repeticoes
    )
    return max(0, pontos)


def avaliacao(pontuacao):
    for minimo, texto in AVALIACOES:
        if pontuacao >= minimo:
            return texto
    return AVALIACOES[-1][1]


def numeros_que(predicado):
    return frozenset(
        n for n in range(MINIMO, MAXIMO + 1)
        if predicado(n)
    )


def factos(segredo):
    """Gera factos verdadeiros sobre o número secreto."""
    algarismos = len(str(segredo))
    nome_algarismos = {
        1: "um algarismo",
        2: "dois algarismos",
        3: "três algarismos",
    }[algarismos]

    lista = [
        (
            "é par" if segredo % 2 == 0 else "é ímpar",
            numeros_que(lambda n, r=segredo % 2: n % 2 == r),
        ),
        (
            f"tem {nome_algarismos}",
            numeros_que(lambda n, k=algarismos: len(str(n)) == k),
        ),
    ]

    divisor = random.choice([3, 5, 7])

    if segredo % divisor == 0:
        lista.append((
            f"é múltiplo de {divisor}",
            numeros_que(lambda n, d=divisor: n % d == 0),
        ))
    else:
        lista.append((
            f"não é múltiplo de {divisor}",
            numeros_que(lambda n, d=divisor: n % d != 0),
        ))

    if segredo > MINIMO:
        limite = random.randint(max(MINIMO, segredo - 40), segredo - 1)
        lista.append((
            f"é maior do que {limite}",
            numeros_que(lambda n, t=limite: n > t),
        ))

    if segredo < MAXIMO:
        limite = random.randint(segredo + 1, min(MAXIMO, segredo + 40))
        lista.append((
            f"é menor do que {limite}",
            numeros_que(lambda n, t=limite: n < t),
        ))

    if segredo == 8:
        lista.append((
            "é exatamente o infinito em pé",
            numeros_que(lambda n: n == 8),
        ))
    elif segredo > 8:
        lista.append((
            "é maior do que o infinito em pé",
            numeros_que(lambda n: n > 8),
        ))
    else:
        lista.append((
            "é menor do que o infinito em pé",
            numeros_que(lambda n: n < 8),
        ))

    lista.append((
        f"termina em {segredo % 10}",
        numeros_que(lambda n, d=segredo % 10: n % 10 == d),
    ))

    return lista


def intersecao(conjuntos):
    resultado = set(range(MINIMO, MAXIMO + 1))
    for conjunto in conjuntos:
        resultado &= conjunto
    return resultado


def todas_necessarias(conjuntos, minimo):
    total = len(intersecao(conjuntos))
    return all(
        len(intersecao(conjuntos[:i] + conjuntos[i + 1:])) - total >= minimo
        for i in range(len(conjuntos))
    )


def pistas_iniciais(segredo):
    """Cria três pistas verdadeiras e uma pista absurda."""
    opcoes = factos(segredo)
    escolhidas = []

    for minimo in (3, 2, 1):
        random.shuffle(opcoes)
        escolhidas = []

        for fragmento, conjunto in opcoes:
            conjuntos = [c for _, c in escolhidas] + [conjunto]

            if todas_necessarias(conjuntos, minimo):
                escolhidas.append((fragmento, conjunto))

                if len(escolhidas) == 3:
                    break

        if len(escolhidas) == 3:
            break

    for fragmento, conjunto in opcoes:
        if len(escolhidas) == 3:
            break

        if (fragmento, conjunto) in escolhidas:
            continue

        escolhidas.append((fragmento, conjunto))

    dossier = [f for f, _ in escolhidas]
    dossier.append(random.choice(DOSSIER_ABSURDAS))
    random.shuffle(dossier)

    candidatos = intersecao([c for _, c in escolhidas])

    return dossier, candidatos


def novo_jogo():
    st.session_state.segredo = random.randint(MINIMO, MAXIMO)
    st.session_state.dossier, st.session_state.candidatos = (
        pistas_iniciais(st.session_state.segredo)
    )
    st.session_state.palpites = []
    st.session_state.mensagem = None
    st.session_state.ultima_pista = None
    st.session_state.ultimo_comentario = None
    st.session_state.venceu = False
    st.session_state.inicio = None
    st.session_state.fim = None
    st.session_state.repeticoes = 0
    st.session_state.pontuacao = None


def finalizar_jogo():
    st.session_state.venceu = True
    st.session_state.fim = time.time()

    segundos = st.session_state.fim - st.session_state.inicio

    st.session_state.pontuacao = calcular_pontuacao(
        len(st.session_state.palpites),
        segundos,
        st.session_state.repeticoes,
    )

    melhor = st.session_state.melhor

    if melhor is None or st.session_state.pontuacao > melhor:
        st.session_state.melhor = st.session_state.pontuacao


def nova_pista(palpite):
    """
    A pista verdadeira indica sempre a direção correta.
    A observação absurda, quando aparece, é identificada separadamente.
    """
    segredo = st.session_state.segredo
    candidatos = st.session_state.candidatos

    if segredo > palpite:
        fragmento = "é maior do que o teu palpite"
        conjunto = numeros_que(lambda n, p=palpite: n > p)
    else:
        fragmento = "é menor do que o teu palpite"
        conjunto = numeros_que(lambda n, p=palpite: n < p)

    abertura = random.choice([
        "O Gerald garante que o número secreto",
        "Segundo o Gerald, o número secreto",
        "O Gerald diz, com ar solene, que o número secreto",
    ])

    pista = f"{abertura} {fragmento}."

    st.session_state.candidatos = candidatos & conjunto

    if random.random() < PROB_PISTA_ABSURDA:
        absurda = random.choice(PISTAS_ABSURDAS)
        pista += (
            "\n\n**Nota burocrática do Gerald:** "
            f"{absurda}"
        )

    st.session_state.ultima_pista = pista
    return pista


def novo_comentario(palpite, tentativas):
    if palpite in COMENTARIOS_ESPECIAIS:
        return COMENTARIOS_ESPECIAIS[palpite]

    if tentativas in COMENTARIOS_MARCOS:
        return COMENTARIOS_MARCOS[tentativas]

    opcoes = [
        c for c in COMENTARIOS
        if c != st.session_state.ultimo_comentario
    ]

    comentario = random.choice(opcoes or COMENTARIOS)
    st.session_state.ultimo_comentario = comentario

    return comentario


def mensagem_vitoria(tentativas):
    if tentativas <= 3:
        return (
            "O Gerald ficou em silêncio. Adivinhaste depressa de mais. "
            "Isto vai dar um relatório."
        )

    if tentativas <= 8:
        return "Acertaste! O Gerald aprova, com reservas e um carimbo."

    return "Acertaste, finalmente. O Gerald já ia abrir um processo por demora."


# --------------------------------------------------
# ESTADO INICIAL
# --------------------------------------------------

if "melhor" not in st.session_state:
    st.session_state.melhor = None

if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False

if "segredo" not in st.session_state:
    novo_jogo()


# --------------------------------------------------
# BOAS-VINDAS
# --------------------------------------------------

@st.dialog("🔢 O Número Secreto do Gerald")
def boas_vindas():
    st.markdown("""
    <div class="welcome-card">
        <div class="welcome-label">
            Departamento de Recursos Gansais
        </div>
        <div class="welcome-title">
            O Número Secreto do Gerald
        </div>
        <div class="welcome-text">
            O Gerald escolheu um número entre
            <strong>1 e 100</strong>.
            A tua missão é descobri-lo antes que a pontuação desapareça.
            <br><br>
            <strong>Investiga o dossier.</strong>
            Três pistas verdadeiras e uma absurda.
            <br><br>
            <strong>Analisa os palpites.</strong>
            O Gerald responde com pistas e comentários.
            <br><br>
            <strong>Controla o tempo.</strong>
            Cada tentativa tem um custo.
        </div>
        <div class="welcome-note">
            O Gerald deseja-te boa sorte. Não prometeu facilitar.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Iniciar jogo", use_container_width=True):
        st.session_state.jogo_iniciado = True
        st.rerun()


if not st.session_state.jogo_iniciado:
    boas_vindas()
    st.stop()


# --------------------------------------------------
# ECRÃ PRINCIPAL
# --------------------------------------------------

st.title("O Número Secreto do Gerald")

st.caption(
    f"O Gerald escolheu um número entre {MINIMO} e {MAXIMO}. "
    "Vai dar-te pistas. A maioria é séria. Algumas, nem por isso."
)

with st.expander("📋 Instruções", expanded=False):
    st.markdown(f"""
1. O Gerald escolheu um número secreto entre **{MINIMO} e {MAXIMO}**.
2. Escreve um palpite e carrega em **Tentar**.
3. O dossier contém três pistas verdadeiras e um disparate.
4. Quando falhas, o Gerald indica se o número secreto é maior ou menor do que o teu palpite.
5. Por vezes, acrescenta uma observação absurda, devidamente identificada.
6. **Não podes repetir palpites.** Cada repetição custa {PENALIZACAO_REPETICAO} pontos.
7. O relógio começa no primeiro palpite.
8. A pontuação começa em {PONTOS_INICIAIS}. Perdes {PENALIZACAO_TENTATIVA} pontos por tentativa a partir da segunda e {PENALIZACAO_SEGUNDO} pontos por segundo.
9. Quando acertares, o Gerald avalia o teu desempenho.
""")

itens = "".join(
    f"<li>{pista}</li>"
    for pista in st.session_state.dossier
)

st.markdown(
    html(f"""
    <div class="dossier">
        <div class="dossier-label">
            Dossier deixado à vista pelo Gerald
        </div>
        <div>O número secreto...</div>
        <ul>{itens}</ul>
    </div>
    """),
    unsafe_allow_html=True,
)


def mostrar_tempo():
    if st.session_state.inicio is None:
        st.caption("⏱ O relógio só começa no primeiro palpite.")
    else:
        decorrido = formatar_tempo(
            time.time() - st.session_state.inicio
        )
        st.caption(
            f"⏱ Tempo: {decorrido} · "
            f"Tentativas: {len(st.session_state.palpites)}"
        )


if not st.session_state.venceu:
    mostrar_tempo()

    with st.form("palpite"):
        palpite = st.number_input(
            "O teu palpite",
            min_value=MINIMO,
            max_value=MAXIMO,
            value=50,
            step=1,
        )

        tentar = st.form_submit_button(
            "Tentar",
            use_container_width=True,
        )

    if tentar:
        palpite = int(palpite)

        if st.session_state.inicio is None:
            st.session_state.inicio = time.time()

        if palpite in st.session_state.palpites:
            st.session_state.repeticoes += 1

            st.session_state.mensagem = (
                "aviso",
                f"Já tentaste o {palpite}. O Gerald cobra "
                f"-{PENALIZACAO_REPETICAO} pontos por repetição.",
            )

        else:
            st.session_state.palpites.append(palpite)
            tentativas = len(st.session_state.palpites)

            st.session_state.candidatos = (
                st.session_state.candidatos - {palpite}
            )

            if palpite == st.session_state.segredo:
                finalizar_jogo()

                st.session_state.mensagem = (
                    "sucesso",
                    mensagem_vitoria(tentativas),
                )

            else:
                pista = nova_pista(palpite)
                comentario = novo_comentario(palpite, tentativas)

                st.session_state.mensagem = (
                    "info",
                    f"**Não é o {palpite}.** {pista}\n\n"
                    f"*{comentario}*",
                )

        st.rerun()


if st.session_state.mensagem:
    tipo, texto = st.session_state.mensagem

    if tipo == "info":
        st.info(texto)
    elif tipo == "aviso":
        st.warning(texto)
    elif tipo == "sucesso":
        st.success(texto)


if st.session_state.palpites:
    st.write(
        f"**Tentativas ({len(st.session_state.palpites)}):** "
        + ", ".join(map(str, st.session_state.palpites))
    )


if st.session_state.venceu:
    st.balloons()

    st.write(
        f"O número secreto era o **{st.session_state.segredo}**."
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Tempo",
        formatar_tempo(
            st.session_state.fim - st.session_state.inicio
        ),
    )

    c2.metric(
        "Tentativas",
        len(st.session_state.palpites),
    )

    c3.metric(
        "Pontuação",
        st.session_state.pontuacao,
    )

    st.write(f"**{avaliacao(st.session_state.pontuacao)}**")


st.button(
    "Novo jogo",
    on_click=novo_jogo,
)

if st.session_state.melhor is not None:
    st.caption(
        f"Melhor pontuação desta sessão: "
        f"{st.session_state.melhor}"
    )
