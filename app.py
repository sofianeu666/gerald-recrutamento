
import random
import streamlit as st

st.set_page_config(
    page_title="Recrutamento Gansal | Gerald",
    page_icon="📋",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- IDENTIDADE VISUAL ----------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Source+Serif+4:wght@600;700&display=swap');

:root {
    --creme: #F5F2EC;
    --cartao: #FFFDFA;
    --terracota: #C97852;
    --terracota-escuro: #8B4F35;
    --texto: #29251F;
    --borda: #E5D7C8;
}

.stApp {
    background: var(--creme);
    color: var(--texto);
    font-family: 'Plus Jakarta Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 760px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: var(--texto) !important;
    font-family: 'Source Serif 4', serif !important;
}

.ger-header {
    background: var(--cartao);
    border: 1px solid var(--borda);
    border-top: 5px solid var(--terracota);
    border-radius: 16px;
    padding: 25px;
    margin-bottom: 24px;
}

.ger-eyebrow {
    color: var(--terracota-escuro);
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
}

.ger-subtitle {
    color: #65594F;
    font-size: 0.95rem;
    line-height: 1.65;
}

.ger-card {
    background: var(--cartao);
    border: 1px solid var(--borda);
    border-radius: 14px;
    padding: 22px;
    margin: 14px 0;
}

.ger-label {
    color: var(--terracota-escuro);
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
}

.ger-quote {
    border-left: 4px solid var(--terracota);
    background: #F0E5D9;
    color: var(--texto);
    border-radius: 0 10px 10px 0;
    padding: 15px 18px;
    margin: 16px 0;
    line-height: 1.65;
}

div.stButton > button {
    background: var(--terracota);
    color: white;
    border: 1px solid var(--terracota);
    border-radius: 9px;
    font-weight: 700;
    min-height: 44px;
    transition: background 0.2s ease;
}

div.stButton > button:hover {
    background: var(--terracota-escuro);
    border-color: var(--terracota-escuro);
    color: white;
}

div[role="radiogroup"] {
    background: var(--cartao);
    border: 1px solid var(--borda);
    border-radius: 12px;
    padding: 12px 16px;
    gap: 10px;
}

[data-testid="stMetric"] {
    background: var(--cartao);
    border: 1px solid var(--borda);
    padding: 14px;
    border-radius: 12px;
}

hr {
    border-color: var(--borda);
}
</style>
""", unsafe_allow_html=True)


# ---------- BANCO DE PERGUNTAS ----------

PERGUNTAS = [
    {
        "id": 1,
        "tema": "Matemática",
        "pergunta": "Qual é o dobro da metade de 4?",
        "opcoes": ["2", "4", "8", "16"],
        "certa": "4",
        "acerto": "A aritmética está de parabéns. O Gerald continua desconfiado.",
        "erro": "Uma conta simples e já temos um problema administrativo.",
    },
    {
        "id": 2,
        "tema": "Lógica",
        "pergunta": "Todos os gansos do departamento usam crachá. O Gerald pertence ao departamento. O que podemos concluir?",
        "opcoes": [
            "O Gerald usa crachá",
            "O Gerald é o diretor",
            "Todos os animais usam crachá",
            "O crachá é opcional",
        ],
        "certa": "O Gerald usa crachá",
        "acerto": "Correto. O crachá continua a ser obrigatório, até para o próprio chefe.",
        "erro": "A lógica não foi aprovada pelo departamento.",
    },
    {
        "id": 3,
        "tema": "Burocracia",
        "pergunta": "O formulário A exige o formulário B. O formulário B exige autorização do formulário A. O que falta?",
        "opcoes": [
            "Um terceiro formulário",
            "Uma autorização de férias",
            "Uma migalha carimbada",
            "Uma decisão que desbloqueie o processo",
        ],
        "certa": "Uma decisão que desbloqueie o processo",
        "acerto": "O Gerald aprova a resposta. O formulário C fica suspenso, por enquanto.",
        "erro": "O processo entrou em ciclo burocrático. A candidatura também.",
    },
    {
        "id": 4,
        "tema": "Matemática",
        "pergunta": "Um funcionário recebe 6 migalhas e entrega metade ao Gerald. Quantas migalhas lhe restam?",
        "opcoes": ["2", "3", "4", "5"],
        "certa": "3",
        "acerto": "Cálculo confirmado. O Gerald está a avaliar se entregaste as migalhas voluntariamente.",
        "erro": "O inventário de migalhas não corresponde aos registos.",
    },
    {
        "id": 5,
        "tema": "Lógica",
        "pergunta": "Hoje é terça-feira. Que dia será daqui a dois dias?",
        "opcoes": ["Quarta-feira", "Quinta-feira", "Sexta-feira", "Domingo"],
        "certa": "Quinta-feira",
        "acerto": "Calendário validado. Podes continuar a fingir que sabes em que dia estás.",
        "erro": "O calendário foi encaminhado para revisão.",
    },
    {
        "id": 6,
        "tema": "Cultura geral",
        "pergunta": "Qual destes animais é um mamífero?",
        "opcoes": ["Pato", "Ganso", "Golfinho", "Galinha"],
        "certa": "Golfinho",
        "acerto": "Correto. O Gerald não gosta de admitir que outros animais têm competências.",
        "erro": "A classificação zoológica foi devolvida para correção.",
    },
    {
        "id": 7,
        "tema": "Burocracia",
        "pergunta": "Um documento foi assinado, mas não tem data. Qual é a atitude mais prudente?",
        "opcoes": [
            "Inventar uma data",
            "Ignorar o documento",
            "Confirmar a data antes de o validar",
            "Assinar por outra pessoa",
        ],
        "certa": "Confirmar a data antes de o validar",
        "acerto": "Procedimento sensato. O Gerald exige agora três cópias dessa prudência.",
        "erro": "O departamento não aceita documentos tratados à base da adivinhação.",
    },
    {
        "id": 8,
        "tema": "Matemática",
        "pergunta": "Uma caixa contém 12 migalhas. O Gerald retira 4 e depois mais 3. Quantas ficam?",
        "opcoes": ["3", "4", "5", "7"],
        "certa": "5",
        "acerto": "Inventário correto. O Gerald quer saber quem autorizou a caixa.",
        "erro": "As migalhas não desaparecem sem um relatório.",
    },
    {
        "id": 9,
        "tema": "Lógica",
        "pergunta": "Se chover, o pátio fica molhado. O pátio está molhado. Podemos garantir que choveu?",
        "opcoes": [
            "Sim, sem dúvida",
            "Não, pode haver outra causa",
            "Só se for segunda-feira",
            "Apenas com autorização do Gerald",
        ],
        "certa": "Não, pode haver outra causa",
        "acerto": "Boa análise. O Gerald não aceita conclusões precipitadas, salvo quando as toma.",
        "erro": "Uma possibilidade não é uma prova. O departamento registou a ocorrência.",
    },
    {
        "id": 10,
        "tema": "Burocracia",
        "pergunta": "O prazo termina hoje, mas o sistema está indisponível. Qual é o melhor primeiro passo?",
        "opcoes": [
            "Apagar o processo",
            "Registar o problema e contactar o responsável",
            "Alterar o relógio",
            "Culpar o estagiário sem investigar",
        ],
        "certa": "Registar o problema e contactar o responsável",
        "acerto": "Procedimento adequado. O Gerald já abriu um processo sobre o sistema.",
        "erro": "O departamento exige evidências, não teorias sobre culpados.",
    },
    {
        "id": 11,
        "tema": "Matemática",
        "pergunta": "Qual é o resultado de 15 menos 3 vezes 2, respeitando a prioridade das operações?",
        "opcoes": ["24", "9", "12", "6"],
        "certa": "9",
        "acerto": "Prioridades respeitadas. O Gerald aplicará a mesma regra aos pedidos de férias.",
        "erro": "A prioridade das operações não pode ser decidida por votação.",
    },
    {
        "id": 12,
        "tema": "Cultura geral",
        "pergunta": "Qual é a capital de Portugal?",
        "opcoes": ["Porto", "Coimbra", "Lisboa", "Faro"],
        "certa": "Lisboa",
        "acerto": "Correto. O Gerald considera abrir uma filial, desde que haja migalhas.",
        "erro": "A geografia foi encaminhada para formação obrigatória.",
    },
    {
        "id": 13,
        "tema": "Burocracia",
        "pergunta": "Um colega pede a tua palavra-passe para concluir uma tarefa. O que deves fazer?",
        "opcoes": [
            "Partilhá-la por mensagem",
            "Escrevê-la num papel",
            "Não a partilhar e indicar um procedimento autorizado",
            "Usar a palavra-passe do Gerald",
        ],
        "certa": "Não a partilhar e indicar um procedimento autorizado",
        "acerto": "Segurança aprovada. O Gerald guarda a própria palavra-passe debaixo de uma pedra.",
        "erro": "O departamento de segurança acabou de levantar uma sobrancelha.",
    },
    {
        "id": 14,
        "tema": "Lógica",
        "pergunta": "Numa fila, estás à frente da pessoa que está em último lugar. Em que posição estás?",
        "opcoes": [
            "Em último",
            "Em penúltimo",
            "Em primeiro",
            "Não é possível determinar",
        ],
        "certa": "Em penúltimo",
        "acerto": "Correto. Estás imediatamente à frente da última pessoa da fila. O Gerald exige uma acta e uma cópia da acta.",
        "erro": "A fila foi reconstituída e a tua posição continua sob investigação.",
    },
    {
        "id": 15,
        "tema": "Burocracia",
        "pergunta": "O Gerald pede um relatório sobre o número de relatórios produzidos hoje. Qual é a primeira coisa a fazer?",
        "opcoes": [
            "Inventar um número convincente",
            "Contar os relatórios existentes",
            "Criar dez relatórios novos",
            "Perguntar ao relatório principal",
        ],
        "certa": "Contar os relatórios existentes",
        "acerto": "Contagem confirmada. O Gerald pede agora um relatório sobre esta contagem.",
        "erro": "O departamento não aceita estatísticas inventadas, exceto nas reuniões.",
    },
]


# ---------- ESTADO DO JOGO ----------

if "quiz_id" not in st.session_state:
    st.session_state.quiz_id = 1
    st.session_state.perguntas = random.sample(PERGUNTAS, 10)
    st.session_state.indice = 0
    st.session_state.pontos = 0
    st.session_state.respondida = False
    st.session_state.historico = []


# ---------- CABEÇALHO ----------

st.markdown("""
<div class="ger-header">
    <div class="ger-eyebrow">Departamento de Recursos Gansais</div>
    <h1>Recrutamento Gansal</h1>
    <div class="ger-subtitle">
        A tua candidatura está sob avaliação. Responde com rigor.
        O Gerald não aceita desculpas, apenas resultados devidamente
        documentados.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- ENTREVISTA ----------

indice = st.session_state.indice
perguntas = st.session_state.perguntas

if indice < len(perguntas):
    q = perguntas[indice]
    numero = indice + 1

    st.progress(numero / len(perguntas))

    col1, col2 = st.columns(2)
    col1.metric("Pergunta", f"{numero} / {len(perguntas)}")
    col2.metric("Pontos", st.session_state.pontos)

    st.markdown(f"""
    <div class="ger-card">
        <div class="ger-label">{q['tema']}</div>
        <h3>Pergunta {numero:02d}</h3>
        <p>{q['pergunta']}</p>
    </div>
    """, unsafe_allow_html=True)

    resposta = st.radio(
        "Seleciona uma resposta:",
        q["opcoes"],
        index=None,
        key=f"resposta_{st.session_state.quiz_id}_{indice}",
        disabled=st.session_state.respondida,
    )

    if not st.session_state.respondida:
        if st.button("Submeter resposta", use_container_width=True):
            if resposta is None:
                st.warning("Seleciona uma resposta antes de continuar.")
            else:
                acertou = resposta == q["certa"]

                if acertou:
                    st.session_state.pontos += 1
                    comentario = q["acerto"]
                else:
                    comentario = q["erro"]

                st.session_state.historico.append({
                    "tema": q["tema"],
                    "pergunta": q["pergunta"],
                    "resposta": resposta,
                    "certa": q["certa"],
                    "acertou": acertou,
                })

                st.session_state.comentario = comentario
                st.session_state.acertou = acertou
                st.session_state.respondida = True
                st.rerun()

    else:
        if st.session_state.acertou:
            st.success("Resposta aceite.")
        else:
            st.error(f"Resposta incorreta. A resposta correta era: {q['certa']}.")

        st.markdown(
            f'<div class="ger-quote">{st.session_state.comentario}</div>',
            unsafe_allow_html=True,
        )

        if st.button("Próxima pergunta →", use_container_width=True):
            st.session_state.indice += 1
            st.session_state.respondida = False
            st.rerun()

else:
    # ---------- RESULTADO FINAL ----------

    pontos = st.session_state.pontos
    total = len(perguntas)
    percentagem = round(pontos / total * 100)

    st.markdown("""
    <div class="ger-card">
        <div class="ger-label">Processo concluído</div>
        <h2>Veredicto do Gerald</h2>
        <p>A entrevista terminou. O departamento emitiu uma decisão.</p>
    </div>
    """, unsafe_allow_html=True)

    a, b = st.columns(2)
    a.metric("Pontuação final", f"{pontos} / {total}")
    b.metric("Respostas certas", f"{percentagem}%")

    if pontos >= 8:
        st.success(
            "Candidatura aprovada! O Gerald está impressionado. "
            "Não confundas isto com confiança."
        )
    elif pontos >= 5:
        st.warning(
            "Candidatura em análise. O Gerald exige formação adicional "
            "e um relatório sobre essa formação."
        )
    else:
        st.error(
            "Candidatura recusada. Foste encaminhado para o inventário "
            "de migalhas até nova avaliação."
        )

    st.markdown("### Relatório da entrevista")

    for i, item in enumerate(st.session_state.historico, start=1):
        simbolo = "✓" if item["acertou"] else "✗"
        with st.expander(f"{simbolo} Pergunta {i}: {item['tema']}"):
            st.write(item["pergunta"])
            st.write(f"**A tua resposta:** {item['resposta']}")
            if not item["acertou"]:
                st.write(f"**Resposta correta:** {item['certa']}")

    if st.button("Nova candidatura", use_container_width=True):
        st.session_state.quiz_id += 1
        st.session_state.perguntas = random.sample(PERGUNTAS, 10)
        st.session_state.indice = 0
        st.session_state.pontos = 0
        st.session_state.respondida = False
        st.session_state.historico = []
        st.rerun()


st.markdown("""
<hr>
<div style="text-align:center;color:#806F60;font-size:0.78rem;">
    Departamento de RH do Gerald · Recursos Gansais ·
    Todas as candidaturas estão sujeitas a contagem de migalhas.
</div>
""", unsafe_allow_html=True)
