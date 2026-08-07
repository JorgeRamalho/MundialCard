# -*- coding: utf-8 -*-
"""
Gera documento PDF e slides PowerPoint de apresentacao ao cliente — MundialCard.
Uso: python scripts/gerar-apresentacao-cliente.py
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from fpdf import FPDF
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
APRESENTACAO = DOCS / "apresentacao"
PDF_OUT = APRESENTACAO / "APRESENTACAO-CLIENTE-MUNDIALCARD.pdf"
PPTX_OUT = APRESENTACAO / "APRESENTACAO-CLIENTE-MUNDIALCARD.pptx"

FONT = Path("C:/Windows/Fonts/arial.ttf")
FONT_BOLD = Path("C:/Windows/Fonts/arialbd.ttf")

# Identidade MundialCard
BRAND = RGBColor(140, 20, 23)
BRAND_DARK = RGBColor(90, 12, 14)
CREAM = RGBColor(247, 244, 238)
SLATE = RGBColor(51, 65, 85)
WHITE = RGBColor(255, 255, 255)
GOLD = RGBColor(212, 160, 23)

TODAY = date(2026, 7, 6)

PHASES = [
    {
        "num": "01",
        "title": "Estrategia e Planejamento",
        "period": "03/07/2026",
        "items": [
            "Definicao do modelo de venda digital escalavel (B2C e B2B)",
            "Mapeamento da jornada: lead, educacao, contratacao, kit de boas-vindas",
            "Alinhamento com o conceito oficial mundialcard.com.br",
            "Documentacao operacional (venda digital, KPIs, funil de vendas)",
        ],
    },
    {
        "num": "02",
        "title": "Identidade Visual e Design",
        "period": "03/07/2026",
        "items": [
            "Criacao da logomarca SVG e favicon",
            "Paleta institucional bordo (#8C1417) com gradientes refinados",
            "Tipografia Plus Jakarta Sans + DM Sans",
            "Renomeacao da marca para MundialCard — Seu cartao de super beneficios",
            "Header branco, rodape alinhado, elementos de requinte nas secoes",
        ],
    },
    {
        "num": "03",
        "title": "Desenvolvimento da Plataforma",
        "period": "03-04/07/2026",
        "items": [
            "Arquitetura Vite + React + React Router (SPA moderna)",
            "Landing page com 11 secoes estrategicas de conversao",
            "9 paginas internas: cadastro, dashboard, area do cliente, parceiros, etc.",
            "Formulario de cupom de lancamento com persistencia local",
            "Planos Bronze, Prata, Ouro, Diamante, Premium e Platinum",
        ],
    },
    {
        "num": "04",
        "title": "Conteudo, Midia e Conversao",
        "period": "03-04/07/2026",
        "items": [
            "Carrossel hero com banners oficiais (familia e colaboradores)",
            "Secao de telemedicina em destaque (posicao estrategica na home)",
            "Videos institucionais com autoplay responsivo (tela cheia)",
            "Rede de parceiros credenciados com logos oficiais",
            "Integracao WhatsApp em todo o funil de contato",
        ],
    },
    {
        "num": "05",
        "title": "Responsividade e Experiencia Mobile",
        "period": "04/07/2026",
        "items": [
            "Correcao de layout para smartphones e tablets (375px a 1024px)",
            "Menu hamburger em drawer fullscreen sobre todo o conteudo",
            "Header mobile otimizado: logo + menu (acoes no drawer)",
            "Carrossel, grids, formularios e videos adaptados por breakpoint",
            "Validacao em dispositivos reais e deploy em producao (Netlify)",
        ],
    },
    {
        "num": "06",
        "title": "Funcionalidades Avancadas e Compliance",
        "period": "05-06/07/2026",
        "items": [
            "Politica de cookies LGPD (Aceitar, Recusar, Configurar)",
            "Area do cliente com login no header (emoji + estilizacao)",
            "Botao voltar ao topo com identidade visual da marca",
            "Reordenacao estrategica de secoes (jornada, suporte, FAQ)",
            "Ajustes finos de header, parceiros e textos institucionais",
        ],
    },
    {
        "num": "07",
        "title": "Publicacao, Versionamento e Entrega",
        "period": "04-06/07/2026",
        "items": [
            "Repositorio GitHub profissional com branches e historico",
            "9 commits documentados na linha do tempo do projeto",
            "Deploy em producao: mundialcard.netlify.app",
            "Scripts de build, preview e acesso em rede local",
            "Documentacao tecnica e historico de registros",
        ],
    },
]

DELIVERABLES = [
    ("Plataforma web completa", "Site institucional + areas logadas + formularios"),
    ("Identidade visual", "Logo SVG, paleta, tipografia, favicon"),
    ("Landing page de conversao", "11 secoes com CTAs, planos e FAQ"),
    ("Area do cliente", "Login, cartao digital, kit de boas-vindas"),
    ("Area B2B", "Portal do representante comercial"),
    ("Dashboard operacional", "KPIs, leads e gestao simulada"),
    ("Central de atendimento", "FAQ, busca, fluxo IA + humano"),
    ("Politica de cookies", "Banner LGPD com preferencias"),
    ("Repositorio GitHub", "Codigo versionado e documentado"),
    ("Deploy em producao", "Netlify com SPA configurada"),
]

SITE_SECTIONS = [
    ("Carrossel", "Banners e imagens de saude/telemedicina"),
    ("Telemedicina", "Destaque principal — consulta online"),
    ("Hero", "Proposta de valor + video do app"),
    ("Beneficios", "Cartao multibeneficios e diferenciais"),
    ("Jornada digital", "Contratacao ate kit de boas-vindas"),
    ("Parceiros", "Rede credenciada + cartao Mundial Card"),
    ("Planos", "Bronze a Platinum com precos"),
    ("Suporte", "Sistema interno para clientes ativos"),
    ("FAQ", "Duvidas + videos explicativos"),
    ("B2B", "Representantes comerciais"),
    ("Lancamento", "Formulario de cupom de inauguracao"),
]

ROUTES = [
    ("/", "Home — landing page"),
    ("/cadastro", "Cupom de inauguracao"),
    ("/area-cliente", "Area do cliente"),
    ("/dashboard", "Dashboard operacional"),
    ("/parceiros", "Area do representante B2B"),
    ("/atendimento", "Central de atendimento"),
    ("/agendamento", "Agendamento telemedicina"),
    ("/produtos", "Produtos e servicos"),
    ("/app", "Download do aplicativo"),
    ("/politica-cookies", "Politica de cookies"),
]

COMMITS = [
    ("04/07", "Release inicial da plataforma digital"),
    ("04/07", "Historico de registros no GitHub"),
    ("04/07", "Correcao layout mobile smartphones"),
    ("04/07", "Menu hamburger sobreposto no mobile"),
    ("04/07", "Menu navbar drawer fullscreen"),
    ("04/07", "Ajuste carrossel desktop/responsivo"),
    ("06/07", "Atualizacao area do cliente"),
]


# ---------------------------------------------------------------------------
# PDF
# ---------------------------------------------------------------------------

class ClientPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("Arial", "", str(FONT))
        self.add_font("Arial", "B", str(FONT_BOLD))
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_x(10)
        self.set_font("Arial", "B", 8)
        self.set_text_color(140, 20, 23)
        self.cell(100, 6, "MundialCard | Apresentacao ao Cliente")
        self.set_font("Arial", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 6, f"Pag. {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(140, 20, 23)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)
        self.set_x(10)

    def footer(self):
        self.set_y(-14)
        self.set_font("Arial", "", 7)
        self.set_text_color(150, 150, 150)
        self.cell(0, 6, f"Documento confidencial | MundialCard | {TODAY.strftime('%d/%m/%Y')}", align="C")

    def ensure_space(self, h=20):
        if self.get_y() > 280 - h:
            self.add_page()

    def h1(self, text):
        self.ensure_space(25)
        self.set_font("Arial", "B", 18)
        self.set_text_color(140, 20, 23)
        self.multi_cell(0, 9, text)
        self.ln(3)
        self.set_text_color(30, 30, 30)

    def h2(self, text):
        self.ensure_space(18)
        self.ln(2)
        self.set_font("Arial", "B", 13)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 7, text)
        self.ln(2)
        self.set_text_color(30, 30, 30)

    def h3(self, text):
        self.ensure_space(14)
        self.set_font("Arial", "B", 11)
        self.set_text_color(140, 20, 23)
        self.multi_cell(0, 6, text)
        self.set_text_color(30, 30, 30)

    def p(self, text):
        self.ensure_space()
        self.set_x(10)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text):
        self.ensure_space()
        self.set_x(10)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5.5, f"  \u2022  {text}")

    def phase_block(self, phase: dict):
        self.ensure_space(40)
        self.set_fill_color(247, 244, 238)
        self.set_font("Arial", "B", 11)
        self.set_text_color(140, 20, 23)
        self.cell(0, 8, f"FASE {phase['num']} — {phase['title']}  |  {phase['period']}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        for item in phase["items"]:
            self.bullet(item)
        self.ln(4)

    def two_col_table(self, headers, rows, widths=(70, 110)):
        self.ensure_space(15)
        self.set_x(10)
        self.set_font("Arial", "B", 9)
        self.set_fill_color(140, 20, 23)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(widths[i], 7, h, border=1, fill=True)
        self.ln()
        self.set_text_color(30, 30, 30)
        self.set_font("Arial", "", 9)
        alt = False
        for row in rows:
            if alt:
                self.set_fill_color(247, 244, 238)
            else:
                self.set_fill_color(255, 255, 255)
            self.set_x(10)
            for i, cell in enumerate(row):
                self.cell(widths[i], 7, cell, border=1, fill=True)
            self.ln()
            alt = not alt

    def cover(self):
        self.add_page()
        self.set_fill_color(140, 20, 23)
        self.rect(0, 0, 210, 95, "F")
        self.set_fill_color(212, 160, 23)
        self.rect(0, 95, 210, 3, "F")
        self.ln(22)
        self.set_font("Arial", "B", 32)
        self.set_text_color(255, 255, 255)
        self.cell(0, 14, "MundialCard", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Arial", "", 14)
        self.cell(0, 8, "Seu cartao de super beneficios", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(28)
        self.set_text_color(30, 30, 30)
        self.set_font("Arial", "B", 20)
        self.cell(0, 10, "Apresentacao do Projeto", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Arial", "", 13)
        self.set_text_color(80, 80, 80)
        self.cell(0, 8, "Plataforma Digital — Do conceito a entrega", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(20)
        self.set_font("Arial", "", 11)
        info = [
            f"Data do documento: {TODAY.strftime('%d de %B de %Y').replace('July', 'julho')}",
            "Cliente: MundialCard",
            "Tipo: Documento de apresentacao e entrega",
            "Periodo do projeto: 03 a 06 de julho de 2026",
            "Repositorio: github.com/JorgeRamalho/Mundialcard",
            "Producao: mundialcard.netlify.app",
        ]
        for line in info:
            self.cell(0, 7, line, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(15)
        self.set_font("Arial", "B", 10)
        self.set_text_color(140, 20, 23)
        self.cell(0, 7, "CONFIDENCIAL — USO INTERNO E APRESENTACAO AO CLIENTE", align="C")


def build_pdf():
    pdf = ClientPDF()
    pdf.cover()

    # SUMARIO EXECUTIVO
    pdf.add_page()
    pdf.h1("1. Sumario Executivo")
    pdf.p(
        "Este documento apresenta de forma estruturada todo o processo de desenvolvimento da "
        "plataforma digital MundialCard — desde a concepcao estrategica da venda digital escalavel "
        "ate a entrega da aplicacao web em producao, com identidade visual propria, experiencia "
        "responsiva e funcionalidades de conversao, atendimento e gestao."
    )
    pdf.p(
        "O projeto foi conduzido em sete fases ao longo de quatro dias, resultando em uma "
        "plataforma web moderna com 10 rotas, 11 secoes de conversao na home, area do cliente, "
        "portal B2B, dashboard operacional, politica de cookies LGPD e publicacao versionada no GitHub."
    )
    pdf.h2("Principais resultados")
    for r in [
        "Plataforma web completa publicada e acessivel",
        "Identidade visual alinhada a marca MundialCard",
        "Experiencia mobile validada em dispositivos reais",
        "Funil de conversao com cupom, planos e telemedicina",
        "Repositorio profissional com historico de alteracoes",
    ]:
        pdf.bullet(r)

    # SOBRE O PROJETO
    pdf.add_page()
    pdf.h1("2. Sobre o Projeto")
    pdf.h2("2.1 Visao do produto")
    pdf.p(
        "A MundialCard oferece cartao de desconto e multibeneficios na area de saude e bem-estar, "
        "com telemedicina, planos funerarios, descontos em rede credenciada e venda digital escalavel "
        "para todo o Brasil — incluindo canal B2B via representantes comerciais."
    )
    pdf.h2("2.2 Problema a resolver")
    for b in [
        "Ausencia de presenca digital moderna alinhada ao posicionamento da marca",
        "Necessidade de funil de conversao online (cupom, planos, cadastro)",
        "Demanda por plataforma de atendimento, suporte e area do cliente",
        "Expansao B2B com portal para representantes comerciais",
        "Conformidade com LGPD (politica de cookies)",
    ]:
        pdf.bullet(b)

    pdf.h2("2.3 Objetivos do projeto")
    for b in [
        "Criar site institucional robusto que transmita confianca no setor de beneficios",
        "Desenvolver identidade visual refinada (logo, cores, tipografia, layout)",
        "Implementar jornada digital completa: da contratacao ao kit de boas-vindas",
        "Destacar telemedicina como diferencial competitivo dos planos",
        "Garantir responsividade total (desktop, tablet, smartphone)",
        "Publicar codigo versionado e deploy em ambiente de producao",
    ]:
        pdf.bullet(b)

    # METODOLOGIA
    pdf.add_page()
    pdf.h1("3. Metodologia de Desenvolvimento")
    pdf.p(
        "O desenvolvimento seguiu uma abordagem iterativa e incremental, com ciclos curtos de "
        "implementacao, validacao visual e ajuste — sempre alinhados ao feedback do cliente em tempo real."
    )
    pdf.h2("3.1 Processo aplicado")
    steps = [
        ("Descoberta", "Levantamento de requisitos, referencias de mercado e alinhamento com site oficial"),
        ("Design", "Identidade visual, paleta, tipografia e composicao das secoes"),
        ("Desenvolvimento", "Implementacao em React com componentes reutilizaveis"),
        ("Conteudo", "Textos institucionais, videos, imagens e rede de parceiros"),
        ("Testes", "Validacao responsiva em multiplos dispositivos e breakpoints"),
        ("Refinamento", "Ajustes de UX, header, menu mobile, secoes e conversao"),
        ("Entrega", "Versionamento Git, documentacao e deploy em producao"),
    ]
    pdf.two_col_table(["Etapa", "Descricao"], steps)

    pdf.h2("3.2 Stack tecnologico")
    pdf.two_col_table(
        ["Camada", "Tecnologia"],
        [
            ("Frontend", "React 19 + Vite 8"),
            ("Roteamento", "React Router 7 (SPA)"),
            ("Estilizacao", "CSS customizado responsivo"),
            ("Build", "Vite (producao otimizada)"),
            ("Versionamento", "Git + GitHub"),
            ("Deploy", "Netlify (CDN global)"),
            ("Midia", "SVG, PNG, MP4 otimizados"),
        ],
    )

    # FASES
    pdf.add_page()
    pdf.h1("4. Linha do Tempo — Fases de Desenvolvimento")
    pdf.p(
        "O projeto foi executado em sete fases distintas, documentadas a seguir com entregas "
        "e marcos de cada etapa."
    )
    for phase in PHASES:
        pdf.phase_block(phase)

    # ENTREGAS
    pdf.add_page()
    pdf.h1("5. Entregas do Projeto")
    pdf.two_col_table(["Entrega", "Descricao"], DELIVERABLES)

    # ESTRUTURA DO SITE
    pdf.add_page()
    pdf.h1("6. Estrutura do Site Entregue")
    pdf.h2("6.1 Secoes da Home (landing page)")
    pdf.two_col_table(["Secao", "Conteudo"], SITE_SECTIONS)

    pdf.h2("6.2 Paginas da plataforma")
    pdf.two_col_table(["Rota", "Funcionalidade"], ROUTES)

    pdf.h2("6.3 Layout global")
    for b in [
        "Navbar fixo com logo, menu de navegacao e area do cliente",
        "Menu hamburger mobile em drawer fullscreen",
        "Botao flutuante WhatsApp em todas as paginas",
        "Botao voltar ao topo com gradiente da marca",
        "Banner de cookies LGPD (Aceitar / Recusar / Configurar)",
        "Rodape institucional com 4 colunas de links",
    ]:
        pdf.bullet(b)

    # IDENTIDADE VISUAL
    pdf.add_page()
    pdf.h1("7. Identidade Visual")
    pdf.two_col_table(
        ["Elemento", "Especificacao"],
        [
            ("Cor principal", "Bordo #8C1417 (confianca e tradicao)"),
            ("Cor de fundo", "Creme #F7F4EE (sofisticacao)"),
            ("Tipografia titulos", "Plus Jakarta Sans (800)"),
            ("Tipografia corpo", "DM Sans (400-700)"),
            ("Logo", "SVG vetorial (header + rodape)"),
            ("Header", "Branco com navegacao limpa"),
            ("Gradientes", "Verde/amarelo em CTAs e scroll"),
            ("Responsividade", "Breakpoints 1024 / 768 / 480 px"),
        ],
    )

    # FUNCIONALIDADES
    pdf.h1("8. Funcionalidades Principais")
    features = [
        ("Conversao", "Formulario de cupom, CTAs, planos com precos, WhatsApp integrado"),
        ("Telemedicina", "Secao dedicada, agendamento, videos explicativos"),
        ("Area do cliente", "Login no header, cartao digital, kit de boas-vindas"),
        ("B2B", "Portal do representante, funil de vendas, comissoes"),
        ("Atendimento", "FAQ expansivel, busca, fluxo IA + atendimento humano"),
        ("Dashboard", "KPIs operacionais, leads, contratos (demonstracao)"),
        ("Compliance", "Politica de cookies LGPD com preferencias do usuario"),
        ("Midia", "Carrossel, videos autoplay, imagens de parceiros"),
    ]
    pdf.two_col_table(["Modulo", "Descricao"], features)

    # VERSIONAMENTO
    pdf.add_page()
    pdf.h1("9. Versionamento e Publicacao")
    pdf.h2("9.1 Commits na linha do tempo")
    pdf.two_col_table(["Data", "Marco"], COMMITS)

    pdf.h2("9.2 Branches do repositorio")
    pdf.two_col_table(
        ["Branch", "Finalidade"],
        [
            ("main", "Linha principal de producao"),
            ("docs/historico-registros", "Historico de alteracoes documentado"),
        ],
    )

    pdf.h2("9.3 Acesso ao projeto")
    pdf.two_col_table(
        ["Ambiente", "URL / Comando"],
        [
            ("Producao", "https://mundialcard.netlify.app"),
            ("Repositorio", "https://github.com/JorgeRamalho/Mundialcard"),
            ("Desenvolvimento", "npm run dev -> localhost:5173"),
            ("Preview local", "npm start -> localhost:5500"),
            ("Rede local", "npm run dev:network -> IP:5173"),
        ],
    )

    # CONCLUSAO
    pdf.add_page()
    pdf.h1("10. Conclusao e Proximos Passos")
    pdf.h2("10.1 Conclusao")
    pdf.p(
        "A plataforma digital MundialCard foi desenvolvida com sucesso, cobrindo todo o ciclo "
        "desde a estrategia de venda digital ate a entrega em producao. O site apresenta identidade "
        "visual propria, experiencia responsiva validada, funil de conversao completo e areas "
        "funcionais para cliente, representante e operacao."
    )
    pdf.h2("10.2 Proximos passos sugeridos")
    for b in [
        "Integracao com gateway de pagamento para contratacao online",
        "Conexao com sistema interno de gestao de clientes (API)",
        "Ativacao de telemedicina com parceiro white-label",
        "Campanhas de marketing digital apontando para a landing page",
        "Monitoramento com analytics (GA4) e otimizacao de conversao",
        "Expansao do portal B2B com comissionamento automatizado",
    ]:
        pdf.bullet(b)

    pdf.h2("10.3 Contato operacional")
    pdf.two_col_table(
        ["Canal", "Informacao"],
        [
            ("Site oficial", "www.mundialcard.com.br"),
            ("WhatsApp", "(65) 99264-5537"),
            ("Telefone", "(65) 3365-1330"),
            ("Endereco", "R. Barao de Melgaco, 2468 — Centro, Cuiaba-MT"),
        ],
    )

    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(140, 20, 23)
    pdf.cell(0, 8, "MundialCard — Beneficios que cabem na vida real.", align="C")

    DOCS.mkdir(parents=True, exist_ok=True)
    pdf.output(str(PDF_OUT))
    print(f"PDF: {PDF_OUT}")


# ---------------------------------------------------------------------------
# POWERPOINT
# ---------------------------------------------------------------------------

def _add_title_slide(prs, title, subtitle=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(1, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BRAND
    bg.line.fill.background()

    accent = slide.shapes.add_shape(1, 0, Inches(3.6), prs.slide_width, Inches(0.06))
    accent.fill.solid()
    accent.fill.fore_color.rgb = GOLD
    accent.line.fill.background()

    box = slide.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(8.5), Inches(1.2))
    tf = box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE

    if subtitle:
        box2 = slide.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(8.5), Inches(1.5))
        tf2 = box2.text_frame
        p2 = tf2.paragraphs[0]
        p2.text = subtitle
        p2.font.size = Pt(18)
        p2.font.color.rgb = CREAM


def _add_content_slide(prs, title, bullets, subtitle=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    header = slide.shapes.add_shape(1, 0, 0, prs.slide_width, Inches(1.1))
    header.fill.solid()
    header.fill.fore_color.rgb = BRAND
    header.line.fill.background()

    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.25), Inches(9), Inches(0.7))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = WHITE

    y = 1.4
    if subtitle:
        sb = slide.shapes.add_textbox(Inches(0.6), Inches(1.3), Inches(9), Inches(0.5))
        sp = sb.text_frame.paragraphs[0]
        sp.text = subtitle
        sp.font.size = Pt(14)
        sp.font.color.rgb = BRAND
        sp.font.italic = True
        y = 1.8

    body = slide.shapes.add_textbox(Inches(0.7), Inches(y), Inches(8.8), Inches(5))
    tf = body.text_frame
    tf.word_wrap = True
    for i, bullet in enumerate(bullets):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = bullet
        para.font.size = Pt(16)
        para.font.color.rgb = SLATE
        para.space_after = Pt(10)
        para.level = 0


def _add_two_col_slide(prs, title, left_title, left_items, right_title, right_items):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    header = slide.shapes.add_shape(1, 0, 0, prs.slide_width, Inches(1.1))
    header.fill.solid()
    header.fill.fore_color.rgb = BRAND
    header.line.fill.background()

    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.25), Inches(9), Inches(0.7))
    p = tb.text_frame.paragraphs[0]
    p.text = title
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = WHITE

    for col, (ctitle, citems), x in [
        (0, (left_title, left_items), 0.5),
        (1, (right_title, right_items), 5.2),
    ]:
        ct = slide.shapes.add_textbox(Inches(x), Inches(1.3), Inches(4.2), Inches(0.4))
        cp = ct.text_frame.paragraphs[0]
        cp.text = ctitle
        cp.font.size = Pt(14)
        cp.font.bold = True
        cp.font.color.rgb = BRAND

        cb = slide.shapes.add_textbox(Inches(x), Inches(1.7), Inches(4.2), Inches(4.5))
        ctf = cb.text_frame
        ctf.word_wrap = True
        for i, item in enumerate(citems):
            para = ctf.paragraphs[0] if i == 0 else ctf.add_paragraph()
            para.text = f"• {item}"
            para.font.size = Pt(13)
            para.font.color.rgb = SLATE
            para.space_after = Pt(6)


def _add_timeline_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    header = slide.shapes.add_shape(1, 0, 0, prs.slide_width, Inches(1.1))
    header.fill.solid()
    header.fill.fore_color.rgb = BRAND
    header.line.fill.background()

    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.25), Inches(9), Inches(0.7))
    p = tb.text_frame.paragraphs[0]
    p.text = "Linha do Tempo do Projeto"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = WHITE

    y_start = 1.35
    for i, phase in enumerate(PHASES):
        y = y_start + i * 0.72
        num_box = slide.shapes.add_shape(1, Inches(0.5), Inches(y), Inches(0.55), Inches(0.55))
        num_box.fill.solid()
        num_box.fill.fore_color.rgb = BRAND if i % 2 == 0 else GOLD
        num_box.line.fill.background()
        nt = num_box.text_frame.paragraphs[0]
        nt.text = phase["num"]
        nt.font.size = Pt(11)
        nt.font.bold = True
        nt.font.color.rgb = WHITE
        nt.alignment = PP_ALIGN.CENTER

        tt = slide.shapes.add_textbox(Inches(1.2), Inches(y - 0.02), Inches(8), Inches(0.6))
        tp = tt.text_frame.paragraphs[0]
        tp.text = f"{phase['title']}  ({phase['period']})"
        tp.font.size = Pt(13)
        tp.font.bold = True
        tp.font.color.rgb = SLATE


def build_pptx():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # 1 Capa
    _add_title_slide(
        prs,
        "MundialCard",
        "Plataforma Digital\nApresentacao do Projeto ao Cliente\n03 a 06 de julho de 2026",
    )

    # 2 Agenda
    _add_content_slide(
        prs,
        "Agenda",
        [
            "Visao e objetivos do projeto",
            "Metodologia de desenvolvimento",
            "Linha do tempo (7 fases)",
            "Entregas realizadas",
            "Estrutura do site",
            "Funcionalidades principais",
            "Identidade visual",
            "Stack tecnico e publicacao",
            "Conclusao e proximos passos",
        ],
    )

    # 3 Visao
    _add_content_slide(
        prs,
        "Visao do Projeto",
        [
            "Cartao de desconto e multibeneficios em saude e bem-estar",
            "Venda digital escalavel para todo o Brasil (B2C + B2B)",
            "Telemedicina como diferencial dos planos",
            "Jornada completa: da contratacao ao kit de boas-vindas",
            "Plataforma de atendimento, suporte e gestao de clientes",
            "Alinhamento com a marca oficial mundialcard.com.br",
        ],
        subtitle="MundialCard — Seu cartao de super beneficios",
    )

    # 4 Objetivos
    _add_two_col_slide(
        prs,
        "Objetivos do Projeto",
        "Negocio",
        [
            "Transmitir confianca no setor de beneficios",
            "Captar leads com cupom de lancamento",
            "Vender planos Bronze a Platinum online",
            "Escalar vendas via representantes B2B",
            "Demonstrar solidez operacional ao cliente",
        ],
        "Experiencia",
        [
            "Site moderno com identidade visual propria",
            "Layout responsivo (desktop, tablet, mobile)",
            "Videos e conteudo explicativo integrados",
            "Area do cliente e central de atendimento",
            "Conformidade LGPD (cookies)",
        ],
    )

    # 5 Metodologia
    _add_content_slide(
        prs,
        "Metodologia",
        [
            "1. Descoberta — requisitos, referencias e alinhamento estrategico",
            "2. Design — identidade visual, paleta, tipografia e layout",
            "3. Desenvolvimento — React + Vite, componentes modulares",
            "4. Conteudo — textos, videos, parceiros e planos",
            "5. Testes — validacao responsiva em dispositivos reais",
            "6. Refinamento — UX, menu mobile, secoes e conversao",
            "7. Entrega — Git, documentacao e deploy em producao",
        ],
        subtitle="Abordagem iterativa com ciclos curtos de feedback",
    )

    # 6 Timeline
    _add_timeline_slide(prs)

    # 7-9 Fases detalhadas (agrupadas)
    for group in [
        ("Fases 1-2: Estrategia e Design", PHASES[0], PHASES[1]),
        ("Fases 3-4: Plataforma e Conteudo", PHASES[2], PHASES[3]),
        ("Fases 5-7: Mobile, Avancado e Entrega", PHASES[4], PHASES[5]),
    ]:
        title, p1, p2 = group
        items = [f"[{p1['num']}] {p1['title']}"] + [f"  • {i}" for i in p1["items"][:3]]
        items += [f"[{p2['num']}] {p2['title']}"] + [f"  • {i}" for i in p2["items"][:3]]
        _add_content_slide(prs, title, items)

    # 10 Entregas
    _add_content_slide(
        prs,
        "Entregas do Projeto",
        [f"• {d[0]} — {d[1]}" for d in DELIVERABLES],
    )

    # 11 Estrutura
    _add_two_col_slide(
        prs,
        "Estrutura do Site",
        "Home (11 secoes)",
        [s[0] for s in SITE_SECTIONS[:6]],
        "Paginas internas",
        [f"{r[0]} {r[1]}" for r in ROUTES[1:7]],
    )

    # 12 Funcionalidades
    _add_content_slide(
        prs,
        "Funcionalidades-Chave",
        [
            "Formulario de cupom com persistencia local",
            "6 planos com precos e CTAs de adesao",
            "Telemedicina em destaque + agendamento",
            "Area do cliente com login no header",
            "Portal B2B para representantes comerciais",
            "FAQ + videos + fluxo de atendimento IA/humano",
            "Politica de cookies LGPD",
            "WhatsApp integrado em todo o funil",
        ],
    )

    # 13 Identidade
    _add_two_col_slide(
        prs,
        "Identidade Visual",
        "Elementos",
        [
            "Cor bordo #8C1417",
            "Fundo creme #F7F4EE",
            "Plus Jakarta Sans + DM Sans",
            "Logo SVG vetorial",
            "Header branco limpo",
        ],
        "Experiencia",
        [
            "Gradientes em CTAs",
            "Carrossel hero impactante",
            "Videos autoplay responsivos",
            "Menu mobile drawer fullscreen",
            "Botao voltar ao topo estilizado",
        ],
    )

    # 14 Stack
    _add_content_slide(
        prs,
        "Stack Tecnico",
        [
            "React 19 — biblioteca UI moderna",
            "Vite 8 — build rapido e otimizado",
            "React Router 7 — navegacao SPA",
            "CSS responsivo — breakpoints 1024/768/480px",
            "Git + GitHub — versionamento profissional",
            "Netlify — deploy CDN global",
        ],
        subtitle="Arquitetura leve, performatica e escalavel",
    )

    # 15 Publicacao
    _add_two_col_slide(
        prs,
        "Publicacao e Acesso",
        "Ambientes",
        [
            "Producao: mundialcard.netlify.app",
            "GitHub: JorgeRamalho/Mundialcard",
            "Dev: npm run dev (porta 5173)",
            "Preview: npm start (porta 5500)",
        ],
        "Marcos Git",
        [f"{c[0]} — {c[1]}" for c in COMMITS],
    )

    # 16 Conclusao
    _add_content_slide(
        prs,
        "Conclusao",
        [
            "Plataforma digital completa entregue em producao",
            "Identidade visual propria e experiencia responsiva",
            "Funil de conversao com cupom, planos e telemedicina",
            "Areas funcionais: cliente, B2B, dashboard, atendimento",
            "Codigo versionado e documentado no GitHub",
            "Pronto para integracao com pagamento e sistema interno",
        ],
    )

    # 17 Obrigado
    _add_title_slide(
        prs,
        "Obrigado!",
        "MundialCard — Beneficios que cabem na vida real.\n\nwww.mundialcard.com.br\nWhatsApp: (65) 99264-5537",
    )

    prs.save(str(PPTX_OUT))
    print(f"PPTX: {PPTX_OUT}")


if __name__ == "__main__":
    build_pdf()
    build_pptx()
    print("Apresentacao ao cliente gerada com sucesso.")
