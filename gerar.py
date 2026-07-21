# -*- coding: utf-8 -*-
"""Gera as paginas HTML do raio-x do nicho Tight-Space Tools a partir do dados-brutos.json."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
DB = json.load(open(os.path.join(BASE, "dados-brutos.json"), encoding="utf-8"))

# ---------- paginas / nav ----------
PAGES = [
    ("index.html", "Painel"),
    ("mercados.html", "Mercados"),
    ("oportunidade.html", "★ A Oportunidade"),
    ("estrategia.html", "Estratégia & Gaps"),
    ("plano-de-acao.html", "Plano de ação"),
    ("loja-wildbear.html", "WildBear"),
    ("loja-bolthero.html", "Bolthero"),
    ("loja-savary.html", "Savary"),
    ("loja-confinedim.html", "Confinedim"),
    ("loja-felmix.html", "Felmix"),
    ("loja-bolthunter.html", "Bolt Hunter"),
]

def nav(cur):
    links = ['<a class="home" href="index.html">RAIO-X · Tight-Space Tools</a>']
    for href, label in PAGES:
        if href == "index.html":
            continue
        on = " on" if href == cur else ""
        links.append(f'<a class="{on.strip()}" href="{href}">{label}</a>')
    return f'<div class="nav"><div class="wrap">{"".join(links)}</div></div>'

def head(title):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><link rel="stylesheet" href="estilo.css"></head><body>"""

def foot():
    return ('<footer><div class="wrap">Raio-x competitivo · Nicho Ferramentas Tight-Space (Offset Extension Wrench) · '
            'Mercado US + Big Five anglo · Dados coletados em 20/07/2026 · Meta Ad Library, SimilarWeb, RDAP, products.json. '
            'Medido = visitas e ticket de catálogo. Estimado = conversão, AOV, faturamento e investimento.</div></footer></body></html>')

def page(fname, title, body):
    html = head(title) + nav(fname) + '<div class="wrap">' + body + '</div>' + foot()
    open(os.path.join(BASE, fname), "w", encoding="utf-8").write(html)
    print("gerado", fname)

def shot(slug, tipo, label):
    """Bloco de print rolável, ou aviso se o arquivo nao existe."""
    fn = f"prints/{slug}-{tipo}.jpg"
    full = os.path.join(BASE, fn)
    if os.path.exists(full):
        return (f'<div class="shot"><div class="cap"><b>{label}</b></div>'
                f'<div class="frame"><img src="{fn}" alt="{label}"></div></div>')
    return ''

# =========================================================================
# INDEX
# =========================================================================
def momentum_html():
    m = DB["momentum_nicho"]; ciclo = m["ciclo_vida"]
    cores = {"EMERGENTE":"p-i","ESCALANDO":"p-a","SATURADO":"p-b","DECLINIO":"p-c","DECLÍNIO":"p-c"}
    pill = f'<span class="pill {cores.get(ciclo,"p-n")}" style="font-size:14px;padding:6px 14px">{ciclo}</span>'
    return f"""
<section>
<h2><span class="n">00</span>Momentum do nicho &nbsp;{pill}</h2>
<p class="lead">O filtro de timing: cruza a demanda (Google Trends) com a saturação de mídia (anúncios ativos e idade dos domínios) pra dizer em que fase o nicho está. <b>ESCALANDO</b> = validado, demanda subindo e ainda com espaço geográfico.</p>
<div class="grid g2">
<div class="card"><h3>Demanda · Google Trends (12 meses)</h3><ul class="cl">
<li>"socket extension": <b>crescente</b> (56 → 64)</li>
<li>"wrench extension": <b>crescente</b> (45 → 56)</li>
<li>"stripped bolt extractor": estável (70 → 72)</li>
<li>UK com interesse relativo <b>60</b>, o maior entre mercados grandes</li>
</ul></div>
<div class="card"><h3>Saturação de mídia</h3><p style="color:var(--dim);font-size:14px">{m["saturacao_midia"]}</p></div>
</div>
<div class="good note"><b>Leitura:</b> {m["leitura"]}</div>
<div class="note" style="font-size:13px">{m["lacuna"]}</div>
</section>
"""

def build_index():
    b = """
<header>
<span class="tag">Inteligência competitiva</span>
<h1>Nicho <em>Tight-Space Tools</em>: a chave que alcança o parafuso que o ratchet não alcança</h1>
<p class="sub">Raio-x completo do nicho de ferramentas de acesso a parafusos escondidos (offset extension wrench) no mercado US e Big Five anglo. Das 6 lojas que o mentorado mandou, separei o que é drop do que não é, e mapeei a rede de operações que está escalando esse mercado agora.</p>
<div class="meta"><span>13+ páginas anunciantes rastreadas</span><span>6 lojas de drop de nicho</span><span>Rede persona→loja resolvida</span><span>Modo profundo</span></div>
</header>
""" + momentum_html() + """

<section>
<h2><span class="n">01</span>A tese em uma frente</h2>
<p class="lead">Existe um nicho quente, validado e com playbook definido rodando agora: uma ferramenta manual de ~$69–99 que resolve uma dor cara e específica (alcançar um parafuso/porca escondido que, na oficina, custa de $540 a $2.800 de mão de obra). O mercado é dominado por advertorial em formato de história pessoal, com páginas de "persona" (nomes de gente, não de marca). Duas das seis lojas que você recebeu são exatamente esse modelo. As outras quatro não são o alvo.</p>
<div class="grid g4">
<div class="stat"><div class="v">~810</div><div class="l">anúncios ativos no nicho</div><div class="d">soma das páginas rastreadas do território tight-space</div></div>
<div class="stat"><div class="v">$69–99</div><div class="l">ticket do produto core</div><div class="d">offset extension wrench, medido nos catálogos</div></div>
<div class="stat"><div class="v">2 meses</div><div class="l">idade da líder</div><div class="d">WildBear reg. nov/2025 e já com 187 ativos</div></div>
<div class="stat"><div class="v">US 74%</div><div class="l">mercado principal</div><div class="d">mas espalha pra AU, CA, MX, UK</div></div>
</div>
</section>

<section>
<h2><span class="n">02</span>As 6 lojas do mentorado, classificadas</h2>
<p class="lead">Você pediu pra separar quem é drop de quem não é. Aqui está. Só duas são o modelo de drop de nicho que interessa; duas são general store (drop sem nicho) e duas não são drop.</p>
<div class="tblwrap"><table>
<thead><tr><th>Loja</th><th>Veredito</th><th>Nicho</th><th>Domínio reg.</th><th>Leitura</th></tr></thead>
<tbody>
"""
    ordem = ["wildbeartools.com","thesavary.com","bling-furnitureshop.com","patiyu.com","onevantool.com","integraltruck.com"]
    pill = {"DROP DE NICHO":"p-a","DROP GENERAL STORE":"p-b","NAO E DROP (marca/catalogo)":"p-c","NAO E DROP (marca DTC)":"p-c"}
    cl = {c["dominio"]:c for c in DB["classificacao_referencias_mentorado"]}
    for d in ordem:
        c = cl[d]
        p = pill.get(c["veredito"],"p-n")
        b += f'<tr><td><b>{d}</b></td><td><span class="pill {p}">{c["veredito"]}</span></td><td>{c["nicho"]}</td><td class="num">{c["dominio_reg"]}</td><td style="color:var(--dim);font-size:13px">{c["obs"]}</td></tr>\n'
    b += """</tbody></table></div>
<div class="note"><b>Tradução:</b> das seis, só <b>WildBear</b> e <b>Savary</b> são o modelo replicável (drop de nicho com oferta única e advertorial). <b>Bling</b> e <b>Patiyu</b> são lojas gerais de drop (vendem de tudo, sem oferta) — servem no máximo como fonte de produto, não de método. <b>Onevan</b> e <b>Integral Truck</b> são marcas de verdade (catálogo próprio / produto patenteado), não drop.</div>
</section>

<section>
<h2><span class="n">03</span>A rede real por trás do nicho</h2>
<p class="lead">O achado central. Cada operação de drop roda várias páginas ao mesmo tempo: a página da marca <b>mais</b> páginas com nome de pessoa (persona) que publicam o advertorial de história. Resolvi o destino de cada uma pela Ad Library pública. É assim que o mapa fecha.</p>
<div class="tblwrap"><table>
<thead><tr><th>Operação</th><th>Loja real</th><th>Páginas que abastecem</th><th>Ativos (soma)</th><th>Veredito</th></tr></thead>
<tbody>
<tr><td><b>WildBear</b></td><td><a href="https://wildbeartools.com">wildbeartools.com</a></td><td>WildBear Tools (187) + <b>Miles Turner</b> (162)</td><td class="num up">~349</td><td><span class="pill p-a">MODELAR</span></td></tr>
<tr><td><b>Bolthero</b></td><td><a href="https://getbolthero.com">getbolthero.com</a></td><td>Bolthero (144) + <b>Mike Hartwell</b> (174)</td><td class="num up">~318</td><td><span class="pill p-a">MODELAR</span></td></tr>
<tr><td><b>Savary</b></td><td><a href="https://thesavary.com">thesavary.com</a></td><td>Savary Tool (20) + <b>John Miller</b> (42) + <b>The Home Garage Journal</b> (31)</td><td class="num up">~93</td><td><span class="pill p-a">MODELAR</span></td></tr>
<tr><td><b>Confinedim</b></td><td><a href="https://confinedim.com">confinedim.com</a></td><td>Confinedim (35 ativos / 2.428 histórico)</td><td class="num">35</td><td><span class="pill p-b">OBSERVAR</span></td></tr>
<tr><td><b>Felmix</b></td><td><a href="https://felmix.com">felmix.com</a></td><td>Felmix (12 ativos / 175 histórico)</td><td class="num">12</td><td><span class="pill p-b">OBSERVAR</span></td></tr>
<tr><td><b>Bolt Hunter</b></td><td><a href="https://bolt-hunter.com">bolt-hunter.com</a></td><td>Robert Thompson (16) — <b>domínio de 3 dias</b></td><td class="num">16</td><td><span class="pill p-b">OBSERVAR</span></td></tr>
<tr><td>Vaylo</td><td>não resolvida</td><td>Vaylo (0 ativos — parada)</td><td class="num down">0</td><td><span class="pill p-c">IGNORAR</span></td></tr>
</tbody></table></div>
<div class="info note"><b>Por que isso importa:</b> "Mike Hartwell" e "Miles Turner" não são pessoas, são páginas de advertorial da Bolthero e da WildBear. Quem olha só a página da marca subestima a operação pela metade. A WildBear real roda ~349 anúncios, não 187.</div>
</section>

<section>
<h2><span class="n">04</span>Comparativo das lojas de drop</h2>
<div class="tblwrap"><table>
<thead><tr><th>Loja</th><th>Ativos / Histórico</th><th>Ticket core</th><th>Tráfego/mês</th><th>Stack de porte</th><th>Idade</th><th>Veredito</th></tr></thead>
<tbody>
<tr><td><b><a href="loja-wildbear.html">WildBear</a></b></td><td class="num">187 / 252</td><td class="num">$79–99</td><td class="num up">42K</td><td>Klaviyo, Trustpilot, UpCart</td><td>2 meses</td><td><span class="pill p-a">MODELAR</span></td></tr>
<tr><td><b><a href="loja-bolthero.html">Bolthero</a></b></td><td class="num">144 / 388</td><td class="num">$69</td><td class="num up">100K</td><td>Klaviyo, Loox, GemPages</td><td>—</td><td><span class="pill p-a">MODELAR</span></td></tr>
<tr><td><b><a href="loja-savary.html">Savary</a></b></td><td class="num">20 / 39</td><td class="num">$45–397</td><td class="num up">20K</td><td><b>Triple Whale, Vitals</b>, GemPages, Shrine</td><td>1 mês</td><td><span class="pill p-a">MODELAR</span></td></tr>
<tr><td><b><a href="loja-confinedim.html">Confinedim</a></b></td><td class="num">35 / <b>2.428</b></td><td class="num">~$30–100</td><td class="num">n/d*</td><td>Recharge, TikTok, Afterpay</td><td>3 meses</td><td><span class="pill p-b">OBSERVAR</span></td></tr>
<tr><td><b><a href="loja-felmix.html">Felmix</a></b></td><td class="num">12 / 175</td><td class="num">n/d</td><td class="num">n/d*</td><td>Klaviyo, Judge.me</td><td>4 meses</td><td><span class="pill p-b">OBSERVAR</span></td></tr>
<tr><td><b><a href="loja-bolthunter.html">Bolt Hunter</a></b></td><td class="num">16 / 17</td><td class="num">$89</td><td class="num">n/d*</td><td>Klaviyo, Recharge, Afterpay</td><td><b>3 dias</b></td><td><span class="pill p-b">OBSERVAR</span></td></tr>
</tbody></table></div>
<p style="color:var(--dim2);font-size:12.5px;margin-top:10px">*n/d = tráfego não obtido no SimilarWeb (lojas de lander/Cloudflare ou domínio novo demais sem histórico). Detalhe e método tentado na página de cada loja.</p>
</section>

<section>
<h2><span class="n">05</span>Onde está o dinheiro que ninguém pegou</h2>
<div class="grid g3">
<div class="op"><div class="r">Brecha geográfica</div><h3>UK e Alemanha abertos</h3><p style="color:var(--dim);font-size:14px">Mesmo termo do nicho: <b>US 295</b> anúncios ativos, <b>Canadá 79</b>, <b>Austrália 70</b>, mas <b>UK só 4</b> e <b>Alemanha 1</b>. Cada um com um validador ativo = prova de que funciona, sem concorrência.</p></div>
<div class="op"><div class="r">Brecha de produto</div><h3>Extractor e swivel</h3><p style="color:var(--dim);font-size:14px">"Flexible/swivel socket extension" tem <b>1</b> ativo e "bolt extractor" <b>27</b>, contra 295 do offset wrench. Mesmo avatar, produtos adjacentes, muito menos disputa.</p></div>
<div class="op"><div class="r">Ativo de copy pronto</div><h3>O advertorial de história</h3><p style="color:var(--dim);font-size:14px">A estrutura está madura e documentada: dealer cobrou $X → era um parafuso escondido → ferramenta de $89 resolveu. Segmentada por máquina (diesel, farm, marine, moto).</p></div>
</div>
<p style="margin-top:20px"><a class="btn" href="estrategia.html">Ver a leitura estratégica completa →</a> <a class="btn" href="plano-de-acao.html">Ver o plano de ação →</a></p>
</section>
"""
    page("index.html", "Raio-x · Nicho Tight-Space Tools", b)

