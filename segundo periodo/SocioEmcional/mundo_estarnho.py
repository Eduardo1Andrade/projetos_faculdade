import random

print("""
MUNDO ESTRANHO

Você e seu amigo(a) despertam em um lugar desconhecido.

Ao longe, uma saída aparece em fragmentos.
Cada escolha pode aproximar ou afastar vocês dela.

Objetivo:
Encontrar 5 fragmentos para abrir a saída.

""")

# ===== ESTADO =====
estabilidade = 50
fragmentos = 0
turnos = 10

jogadores = [
    {"nome": "Jogador 1", "energia": 30},
    {"nome": "Jogador 2", "energia": 30}
]

# ===== EVENTOS =====
eventos = [
    {
        "descricao": "O caminho se divide.",
        "opcoes": [
            ("Seguir sozinho", {"self": +5, "other": -5, "world": -5, "frag": -1}),
            ("Esperar o outro", {"self": -2, "other": +2, "world": +5, "frag": +1})
        ]
    },
    {
        "descricao": "Uma voz sussurra respostas rápidas.",
        "opcoes": [
            ("Confiar no impulso", {"self": +5, "world": -5, "frag": -1}),
            ("Pensar antes de agir", {"self": -2, "world": +5, "frag": +1})
        ]
    },
    {
        "descricao": "Uma porta antiga aparece.",
        "opcoes": [
            ("Forçar a passagem", {"self": -5, "world": -5, "frag": -1}),
            ("Observar o mecanismo", {"world": +5, "frag": +1})
        ]
    },
    {
        "descricao": "O outro jogador hesita.",
        "opcoes": [
            ("Ignorar", {"self": +5, "other": -5, "frag": -1}),
            ("Ajustar o ritmo", {"self": -2, "other": +3, "frag": +1})
        ]
    }
]

# ===== FUNÇÕES =====
def aplicar_efeitos(jogador, outro, efeitos):
    global estabilidade, fragmentos

    if "self" in efeitos:
        jogador["energia"] += efeitos["self"]

    if "other" in efeitos:
        outro["energia"] += efeitos["other"]

    if "world" in efeitos:
        estabilidade += efeitos["world"]

    if "frag" in efeitos:
        fragmentos += efeitos["frag"]

        if efeitos["frag"] > 0:
            print("Vocês encontraram um fragmento da saída.")
        elif efeitos["frag"] < 0:
            print("Um fragmento se desfaz diante de vocês.")

def mostrar_status():
    print("\n--- PROGRESSO ---")
    print(f"Fragmentos: {fragmentos}/5")

    if estabilidade > 30:
        print("Ambiente: Estável")
    else:
        print("Ambiente: Instável")

    for j in jogadores:
        print(f"{j['nome']}: Energia {j['energia']}")
    print("-----------------\n")

def verificar_estado():
    if fragmentos >= 5:
        print("\nA saída finalmente se completa.")
        print("Vocês escaparam do Mundo Estranho.")
        exit()

    for j in jogadores:
        if j["energia"] <= 0:
            print(f"\n{j['nome']} não consegue continuar.")
            print("A saída desaparece.")
            exit()

    if estabilidade <= 0:
        print("\nO ambiente colapsa.")
        exit()

# ===== LOOP =====
for turno in range(1, turnos + 1):
    print(f"\n--- TURNO {turno} ---")

    for i in range(2):
        jogador = jogadores[i]
        outro = jogadores[1 - i]

        evento = random.choice(eventos)

        # embaralhar opções (aqui está a melhoria principal)
        opcoes = evento["opcoes"][:]
        random.shuffle(opcoes)

        print(f"\n{jogador['nome']}")
        print(evento["descricao"])

        for idx, (texto, _) in enumerate(opcoes, 1):
            print(f"{idx} - {texto}")

        escolha = input("> ")

        if not escolha.isdigit() or int(escolha) not in [1, 2]:
            print("A indecisão atrasa vocês.")
            estabilidade -= 5
            continue

        _, efeitos = opcoes[int(escolha) - 1]
        aplicar_efeitos(jogador, outro, efeitos)

        mostrar_status()
        verificar_estado()

print("\nO tempo se esgota.")
mostrar_status()