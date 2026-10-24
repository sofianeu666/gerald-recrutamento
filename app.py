import random
import time
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

div[data-testid="stMetric"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
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

/* Modal de boas-vindas */
div[data-testid="stDialog"] > div {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 22px;
}

.welcome-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-top: 6px solid var(--accent);
    border-radius: 16px;
    padding: 24px;
    margin: 8px 0 18px;
}

.welcome-label {
    color: var(--accent-dark);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-size: 0.7rem;
    font-weight: 700;
    margin-bottom: 12px;
}

.welcome-title {
    font-family: 'Source Serif 4', serif;
    font-size: 1.8rem;
    line-height: 1.2;
    color: var(--text);
    margin-bottom: 14px;
}

.welcome-text {
    color: var(--muted);
    line-height: 1.7;
    font-size: 0.92rem;
}

.welcome-note {
    color: var(--accent-dark);
    font-style: italic;
    margin-top: 18px;
    font-size: 0.88rem;
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

# Das pistas verdadeiras, qual a probabilidade de ser do género «estás quente / frio»
PROB_TEMPERATURA = 0.35

# Pontuação: começa em PONTOS_INICIAIS e o Gerald vai cobrando
PONTOS_INICIAIS = 1000
PENALIZACAO_TENTATIVA = 40   # por cada tentativa a partir da segunda
PENALIZACAO_SEGUNDO = 2      # por cada segundo desde o primeiro palpite
PENALIZACAO_REPETICAO = 25   # por cada palpite repetido


# --------------------------------------------------
# TEXTOS
# --------------------------------------------------

# Pistas absurdas (frases completas, para depois de cada palpite)
PISTAS_ABSURDAS = [
    "O número secreto é um número.",
    "O Gerald garante que o número secreto não é nenhum animal. Exceto, talvez, ele próprio.",
    "O número secreto está algures. O Gerald não pode dizer mais, é confidencial.",
    "Pista oficial: o número secreto tem uma cor. O Gerald não vai dizer qual.",
    "O número secreto é mais ou menos do tamanho de um ganso. Depende do ganso.",
    "O Gerald sonhou com o número, mas acordou antes do fim.",
    "O Gerald diz que o número secreto prefere as terças-feiras.",
    "O número secreto tem medo de formulários. Isto não ajuda ninguém, mas é verdade.",
    "O Gerald escreveu o número secreto num post-it e perdeu o post-it.",
    "HONK. (O Gerald garante que isto é uma pista. Não é.)",
    "O número secreto esteve de baixa médica na semana passada.",
    "A pista de hoje foi cancelada por falta de orçamento.",
    "O número secreto não gosta de ser adivinhado. Tem direito a privacidade.",
    "O Gerald diz que estás «quente». Estava a falar da temperatura da sala.",
    "Pista confidencial: o número secreto é exatamente o número que é.",
    "O Gerald pediu uma segunda opinião ao ganso do departamento ao lado. Também não sabe.",
    "Esta pista está sob análise jurídica.",
    "O número secreto foi visto pela última vez perto da máquina do café.",
    "O Gerald pensou numa pista, mas ficou com fome e comeu-a.",
]

# Pistas absurdas para o dossier inicial (fragmentos que continuam «O número...»)
DOSSIER_ABSURDAS = [
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
    1: "O 1. O Gerald respeita a coragem de quem tenta logo o limite mínimo.",
    7: "O 7. O Gerald diz que toda a gente tenta o 7. É estatística.",
    8: "O 8. O Gerald diz que isso é o infinito em pé e pediu que não o mexas.",
    13: "O 13. O Gerald fez uma pausa para uma cerimónia de mau agouro.",
    42: "O 42. O Gerald diz que essa é a resposta de outro jogo.",
    50: "O 50. O Gerald elogia a coragem de quem tenta sempre o meio.",
    69: "O 69. O Gerald corou e pediu que isto não conste da ata.",
    100: "O 100. O Gerald diz que quem tenta o limite máximo tem pouca paciência.",
}

# Comentários para marcos de tentativas
COMENTARIOS_MARCOS = {
    10: "Já vais em 10 tentativas. O Gerald abriu uma ficha de acompanhamento.",
    20: "20 tentativas. O Gerald começou a apostar com os colegas.",
    30: "30 tentativas. O Gerald trouxe uma cadeira.",
    50: "50 tentativas. O Gerald enviou um email aos Recursos Humanos. Ele é os Recursos Humanos.",
}

# Pistas de temperatura (verdadeiras, calculadas pela distância ao número secreto)
TEMPERATURAS = {
    "gelado": [
        "O Gerald diz que estás gelado. Longe, mesmo longe.",
        "Gelado. O Gerald vestiu o casaco só de olhar para o teu palpite.",
    ],
    "frio": [
        "O Gerald diz que estás frio. Está longe.",
        "Frio. O Gerald está a ver a respiração dele a formar nuvens.",
    ],
    "morno": [
        "O Gerald diz que estás morno. Nem frio nem quente.",
        "Morno. O Gerald pediu um chá, que é a temperatura certa para isto.",
    ],
    "quente": [
        "O Gerald diz que estás quente. Estás perto!",
        "Quente! O Gerald começou a abanar as penas.",
    ],
    "escaldante": [
        "O Gerald diz que estás escaldante. É mesmo aqui ao pé!",
        "Escaldante! O Gerald escondeu o número atrás da prancheta.",
    ],
}

# Avaliação final conforme a pontuação
AVALIACOES = [
    (800, "Desempenho exemplar. O Gerald está desconfiado."),
    (500, "Desempenho aceitável. O Gerald vai arquivar o processo."),
    (250, "Desempenho em análise. O Gerald pede mais dez palpites."),
    (0, "Desempenho a justificar. O Gerald marcou-te uma reunião."),
]


# --------------------------------------------------
# LÓGICA
# --------------------------------------------------

def categoria_temperatura(distancia):
    if distancia >= 50:
        return "gelado"
    if distancia >= 25:
        return "frio"
    if distancia >= 10:
        return "morno"
    if distancia >= 4:
        return "quente"
    return "escaldante"


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

def numeros_que(predicado):
    """Conjunto dos números do jogo que cumprem uma condição."""
    return frozenset(n for n in range(MINIMO, MAXIMO + 1) if predicado(n))


def factos(segredo, palpite=None, incluir_final=True):
    """Factos verdadeiros sobre o número secreto.
    Cada um é (fragmento que continua «O número secreto...», números compatíveis)."""
    divisor = random.choice([3, 5, 7])
    algarismos = len(str(segredo))
    nome_algarismos = {1: "um algarismo", 2: "dois algarismos", 3: "três algarismos"}[algarismos]

    lista = [
        ("é par" if segredo % 2 == 0 else "é ímpar",
         numeros_que(lambda n, r=segredo % 2: n % 2 == r)),
        (f"tem {nome_algarismos}",
         numeros_que(lambda n, k=algarismos: len(str(n)) == k)),
    ]

    if segredo % divisor == 0:
        lista.append((f"é múltiplo de {divisor}", numeros_que(lambda n, d=divisor: n % d == 0)))
    else:
        lista.append((f"não é múltiplo de {divisor}", numeros_que(lambda n, d=divisor: n % d != 0)))

    # Limites sempre dentro do intervalo do jogo (nada de «menor do que 101»)
    if segredo > MINIMO:
        t = random.randint(max(MINIMO, segredo - 40), segredo - 1)
        lista.append((f"é maior do que {t}", numeros_que(lambda n, t=t: n > t)))
    if segredo < MAXIMO:
        t = random.randint(segredo + 1, min(MAXIMO, segredo + 40))
        lista.append((f"é menor do que {t}", numeros_que(lambda n, t=t: n < t)))

    # O infinito em pé é o 8
    if segredo == 8:
        lista.append(("é exatamente o infinito em pé", numeros_que(lambda n: n == 8)))
    elif segredo > 8:
        lista.append(("é maior do que o infinito em pé", numeros_que(lambda n: n > 8)))
    else:
        lista.append(("é menor do que o infinito em pé", numeros_que(lambda n: n < 8)))

    if incluir_final:
        lista.append((f"termina em {segredo % 10}",
                      numeros_que(lambda n, d=segredo % 10: n % 10 == d)))

    if palpite is not None:
        # A pista clássica: mais alto ou mais baixo (com peso a dobrar)
        if segredo > palpite:
            direcao = ("é maior do que o teu palpite", numeros_que(lambda n, p=palpite: n > p))
        else:
            direcao = ("é menor do que o teu palpite", numeros_que(lambda n, p=palpite: n < p))
        lista += [direcao, direcao]

    return lista


def corta_o_suficiente(candidatos, conjunto):
    """Uma pista só vale a pena se tirar números a sério (pelo menos 5% dos que restam).
    Assim o Gerald não diz «maior do que 8» a quem já sabe que o número tem dois algarismos."""
    minimo = max(1, -(-len(candidatos) * 5 // 100))
    return len(candidatos) - len(candidatos & conjunto) >= minimo


def escolher_util(opcoes, candidatos):
    """Escolhe uma opção que traga informação nova. Se nenhuma trouxer, aceita a menos má."""
    uteis = [o for o in opcoes if corta_o_suficiente(candidatos, o[1])]
    if not uteis:
        uteis = [o for o in opcoes if len(candidatos & o[1]) < len(candidatos)]
    return random.choice(uteis or opcoes)


def intersecao(conjuntos):
    resultado = set(range(MINIMO, MAXIMO + 1))
    for conjunto in conjuntos:
        resultado &= conjunto
    return resultado


def todas_necessarias(conjuntos, minimo):
    """Cada pista tem de acrescentar informação que as outras não dão (pelo menos `minimo` números)."""
    total = len(intersecao(conjuntos))
    return all(
        len(intersecao(conjuntos[:i] + conjuntos[i + 1:])) - total >= minimo
        for i in range(len(conjuntos))
    )


def pistas_iniciais(segredo):
    """Dossier inicial: três pistas verdadeiras e uma absurda.
    Nenhuma pista verdadeira pode ser consequência das outras
    (por exemplo, «dois algarismos» e «maior do que 8» nunca aparecem juntas).
    Devolve as pistas e os números que ainda são possíveis depois delas."""
    opcoes = factos(segredo, incluir_final=False)
    escolhidas = []

    for minimo in (3, 2, 1):  # se for difícil, vai-se aceitando pistas menos exigentes
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

    # Último recurso: completa com pistas verdadeiras, mesmo que repitam informação
    for fragmento, conjunto in opcoes:
        if len(escolhidas) == 3:
            break
        if (fragmento, conjunto) in escolhidas:
            continue
        ja_ditas = " ".join(f for f, _ in escolhidas)
        if "algarismo" in ja_ditas and "infinito" in fragmento:
            continue
        if "infinito" in ja_ditas and "algarismo" in fragmento:
            continue
        escolhidas.append((fragmento, conjunto))

    candidatos = intersecao([c for _, c in escolhidas])
    dossier = [f for f, _ in escolhidas] + [random.choice(DOSSIER_ABSURDAS)]
    random.shuffle(dossier)
    return dossier, candidatos


def novo_jogo():
    st.session_state.segredo = random.randint(MINIMO, MAXIMO)
    st.session_state.dossier, st.session_state.candidatos = pistas_iniciais(st.session_state.segredo)
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
        len(st.session_state.palpites), segundos, st.session_state.repeticoes
    )
    melhor = st.session_state.melhor
    if melhor is None or st.session_state.pontuacao > melhor:
        st.session_state.melhor = st.session_state.pontuacao


def nova_pista(palpite):
    segredo = st.session_state.segredo
    candidatos = st.session_state.candidatos

    # Evita repetir a mesma pista duas vezes seguidas
    for _ in range(10):
        conjunto = None

        if random.random() < PROB_PISTA_ABSURDA:
            pista = random.choice(PISTAS_ABSURDAS)
        else:
            categoria = categoria_temperatura(abs(segredo - palpite))
            conj_temp = numeros_que(
                lambda n: categoria_temperatura(abs(n - palpite)) == categoria
            )

            if random.random() < PROB_TEMPERATURA and corta_o_suficiente(candidatos, conj_temp):
                pista, conjunto = random.choice(TEMPERATURAS[categoria]), conj_temp
            else:
                fragmento, conjunto = escolher_util(factos(segredo, palpite), candidatos)
                abertura = random.choice([
                    "O Gerald garante que o número secreto",
                    "Segundo o Gerald, o número secreto",
                    "O Gerald diz, com ar solene, que o número secreto",
                ])
                pista = f"{abertura} {fragmento}."

        if pista != st.session_state.ultima_pista:
            break

    st.session_state.ultima_pista = pista
    if conjunto is not None:
        st.session_state.candidatos = candidatos & conjunto
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


@st.dialog("🔢 O Número Secreto do Gerald")
def boas_vindas():
    st.markdown("""
    <div class="welcome-card">
        <div class="welcome-label">Departamento de Recursos Gansais</div>
        <div class="welcome-title">O Número Secreto do Gerald</div>
        <div class="welcome-text">
            O Gerald escolheu um número entre <strong>1 e 100</strong>.
            A tua missão é descobri-lo antes que a pontuação desapareça.
            <br><br>
            <strong>Investiga o dossier.</strong> Três pistas verdadeiras e uma absurda.
            <br><br>
            <strong>Analisa os palpites.</strong> O Gerald responde com pistas e comentários.
            <br><br>
            <strong>Controla o tempo.</strong> Cada tentativa tem um custo.
        </div>
        <div class="welcome-note">
            O Gerald deseja-te boa sorte. Não prometeu facilitar.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Iniciar jogo", use_container_width=True, key="iniciar_jogo"):
        st.session_state.jogo_iniciado = True
        st.rerun()


if "melhor" not in st.session_state:
    st.session_state.melhor = None

if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False

if "segredo" not in st.session_state:
    novo_jogo()

if not st.session_state.jogo_iniciado:
    boas_vindas()
    st.stop()


# --------------------------------------------------
# ECRÃ
# --------------------------------------------------

st.title("O Número Secreto do Gerald")
st.caption(
    f"O Gerald escolheu um número entre {MINIMO} e {MAXIMO}. "
    "Vai dar-te pistas. A maioria é séria. Algumas, nem por isso."
)

with st.expander("📋 Instruções", expanded=False):
    st.markdown(
        f"""
1. O Gerald escolheu um **número secreto entre {MINIMO} e {MAXIMO}**.
2. Escreve um palpite e carrega em **Tentar**.
3. O **dossier** já traz umas pistas à vista. Algumas são verdadeiras, outras são disparates do Gerald. Cabe-te a ti perceber quais.
4. Quando falhas, o Gerald dá uma **pista** (quase sempre verdadeira, de vez em quando absurda) e faz um **comentário**.
5. A pista também pode ser **frio ou quente**: quanto mais perto do número, mais quente.
6. **Não podes repetir palpites.** Se repetires, o Gerald cobra uma taxa de {PENALIZACAO_REPETICAO} pontos.
7. Não há limite de tentativas, mas o Gerald está a contá-las. O **relógio começa no primeiro palpite**.
8. A **pontuação** começa em {PONTOS_INICIAIS}. Perdes {PENALIZACAO_TENTATIVA} pontos por cada tentativa a partir da segunda, {PENALIZACAO_SEGUNDO} por cada segundo e {PENALIZACAO_REPETICAO} por cada repetição.
9. Quando acertares, o Gerald avalia o teu desempenho.
"""
    )

itens = "".join(f"<li>{pista}</li>" for pista in st.session_state.dossier)
st.markdown(
    html(f"""
    <div class="dossier">
        <div class="dossier-label">Dossier deixado à vista pelo Gerald</div>
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
        decorrido = formatar_tempo(time.time() - st.session_state.inicio)
        st.caption(f"⏱ Tempo: {decorrido}  ·  Tentativas: {len(st.session_state.palpites)}")


if not st.session_state.venceu:
    # O relógio atualiza-se sozinho a cada segundo (Streamlit recente); senão, só a cada jogada
    ativo = st.session_state.inicio is not None
    if hasattr(st, "fragment"):
        try:
            mostrar_tempo = st.fragment(run_every=1 if ativo else None)(mostrar_tempo)
        except TypeError:
            pass
    mostrar_tempo()

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

        if st.session_state.inicio is None:
            st.session_state.inicio = time.time()

        if palpite in st.session_state.palpites:
            st.session_state.repeticoes += 1
            st.session_state.mensagem = (
                "aviso",
                f"Já tentaste o {palpite}. O Gerald está a cobrar taxa por repetição: "
                f"-{PENALIZACAO_REPETICAO} pontos.",
            )
        else:
            st.session_state.palpites.append(palpite)
            tentativas = len(st.session_state.palpites)
            st.session_state.candidatos = st.session_state.candidatos - {palpite}

            if palpite == st.session_state.segredo:
                finalizar_jogo()
                st.session_state.mensagem = ("sucesso", mensagem_vitoria(tentativas))
            else:
                st.session_state.mensagem = (
                    "info",
                    f"**Não é o {palpite}.** {nova_pista(palpite)}\n\n"
                    f"*{novo_comentario(palpite, tentativas)}*",
                )

        # Redesenha já o ecrã (relógio a contar, formulário escondido ao ganhar)
        st.rerun()

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

    c1, c2, c3 = st.columns(3)
    c1.metric("Tempo", formatar_tempo(st.session_state.fim - st.session_state.inicio))
    c2.metric("Tentativas", len(st.session_state.palpites))
    c3.metric("Pontuação", st.session_state.pontuacao)
    st.write(f"**{avaliacao(st.session_state.pontuacao)}**")

st.button("Novo jogo", on_click=novo_jogo)

if st.session_state.melhor is not None:
    st.caption(f"Melhor pontuação desta sessão: {st.session_state.melhor}")