# =========================================================================
# ESTRATEGIA
# =========================================================================
def angulo_dominante_html():
    a = DB["angulo_dominante"]
    linhas = [("Big idea", a["big_idea"]),("Mecanismo", a["mecanismo"]),("Hook dominante", a["hook_dominante"]),
              ("Prova", a["prova"]),("Objeção central", a["objecao_central"])]
    rows = "".join(f'<tr><td style="white-space:nowrap;color:var(--dim2);text-transform:uppercase;font-size:11px;letter-spacing:.05em">{k}</td><td>{v}</td></tr>' for k,v in linhas)
    return f"""
<section>
<h2><span class="n">02b</span>O ângulo dominante do nicho</h2>
<p class="lead">Cruzando a anatomia dos vencedores, o padrão que se repete entre eles. É isto que alimenta a <code>/advertorial</code> e a <code>/criar-oferta</code>.</p>
<div class="tblwrap"><table><tbody>{rows}</tbody></table></div>
<div class="note" style="font-size:13px">{a["nota"]}</div>
</section>
"""

def pl_html():
    p = DB["pl_mentorado"]; cards = ""
    for c in p["cenarios"]:
        cards += (f'<div class="card"><h3>{c["nome"]}</h3><dl class="kv">'
                  f'<dt>Preço de venda</dt><dd>€{c["preco"]}</dd>'
                  f'<dt>− Custo produto</dt><dd>€{c["custo"]} <span style="color:var(--dim2)">(est.)</span></dd>'
                  f'<dt>− Frete</dt><dd>€{c["frete"]} <span style="color:var(--dim2)">(est.)</span></dd>'
                  f'<dt>− Gateway</dt><dd>€{c["gateway"]}</dd>'
                  f'<dt>− CPA alvo</dt><dd>€{c["cpa"]} <span style="color:var(--dim2)">(benchmark)</span></dd>'
                  f'<dt>= Margem</dt><dd style="color:var(--acc);font-weight:800">€{c["margem"]} · {c["margem_pct"]}</dd>'
                  f'</dl></div>')
    return f"""
<section>
<h2><span class="n">05b</span>Economia por pedido (P&L do mentorado)</h2>
<p class="lead">A conta de quem vai montar a loja: a margem sobrevive ao frete da China e ao CPA do setor? {p["nota"]}</p>
<div class="grid g2">{cards}</div>
<div class="good note"><b>Leitura:</b> {p["leitura"]}</div>
</section>
"""

def ranking_oportunidades():
    lojas_ord = [("wildbeartools.com","loja-wildbear.html"),("getbolthero.com","loja-bolthero.html"),
                 ("thesavary.com","loja-savary.html"),("confinedim.com","loja-confinedim.html"),
                 ("felmix.com","loja-felmix.html"),("bolt-hunter.com","loja-bolthunter.html")]
    def nlpill(nv,sc):
        c={'INICIANTE':'p-a','MEDIO':'p-b','MÉDIO':'p-b','AVANCADO':'p-c','AVANÇADO':'p-c'}.get(nv or '','p-n')
        return f'<span class="pill {c}">{nv} · {sc}/12</span>' if nv else '<span class="pill p-n">—</span>'
    def traf(o):
        t=o.get('trafego'); return t.get('visitas_mes','n/d') if isinstance(t,dict) else 'n/d'
    mod=''; obs=''
    for key,href in lojas_ord:
        o=DB['lojas'][key]
        r=(f'<tr><td><b><a href="{href}">{o.get("marca",key)}</a></b></td>'
           f'<td>{nlpill(o.get("nivel"),o.get("score"))}</td>'
           f'<td class="num">{o.get("ativos","?")}</td><td class="num">{traf(o)}</td></tr>')
        if str(o.get('veredito','')).startswith('MODELAR'): mod+=r
        else: obs+=r
    return f"""
<section>
<h2><span class="n">00</span>Ranking de oportunidades <span style="color:var(--acc)">MODELAR + DROPSHIPPING</span></h2>
<p class="lead">Todas as lojas do nicho são <b>dropshipping</b> (molde replicável), nenhuma é marca com estoque próprio. Ordenadas por força de oportunidade, com o selo de nível dizendo pra qual operador cada uma serve. Nível avançado não é descarte: é etiqueta de perfil.</p>
<h3>Molde replicável · MODELAR</h3>
<div class="tblwrap"><table><thead><tr><th>Operação</th><th>Nível (pra quem serve)</th><th>Anúncios ativos</th><th>Visitas/mês</th></tr></thead><tbody>{mod}</tbody></table></div>
<h3>Relevantes, mas OBSERVAR</h3>
<div class="tblwrap"><table><thead><tr><th>Operação</th><th>Nível</th><th>Anúncios ativos</th><th>Visitas/mês</th></tr></thead><tbody>{obs}</tbody></table></div>
<div class="info note"><b>Marcas (não replicáveis):</b> onevantool.com (catálogo de power tools ONEVAN) e integraltruck.com (produto proprietário de truck storage) vieram na lista do mentorado mas <b>não são molde</b>: estoque próprio / produto patenteado. Servem pra estudar ângulo, nunca pra copiar a operação. Fora do ranking.</div>
</section>
"""

