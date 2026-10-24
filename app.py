import random
import streamlit as st

st.set_page_config(
    page_title="Recrutamento Gansal | Gerald",
    page_icon="📋",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# VISUAL
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
}

.stApp {
    background: var(--bg);
    color: var(--text);
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: var(--text) !important;
    font-family: 'Source Serif 4', serif !important;
}

.ger-header {
    background: var(--card);
    border: 1px solid var(--border);
    border-top: 6px solid var(--accent);
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 22px;
}

.ger-kicker {
    color: var(--accent-dark);
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.72rem;
    font-weight: 700;
}

.ger-title {
    font-family: 'Source Serif 4', serif;
    font-size: clamp(2rem, 6vw, 3rem);
    line-height: 1.12;
    font-weight: 700;
    margin: 10px 0;
}

.ger-subtitle {
    color: var(--muted);
    line-height: 1.7;
    margin-top: 10px;
}

.ger-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    margin: 16px 0;
}

.ger-label {
    color: var(--accent-dark);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

.ger-quote {
    background: #F0E5D9;
    border-left: 4px solid var(--accent);
    border-radius: 8px;
    padding: 14px 16px;
    margin: 16px 0;
    color: var(--text);
    line-height: 1.65;
}

div.stButton > button {
    background: var(--accent);
    color: white;
    border: 1px solid var(--accent);
    border-radius: 10px;
    min-height: 46px;
    font-weight: 700;
    transition: 0.2s ease;
}

div.stButton > button:hover {
    background: var(--accent-dark);
    border-color: var(--accent-dark);
    color: white;
}

div.stButton > button:focus {
    box-shadow: 0 0 0 3px #C9785255;
}

div[data-testid="stRadio"] label {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px 12px;
    margin-bottom: 6px;
}

div[data-testid="stMetric"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px;
}

hr {
    border-color: var(--border);
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# GERALD EM SVG, DENTRO DO PRÓPRIO CÓDIGO
# --------------------------------------------------

GERALD_SVG = """
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 240 210"
     width="180"
     role="img"
     aria-label="Gerald, o ganso dos Recursos Humanos">

  <ellipse cx="120" cy="192" rx="64" ry="9"
           fill="#29251F" opacity="0.10"/>

  <!-- Corpo -->
  <ellipse cx="112" cy="137" rx="66" ry="48"
           fill="#FFFDFA" stroke="#29251F" stroke-width="3"/>

  <!-- Asa -->
  <path d="M91 123 Q125 105 151 135
           Q132 163 96 157 Q113 143 91 123Z"
        fill="#E8DCCB" stroke="#29251F" stroke-width="2.5"/>

  <!-- Pescoço -->
  <path d="M132 133 C145 113 139 88 128 68
           L108 39 Q103 29 113 25 Q124 21 130 33
           L150 65 C169 96 165 124 151 145Z"
        fill="#FFFDFA" stroke="#29251F" stroke-width="3"/>

  <!-- Cabeça -->
  <ellipse cx="119" cy="33" rx="29" ry="25"
           fill="#FFFDFA" stroke="#29251F" stroke-width="3"/>

  <!-- Bico -->
  <path d="M92 34 L65 43 L93 49 Q100 43 92 34Z"
        fill="#C97852" stroke="#29251F" stroke-width="2.5"/>

  <!-- Olho e sobrancelha -->
  <circle cx="111" cy="28" r="3.5" fill="#29251F"/>
  <path d="M104 20 L118 24"
        stroke="#29251F" stroke-width="3"
        stroke-linecap="round"/>

  <!-- Gravata -->
  <path d="M135 83 L147 83 L144 96 L151 121
           L139 116 L131 121 L137 96Z"
        fill="#C97852" stroke="#8B4F35" stroke-width="2"/>

  <!-- Crachá -->
  <rect x="145" y="139" width="32" height="23" rx="4"
        fill="#F5F2EC" stroke="#29251F" stroke-width="2"/>
  <path d="M151 146 H169 M151 152 H165"
        stroke="#8B4F35" stroke-width="2"
        stroke-linecap="round"/>

  <!-- Pernas e patas -->
  <path d="M88 177 L86 190 M139 178 L142 190"
        stroke="#C97852" stroke-width="5"
        stroke-linecap="round"/>
  <path d="M74 191 H94 M130 191 H153"
        stroke="#C97852" stroke-width="5"
        stroke-linecap="round"/>

  <!-- Prancheta -->
  <rect x="171" y="91" width="35" height="46" rx="4"
        fill="#E8DCCB" stroke="#29251F" stroke-width="2.5"/>
  <rect x="181" y="86" width="15" height="9" rx="3"
        fill="#C97852" stroke="#29251F" stroke-width="2"/>
  <path d="M179 105 H198 M179 114 H198 M179 123 H193"
        stroke="#8B4F35" stroke-width="2.5"
        stroke-linecap="round"/>
</svg>
"""


# --------------------------------------------------
# PERGUNTAS E CONSEQUÊNCIAS
# Não há respostas universalmente certas ou erradas.
# --------------------------------------------------

PERGUNTAS = [
    {
        "tema": "Burocracia circular",
        "pergunta": "O Gerald exige um formulário que só pode ser obtido depois de ser aprovado. A aprovação exige que entregues o formulário.",
        "opcoes": [
            {
                "texto": "Criar um formulário provisório para registar o impasse.",
                "efeitos": {"suspeita": 5, "burocracia": 15, "reputacao": 5, "migalhas": 0},
                "resultado": "O formulário provisório foi aceite. O Gerald exige agora três cópias e uma cópia da cópia.",
            },
            {
                "texto": "Pedir ao Gerald uma autorização especial.",
                "efeitos": {"suspeita": 0, "burocracia": 10, "reputacao": -5, "migalhas": 0},
                "resultado": "O Gerald autoriza o pedido. A autorização precisa de ser autorizada por ele próprio.",
            },
            {
                "texto": "Declarar que o sistema está bloqueado e aguardar.",
                "efeitos": {"suspeita": 10, "burocracia": -5, "reputacao": 0, "migalhas": 0},
                "resultado": "O processo fica suspenso. O Gerald suspeita que estejas a tentar acabar o trabalho a horas.",
            },
        ],
    },
    {
        "tema": "Horário laboral",
        "pergunta": "São 17h00. O teu horário terminou, mas o Gerald aparece com um relatório de 46 páginas.",
        "opcoes": [
            {
                "texto": "Invocar o horário de trabalho e sair.",
                "efeitos": {"suspeita": 20, "burocracia": 5, "reputacao": 10, "migalhas": 0},
                "resultado": "Saíste a horas. O Gerald criou um registo de saída suspeita e os colegas estão a tomar notas.",
            },
            {
                "texto": "Aceitar ficar, desde que as horas sejam registadas.",
                "efeitos": {"suspeita": -5, "burocracia": 10, "reputacao": 5, "migalhas": 1},
                "resultado": "O Gerald concorda com o registo. Recebeste uma migalha como compensação provisória.",
            },
            {
                "texto": "Negociar a leitura de apenas uma página por migalha.",
                "efeitos": {"suspeita": 5, "burocracia": 0, "reputacao": 0, "migalhas": 3},
                "resultado": "O acordo foi assinado. O Gerald está a calcular quantas migalhas vale a página 47.",
            },
        ],
    },
    {
        "tema": "Segurança interna",
        "pergunta": "O Gerald corre na tua direção a 40 km/h. Grita que tens de comparecer numa reunião urgente.",
        "opcoes": [
            {
                "texto": "Perguntar qual é a ordem de trabalhos enquanto recuas.",
                "efeitos": {"suspeita": 5, "burocracia": 10, "reputacao": 0, "migalhas": 0},
                "resultado": "O Gerald abranda para consultar a agenda. A reunião ganha mais quatro pontos na ordem de trabalhos.",
            },
            {
                "texto": "Correr para um local seguro.",
                "efeitos": {"suspeita": 25, "burocracia": 0, "reputacao": 5, "migalhas": 0},
                "resultado": "FUGA DETETADA. Conheces agora a localização de uma saída de emergência que não consta da planta.",
            },
            {
                "texto": "Comparecer imediatamente com um bloco de notas.",
                "efeitos": {"suspeita": -5, "burocracia": 15, "reputacao": -5, "migalhas": 0},
                "resultado": "O Gerald está satisfeito. Foste nomeado secretário permanente de todas as reuniões futuras.",
            },
        ],
    },
    {
        "tema": "Gestão de recursos",
        "pergunta": "Descobres que o Gerald está a comer as migalhas reservadas aos funcionários.",
        "opcoes": [
            {
                "texto": "Pedir um inventário oficial das migalhas.",
                "efeitos": {"suspeita": 5, "burocracia": 20, "reputacao": 10, "migalhas": 0},
                "resultado": "O inventário revelou uma discrepância de três migalhas. O Gerald convocou uma auditoria ao inventário.",
            },
            {
                "texto": "Negociar uma reserva alimentar para os funcionários.",
                "efeitos": {"suspeita": 0, "burocracia": 5, "reputacao": 15, "migalhas": 2},
                "resultado": "Foi criada uma reserva. O Gerald exige ser informado de cada migalha consumida.",
            },
            {
                "texto": "Não intervir e proteger a tua própria reserva.",
                "efeitos": {"suspeita": -5, "burocracia": 0, "reputacao": -5, "migalhas": 3},
                "resultado": "A tua reserva está segura. Os colegas começaram a chamar-te responsável de logística alimentar.",
            },
        ],
    },
    {
        "tema": "Trabalho de equipa",
        "pergunta": "Um colega cometeu um erro num relatório. O Gerald quer saber quem foi responsável.",
        "opcoes": [
            {
                "texto": "Assumir a revisão do relatório em conjunto.",
                "efeitos": {"suspeita": -5, "burocracia": 10, "reputacao": 20, "migalhas": 0},
                "resultado": "O colega agradece a ajuda. O Gerald criou uma comissão para estudar a vossa colaboração.",
            },
            {
                "texto": "Apresentar os registos para esclarecer o que aconteceu.",
                "efeitos": {"suspeita": 10, "burocracia": 15, "reputacao": 0, "migalhas": 0},
                "resultado": "Os registos foram aceites. O Gerald quer agora os registos que comprovam a autenticidade dos registos.",
            },
            {
                "texto": "Propor uma formação para toda a equipa.",
                "efeitos": {"suspeita": 0, "burocracia": 20, "reputacao": 10, "migalhas": 0},
                "resultado": "A formação foi aprovada. O Gerald nomeou-te responsável pelo módulo obrigatório sobre erros em relatórios.",
            },
        ],
    },
    {
        "tema": "Comunicação institucional",
        "pergunta": "Recebes um email do Gerald com o assunto «URGENTE». O corpo diz apenas: «Precisamos de falar.»",
        "opcoes": [
            {
                "texto": "Responder a pedir o tema e a urgência concreta.",
                "efeitos": {"suspeita": 5, "burocracia": 5, "reputacao": 5, "migalhas": 0},
                "resultado": "O Gerald respondeu: «É urgente.» O mistério permanece e o email já tem quatro respostas.",
            },
            {
                "texto": "Preparar um resumo de tudo o que fizeste nessa semana.",
                "efeitos": {"suspeita": -5, "burocracia": 15, "reputacao": 0, "migalhas": 0},
                "resultado": "O resumo foi recebido. O Gerald pediu uma versão mais curta, seguida de uma versão completa.",
            },
            {
                "texto": "Marcar uma reunião e pedir uma agenda.",
                "efeitos": {"suspeita": 0, "burocracia": 20, "reputacao": 5, "migalhas": 0},
                "resultado": "A reunião está marcada. A agenda tem agora uma secção dedicada à preparação da agenda.",
            },
        ],
    },
    {
        "tema": "Ética gansal",
        "pergunta": "O Gerald pede-te a palavra-passe de um colega para «resolver uma coisa rapidamente».",
        "opcoes": [
            {
                "texto": "Recusar e indicar o procedimento autorizado.",
                "efeitos": {"suspeita": 10, "burocracia": 5, "reputacao": 15, "migalhas": 0},
                "resultado": "Protegeste o acesso. O Gerald não está contente, mas o departamento de segurança registou a tua decisão.",
            },
            {
                "texto": "Propor que o colega faça o acesso pessoalmente.",
                "efeitos": {"suspeita": 0, "burocracia": 0, "reputacao": 10, "migalhas": 0},
                "resultado": "O acesso foi feito pelo titular. O Gerald pergunta porque é que ninguém pensou nisso antes.",
            },
            {
                "texto": "Pedir um pedido formal e rastreável.",
                "efeitos": {"suspeita": 5, "burocracia": 20, "reputacao": 5, "migalhas": 0},
                "resultado": "O pedido entrou no sistema. O prazo de resposta estimado é de três eras geológicas.",
            },
        ],
    },
    {
        "tema": "Avaliação de desempenho",
        "pergunta": "O Gerald pede um relatório sobre o número de relatórios produzidos hoje. Ainda não acabaste nenhum.",
        "opcoes": [
            {
                "texto": "Registar o estado real do trabalho e o tempo disponível.",
                "efeitos": {"suspeita": 5, "burocracia": 10, "reputacao": 10, "migalhas": 0},
                "resultado": "O relatório é transparente. O Gerald pede uma previsão de quando terminarás o relatório sobre os relatórios.",
            },
            {
                "texto": "Criar uma tabela de acompanhamento dos relatórios.",
                "efeitos": {"suspeita": 0, "burocracia": 25, "reputacao": 5, "migalhas": 0},
                "resultado": "A tabela foi elogiada. Agora precisas de um relatório que explique a tabela.",
            },
            {
                "texto": "Perguntar se o próprio pedido conta como relatório.",
                "efeitos": {"suspeita": 15, "burocracia": 5, "reputacao": 5, "migalhas": 0},
                "resultado": "O Gerald ficou em silêncio durante oito segundos. A pergunta foi encaminhada para análise superior.",
            },
        ],
    },
    {
        "tema": "Gestão de crise",
        "pergunta": "O sistema informático deixou de funcionar dez minutos antes do prazo. O Gerald está a aproximar-se.",
        "opcoes": [
            {
                "texto": "Registar a falha e contactar o suporte técnico.",
                "efeitos": {"suspeita": 0, "burocracia": 10, "reputacao": 10, "migalhas": 0},
                "resultado": "A falha ficou documentada. O Gerald pergunta se o suporte técnico também precisa de autorização.",
            },
            {
                "texto": "Preparar uma cópia local dos dados disponíveis.",
                "efeitos": {"suspeita": 5, "burocracia": 5, "reputacao": 15, "migalhas": 0},
                "resultado": "Os dados foram preservados. O Gerald exige que a cópia tenha uma cópia de segurança da cópia.",
            },
            {
                "texto": "Pedir uma extensão do prazo com justificação.",
                "efeitos": {"suspeita": 10, "burocracia": 15, "reputacao": 5, "migalhas": 0},
                "resultado": "O pedido foi recebido. A decisão chegará depois do prazo original.",
            },
        ],
    },
    {
        "tema": "Liderança",
        "pergunta": "Os teus colegas querem organizar uma pausa coletiva. O Gerald acaba de declarar que as pausas devem ser individuais.",
        "opcoes": [
            {
                "texto": "Propor uma escala de pausas para garantir cobertura.",
                "efeitos": {"suspeita": 0, "burocracia": 15, "reputacao": 15, "migalhas": 0},
                "resultado": "A escala foi aprovada. O Gerald exige que cada pausa tenha uma ata de início e de fim.",
            },
            {
                "texto": "Ouvir os colegas e apresentar uma proposta conjunta.",
                "efeitos": {"suspeita": 10, "burocracia": 10, "reputacao": 25, "migalhas": 0},
                "resultado": "A equipa está mais unida. O Gerald começou a perguntar quem é o responsável pela união.",
            },
            {
                "texto": "Fazer a pausa sozinho e observar o que acontece.",
                "efeitos": {"suspeita": 15, "burocracia": 0, "reputacao": 0, "migalhas": 1},
                "resultado": "Tiveste cinco minutos de paz. O Gerald está a estudar se isso constitui um precedente perigoso.",
            },
        ],
    },
    {
        "tema": "Negociação",
        "pergunta": "O Gerald oferece-te uma promoção, mas o novo cargo implica preencher todos os formulários do departamento.",
        "opcoes": [
            {
                "texto": "Aceitar e pedir uma descrição escrita das funções.",
                "efeitos": {"suspeita": 5, "burocracia": 15, "reputacao": 10, "migalhas": 1},
                "resultado": "A promoção foi registada. A descrição das funções tem 38 páginas e inclui anexos.",
            },
            {
                "texto": "Negociar uma equipa para partilhar a carga de trabalho.",
                "efeitos": {"suspeita": 10, "burocracia": 5, "reputacao": 20, "migalhas": 0},
                "resultado": "O Gerald aceitou estudar a proposta. A equipa ainda não existe, mas já tem um organograma.",
            },
            {
                "texto": "Recusar a promoção e manter o teu horário.",
                "efeitos": {"suspeita": 20, "burocracia": -5, "reputacao": 10, "migalhas": 2},
                "resultado": "Recusaste a promoção. O Gerald considera a decisão intrigante e enviou-te duas migalhas por correio interno.",
            },
        ],
    },
    {
        "tema": "Planeamento estratégico",
        "pergunta": "O Gerald quer que aumentes a produtividade em 200%, sem recursos adicionais nem alteração de horário.",
        "opcoes": [
            {
                "texto": "Pedir prioridades e definir o que fica por fazer.",
                "efeitos": {"suspeita": 5, "burocracia": 10, "reputacao": 15, "migalhas": 0},
                "resultado": "As prioridades foram definidas. O Gerald acrescentou «tudo o resto» à categoria prioritária.",
            },
            {
                "texto": "Propor automatizar as tarefas repetitivas.",
                "efeitos": {"suspeita": 10, "burocracia": 5, "reputacao": 20, "migalhas": 0},
                "resultado": "A proposta foi considerada inovadora. O Gerald quer automatizar também a aprovação da automatização.",
            },
            {
                "texto": "Apresentar os limites de capacidade e os riscos.",
                "efeitos": {"suspeita": 15, "burocracia": 10, "reputacao": 10, "migalhas": 0},
                "resultado": "Os riscos ficaram documentados. O Gerald pede um plano para eliminar todos os riscos até amanhã.",
            },
        ],
    },
    {
        "tema": "Gestão de reputação",
        "pergunta": "Um colega publicou no chat interno: «O Gerald tem demasiado poder». O diretor pede-te uma resposta oficial.",
        "opcoes": [
            {
                "texto": "Responder que as preocupações devem ser tratadas com transparência.",
                "efeitos": {"suspeita": 10, "burocracia": 10, "reputacao": 15, "migalhas": 0},
                "resultado": "A resposta foi considerada diplomática. O Gerald quer saber porque não disseste que ele tem razão.",
            },
            {
                "texto": "Propor uma consulta anónima à equipa.",
                "efeitos": {"suspeita": 20, "burocracia": 15, "reputacao": 25, "migalhas": 0},
                "resultado": "A consulta foi aberta. O Gerald exige garantias de que será impossível identificar quem respondeu.",
            },
            {
                "texto": "Não responder até receber instruções claras.",
                "efeitos": {"suspeita": 5, "burocracia": 0, "reputacao": -5, "migalhas": 0},
                "resultado": "O silêncio foi registado. O Gerald considera criar um formulário para declarar a intenção do silêncio.",
            },
        ],
    },
    {
        "tema": "Controlo de danos",
        "pergunta": "Entornaste café sobre um documento importante. O Gerald ainda não reparou.",
        "opcoes": [
            {
                "texto": "Informar o responsável e tentar recuperar o documento.",
                "efeitos": {"suspeita": 0, "burocracia": 10, "reputacao": 15, "migalhas": 0},
                "resultado": "O incidente foi comunicado. O Gerald quer saber se o café tinha autorização para entrar na sala.",
            },
            {
                "texto": "Digitalizar o que ainda está legível e identificar as partes em falta.",
                "efeitos": {"suspeita": 5, "burocracia": 5, "reputacao": 20, "migalhas": 0},
                "resultado": "O documento foi recuperado parcialmente. O Gerald pede uma digitalização do original antes do acidente.",
            },
            {
                "texto": "Preparar uma nova versão e assinalar que é uma reconstrução.",
                "efeitos": {"suspeita": 10, "burocracia": 15, "reputacao": 5, "migalhas": 0},
                "resultado": "A reconstrução foi entregue. O Gerald abriu um processo para investigar o desaparecimento do café.",
            },
        ],
    },
    {
        "tema": "O futuro do departamento",
        "pergunta": "O Gerald vai de férias e precisa de alguém que assuma temporariamente a direção.",
        "opcoes": [
            {
                "texto": "Aceitar, com poderes e responsabilidades definidos por escrito.",
                "efeitos": {"suspeita": 15, "burocracia": 10, "reputacao": 20, "migalhas": 1},
                "resultado": "Assumiste a direção interina. O Gerald deixou 74 instruções e uma nota: «Não alteres nada».",
            },
            {
                "texto": "Propor uma gestão partilhada entre a equipa.",
                "efeitos": {"suspeita": 10, "burocracia": 20, "reputacao": 25, "migalhas": 0},
                "resultado": "A equipa aceitou experimentar. O Gerald enviou uma mensagem a perguntar quem autorizou a experiência.",
            },
            {
                "texto": "Aproveitar as férias para simplificar os processos.",
                "efeitos": {"suspeita": 30, "burocracia": -15, "reputacao": 20, "migalhas": 2},
                "resultado": "Eliminaste vários passos desnecessários. O Gerald regressa amanhã e ainda não sabe que a burocracia diminuiu.",
            },
        ],
    },
]


# --------------------------------------------------
# ESTADO DA CANDIDATURA
# --------------------------------------------------

INDICADORES_INICIAIS = {
    "suspeita": 15,
    "burocracia": 20,
    "reputacao": 50,
    "migalhas": 0,
}


def iniciar_candidatura():
    st.session_state.perguntas = random.sample(PERGUNTAS, 10)
    st.session_state.indicadores = INDICADORES_INICIAIS.copy()
    st.session_state.indice = 0
    st.session_state.historico = []
    st.session_state.ultimo_resultado = None
    st.session_state.jogo_iniciado = True


def aplicar_efeitos(efeitos):
    indicadores = st.session_state.indicadores

    for nome, valor in efeitos.items():
        indicadores[nome] += valor

        if nome == "migalhas":
            indicadores[nome] = max(0, min(10, indicadores[nome]))
        else:
            indicadores[nome] = max(0, min(100, indicadores[nome]))


def obter_final(indicadores):
    suspeita = indicadores["suspeita"]
    burocracia = indicadores["burocracia"]
    reputacao = indicadores["reputacao"]
    migalhas = indicadores["migalhas"]

    if suspeita >= 75:
        return (
            "FUGITIVA SOB VIGILÂNCIA",
            "O Gerald considera-te um risco para a segurança gansal. "
            "O teu processo continua aberto e há relatos de um ganso a correr no corredor.",
        )

    if reputacao >= 75 and burocracia <= 35:
        return (
            "REVOLUÇÃO ADMINISTRATIVA",
            "Os colegas confiam em ti e os processos começaram a desaparecer. "
            "O Gerald convocou uma reunião urgente para discutir esta situação.",
        )

    if reputacao >= 75:
        return (
            "REPRESENTANTE DOS FUNCIONÁRIOS",
            "Conquistaste a confiança da equipa. O Gerald reconhece a tua influência, "
            "mas está a preparar um formulário para regular a representação.",
        )

    if burocracia >= 80:
        return (
            "DIRETORA DOS FORMULÁRIOS CIRCULARES",
            "Criaste um sistema administrativo tão complexo que ninguém consegue "
            "terminá-lo, incluindo o Gerald.",
        )

    if migalhas >= 6:
        return (
            "GESTORA DO PATRIMÓNIO ALIMENTAR",
            "A tua reserva de migalhas é impressionante. O Gerald quer discutir "
            "a possibilidade de criar um imposto sobre as migalhas.",
        )

    if suspeita <= 25 and reputacao >= 45:
        return (
            "FUNCIONÁRIA DE CONFIANÇA DUVIDOSA",
            "Conseguiste sobreviver sem levantar suspeitas excessivas. O Gerald "
            "confia em ti o suficiente para te entregar uma chave. Não explicou de quê.",
        )

    return (
        "CONTRATO EM ANÁLISE",
        "A candidatura não foi rejeitada nem aprovada. O Gerald considera que "
        "são necessárias mais dez perguntas para esclarecer a situação.",
    )


# --------------------------------------------------
# CABEÇALHO COM GERALD
# --------------------------------------------------

st.markdown(
    f"""
    <div class="ger-header">
        <div style="text-align:center; margin-bottom:16px;">
            {GERALD_SVG}
        </div>
        <div class="ger-kicker">Departamento de Recursos Humanos</div>
        <div class="ger-title">Recrutamento Gansal</div>
        <div class="ger-subtitle">
            Uma candidatura. Dez decisões. Consequências potencialmente permanentes.
            O Gerald está a avaliar a tua capacidade de sobreviver à instituição.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# ECRÃ INICIAL
# --------------------------------------------------

if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False

if not st.session_state.jogo_iniciado:
    st.markdown("""
    <div class="ger-card">
        <div class="ger-label">Aviso ao candidato</div>
        <h3>Não existe uma resposta perfeitamente segura.</h3>
        <p>
            As tuas decisões alteram a suspeita do Gerald, a burocracia,
            a reputação entre colegas e a tua reserva de migalhas.
            Algumas consequências podem ajudar-te agora e complicar o futuro.
        </p>
        <div class="ger-quote">
            «O Departamento não garante que as decisões sejam justas.
            Garante apenas que serão registadas.»
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.button(
        "Iniciar candidatura",
        type="primary",
        use_container_width=True,
        on_click=iniciar_candidatura,
    )

    st.caption("Ao iniciar, serão sorteadas 10 perguntas de um conjunto de 15 situações.")
    st.stop()


# --------------------------------------------------
# INDICADORES
# --------------------------------------------------

indicadores = st.session_state.indicadores

st.markdown("### Estado da candidatura")

c1, c2 = st.columns(2)
c1.metric("Suspeita do Gerald", f"{indicadores['suspeita']}/100")
c2.metric("Burocracia acumulada", f"{indicadores['burocracia']}/100")

c3, c4 = st.columns(2)
c3.metric("Reputação entre colegas", f"{indicadores['reputacao']}/100")
c4.metric("Migalhas na reserva", f"{indicadores['migalhas']}/10")

total = len(st.session_state.perguntas)
indice = st.session_state.indice
respondidas = len(st.session_state.historico)

st.progress(respondidas / total)
st.caption(
    f"Decisão {min(respondidas + 1, total)} de {total}"
    if respondidas < total
    else "Entrevista concluída"
)


# --------------------------------------------------
# CONSEQUÊNCIA MAIS RECENTE
# --------------------------------------------------

if st.session_state.ultimo_resultado:
    st.markdown(
        f"""
        <div class="ger-quote">
            <strong>Consequência da decisão anterior</strong><br><br>
            {st.session_state.ultimo_resultado}
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# PERGUNTAS
# --------------------------------------------------

if indice < total:
    pergunta = st.session_state.perguntas[indice]

    st.markdown(
        f"""
        <div class="ger-card">
            <div class="ger-label">{pergunta['tema']}</div>
            <h3>{pergunta['pergunta']}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    chave_resposta = f"resposta_{indice}"

    with st.form(key=f"form_{indice}"):
        escolha = st.radio(
            "Como decides agir?",
            options=range(len(pergunta["opcoes"])),
            format_func=lambda i: pergunta["opcoes"][i]["texto"],
            index=None,
            key=chave_resposta,
        )

        submeter = st.form_submit_button(
            "Registar decisão",
            use_container_width=True,
        )

    if submeter:
        if escolha is None:
            st.warning("Tens de tomar uma decisão. O Gerald está à espera.")
        else:
            opcao = pergunta["opcoes"][escolha]

            aplicar_efeitos(opcao["efeitos"])

            st.session_state.historico.append({
                "tema": pergunta["tema"],
                "pergunta": pergunta["pergunta"],
                "escolha": opcao["texto"],
                "resultado": opcao["resultado"],
                "efeitos": opcao["efeitos"].copy(),
            })

            st.session_state.ultimo_resultado = opcao["resultado"]
            st.session_state.indice += 1
            st.rerun()


# --------------------------------------------------
# RESULTADO FINAL
# --------------------------------------------------

else:
    titulo_final, descricao_final = obter_final(st.session_state.indicadores)

    st.markdown("---")
    st.markdown("## Resultado da candidatura")

    st.markdown(
        f"""
        <div class="ger-card">
            <div class="ger-label">Decisão do departamento</div>
            <h2>{titulo_final}</h2>
            <p>{descricao_final}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Histórico da entrevista")

    for numero, item in enumerate(st.session_state.historico, start=1):
        with st.expander(f"Decisão {numero}: {item['tema']}"):
            st.write(item["pergunta"])
            st.markdown(f"**A tua escolha:** {item['escolha']}")
            st.write(item["resultado"])

            efeitos_visiveis = {
                "Suspeita": item["efeitos"].get("suspeita", 0),
                "Burocracia": item["efeitos"].get("burocracia", 0),
                "Reputação": item["efeitos"].get("reputacao", 0),
                "Migalhas": item["efeitos"].get("migalhas", 0),
            }

            st.write("**Efeitos desta decisão:**")
            st.json(efeitos_visiveis)

    st.markdown("""
    <div class="ger-quote">
        «A tua candidatura foi encerrada provisoriamente.
        O Gerald reserva-se o direito de a reabrir por motivos relacionados
        com migalhas, formulários ou assuntos que ainda não foram inventados.»
    </div>
    """, unsafe_allow_html=True)

    st.button(
        "Nova candidatura",
        type="primary",
        use_container_width=True,
        on_click=iniciar_candidatura,
    )

st.markdown("---")
st.caption("Departamento de Recursos Gansais · Todas as decisões ficam sujeitas a revisão administrativa.")
 
