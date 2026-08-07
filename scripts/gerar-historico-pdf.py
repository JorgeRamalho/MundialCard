# -*- coding: utf-8 -*-
"""Gera PDF com historico completo das conversas do projeto MundialCard."""

from pathlib import Path
from fpdf import FPDF

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "docs" / "historico" / "HISTORICO-CHAT-COMPLETO.pdf"
FONT = Path("C:/Windows/Fonts/arial.ttf")
FONT_BOLD = Path("C:/Windows/Fonts/arialbd.ttf")


class HistoricoPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("Arial", "", str(FONT))
        self.add_font("Arial", "B", str(FONT_BOLD))
        self.set_auto_page_break(auto=True, margin=18)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_x(self.l_margin)
        self.set_font("Arial", "B", 9)
        self.set_text_color(100, 20, 23)
        self.cell(0, 8, "MundialCard - Historico Completo de Conversas", align="L")
        self.set_font("Arial", "", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, f"Pagina {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(140, 20, 23)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
        self.set_x(self.l_margin)

    def footer(self):
        self.set_y(-12)
        self.set_font("Arial", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "Projeto MundialCard | Documento gerado em 06/07/2026", align="C")

    def cover(self):
        self.add_page()
        self.set_fill_color(140, 20, 23)
        self.rect(0, 0, 210, 70, "F")
        self.ln(18)
        self.set_font("Arial", "B", 26)
        self.set_text_color(255, 255, 255)
        self.cell(0, 14, "MundialCard", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Arial", "", 14)
        self.cell(0, 10, "Historico Completo de Conversas com a IA", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(30)
        self.set_text_color(30, 30, 30)
        self.set_font("Arial", "B", 12)
        self.cell(0, 8, "Projeto: Plataforma Digital MundialCard", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_font("Arial", "", 11)
        meta = [
            "Periodo: 03/07/2026 a 06/07/2026",
            "Repositorio: https://github.com/JorgeRamalho/Mundialcard",
            "Producao: https://mundialcard.netlify.app",
            "Stack: Vite + React + React Router",
            "Documento: registro integral dos prompts, alteracoes e entregas",
        ]
        for line in meta:
            self.cell(0, 7, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(8)
        self.set_font("Arial", "B", 11)
        self.cell(0, 8, "Sessoes de chat registradas: 5", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Arial", "", 10)
        sessions = [
            "1. Criacao do site e identidade visual (03-04/07/2026)",
            "2. Menu hamburger, carrossel e Live Server (04/07/2026)",
            "3. Live Server definitivo e parceiros (04/07/2026 noite)",
            "4. Layout, cookies e area do cliente (05-06/07/2026)",
            "5. Solicitacao deste historico (06/07/2026)",
        ]
        for s in sessions:
            self.cell(0, 6, f"  - {s}", new_x="LMARGIN", new_y="NEXT")

    def section_title(self, title, level=1):
        self.ln(4 if level == 1 else 2)
        size = 16 if level == 1 else 13
        self.set_font("Arial", "B", size)
        self.set_text_color(140, 20, 23 if level == 1 else 60)
        self.multi_cell(0, 8, title)
        self.set_text_color(30, 30, 30)
        self.ln(2)

    def subsection(self, title):
        self.ln(2)
        self.set_font("Arial", "B", 11)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 7, title)
        self.set_text_color(30, 30, 30)
        self.ln(1)

    def paragraph(self, text):
        if self.get_y() > 265:
            self.add_page()
        self.set_font("Arial", "", 10)
        self.set_x(self.l_margin)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def bullet(self, text):
        if self.get_y() > 265:
            self.add_page()
        self.set_font("Arial", "", 10)
        self.set_x(self.l_margin)
        self.multi_cell(0, 5.5, f"  - {text}")

    def table_row(self, cols, bold=False, fill=False):
        if self.get_y() > 270:
            self.add_page()
        widths = [38, 22, 130]
        self.set_x(self.l_margin)
        self.set_font("Arial", "B" if bold else "", 9)
        if fill:
            self.set_fill_color(247, 244, 238)
        for i, col in enumerate(cols):
            self.cell(widths[i], 7, col, border=1, fill=fill)
        self.ln()


def build_pdf():
    pdf = HistoricoPDF()
    pdf.cover()

    # INDICE
    pdf.add_page()
    pdf.set_margins(10, 10, 10)
    pdf.section_title("Indice")
    index = [
        "1. Visao geral do projeto",
        "2. Chat 1 - Criacao do site (03-04/07/2026)",
        "3. Chat 2 - Navbar, carrossel e Live Server (04/07/2026)",
        "4. Chat 3 - Live Server e parceiros (04/07/2026 noite)",
        "5. Chat 4 - Layout, cookies e area do cliente (05-06/07/2026)",
        "6. Linha do tempo Git (commits)",
        "7. Estrutura atual do site",
        "8. Estado final por tema",
        "9. Como acessar o projeto",
    ]
    for item in index:
        pdf.bullet(item)

    # 1. VISAO GERAL
    pdf.add_page()
    pdf.section_title("1. Visao Geral do Projeto")
    pdf.paragraph(
        "O projeto MundialCard nasceu em 03/07/2026 com um playbook de venda digital escalavel "
        "e evoluiu para uma plataforma web completa em React. A marca inicial VivaPay foi "
        "renomeada para MundialCard, alinhada ao site oficial mundialcard.com.br."
    )
    pdf.paragraph(
        "O desenvolvimento ocorreu em multiplas sessoes de chat com a IA no Cursor, cobrindo "
        "identidade visual, conteudo institucional, responsividade mobile, menu hamburger, "
        "carrossel, integracao de videos, secao de parceiros, politica de cookies (LGPD), "
        "area do cliente e publicacao no GitHub/Netlify."
    )
    pdf.subsection("Entregas principais")
    for item in [
        "Site institucional com 9+ paginas e landing page completa",
        "Identidade visual bordô (#8C1417), header branco, tipografia Plus Jakarta Sans",
        "Carrossel, telemedicina em destaque, planos Bronze a Platinum",
        "Formulario de cupom de lancamento com localStorage",
        "Dashboard, area do cliente, area do representante B2B",
        "Documentacao: venda-digital-escalavel.md e HISTORICO-REGISTROS.md",
        "Repositorio GitHub publicado com branches e historico profissional",
    ]:
        pdf.bullet(item)

    # CHAT 1
    pdf.add_page()
    pdf.section_title("2. Chat 1 - Criacao do Site (03-04/07/2026)")

    chat1 = [
        ("03/07 18:50", "Venda digital escalavel", "Playbook operacional: jornada lead->kit, ferramentas, KPIs, B2B, telemedicina, plano funerario Brasil."),
        ("03/07 19:19", "Desenvolvimento do site (1o prompt)", "Scaffold Vite+React. Logo, slogan, formulario cupom, hero, telemedicina, planos, dashboard, B2B. Nome inicial: VivaPay."),
        ("03/07 19:21", "Videos enviados", "Integracao de mundialcard-app.mp4 e mundialcard-institucional.mp4."),
        ("03/07 20:20", "Responsivo 375x667 + cor #8C1417E6", "Ajustes de dimensao e background."),
        ("03/07 20:22", "Cabecalho branco", "Header alterado para branco."),
        ("03/07 20:22", "VivaPay -> MundialCard", "Renomeacao completa da marca."),
        ("03/07 20:36", "Slogan azul claro", "Legenda do header alterada de verde para azul claro."),
        ("03/07 20:42", "Cor da legenda fora do padrao", "Corrigido conforme imagem enviada."),
        ("03/07 20:44", "Mesma funcao no rodape", "Rodape alinhado ao header."),
        ("03/07 20:47", "Videos com autoplay", "Componente AutoPlayVideo criado."),
        ("03/07 20:49", "Icones header: vermelho/cinza hover", "Inversao de cores no hover."),
        ("03/07 20:51", "Carrossel acima do hero", "HeroCarousel com ~7 fotos de saude/telemedicina."),
        ("03/07 20:53", "Destaque telemedicina", "Secao reforcada para atrair clientes."),
        ("03/07 22:17", "Estrutura do site", "Mapa das secoes apresentado."),
        ("03/07 22:19", "Telemedicina para posicao 2", "Reordenacao das secoes."),
        ("03/07 22:22", "Video celular maior/tela cheia", "Player ampliado sem cortes."),
        ("03/07 22:28", "Varredura de videos responsivos", "Todos os videos ajustados."),
        ("03/07 22:34", "Duas fotos no carrossel", "Banners adicionados."),
        ("03/07 22:39", "Conteudo site oficial", "Textos e parceiros de mundialcard.com.br."),
        ("03/07 23:35", "Ajustar medidas carrossel", "Tentativa de otimizacao."),
        ("03/07 23:43", "Reverter carrossel", "Estado original restaurado."),
        ("03/07 23:47", "Remover imagem carrossel", "Imagem removida."),
        ("03/07 23:58", "Adicionar foto Mundial Card", "Banner colaboradores adicionado."),
        ("04/07 03:45", "Commit inicial GitHub", "main + docs/historico-registros. Push para JorgeRamalho/Mundialcard."),
        ("04/07 04:07", "Verificar mobile", "Grande refatoracao CSS + Navbar."),
        ("04/07 04:15", "Desfazer funcao", "Revertido via git."),
        ("04/07 04:18", "Layout mobile quebrado", "Botao Cupom removido do header mobile."),
        ("04/07 04:26", "Problema persistia Netlify", "Fix reforcado + push main."),
        ("04/07 04:31", "Aprovacao mobile", "Usuario confirmou: Agora sim deu certo!"),
        ("04/07 04:33", "Hamburger sobreposto", "z-index elevado."),
        ("04/07 04:36", "Commit modo responsivo", "Commits 0ab6281, 26c8d70, bfb624c."),
    ]
    pdf.table_row(["Data/Hora", "Pedido", "Resultado"], bold=True, fill=True)
    for row in chat1:
        pdf.set_font("Arial", "", 8)
        x, y = pdf.get_x(), pdf.get_y()
        pdf.multi_cell(38, 5, row[0], border=1)
        pdf.set_xy(x + 38, y)
        pdf.multi_cell(22, 5, row[1], border=1)
        pdf.set_xy(x + 60, y)
        pdf.multi_cell(130, 5, row[2], border=1)
        pdf.set_xy(10, y + max(5 * (len(row[2]) // 45 + 1), 7))

    # CHAT 2
    pdf.add_page()
    pdf.section_title("3. Chat 2 - Navbar, Carrossel e Live Server (04/07/2026)")
    chat2 = [
        ("12:41", "Menu hamburger em destaque", "z-index, overlay, createPortal React."),
        ("12:51", "Menu a frente do carrossel", "Ajustes de empilhamento CSS."),
        ("12:55", "Correcao definitiva hamburger", "Drawer fullscreen z-index 2147483646."),
        ("12:59", "Link Live Server", "localhost:5173 e IP rede 192.168.15.7:5173."),
        ("13:01", "Commit menu nav bar", "Commit de06668 + push."),
        ("13:12", "Carrossel desktop alinhado", "Tentativa de alinhamento."),
        ("13:15", "Desfazer", "Revertido."),
        ("13:18", "Aumentar imagens carrossel desktop", "Altura aumentada."),
        ("13:21", "Desfazer toda funcao", "Revertido."),
        ("13:23", "Aumentar desktop responsivo", "Novo ajuste de altura."),
        ("13:27", "Arrumar carrossel + altura", "clamp() e CSS ajustado."),
        ("13:33", "Enquadramento igual ao mobile", "Altura unificada."),
        ("13:36", "Commit ajuste carrossel", "Commit 69d3fb6 + push."),
        ("14:23", "Resolver Live Server", "Scripts live, setup-live-server.mjs."),
        ("14:25", "Acessar index.html Live Server", "Varias tentativas."),
        ("14:31", "Live Server ainda nao funciona", "Mais correcoes."),
        ("14:48", "Desfazer TUDO Live Server", "Revertido. Voltou ao npm run dev."),
    ]
    pdf.table_row(["Hora", "Pedido", "Resultado"], bold=True, fill=True)
    for row in chat2:
        pdf.set_font("Arial", "", 8)
        x, y = pdf.get_x(), pdf.get_y()
        pdf.multi_cell(20, 5, row[0], border=1)
        pdf.set_xy(x + 20, y)
        pdf.multi_cell(55, 5, row[1], border=1)
        pdf.set_xy(x + 75, y)
        pdf.multi_cell(115, 5, row[2], border=1)
        pdf.set_xy(10, y + 7)

    # CHAT 3
    pdf.add_page()
    pdf.section_title("4. Chat 3 - Live Server e Parceiros (04/07/2026 noite)")
    chat3 = [
        ("19:41", "Por que Live Server nao abre site?", "Explicado: React/JSX precisa do Vite."),
        ("19:45", "Abrir site completo Live Server", "Config .vscode, build dist/."),
        ("19:53", "Nao funcionou", "Caminhos relativos, HashRouter, assetUrl()."),
        ("20:00", "Solucao definitiva", "npm start, build:live, preview.html, verify-live.cjs."),
        ("20:27", "Imagem cartao em parceiros", "partners-showcase criado."),
        ("20:31", "Desfazer imagem parceiros", "Imagem e CSS removidos."),
    ]
    for row in chat3:
        pdf.bullet(f"{row[0]} | {row[1]} -> {row[2]}")

    pdf.subsection("Solucao Live Server aplicada")
    for item in [
        "base: './' no vite.config.js",
        "HashRouter para rotas no Live Server",
        "Helper assetUrl() para imagens e videos",
        "npm start e npm run build:live",
        "preview.html com redirecionamento para dist/",
        "scripts/verify-live.cjs para validacao",
        ".vscode/settings.json, tasks.json, extensions.json",
        "Redirect removido do build de producao",
        "BOM invalido removido do package.json",
    ]:
        pdf.bullet(item)

    # CHAT 4
    pdf.add_page()
    pdf.section_title("5. Chat 4 - Layout, Cookies e Area do Cliente (05-06/07/2026)")
    chat4 = [
        ("05/07 15:48", "Historico de conversas", "Primeira compilacao do historico."),
        ("05/07 15:59", "Problema de acesso ao site", "npm start, netlify.toml, mensagem ajuda index.html."),
        ("05/07 16:12-16:15", "Logo pequena no header", "Ajustes: 32px->64px, --logo-h, max-width removido."),
        ("05/07 16:19", "Botoes fora do header desktop", "nav-utility criada."),
        ("05/07 16:21", "Desfazer", "Revertido."),
        ("05/07 16:27", "Desfazer todas funcoes header", "git checkout do ultimo commit."),
        ("05/07 16:32", "Logo 42px + remover botoes desktop", "Logo alinhada; botoes so no mobile."),
        ("05/07 16:35", "Kit boas-vindas acima parceiros", "Movido e depois desfeito."),
        ("05/07 16:38", "Estrutura completa do site", "Mapa detalhado de secoes e rotas."),
        ("05/07 16:41", "Jornada acima Parceiros", "Confirmado e mantido."),
        ("05/07 16:46", "Link outro dispositivo", "192.168.15.10:5173 dev:network."),
        ("05/07 16:49", "Link acompanhar mudancas", "Hot reload via dev:network."),
        ("05/07 19:26", "Suporte acima FAQ", "Secao reordenada."),
        ("05/07 20:04", "Titulo Hero branco", "Gradiente removido do span."),
        ("05/07 20:06", "Imagem cartao parceiros", "Adicionada e desfeita."),
        ("05/07 20:13", "Layout grade 2x4 parceiros", "8o card com cartao Mundial Card."),
        ("05/07 20:17", "Link Hospital Militar", "Instagram hospitalmilitaroficial."),
        ("05/07 20:57", "Remover links parceiros", "Cards sem links externos."),
        ("05/07 21:00", "Header scroll + voltar topo", "Implementado e depois parcialmente revertido."),
        ("05/07 21:05", "Botao voltar ao topo", "BackToTop criado."),
        ("05/07 21:07", "Header destaque no scroll", "z-index + sombra."),
        ("05/07 21:09", "Gradiente verde/amarelo botao topo", "CSS gradiente aplicado."),
        ("05/07 22:16", "Remover efeitos scroll header", "Efeitos removidos."),
        ("05/07 22:17", "Gradiente verde/amarelo no scroll", "Header com gradiente ao rolar."),
        ("05/07 22:18", "Header acompanha scroll", "position sticky mantido."),
        ("05/07 22:48", "Texto cookies LGPD", "Aceitar, Recusar, Configurar."),
        ("05/07 22:50", "Aplicar politica cookies", "CookieConsent.jsx implementado."),
        ("05/07 23:06", "Area cliente no header", "Login usuario/senha no navbar."),
        ("05/07 23:09", "Login mais adaptavel", "Estilizacao refinada."),
        ("05/07 23:13", "Emoji usuario + remover do hamburger", "ClientLoginButton estilizado."),
        ("05/07 23:33", "B2C -> B2B representantes", "Texto alterado."),
        ("05/07 23:37", "Associado Demo -> Cliente Mundial Card", "Nome alterado."),
        ("06/07 00:19", "Commit area do cliente", "Commit 62c427e + push main."),
    ]
    for row in chat4:
        pdf.bullet(f"{row[0]} | {row[1]}")

    # GIT
    pdf.add_page()
    pdf.section_title("6. Linha do Tempo Git (Commits)")
    commits = [
        ("42a3ef7", "04/07/2026", "Initial commit: plataforma digital MundialCard"),
        ("0afad7a", "04/07/2026", "docs: registrar historico de alteracoes"),
        ("235e231", "04/07/2026", "Merge pull request #1 docs/historico-registros"),
        ("0ab6281", "04/07/2026", "fix: corrigir layout mobile em smartphones"),
        ("26c8d70", "04/07/2026", "fix: menu hamburger sobreposto no mobile"),
        ("bfb624c", "04/07/2026", "docs: registrar modo responsivo"),
        ("de06668", "04/07/2026", "fix: menu navbar mobile drawer fullscreen"),
        ("69d3fb6", "04/07/2026", "fix: ajuste tamanho carrossel desktop/responsivo"),
        ("62c427e", "06/07/2026", "feat: atualizacao area do cliente"),
    ]
    pdf.table_row(["Hash", "Data", "Mensagem"], bold=True, fill=True)
    for c in commits:
        pdf.table_row(list(c))

    # ESTRUTURA
    pdf.add_page()
    pdf.section_title("7. Estrutura Atual do Site")
    pdf.subsection("Rotas")
    routes = [
        ("/", "Home - landing page institucional"),
        ("/cadastro", "Formulario cupom de inauguracao"),
        ("/dashboard", "Painel operacional KPIs"),
        ("/area-cliente", "Cartao digital, kit boas-vindas"),
        ("/parceiros", "Area do representante B2B"),
        ("/atendimento", "Central FAQ + IA simulada"),
        ("/agendamento", "Agendamento telemedicina"),
        ("/produtos", "Beneficios e planos"),
        ("/app", "Download do aplicativo"),
    ]
    pdf.table_row(["Rota", "Descricao"], bold=True, fill=True)
    for r in routes:
        pdf.table_row(list(r))

    pdf.subsection("Ordem das secoes na Home")
    sections = [
        "1. Carrossel (HeroCarousel)",
        "2. Telemedicina (#telemedicina)",
        "3. Hero (#hero)",
        "4. Beneficios (#beneficios)",
        "5. Kit de boas-vindas (#jornada)",
        "6. Nossos parceiros (#parceiros-rede)",
        "7. Planos (#planos) - Bronze a Platinum",
        "8. Suporte (#suporte)",
        "9. FAQ (#faq)",
        "10. B2B (#b2b)",
        "11. Lancamento (#lancamento)",
    ]
    for s in sections:
        pdf.bullet(s)

    pdf.subsection("Header desktop (estado atual)")
    for item in [
        "Logo 42px alinhada aos icones",
        "Sem botoes WhatsApp, Agendar e Cupom (permanecem no mobile/hamburger)",
        "Login area do cliente com emoji de usuario",
        "Sticky com gradiente verde/amarelo no scroll",
        "Botao voltar ao topo com gradiente",
    ]:
        pdf.bullet(item)

    # RESUMO
    pdf.add_page()
    pdf.section_title("8. Estado Final por Tema")
    themes = [
        ("Site React MundialCard", "Criado e evoluido"),
        ("Identidade visual", "Bordo #8C1417, header branco, Plus Jakarta Sans"),
        ("Carrossel", "Banners familia + colaboradores; altura ajustada"),
        ("Telemedicina", "Destaque na home posicao 2"),
        ("Mobile", "Corrigido e aprovado pelo usuario"),
        ("Menu hamburger", "Drawer fullscreen com portal React"),
        ("Live Server", "Solucao via npm start / Vite Preview"),
        ("GitHub", "Publicado com docs/historico/HISTORICO-REGISTROS.md"),
        ("Parceiros", "Grade 2x4 com cartao Mundial Card; links removidos"),
        ("Cookies LGPD", "CookieConsent implementado"),
        ("Area do cliente", "Login no header; commit 62c427e"),
    ]
    pdf.table_row(["Tema", "Status"], bold=True, fill=True)
    for t in themes:
        pdf.table_row(list(t))

    pdf.section_title("9. Como Acessar o Projeto")
    access = [
        ("Desenvolvimento", "npm run dev", "http://localhost:5173"),
        ("Rede local", "npm run dev:network", "http://[IP-LOCAL]:5173"),
        ("Build + preview", "npm start", "http://127.0.0.1:5500"),
        ("Producao", "Netlify deploy", "https://mundialcard.netlify.app"),
    ]
    pdf.table_row(["Metodo", "Comando", "URL"], bold=True, fill=True)
    for a in access:
        pdf.table_row(list(a))

    pdf.ln(6)
    pdf.subsection("Arquivos principais do repositorio")
    files = [
        "index.html, public/style.css",
        "public/media/ - videos de propaganda",
        "public/images/ - carrossel e parceiros",
        "src/App.jsx, src/components/, src/pages/",
        "src/data/content.js - textos, planos, FAQ, parceiros",
        "docs/historico/HISTORICO-REGISTROS.md",
        "docs/venda-digital-escalavel.md",
        "docs/historico/HISTORICO-CHAT-COMPLETO.pdf (este documento)",
    ]
    for f in files:
        pdf.bullet(f)

    pdf.ln(8)
    pdf.set_font("Arial", "I", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(
        0,
        5,
        "Documento gerado automaticamente a partir dos transcripts de conversa "
        "armazenados no Cursor IDE para o projeto MundialCard. "
        "Contem registro integral dos prompts do usuario, respostas da IA, "
        "alteracoes realizadas e estado do repositorio ate 06/07/2026.",
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUTPUT))
    print(f"PDF gerado: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