def build_estrategia():
    b = """
<header>
<span class="tag">Leitura estratégica</span>
<h1>Onde entrar, com que ângulo e por quê</h1>
<p class="sub">O nicho está validado e quente. Entrar de frente contra a WildBear no offset wrench em US é o caminho mais caro. Aqui estão as assimetrias que valem mais que o território óbvio.</p>
</header>
""" + ranking_oportunidades() + """

<section>
<h2><span class="n">01</span>O mecanismo de compra: dor + medo de prejuízo</h2>
<p class="lead">Esse nicho não vende ferramenta, vende <b>evitar um prejuízo</b>. O comprador é quem sofre a dor (mecânico DIY, dono de oficina, fazendeiro, dono de RV/barco) e a urgência é alta porque a máquina parada custa dinheiro todo dia. Isso sustenta ticket médio-alto ($69–99) para um item que, de catálogo, custaria $10–20. A ancoragem não é desconto, é a conta do mecânico: "o dealer queria $850, essa ferramenta custa $89".</p>
<div class="grid g3">
<div class="stat"><div class="v">Dor física + prejuízo</div><div class="l">mecanismo</div><div class="d">quem sofre compra, urgência alta, ticket suportado alto</div></div>
<div class="stat"><div class="v">$540–2.800</div><div class="l">âncora de preço</div><div class="d">custo da mão de obra citado nos anúncios</div></div>
<div class="stat"><div class="v">$69–99</div><div class="l">preço da ferramenta</div><div class="d">10x–40x o custo de catálogo do item</div></div>
</div>
</section>

<section>
<h2><span class="n">02</span>Os dois modelos de escala que coexistem</h2>
<p class="lead">Medi a cadência de criativo das duas maiores operações. Elas escalam de formas opostas — e isso define que jogo você quer jogar.</p>
<div class="grid g2">
<div class="card"><h3 style="color:var(--acc)">WildBear — escala por público</h3>
<ul class="cl">
<li><b>~9,6 anúncios/dia</b>, mas só <b>~8 criativos únicos</b> na amostra</li>
<li>Fator de duplicação <b>~6,3x</b>: o mesmo criativo em muitos públicos</li>
<li>Ângulos de oferta (Black Friday, 50% OFF, "reaches where nothing else can")</li>
<li>Barreira de entrada: <b>budget de mídia</b>, não produção de criativo</li>
</ul></div>
<div class="card"><h3 style="color:var(--acc)">Bolthero — escala por criativo</h3>
<ul class="cl">
<li><b>~20 anúncios/dia</b> com <b>~44 criativos únicos</b> (persona Mike Hartwell)</li>
<li>Fator de duplicação <b>~1,1x</b>: quase todo anúncio é história nova</li>
<li>Segmenta por máquina: diesel, farm/Kubota, marine/impeller, moto Yamaha, spark plugs</li>
<li>Barreira de entrada: <b>máquina de produzir ângulos de história</b></li>
</ul></div>
</div>
<div class="good note"><b>Sua vantagem aqui:</b> você já tem fábrica de advertorial e de história (é o que a operação de Criador de Ofertas faz). O modelo Bolthero — muitos ângulos de história por máquina/ofício — é o que joga a seu favor, não o de queimar budget contra a WildBear.</div>
</section>
""" + angulo_dominante_html() + """

<section>
<h2><span class="n">03</span>As brechas, medidas (não achismo)</h2>
<p class="lead">Rodei o mesmo termo do nicho em vários países e vários ângulos de produto. Números são de anúncios ativos na Ad Library.</p>
<h3>Assimetria geográfica</h3>
<div class="tblwrap"><table>
<thead><tr><th>País</th><th>Ativos (termo do nicho)</th><th>Leitura</th></tr></thead>
<tbody>
<tr><td>Estados Unidos</td><td class="num down">295</td><td>Saturado. WildBear/Bolthero dominam. Caro entrar de frente.</td></tr>
<tr><td>Canadá</td><td class="num">79</td><td>Já sendo atacado (WildBear espalha pra cá)</td></tr>
<tr><td>Austrália</td><td class="num">70</td><td>Já sendo atacado</td></tr>
<tr><td>Reino Unido</td><td class="num up">4</td><td><b>Quase vazio, 1 validador ativo</b> — mesmo mercado anglo, mesmo idioma</td></tr>
<tr><td>Alemanha</td><td class="num up">1</td><td><b>Quase vazio, 1 validador ativo</b> ("Die Antwort auf jeden verbauten Motorraum")</td></tr>
</tbody></table></div>
<div class="note"><b>Ressalva honesta:</b> UK e Alemanha vazios podem significar "ninguém tentou" <b>ou</b> "mercado menor/logística pior". O sinal a favor: existe ao menos 1 anúncio ativo em cada, o que prova que a oferta converte lá. Não é deserto por falta de demanda; é território não ocupado. Teste com budget pequeno antes de escalar.</div>

<h3>Assimetria de produto (mesmo avatar, menos disputa)</h3>
<div class="tblwrap"><table>
<thead><tr><th>Ângulo de produto (US)</th><th>Ativos</th><th>Leitura</th></tr></thead>
<tbody>
<tr><td>Offset extension wrench (o óbvio)</td><td class="num down">295</td><td>Território principal, saturado</td></tr>
<tr><td>Bolt extractor / parafuso espanado</td><td class="num">27</td><td>Dor cara e recorrente ("rounded bolt cost $1,400"), pouco explorada</td></tr>
<tr><td>Stubby / mini ratchet tight space</td><td class="num">32</td><td>Produto adjacente, menos disputa</td></tr>
<tr><td>Flexible / swivel socket extension</td><td class="num up">1</td><td><b>Quase vazio</b> — mesmo problema, formato diferente</td></tr>
</tbody></table></div>
</section>

<section>
<h2><span class="n">04</span>Fraude de prova social é a regra do nicho</h2>
<p class="lead">Cruzei toda alegação com a idade real do domínio. O nicho tolera inflação agressiva e ninguém está sendo punido — o que também significa que a barreira de credibilidade é baixa.</p>
<div class="tblwrap"><table>
<thead><tr><th>Loja</th><th>Alega</th><th>Idade real do domínio</th><th>Veredito</th></tr></thead>
<tbody>
<tr><td>WildBear</td><td>"20.000+ customers"</td><td class="num">~2 meses (nov/2025)</td><td><span class="pill p-c">inflado</span></td></tr>
<tr><td>Bolt Hunter</td><td>"40.000+ customers"</td><td class="num">~3 dias (17/jul/2026)</td><td><span class="pill p-c">fraude flagrante</span></td></tr>
</tbody></table></div>
</section>

<section>
<h2><span class="n">05</span>Veredito estratégico</h2>
<div class="op"><h3>Entre — mas não pela porta da frente</h3>
<p style="color:var(--dim)">O nicho é real, o produto é barato de comprar, a copy está madura e a barreira de credibilidade é baixa. O erro seria brigar por budget contra a WildBear no offset wrench em US. As três jogadas de maior retorno estão abaixo, no plano de ação.</p></div>
<div class="grid g3">
<div class="stat"><div class="v sm">Jogada A</div><div class="l">Offset wrench em UK/DE</div><div class="d">mesmo produto e copy, território aberto com validador</div></div>
<div class="stat"><div class="v sm">Jogada B</div><div class="l">Produto adjacente em US</div><div class="d">extractor/swivel: mesmo avatar, menos disputa</div></div>
<div class="stat"><div class="v sm">Jogada C</div><div class="l">Ângulo por máquina</div><div class="d">clonar o método Bolthero: 1 história por ofício</div></div>
</div>
</section>
"""
    page("estrategia.html", "Estratégia & Gaps · Tight-Space Tools", b)

# =========================================================================
# PLANO DE ACAO
# =========================================================================
def arquitetura_html():
    a = DB['arquitetura_catalogo']
    out = f'<p style="color:var(--dim);font-size:14px;margin-bottom:16px">{a["nota"]}</p>'
    for col in a['colecoes']:
        rows = ''
        for p in col['produtos']:
            link = f'<a href="{p["link"]}">buscar fornecedor →</a>' if p.get('link') else '<span style="color:var(--dim2)">montado/produzido por você</span>'
            rows += f'<tr><td>{p["t"]}</td><td><code>{p["kw"]}</code></td><td>{link}</td></tr>'
        out += (f'<h3>{col["nome"]}</h3><p style="color:var(--dim);font-size:13px;margin:4px 0 8px">{col["papel"]}</p>'
                f'<div class="tblwrap"><table><thead><tr><th>Produto</th><th>Palavra-chave</th><th>Fornecedor</th></tr></thead>'
                f'<tbody>{rows}</tbody></table></div>')
    return out

def paleta_html():
    p = DB['paleta_marca']
    sw = ''
    for s in p['swatches']:
        sw += (f'<div class="swatch"><div class="sw" style="background:{s["hex"]}"></div>'
               f'<div class="info"><b>{s["nome"]}</b><div class="hex">{s["hex"]}</div><div class="fn">{s["fn"]}</div></div></div>')
    return f'<div class="palette">{sw}</div><p style="color:var(--dim2);font-size:12.5px;margin-top:6px">{p["nota"]}</p>'

