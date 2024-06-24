from flask import Flask, request, render_template_string

app = Flask(__name__)

# Template HTML básico com melhorias de design
template = """
<!doctype html>
<html>
<head>
    <title>Jogo de Aventura</title>
   <style>
    body {
        font-family: 'Arial', sans-serif;
        background: linear-gradient(to bottom, #2c3e50, #bdc3c7);
        color: #ecf0f1;
        text-align: center;
        padding: 20px;
        animation: backgroundAnimation 10s infinite alternate;
    }
    @keyframes backgroundAnimation {
        0% { background: linear-gradient(to bottom, #2c3e50, #bdc3c7); }
        100% { background: linear-gradient(to bottom, #bdc3c7, #2c3e50); }
    }
    h1 {
        font-size: 2.5em;
    }
    p {
        font-size: 1.2em;
    }
    .container {
        max-width: 600px;
        margin: auto;
        background: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }
    .button {
        background-color: #3498db;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        border-radius: 5px;
        transition: background-color 0.3s, transform 0.3s;
    }
    .button:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }
    input[type="radio"] {
        margin: 10px;
    }
</style>

</head>
<body>
    <div class="container">
        <h1>{{ title }}</h1>
        <p>{{ message }}</p>
        <form method="post">
            {% for option in options %}
                <input type="radio" name="choice" value="{{ option['value'] }}" id="{{ option['value'] }}">
                <label for="{{ option['value'] }}">{{ option['text'] }}</label><br>
            {% endfor %}
            <input type="submit" value="Enviar" class="button">
        </form>
        <p>{{ error }}</p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    global state
    if request.method == "POST":
        choice = request.form.get("choice")
        if choice:
            state = state['actions'][choice]()
        else:
            state['error'] = "Escolha inválida. Por favor, escolha novamente."

    return render_template_string(template, **state)

def iniciar_jogo():
    return {
        'title': "Bem-vindo ao Jogo de Aventura!",
        'message': "Você é o Cavaleiro de Prata, acompanhado por seu fiel poodle de olhos esverdeados. Prepare-se para uma jornada épica em um mundo cheio de mistérios! Você está em uma encruzilhada na floresta escura...",
        'options': [
            {'value': 'trilha_sombras', 'text': 'Seguir pela trilha das sombras'},
            {'value': 'trilha_luz', 'text': 'Seguir pela trilha da luz'}
        ],
        'actions': {
            'trilha_sombras': trilha_das_sombras,
            'trilha_luz': trilha_da_luz
        },
        'error': ''
    }

def escolher_caminho():
    return {
        'title': "Encruzilhada na Floresta Escura",
        'message': "O que você deseja fazer?",
        'options': [
            {'value': 'trilha_sombras', 'text': 'Seguir pela trilha das sombras'},
            {'value': 'trilha_luz', 'text': 'Seguir pela trilha da luz'}
        ],
        'actions': {
            'trilha_sombras': trilha_das_sombras,
            'trilha_luz': trilha_da_luz
        },
        'error': ''
    }

def trilha_das_sombras():
    return {
        'title': "Trilha das Sombras",
        'message': "Você escolheu seguir pela trilha das sombras. A trilha fica mais estreita à medida que avança. Você se depara com uma caverna misteriosa. Deseja entrar na caverna?",
        'options': [
            {'value': 'sim_caverna', 'text': 'Sim'},
            {'value': 'nao_caverna', 'text': 'Não'}
        ],
        'actions': {
            'sim_caverna': explorar_caverna,
            'nao_caverna': continuar_trilha_sombras
        },
        'error': ''
    }

def trilha_da_luz():
    return {
        'title': "Trilha da Luz",
        'message': "Você escolheu seguir pela trilha da luz. A trilha está bem iluminada pelos raios do sol. Você avista uma cabana à distância. Deseja visitar a cabana?",
        'options': [
            {'value': 'sim_cabana', 'text': 'Sim'},
            {'value': 'nao_cabana', 'text': 'Não'}
        ],
        'actions': {
            'sim_cabana': visitar_cabana,
            'nao_cabana': continuar_trilha_luz
        },
        'error': ''
    }

def explorar_caverna():
    return {
        'title': "Explorando a Caverna",
        'message': "Você entra na caverna escura. Dentro, você encontra tesouros antigos e inscrições misteriosas. Você deseja pegar algum tesouro?",
        'options': [
            {'value': 'sim_tesouro', 'text': 'Sim'},
            {'value': 'nao_tesouro', 'text': 'Não'}
        ],
        'actions': {
            'sim_tesouro': pegar_tesouro,
            'nao_tesouro': continuar_jogo
        },
        'error': ''
    }

def visitar_cabana():
    return {
        'title': "Visitando a Cabana",
        'message': "Você se aproxima da cabana e bate à porta. Um velho sábio abre a porta e o convida para entrar. Ele lhe oferece um elixir mágico que pode curar ferimentos. Você deseja beber o elixir?",
        'options': [
            {'value': 'sim_elixir', 'text': 'Sim'},
            {'value': 'nao_elixir', 'text': 'Não'}
        ],
        'actions': {
            'sim_elixir': beber_elixir,
            'nao_elixir': continuar_jogo
        },
        'error': ''
    }

def pegar_tesouro():
    return {
        'title': "Tesouro Encontrado",
        'message': "Você pega um artefato antigo e decide continuar sua jornada.",
        'options': [
            {'value': 'continuar', 'text': 'Continuar'}
        ],
        'actions': {
            'continuar': escolher_caminho
        },
        'error': ''
    }

def beber_elixir():
    return {
        'title': "Bebendo o Elixir",
        'message': "Você bebe o elixir e se sente revigorado.",
        'options': [
            {'value': 'continuar', 'text': 'Continuar'}
        ],
        'actions': {
            'continuar': escolher_caminho
        },
        'error': ''
    }

def continuar_jogo():
    return {
        'title': "Continuando a Jornada",
        'message': "Deseja continuar sua jornada?",
        'options': [
            {'value': 'sim_continuar', 'text': 'Sim'},
            {'value': 'nao_continuar', 'text': 'Não'}
        ],
        'actions': {
            'sim_continuar': escolher_caminho,
            'nao_continuar': encerrar_jogo
        },
        'error': ''
    }

def continuar_trilha_sombras():
    return {
        'title': "Trilha das Sombras",
        'message': "Você decide não arriscar e continua pela trilha das sombras. Mais adiante, você encontra um rio perigoso. Deseja tentar atravessar o rio?",
        'options': [
            {'value': 'sim_rio', 'text': 'Sim'},
            {'value': 'nao_rio', 'text': 'Não'}
        ],
        'actions': {
            'sim_rio': atravessar_rio,
            'nao_rio': escolher_caminho
        },
        'error': ''
    }

def atravessar_rio():
    return {
        'title': "Atravessando o Rio",
        'message': "Você tenta atravessar o rio, mas a correnteza é forte. Com muito esforço, você consegue chegar ao outro lado.",
        'options': [
            {'value': 'continuar', 'text': 'Continuar'}
        ],
        'actions': {
            'continuar': escolher_caminho
        },
        'error': ''
    }

def continuar_trilha_luz():
    return {
        'title': "Trilha da Luz",
        'message': "Você decide não parar e continua pela trilha da luz. Mais adiante, você encontra um jardim encantado. Deseja explorar o jardim?",
        'options': [
            {'value': 'sim_jardim', 'text': 'Sim'},
            {'value': 'nao_jardim', 'text': 'Não'}
        ],
        'actions': {
            'sim_jardim': explorar_jardim,
            'nao_jardim': escolher_caminho
        },
        'error': ''
    }

def explorar_jardim():
    return {
        'title': "Explorando o Jardim",
        'message': "Você decide explorar o jardim e encontra plantas exóticas e criaturas mágicas. Você sente que o jardim guarda um segredo.",
        'options': [
            {'value': 'continuar', 'text': 'Continuar'}
        ],
        'actions': {
            'continuar': escolher_caminho
        },
        'error': ''
    }

def encerrar_jogo():
    return {
        'title': "Fim da Jornada",
        'message': "Obrigado por jogar o Jogo de Aventura! Até a próxima.",
        'options': [],
        'actions': {},
        'error': ''
    }

# Estado inicial do jogo
state = iniciar_jogo()

if __name__ == "__main__":
    app.run(debug=True)
