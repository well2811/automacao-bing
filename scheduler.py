import random
import time
import subprocess
from datetime import datetime, timedelta

# Lista de palavras (mesma sua lista original)
palavras = [
    "inteligência artificial", "mudanças climáticas", "realidade virtual",
    "computação quântica", "carros autônomos", "energia renovável",
    "exploração espacial", "blockchain", "metaverso", "nanotecnologia",
    "biotecnologia", "robótica", "cibersegurança", "impressão 3D",
    "internet das coisas", "big data", "machine learning", "cloud computing",
    "redes neurais", "assistente virtual", "desenvolvimento sustentável",
    "medicina personalizada", "engenharia genética", "agricultura vertical",
    "educação a distância", "telemedicina", "mobilidade urbana",
    "veículos elétricos", "criptomoedas", "realidade aumentada",
    "transformação digital", "automação industrial", "cidades inteligentes",
    "saúde mental", "nutrição esportiva", "história antiga", "mitologia grega",
    "arte moderna", "literatura clássica", "filosofia contemporânea",
    "geografia física", "economia global", "psicologia positiva",
    "sociologia urbana", "antropologia cultural", "arqueologia",
    "direitos humanos", "justiça social", "pandemia", "vacinas",
    "poluição plástica", "desmatamento", "biodiversidade", "oceanos",
    "animais selvagens", "aves migratórias", "cultivo hidropônico",
    "jardinagem orgânica", "culinária vegana", "cozinha molecular",
    "gastronomia", "cafeterias", "chocolates finos", "vinhos",
    "cervejas artesanais", "viagens de aventura", "turismo ecológico",
    "mochilão na europa", "praias do nordeste", "montanhismo",
    "mergulho", "esportes radicais", "futebol", "basquete", "vôlei",
    "tênis", "natação", "corrida de rua", "yoga", "meditação",
    "pilates", "musculação", "alimentação saudável", "dietas",
    "receitas fit", "programação python", "desenvolvimento web",
    "aplicativos mobile", "jogos eletrônicos", "e-sports", "streaming",
    "fotografia digital", "edição de vídeo", "design gráfico",
    "escrita criativa", "poesia", "contos", "romances", "biografias",
    "documentários", "séries de TV", "filmes clássicos", "música pop",
    "rock alternativo", "jazz", "blues", "samba", "mpb", "eletrônica",
    "indústria da moda", "design de interiores", "arquitetura sustentável",
    "urbanismo", "política internacional", "relações exteriores",
    "direito penal", "direito civil", "educação infantil",
    "pedagogia", "psicopedagogia", "neurociência", "astronomia",
    "cosmologia", "física quântica", "química orgânica", "biologia molecular"
]

random.shuffle(palavras)
palavras = palavras[:30]

def gerar_horarios():
    base = datetime.now().replace(hour=7, minute=0, second=0, microsecond=0)
    fim = datetime.now().replace(hour=23, minute=0, second=0, microsecond=0)

    segundos_totais = int((fim - base).total_seconds())
    horarios = sorted(random.sample(range(segundos_totais), 30))
    
    return [base + timedelta(seconds=s) for s in horarios]

horarios = gerar_horarios()

for i, horario in enumerate(horarios, start=1):
    agora = datetime.now()
    
    espera = (horario - agora).total_seconds()
    if espera > 0:
        print(f"[{agora}] Aguardando até {horario} para a pesquisa {i}/30...")
        time.sleep(espera)

    palavra = palavras[i - 1]
    print(f"[{datetime.now()}] Executando pesquisa {i}/30: {palavra}")

    subprocess.run(["python3", "bot.py", palavra])