def build_plano():
    b = """
<header>
<span class="tag">Plano de ação</span>
<h1>Como você entra nesse nicho</h1>
<p class="sub">Marca, produto com fornecedor, escada de oferta, ângulos de copy, funil e orçamento. Tudo derivado do que as operações que já escalam estão fazendo.</p>
</header>

<section>
<h2><span class="n">01</span>Arquitetura de catálogo da loja nova</h2>
<p class="lead">Não é lista solta de produto: é a loja montada em coleções, cada item com a palavra-chave e o link de fornecedor ao vivo (ordenado por volume de pedidos). Enxuta de propósito: 1 core + escada, não catálogo largo.</p>
""" + arquitetura_html() + """
<div class="info note"><b>Nota de método:</b> a Bolthero vende um eBook digital de $15 como bump (33 reviews, nota 4.8). Margem 100%, sobe o AOV sem custo de frete. Está na coleção "Bundles & Digital". Copie.</div>
</section>

<section>
<h2><span class="n">02</span>Marca e identidade</h2>
<p class="lead">Nomes curtos, "tool-sounding", com sufixo de força/precisão. Antes de fechar, conferi que os nomes abaixo <b>não</b> colidem com marca dos concorrentes coletados (WildBear, Bolthero, Bolt Hunter, Savary, Confinedim, Felmix).</p>
<div class="grid g4">
<div class="stat"><div class="v sm">GripReach</div><div class="l">sugestão 1</div></div>
<div class="stat"><div class="v sm">TorqPath</div><div class="l">sugestão 2</div></div>
<div class="stat"><div class="v sm">DeepSocket</div><div class="l">sugestão 3</div></div>
<div class="stat"><div class="v sm">RigidReach</div><div class="l">sugestão 4</div></div>
</div>
<p style="color:var(--dim2);font-size:12.5px;margin-top:10px">Confirme disponibilidade de .com/.de e de marca antes de fechar. Imagens: as lojas usam IA (Higgsfield/Gemini detectados no catálogo da Savary), você não precisa fotografar produto.</p>
<h3>Paleta da marca-produto</h3>
""" + paleta_html() + """
</section>

<section>
<h2><span class="n">03</span>Ângulos de copy prontos (modelo Bolthero)</h2>
<p class="lead">A espinha do advertorial: <b>(1)</b> a oficina/dealer me cobrou $X absurdo → <b>(2)</b> descobri que era um parafuso escondido que nada alcança → <b>(3)</b> essa ferramenta de $89 resolveu em minutos → CTA. Produza uma variação por máquina/ofício:</p>
<div class="grid g2">
<div class="card"><h3>Por veículo/máquina</h3><ul class="cl">
<li><b>Diesel truck:</b> "manifold studs no 5.9/12-valve", "$2.300 pra alcançar 4 studs"</li>
<li><b>Farm:</b> "Kubota/Farmall", "$9.000 de feno parado por um parafuso"</li>
<li><b>Marine:</b> "impeller", "a marina queria $600 e 3 semanas"</li>
<li><b>Moto:</b> "Yamaha salt-seized bolts", "$2.400 por um parafuso de $9"</li>
<li><b>Spark plugs:</b> "Ford/Subaru", "dealer queria $760 por 4 velas"</li>
</ul></div>
<div class="card"><h3>Headlines de oferta (topo)</h3><ul class="cl">
<li>"Reaches the bolt your ratchet can't"</li>
<li>"When your impact won't fit"</li>
<li>"This tool would've saved me hundreds"</li>
<li>"$275/hr tech vs $89 tool. Same bolt."</li>
<li>Oferta: "Up to 50% OFF — this week only"</li>
</ul></div>
</div>
</section>

<section>
<h2><span class="n">04</span>Funil e stack</h2>
<div class="funnel">
<i class="k">Anúncio persona (história)</i><s>→</s><i>Advertorial (página de história)</i><s>→</s><i class="k">PDP com escada</i><s>→</s><i>Bump no carrinho</i><s>→</s><i>Upsell pós-compra</i>
</div>
<p class="lead">Stack mínimo copiando o que o nicho usa: <b>Shopify + GemPages/Shrine</b> (advertorial e PDP), <b>Loox ou Judge.me</b> (reviews), <b>Klaviyo</b> (e-mail), <b>UpCart/ReConvert</b> (bump e upsell), <b>Trustpilot</b> (selo). A Savary, a mais madura, roda ainda Triple Whale (atribuição) e Vitals — deixe pra quando escalar.</p>
</section>

<section>
<h2><span class="n">05</span>Orçamento e economia da operação</h2>
<p class="lead">Números do modelo aplicado à líder (WildBear, 42K visitas/mês) como referência de porte. <b>Medido</b> = visitas. <b>Estimado</b> = o resto. Benchmark IRP jun/2026 (Cars&Motorcycling / Sports&Rec).</p>
<div class="grid g4">
<div class="stat"><div class="v">42K</div><div class="l">visitas/mês (medido)</div><div class="d">SimilarWeb, WildBear</div></div>
<div class="stat"><div class="v">$34–64K</div><div class="l">faturamento/mês (est.)</div><div class="d">conv 1,0%–1,9% × AOV ~$80</div></div>
<div class="stat"><div class="v">~$20K</div><div class="l">mídia/mês (est.)</div><div class="d">via cliques×CPC, ~70% pago</div></div>
<div class="stat"><div class="v">$69→$80+</div><div class="l">AOV core→escada</div><div class="d">core + bump/upsell</div></div>
</div>
<div class="note"><b>Ressalva sobre o investimento:</b> o CPA do IRP (~8% da receita) modela lojas estabelecidas e <b>subestima</b> drop de tráfego pago, que costuma gastar 30–50% da receita em mídia. Por isso reportei o gasto pela via cliques×CPC (~$20K/mês), que bate melhor com o porte da operação. Para você começar, pense em <b>$30–50/dia por criativo em teste</b> e escale só o que passar de ROAS 1,3–1,5 nos primeiros 3 dias.</div>
</section>
""" + pl_html() + """

<section>
<h2><span class="n">06</span>Cronograma de 21 dias</h2>
<ol class="steps">
<li><b>Dias 1–3:</b> fechar fornecedor do core + 2 upsells, registrar marca/domínio, pedir amostra e gravar UGC próprio</li>
<li><b>Dias 4–8:</b> montar loja (Shopify + GemPages), escrever advertorial base e 8–10 variações de história por máquina</li>
<li><b>Dias 9–14:</b> subir campanha de teste em <b>US</b> (validar oferta) com 5–8 criativos persona, $30–50/dia cada</li>
<li><b>Dias 15–21:</b> matar o que não passou, escalar o vencedor e abrir <b>UK + Alemanha</b> (território vazio) com a mesma copy traduzida</li>
</ol>
</section>
"""
    page("plano-de-acao.html", "Plano de ação · Tight-Space Tools", b)

# =========================================================================
# PAGINAS DE LOJA
# =========================================================================
def veredito_pill(v):
    if v.startswith("MODELAR"): return '<span class="pill p-a">MODELAR</span>'
    if v.startswith("OBSERVAR"): return '<span class="pill p-b">OBSERVAR</span>'
    if v.startswith("IGNORAR"): return '<span class="pill p-c">IGNORAR</span>'
    return f'<span class="pill p-n">{v}</span>'

def _momentum_loja_html(d):
    mm = d.get("momentum_loja")
    if not mm: return ''
    cor = {"crescendo":"var(--acc)","emergente":"var(--info)","estavel":"var(--dim)","retraindo":"var(--bad)"}.get(mm,"var(--dim)")
    return (f'<p style="color:var(--dim);font-size:14px;margin-top:12px"><b>Momentum da operação:</b> '
            f'<span style="color:{cor};font-weight:700;text-transform:uppercase">{mm}</span> '
            f'<span style="color:var(--dim2)">(de Tranco + sobrevivência de criativo + idade do campeão)</span></p>')

def anatomia_html(d):
    a = d.get("anatomia")
    if not a: return ''
    linhas = [("Big idea / ângulo", a.get("big_idea","")), ("Mecanismo único", a.get("mecanismo","")),
              ("Formato de hook", a.get("hook","")), ("Estrutura do presell", a.get("presell","")),
              ("Objeção principal", a.get("objecao",""))]
    rows = "".join(f'<tr><td style="white-space:nowrap;color:var(--dim2);text-transform:uppercase;font-size:11px;letter-spacing:.05em">{k}</td><td>{v}</td></tr>' for k,v in linhas)
    return (f'<section><h2><span class="n">06</span>Anatomia do vencedor</h2>'
            f'<p class="lead">Contar anúncio diz quem ganha; isto diz <b>por que</b> ganha, que é o que se copia. Decodificado dos criativos e do funil coletados.</p>'
            f'<div class="tblwrap"><table><tbody>{rows}</tbody></table></div></section>')

def build_loja(fname, slug, key, extra):
    d = DB["lojas"][key]
    prods = d.get("produtos", [])
    hero = prods[0] if prods else {"t": key, "price": "?"}
    ativos = d.get("ativos", "?"); hist = d.get("hist", "?")
    surv = f'{round(ativos/hist*100,1)}%' if isinstance(ativos,int) and isinstance(hist,int) and hist else "n/d"
    pid = d.get('page_id','')
    adlib_url = f"https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id={pid}"
    site_btn = f'<a class="adlib store" href="https://{key}" target="_blank">🛒 Abrir a loja · {key}</a>'
    adlib_btn = (f'<a class="adlib" href="{adlib_url}" target="_blank">📚 Biblioteca de anúncios da Meta →</a>'
                 if pid else '<span class="adlib off">Biblioteca de anúncios: page_id não obtido</span>')
    b = f"""
<header>
<span class="tag">Ficha de loja</span>
<h1>{d.get('marca',key)}</h1>
<p class="sub">{extra.get('sub','')}</p>
<div class="meta"><span>{d.get('plataforma','')}</span><span>Domínio: {d.get('dominio_reg','')}</span></div>
<div class="toplinks">{site_btn}{adlib_btn}</div>
</header>

<section>
<h2><span class="n">01</span>Produto campeão e oferta</h2>
<div class="hero-prod">
<div><div class="r">Produto herói</div><h3>{hero['t']}</h3>
<div class="preco">${hero['price']}</div>
<p style="color:var(--dim);margin-top:12px;font-size:14px">{extra.get('oferta','')}</p></div>
</div>
<h3>Catálogo / escada</h3>
<div class="tblwrap"><table><thead><tr><th>Produto</th><th>Preço</th></tr></thead><tbody>
"""
    for p in prods:
        b += f'<tr><td>{p["t"]}</td><td class="num">${p["price"]}</td></tr>\n'
    b += f"""</tbody></table></div>
<p style="color:var(--dim);font-size:14px;margin-top:12px">{d.get('escada','')}</p>
</section>

<section>
<h2><span class="n">02</span>Mídia paga</h2>
<div class="grid g4">
<div class="stat"><div class="v">{ativos}</div><div class="l">anúncios ativos</div></div>
<div class="stat"><div class="v">{hist}</div><div class="l">histórico total</div></div>
<div class="stat"><div class="v">{surv}</div><div class="l">sobrevivência</div><div class="d">ativos ÷ histórico</div></div>
<div class="stat"><div class="v sm">{d.get('cluster_ativos','—')}</div><div class="l">ativos do cluster</div><div class="d">com páginas-persona</div></div>
</div>
{extra.get('cadencia_html','')}
{extra.get('midia_nota','')}
{_momentum_loja_html(d)}
</section>
"""
    # trafego
    tr = d.get("trafego")
    if isinstance(tr, dict):
        paises = " · ".join(f'{k} {v}' for k,v in tr.get("paises",{}).items())
        b += f"""
<section>
<h2><span class="n">03</span>Tráfego (SimilarWeb)</h2>
<div class="grid g4">
<div class="stat"><div class="v">{tr.get('visitas_mes','n/d')}</div><div class="l">visitas/mês</div><div class="d">medido</div></div>
<div class="stat"><div class="v sm">{tr.get('bounce','n/d')}</div><div class="l">bounce rate</div></div>
<div class="stat"><div class="v sm">{tr.get('pg_visita','n/d')}</div><div class="l">páginas/visita</div></div>
<div class="stat"><div class="v sm">{tr.get('duracao','n/d')}</div><div class="l">duração da visita</div></div>
</div>
<p style="color:var(--dim);font-size:14px;margin-top:12px"><b>Origem do tráfego:</b> {paises}</p>
{extra.get('faturamento_html','')}
</section>
"""
    else:
        b += f"""
<section>
<h2><span class="n">03</span>Tráfego</h2>
<div class="note"><b>Dado não obtido: tráfego SimilarWeb.</b><br>Tentativas: (1) SimilarWeb via navegador real no domínio da loja; (2) domínio alternativo (lander); (3) proxy por reviews.<br>Motivo: {tr if isinstance(tr,str) else 'lander/Cloudflare ou domínio novo demais sem histórico no SimilarWeb'}.<br>Impacto: faturamento não estimável por visitas; use os reviews e o volume de anúncios como proxy de porte.</div>
</section>
"""
    # reviews
    rv = d.get("reviews")
    if isinstance(rv, dict):
        b += f"""
<section>
<h2><span class="n">04</span>Prova social (reviews verificados)</h2>
<div class="good note"><b>Reviews reais via Loox (JSON-LD):</b> amostra de {rv.get('amostra')} reviews em produtos individuais. Pedidos estimados: <b>{rv.get('pedidos_estimados')}</b>. Base é piso (só produtos amostrados), não total da loja.</div>
</section>
"""
    elif isinstance(rv, str):
        b += f'<section><h2><span class="n">04</span>Prova social</h2><p style="color:var(--dim)">{rv}</p>'
        if d.get("fraude_prova_social"):
            b += f'<div class="danger note"><b>Fraude de prova social:</b> {d["fraude_prova_social"]}</div>'
        b += '</section>'
    if d.get("fraude_prova_social") and not isinstance(rv, str):
        b += f'<section><h2><span class="n">04b</span>Prova social</h2><div class="danger note"><b>Fraude de prova social:</b> {d["fraude_prova_social"]}</div></section>'

    # prints
    home_s = shot(slug,"home","Home"); pdp_s = shot(slug,"pdp","Página de produto")
    shots = home_s + pdp_s
    if shots:
        falta_pdp = ('' if pdp_s else '<div class="note"><b>PDP não capturada:</b> products.json bloqueado (Cloudflare) e sem handle de produto pro Playwright. Só a home foi capturada. Método tentado: prints.js via best-sellers e products.json.</div>')
        b += f'<section><h2><span class="n">05</span>Prints</h2><div class="shots">{shots}</div>{falta_pdp}</section>'
    else:
        b += ('<section><h2><span class="n">05</span>Prints</h2>'
               '<div class="note"><b>Dado não obtido: prints.</b> A captura via Playwright não foi concluída para esta loja nesta rodada. '
               'Método tentado: navegador real headless:false. Reexecutar o prints.js resolve.</div></section>')

    # anatomia do vencedor (6b)
    b += anatomia_html(d)
    # stack + veredito
    stack_chips = "".join(f'<span class="{"hi" if s in ("triplewhale","vitals","gempages","shrine") else ""}">{s}</span>' for s in d.get("stack",[]))
    b += f"""
<section>
<h2><span class="n">06b</span>Stack e leitura</h2>
<div class="chips">{stack_chips}</div>
<p style="color:var(--dim);font-size:14px;margin-top:12px">{d.get('stack_leitura','')}</p>
{extra.get('leitura','')}
</section>
"""
    # === selos: modelo + veredito + nivel ===
    modelo = d.get('modelo','')
    if modelo.startswith('DROP'): modelo_pill = '<span class="pill p-a">DROPSHIPPING</span>'
    elif modelo.startswith('MARCA'): modelo_pill = '<span class="pill p-i">MARCA (não replicável)</span>'
    else: modelo_pill = f'<span class="pill p-n">{modelo or "modelo n/d"}</span>'
    nivel = d.get('nivel'); score = d.get('score')
    nivel_pill = ''
    if nivel:
        ncls = {'INICIANTE':'p-a','MEDIO':'p-b','MÉDIO':'p-b','AVANCADO':'p-c','AVANÇADO':'p-c'}.get(nivel,'p-n')
        nivel_pill = f'<span class="pill {ncls}">NÍVEL {nivel} · {score}/12</span>'
    # sinais que sustentam o selo DROPSHIPPING (check 7b)
    sinais = []
    st = d.get('stack',[])
    if any(x in st for x in ['loox','judge.me','vitals']): sinais.append('Shopify + app de review (Loox/Judge.me/Vitals)')
    if d.get('img_ai'): sinais.append('imagens geradas por IA (' + ', '.join(d['img_ai'].keys()) + ')')
    if d.get('fraude_prova_social'): sinais.append('prova social inflada vs idade real do domínio')
    sinais.append('produto genérico achável no AliExpress, catálogo rebrandeado')
    sinais_html = '<ul class="cl">' + ''.join(f'<li>{s}</li>' for s in sinais) + '</ul>'
    # scorecard
    sc = d.get('scorecard'); sc_html = ''
    if sc:
        rows = ''.join(f'<tr><td>{k}</td><td class="num">{v}/2</td></tr>' for k,v in sc.items())
        sc_html = (f'<h3>Scorecard de nível de execução</h3><div class="tblwrap"><table>'
                   f'<thead><tr><th>Eixo (0–2)</th><th>Pontos</th></tr></thead><tbody>{rows}'
                   f'<tr><td><b>Total</b></td><td class="num up"><b>{score}/12</b></td></tr></tbody></table></div>'
                   f'<p style="color:var(--dim);font-size:13.5px;margin-top:10px">{d.get("nivel_just","")}</p>')
    b += f"""
<section>
<h2><span class="n">07</span>Veredito e selos</h2>
<div class="{'op' if d['veredito'].startswith('MODELAR') else 'card'}">
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px">{modelo_pill}{veredito_pill(d['veredito'])}{nivel_pill}</div>
<p style="color:var(--dim)">{extra.get('veredito_txt','')}</p>
</div>
<h3>Por que é DROPSHIPPING (não marca)</h3>
{sinais_html}
{sc_html}
</section>
"""
    page(fname, f"{d.get('marca',key)} · Raio-x", b)

# ---- conteudo especifico por loja ----
LOJAS = {
 "loja-wildbear.html": ("wildbear","wildbeartools.com",{
   "sub":"A líder do nicho. 2 meses de domínio, 187 anúncios ativos na página da marca e mais 162 na persona Miles Turner. Escala por público, poucos criativos duplicados.",
   "oferta":"Ancora em Black Friday / 'Up to 55% OFF'. Ancoragem por economia contra o preço do mecânico.",
   "cadencia_html":'<h3>Cadência de criativo</h3><div class="grid g3"><div class="stat"><div class="v sm">~9,6/dia</div><div class="l">anúncios/dia</div></div><div class="stat"><div class="v sm">~8</div><div class="l">criativos únicos (amostra 50)</div></div><div class="stat"><div class="v sm">~6,3x</div><div class="l">duplicação</div></div></div><p style="color:var(--dim);font-size:14px;margin-top:10px">Poucos criativos em muitos públicos = escala por budget, não por produção. Cluster real ~349 ativos (marca + Miles Turner).</p>',
   "faturamento_html":'<div class="grid g3" style="margin-top:16px"><div class="stat"><div class="v">$34–64K</div><div class="l">faturamento/mês (est.)</div><div class="d">conv 1,0%–1,9% × AOV ~$80</div></div><div class="stat"><div class="v sm">~$20K</div><div class="l">mídia/mês (est.)</div><div class="d">cliques×CPC ~70% pago</div></div><div class="stat"><div class="v sm">$69–99</div><div class="l">ticket core (medido)</div></div></div><p style="color:var(--dim2);font-size:12px;margin-top:8px">Bounce 45,6% (audiência na média) + espalha pra AU/CA/MX = operação buscando volume no anglo inteiro.</p>',
   "leitura":'<div class="info note"><b>O que copiar:</b> a ancoragem por preço-do-mecânico, o UpCart pra bump, e a estratégia de página-persona (Miles Turner) rodando o mesmo criativo pra diluir risco de ban.</div>',
   "veredito_txt":"Escala provada, estrutura replicável no seu porte, produto barato e copy madura. É o benchmark a modelar — mas não a enfrentar de frente por budget em US. Modele a estrutura, ataque território aberto (UK/DE) ou produto adjacente.",
 }),
 "loja-bolthero.html": ("bolthero","getbolthero.com",{
   "sub":"A operação de maior volume de criativo. Loja em getbolthero.com, abastecida pela página Bolthero (144) + persona Mike Hartwell (174). ~44 histórias únicas por amostra: escala por ângulo.",
   "oferta":"Core $69 'Reach The Bolts Your Ratchet Can't'. Escada com espelho/magnet $25 e eBook digital $15.",
   "cadencia_html":'<h3>Cadência de criativo</h3><div class="grid g3"><div class="stat"><div class="v sm">~20/dia</div><div class="l">anúncios/dia</div></div><div class="stat"><div class="v sm">~44</div><div class="l">criativos únicos (amostra 50)</div></div><div class="stat"><div class="v sm">~1,1x</div><div class="l">duplicação</div></div></div><p style="color:var(--dim);font-size:14px;margin-top:10px">Quase todo anúncio é história nova, segmentada por máquina (diesel, farm, marine, moto, spark plug). É a máquina de produção de ângulo do nicho.</p>',
   "faturamento_html":'<div class="grid g3" style="margin-top:16px"><div class="stat"><div class="v">$80–152K</div><div class="l">faturamento/mês (est.)</div><div class="d">conv 1,0%–1,9% × AOV ~$80</div></div><div class="stat"><div class="v sm">~$47K</div><div class="l">mídia/mês (est.)</div><div class="d">cliques×CPC ~70% pago</div></div><div class="stat"><div class="v sm">100K</div><div class="l">visitas/mês (medido)</div></div></div><p style="color:var(--dim2);font-size:12px;margin-top:8px">Maior tráfego do nicho — mais que o dobro da WildBear. Duração 26s + bounce 54% = tráfego frio de anúncio (use o cenário conservador). Espalha US/AU/CA + começa Espanha.</p>',
   "leitura":'<div class="good note"><b>O que copiar (mais importante da pesquisa):</b> o método de 1 história por ofício/máquina. É replicável com IA e é onde você tem vantagem. Também o eBook digital de $15 como bump de margem 100%.</div>',
   "veredito_txt":"A MAIOR operação do nicho por tráfego (100K/mês). Escala por criativo, não por budget puro. Reviews Loox verificados (piso 55) sustentam 1.833–5.500 pedidos. Modele o método de ângulo por máquina.",
 }),
 "loja-savary.html": ("savary","thesavary.com",{
   "sub":"A operação mais madura em CRO. 1 mês de domínio mas já com Triple Whale, Vitals, GemPages e Shrine. Catálogo mais largo ($45–397) e escada com garantias vendidas como SKU.",
   "oferta":"Core offset extension / torque multiplier até $397. Warranties de 1–2 anos vendidas como order bump.",
   "midia_nota":'<div class="note"><b>Cluster:</b> a página Savary Tool tem só 20 ativos, mas John Miller (42) + The Home Garage Journal (31) apontam pra thesavary.com — cluster real ~93 ativos. Também anuncia em espanhol ("Llave de Extensión Acodada PRO").</div>',
   "faturamento_html":'<div class="grid g3" style="margin-top:16px"><div class="stat"><div class="v">$18–34K</div><div class="l">faturamento/mês (est.)</div><div class="d">conv 1,0%–1,9% × AOV ~$90</div></div><div class="stat"><div class="v sm">~$9,4K</div><div class="l">mídia/mês (est.)</div><div class="d">cliques×CPC ~70% pago</div></div><div class="stat"><div class="v sm">$45–397</div><div class="l">faixa de ticket (medido)</div></div></div><p style="color:var(--dim2);font-size:12px;margin-top:8px">Bounce 59% (mais frio) + 95% US. Ticket mais alto e catálogo mais largo = AOV maior por unidade de tráfego.</p>',
   "leitura":'<div class="info note"><b>O que copiar:</b> vender garantia estendida como SKU (bump explícito e margem quase pura), o catálogo mais largo pra sustentar AOV alto, e a operação multilíngue (US + espanhol) pra ampliar mercado.</div>',
   "veredito_txt":"Operação séria de CRO num domínio novíssimo. O stack (Triple Whale + Vitals) indica quem investe pra durar. Modele a escada de garantia e o catálogo mais largo. Menos anúncios que WildBear, mas ticket maior.",
 }),
 "loja-confinedim.html": ("confinedim","confinedim.com",{
   "sub":"O maior histórico do grupo: 2.428 anúncios já rodados, mas só 35 ativos (sobrevivência 1,4%). Queima massiva de criativo em volume — ou operação esfriando.",
   "oferta":"Extension Clamp Tool 'Perfect Tool For Tight Spaces'. Faixa de preço vista no HTML ~$5–100.",
   "midia_nota":'<div class="note"><b>Leitura da sobrevivência:</b> 1,4% (35/2.428). Em nicho de rotação agressiva isso pode ser método de queima em volume, não fracasso. Mas com poucos ativos hoje, o sinal é de operação em desaceleração. products.json bloqueado por Cloudflare.</div>',
   "leitura":'<div class="note"><b>Cautela:</b> o histórico enorme prova que já testaram muito; os poucos ativos hoje sugerem que ou acharam o vencedor e enxugaram, ou estão saindo. Observar, não modelar às cegas.</div>',
   "veredito_txt":"Histórico impressionante mas presente fraco. Serve de evidência de que o nicho comporta queima de milhares de criativos. Observar a evolução antes de tratar como referência ativa.",
 }),
 "loja-felmix.html": ("felmix","felmix.com",{
   "sub":"Operação menor e mais recente. 12 ativos / 175 histórico. 'When Your Impact Won't Fit' — mesmo produto core do nicho.",
   "oferta":"Ângulo 'quando seu impacto não cabe' — o mesmo problema de acesso, dito pelo lado da ferramenta pneumática.",
   "leitura":'<div class="note"><b>Leitura:</b> operação em estágio inicial/teste. Imagens IA (Gemini) confirmam produção sem fotografia. Judge.me em vez de Loox. Pouca escala ainda.</div>',
   "veredito_txt":"Player pequeno testando o mesmo core. Útil como confirmação de que o nicho atrai novos entrantes toda semana, mas sem escala pra modelar.",
 }),
 "loja-bolthunter.html": ("bolthunter","bolt-hunter.com",{
   "sub":"Loja registrada há 3 dias (17/jul/2026) e já rodando 16 anúncios e alegando '40.000+ customers'. O retrato de quão rápido e agressivo é o ciclo de entrada nesse nicho.",
   "oferta":"Core Bolthunter Offset-Extension $89 + LED Headlamp $18 (upsell) + Shipping Protection $3 (bump). Escada montada desde o dia 1.",
   "midia_nota":'<div class="danger note"><b>Fraude flagrante:</b> alega "40.000+ customers" com domínio de 3 dias. Prova de que o nicho tolera inflação total sem punição — e de que a barreira de credibilidade é baixíssima.</div>',
   "leitura":'<div class="info note"><b>O que aprender:</b> a velocidade. Loja nova monta escada completa (core+upsell+bump) e sobe advertorial de história (Robert Thompson) em dias. É o ritmo que você precisa igualar.</div>',
   "veredito_txt":"Nova demais pra julgar performance, mas valiosa como espelho do playbook de entrada: escada pronta no dia 1, persona de história, prova social inflada. Observar como se comporta nas próximas 2 semanas.",
 }),
}

def build_oportunidade():
    b = """
<header>
<span class="tag">Gap de oportunidade · a jogada recomendada</span>
<h1><em>Winkelmeister</em> — a ferramenta campeã dos EUA no mercado alemão que ninguém ocupou</h1>
<p class="sub">Uma oferta que já converte nos Estados Unidos (295 anúncios ativos, operações escalando desde novembro), levada pro espaço de língua alemã (DE + Áustria + Suíça) onde o nicho está praticamente zerado — mas onde a demanda de categoria já existe. Dropshipping puro, criativo 100% IA, sem influenciador, montável em duas semanas.</p>
<div class="meta"><span>Produto validado</span><span>Território virgem</span><span>Sem estoque</span><span>Sem influenciador</span><span>Copy pronta pra clonar</span></div>
</header>

<section>
<h2><span class="n">01</span>Por que esta é a jogada — os seus 6 critérios, atendidos</h2>
<p class="lead">Você foi específico no que queria. Cada linha abaixo é uma exigência sua e como esta oportunidade a cumpre, com a prova ao lado.</p>
<div class="tblwrap"><table>
<thead><tr><th>Seu critério</th><th>Como esta jogada atende</th><th>Prova</th></tr></thead>
<tbody>
<tr><td><b>Nicho não concorrido</b></td><td>O nicho tight-space no espaço alemão está zerado</td><td class="num up">0 anúncios ativos (DACH)</td></tr>
<tr><td><b>Posicionamento não concorrido</b></td><td>Nenhuma marca dedicada; ângulo "Schrauber alemão × Werkstatt cara" livre</td><td>nenhum concorrente direto encontrado</td></tr>
<tr><td><b>Sem comprar/estocar produto</b></td><td>Dropshipping: fornecedor envia, você nunca toca no produto</td><td>link AliExpress na seção 07</td></tr>
<tr><td><b>Sem influenciador</b></td><td>Advertorial de história + tráfego pago frio (o playbook do nicho)</td><td>é assim que WildBear/Bolthero escalam</td></tr>
<tr><td><b>IA faz o trabalho pesado</b></td><td>Imagem (Higgsfield/Gemini), voz (ElevenLabs), copy (advertorial). Você não grava nada</td><td>Savary já usa imagem IA no catálogo</td></tr>
<tr><td><b>Barato, rápido, vende nos primeiros dias</b></td><td>A oferta já é validada — você não testa demanda, só traduz e sobe num lugar sem concorrência</td><td>295 ativos em US provam que converte</td></tr>
</tbody></table></div>
</section>

<section>
<h2><span class="n">02</span>A prova: o oceano azul, medido</h2>
<p class="lead">Não é achismo. Medi o mesmo produto em vários territórios e vários termos alemães. O específico está vazio; o amplo mostra que tem gente comprando ferramenta automotiva no DE.</p>
<div class="grid g4">
<div class="stat"><div class="v down">295</div><div class="l">EUA — ativos</div><div class="d">saturado, WildBear/Bolthero dominam</div></div>
<div class="stat"><div class="v up">0</div><div class="l">Alemanha — ativos</div><div class="d">5 termos testados (EN + nativos), todos 0–1</div></div>
<div class="stat"><div class="v up">0</div><div class="l">Áustria — ativos</div><div class="d">território de língua alemã livre</div></div>
<div class="stat"><div class="v">19</div><div class="l">demanda de categoria (DE)</div><div class="d">anúncios de "KFZ Werkzeug / Werkstatt" — apetite existe</div></div>
</div>
<div class="good note"><b>A leitura:</b> vazio no ângulo específico + demanda viva na categoria = o cenário que você quer. Não é deserto por falta de compradores; é território que ninguém ocupou ainda. O mercado de drop no DACH costuma vir 3–6 meses atrás do US, e o produto só virou campeão em US a partir de nov/2025 — a janela está aberta agora.</div>
<div class="note"><b>Ressalva honesta (não vou esconder):</b> "0 anúncios" também pode significar "tentaram e não funcionou". O que pesa a favor de "ninguém tentou": a cultura Schrauber (faça-você-mesmo automotivo) é forte no DACH, a oficina alemã cobra €120–180/hora, e existe demanda de categoria (19). Mesmo assim, a validação real vem do seu próprio teste com budget pequeno — por isso o plano começa com €30–40/dia, não com escala.</div>
</section>

<section>
<h2><span class="n">03</span>O IPP — a oferta que o cliente vê</h2>
<p class="lead">O mesmo mecanismo que funciona em US: ancorar no preço da oficina, não em desconto. Preços em euro, escada montada desde o dia 1.</p>
<div class="hero-prod">
<div><div class="r">Produto herói</div><h3>Winkelmeister — Winkel-Verlängerung</h3>
<div class="preco">€69<span class="de">€129</span><span class="off">−46%</span></div>
<p style="color:var(--dim);margin-top:12px;font-size:14px">"Erreicht die Schraube, an die keine Ratsche kommt." A chave de extensão em ângulo que alcança o parafuso escondido no cofre de motor apertado — sem desmontar meia peça.</p></div>
</div>
<h3>A escada (AOV alvo €85–95)</h3>
<div class="tblwrap"><table>
<thead><tr><th>Papel</th><th>Produto</th><th>Preço</th><th>Função</th></tr></thead>
<tbody>
<tr><td><b>Core</b></td><td>Winkelmeister Winkel-Verlängerung</td><td class="num">€69</td><td>o herói do advertorial</td></tr>
<tr><td>Bump</td><td>4er Adapter-Set (Steckschlüssel)</td><td class="num">€15</td><td>caixa marcada por padrão</td></tr>
<tr><td>Upsell 1</td><td>Teleskop-Inspektionsspiegel</td><td class="num">€25</td><td>"veja o parafuso antes de alcançá-lo"</td></tr>
<tr><td>Upsell 2</td><td>Magnet-Greifer mit LED-Licht</td><td class="num">€25</td><td>"pegue o parafuso que caiu"</td></tr>
<tr><td>Bump digital</td><td>eBook "10 Schrauber-Tricks" (custo zero)</td><td class="num">€9</td><td>margem 100%, sobe o AOV</td></tr>
</tbody></table></div>
<div class="info note"><b>A ancoragem (o coração da copy):</b> "Die Werkstatt wollte €640, nur um an eine Schraube zu kommen." O preço de referência não é o desconto — é a conta da oficina. É o que faz um item de €8 de custo vender a €69.</div>
</section>

<section>
<h2><span class="n">04</span>A marca</h2>
<div class="grid g2">
<div class="card"><h3>Identidade</h3>
<dl class="kv">
<dt>Nome</dt><dd><b>Winkelmeister</b> ("mestre do ângulo") — soa a engenharia alemã, que é o que o avatar respeita</dd>
<dt>Tagline</dt><dd>"Das Werkzeug, das dir die Werkstatt nicht verrät." (a ferramenta que a oficina não te conta)</dd>
<dt>Posicionamento</dt><dd>Orgulho do Schrauber: você conserta sozinho, não paga a hora absurda da Werkstatt</dd>
<dt>Alternativas</dt><dd>TiefGriff · SchraubProfi · MotorGriff (registrar .de/.com e conferir marca antes de fechar)</dd>
</dl></div>
<div class="card"><h3>Visual (tudo gerável por IA)</h3>
<ul class="cl">
<li><b>Paleta:</b> preto/antracite + laranja-sinal (ferramenta séria) ou preto + amarelo-industrial</li>
<li><b>Tipografia:</b> sem-serifa condensada, robusta (cara de oficina alemã)</li>
<li><b>Fotos de produto:</b> Higgsfield/Gemini — ferramenta em cofre de motor real, mão segurando. Sem fotografar nada</li>
<li><b>Selo:</b> "Entwickelt für deutsche Schrauber" + trust badges de pagamento</li>
</ul></div>
</div>
<div class="note"><b>Nota de checagem:</b> "Winkelmeister" e as alternativas não aparecem em nenhum catálogo dos concorrentes coletados (todos US). Ainda assim, confirme disponibilidade de domínio e marca registrada antes de fechar.</div>
</section>

<section>
<h2><span class="n">05</span>A estrutura da loja — profissional, clonável</h2>
<p class="lead">Nada de reinventar. Copia-se o esqueleto que as operações de US já provaram, adaptado ao alemão.</p>
<div class="funnel">
<i class="k">Anúncio persona (Schrauber conta a história)</i><s>→</s><i>Advertorial (página de história)</i><s>→</s><i class="k">PDP com escada</i><s>→</s><i>Bump no carrinho</i><s>→</s><i>Upsell pós-compra</i><s>→</s><i>E-mail (Klaviyo)</i>
</div>
<div class="grid g2">
<div class="card"><h3>Páginas</h3><ul class="cl">
<li><b>Home</b> em formato de oferta (herói + prova + escada)</li>
<li><b>Advertorial</b> "/pages/story" — a história do Schrauber</li>
<li><b>PDP</b> com bump, garantia e reviews</li>
<li><b>Über uns · FAQ · Versand · AGB · Widerruf</b> (obrigatórias no DE — direito de devolução)</li>
</ul></div>
<div class="card"><h3>Stack mínimo</h3><div class="chips">
<span class="hi">Shopify</span><span class="hi">GemPages</span><span>Loox (reviews)</span><span>Klaviyo</span><span>UpCart (bump)</span><span>ReConvert (upsell)</span><span>Trustpilot</span><span>Klarna/PayPal</span>
</div><p style="color:var(--dim);font-size:13px;margin-top:10px">Klarna e PayPal são quase obrigatórios no checkout alemão — o alemão desconfia de loja sem eles.</p></div>
</div>
</section>

<section>
<h2><span class="n">06</span>A máquina de criativo com IA — sem gravar, sem influenciador</h2>
<p class="lead">Aqui é onde a sua estrutura vence. Todo o criativo sai de IA e do método de história já validado no nicho.</p>
<div class="grid g3">
<div class="stat"><div class="v sm">Copy</div><div class="l">advertorial de história</div><div class="d">1 história por máquina, em alemão — gerada e refinada por IA</div></div>
<div class="stat"><div class="v sm">Imagem</div><div class="l">Higgsfield / Gemini</div><div class="d">produto em cofre de motor, mão segurando, sem fotografar</div></div>
<div class="stat"><div class="v sm">Vídeo/voz</div><div class="l">avatar IA + ElevenLabs</div><div class="d">UGC sintético narrado em alemão nativo</div></div>
</div>
<h3>Ângulos por máquina (o método Bolthero, em alemão)</h3>
<div class="chips">
<span>VW/Audi TDI (Diesel)</span><span>BMW N47 Steuerkette</span><span>Mercedes verbauter Motorraum</span><span>Traktor / Landwirtschaft</span><span>Motorrad</span><span>Wohnmobil</span>
</div>
<p style="color:var(--dim);font-size:14px;margin-top:12px">Cada anúncio é uma história curta: a Werkstatt queria €X por um parafuso escondido → era só um parafuso que nada alcança → esta ferramenta de €69 resolveu em minutos. Você produz 8–10 variações no dia 1, sem gravar nada.</p>
</section>

<section>
<h2><span class="n">07</span>Fornecedor e margem</h2>
<div class="tblwrap"><table>
<thead><tr><th>Produto</th><th>Custo estimado</th><th>Venda</th><th>Buscar fornecedor (ao vivo)</th></tr></thead>
<tbody>
<tr><td>Offset extension wrench (core)</td><td class="num">~€8–12</td><td class="num">€69</td><td><a href="https://www.aliexpress.com/w/wholesale-offset-extension-wrench.html?SortType=total_tranpro_desc">buscar →</a></td></tr>
<tr><td>Socket adapter set</td><td class="num">~€3–5</td><td class="num">€15</td><td><a href="https://www.aliexpress.com/w/wholesale-socket-adapter-set.html?SortType=total_tranpro_desc">buscar →</a></td></tr>
<tr><td>Inspektionsspiegel teleskop</td><td class="num">~€4–7</td><td class="num">€25</td><td><a href="https://www.aliexpress.com/w/wholesale-telescoping-inspection-mirror.html?SortType=total_tranpro_desc">buscar →</a></td></tr>
<tr><td>Magnet-Greifer LED</td><td class="num">~€3–6</td><td class="num">€25</td><td><a href="https://www.aliexpress.com/w/wholesale-magnetic-pickup-tool-light.html?SortType=total_tranpro_desc">buscar →</a></td></tr>
</tbody></table></div>
<p style="color:var(--dim2);font-size:12.5px;margin-top:10px">Ordene por volume de pedidos (já é o link), escolha fornecedor com histórico e avaliação &gt; 4.5, e confira prazo de entrega para a UE. Custo é estimativa de busca, não medido — confirme no fornecedor antes de fechar margem.</p>
</section>

<section>
<h2><span class="n">08</span>Orçamento e cronograma de 14 dias</h2>
<div class="grid g4">
<div class="stat"><div class="v sm">~€100/mês</div><div class="l">setup (Shopify + apps)</div></div>
<div class="stat"><div class="v sm">€30–40/dia</div><div class="l">budget de teste inicial</div></div>
<div class="stat"><div class="v sm">€8–12</div><div class="l">custo do core</div></div>
<div class="stat"><div class="v sm">ROAS 1,3+</div><div class="l">gatilho pra escalar</div></div>
</div>
<ol class="steps">
<li><b>Dias 1–3:</b> registrar marca/domínio .de, montar Shopify + GemPages, escolher fornecedor, gerar fotos IA do produto</li>
<li><b>Dias 4–7:</b> escrever advertorial base em alemão + 8–10 variações de história por máquina; montar PDP com escada e Klarna/PayPal</li>
<li><b>Dias 8–11:</b> subir teste em DE (5–8 criativos persona, €30–40/dia); começar a vender e ler os dados</li>
<li><b>Dias 12–14:</b> matar o que não deu, escalar o vencedor, abrir Áustria + Suíça com a mesma copy</li>
</ol>
<div class="good note"><b>Por que vende nos primeiros dias:</b> você não está apostando se o produto converte — isso já foi provado por 295 anúncios ativos em US. Está levando uma oferta madura pra um leilão sem concorrência, onde o CPM é mais barato e o clique não disputa com WildBear nem Bolthero.</div>
</section>

<section>
<h2><span class="n">09</span>Os riscos, na mesa</h2>
<ul class="cl">
<li><b>Mercado menor que US.</b> DACH é grande e rico, mas não é o volume americano. Compensa com concorrência quase nula.</li>
<li><b>"0 anúncios" não é garantia.</b> Pode ser que ninguém tenha achado que vale — ou que já testaram. A demanda de categoria (19) e a cultura Schrauber pesam a favor, mas quem confirma é o seu teste.</li>
<li><b>Logística UE.</b> Prazo de entrega do fornecedor precisa ser aceitável pro cliente alemão (que é exigente). Considere fornecedor com armazém na Europa se o volume justificar.</li>
<li><b>Conformidade DE.</b> Widerrufsrecht (direito de devolução), Impressum e AGB são obrigatórios. É só configurar, mas não pule.</li>
</ul>
<div class="info note" style="margin-top:20px"><b>Sequência (ver <a href="mercados.html">Mercados</a>):</b> o passo 0 mais barato é o <b>Reino Unido</b> — mesma copy inglesa dos EUA, sem tradução, com demanda de Trends alta e ângulo quase vazio. O DACH (Winkelmeister, em alemão) é o passo seguinte: o oceano mais azul, mas exige traduzir. Comece validando em inglês no UK, depois abra a marca dedicada no alemão.</div>
<div class="op" style="margin-top:16px"><h3>Veredito</h3><p style="color:var(--dim)">É a jogada de menor risco e menor esforço pra resultado rápido dentro de tudo que mapeei: oferta pronta, território vazio, zero dependência de estoque ou de influenciador, criativo 100% IA. Se quiser, o próximo passo é eu rodar a <code>/criar-oferta</code> e já entregar o advertorial (UK em inglês ou DACH em alemão) + a PDP escrita.</p></div>
</section>
"""
    page("oportunidade.html", "A Oportunidade · Winkelmeister (DACH)", b)

def build_mercados():
    m = DB["mercados"]
    rows = ""
    for p in m["paises"]:
        razf = float(p["razao"].replace(',','.'))
        cls = "up" if razf < 1 else "down" if razf > 5 else ""
        rows += (f'<tr><td><b>{p["pais"]}</b></td><td class="num">{p["amplo"]}</td><td class="num">{p["angulo"]}</td>'
                 f'<td class="num {cls}">{p["razao"]}</td><td>{p["idioma"]}</td><td style="color:var(--dim);font-size:13px">{p["leitura"]}</td></tr>')
    seq = "".join(f'<li>{s}</li>' for s in m["sequencia"])
    b = f"""
<header>
<span class="tag">Mercado · qual país e idioma atacar</span>
<h1>Onde tem <em>dinheiro andando</em> e o ângulo ainda está vazio</h1>
<p class="sub">Demografia não decide mercado de drop, dado decide. Medi cada país por dois termos na Ad Library: o amplo (tamanho da categoria) e o do ângulo (concorrência no meu ângulo). A razão ângulo÷amplo aponta o oceano azul.</p>
</header>
<section>
<h2><span class="n">01</span>O método</h2>
<p class="lead">{m["metodo"]}</p>
<div class="tblwrap"><table>
<thead><tr><th>País</th><th>Mercado (amplo)</th><th>Ângulo</th><th>Razão ângulo÷amplo</th><th>Idioma</th><th>Leitura</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<p style="color:var(--dim2);font-size:12.5px;margin-top:10px">Razão <b>baixa</b> (verde) com mercado amplo presente = dinheiro circulando e ninguém no ângulo. Razão <b>alta</b> (vermelho) = ângulo saturado.</p>
</section>
<section>
<h2><span class="n">02</span>Cruzamento com a demanda (Google Trends)</h2>
<div class="grid g3">
<div class="stat"><div class="v sm">Crescente</div><div class="l">"socket extension" (global)</div><div class="d">56 → 64 em 12 meses</div></div>
<div class="stat"><div class="v sm">Crescente</div><div class="l">"wrench extension" (global)</div><div class="d">45 → 56 em 12 meses</div></div>
<div class="stat"><div class="v sm">UK 60</div><div class="l">interesse relativo</div><div class="d">maior entre mercados grandes</div></div>
</div>
<div class="good note"><b>O UK ganha reforço duplo:</b> razão de ângulo baixa (0,57) <b>e</b> o maior interesse de Trends entre mercados grandes (60). É demanda subindo num ângulo quase vazio, em inglês.</div>
</section>
<section>
<h2><span class="n">03</span>A sequência de entrada (mais barato → mais caro)</h2>
<ol class="steps">{seq}</ol>
<div class="info note"><b>Idioma:</b> {m["idioma"]}</div>
</section>
<section>
<h2><span class="n">04</span>Limitações declaradas</h2>
<div class="note">{m["limitacao"]}<br><br><b>Google Trends por país:</b> retornou ruído de baixo volume (Gambia 100), então usei só o sinal global (crescente) + o destaque do UK. A granularidade geográfica fica sustentada na medição de mídia da Ad Library, mais confiável aqui.</div>
</section>
"""
    page("mercados.html", "Mercados · Tight-Space Tools", b)

if __name__ == "__main__":
    build_index()
    build_mercados()
    build_oportunidade()
    build_estrategia()
    build_plano()
    for fname,(slug,key,extra) in LOJAS.items():
        build_loja(fname, slug, key, extra)
    print("\nTODAS AS PAGINAS GERADAS.")
