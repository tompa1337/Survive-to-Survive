"""Genererar fyra alternativa karaktärsstilar: art/alternativ_a..d.svg

Kör:  python art/make_alternativ.py
Varje stil visar samma tre roller (Jägaren, Byggaren, Shamanen) så de går att jämföra.
"""
import math
import random
from pathlib import Path

W, H = 1500, 860
XS = (300, 750, 1200)
OUT = Path(__file__).parent


def pts(cx, gy, p):
    return " ".join(f"{cx + x:.1f},{gy + y:.1f}" for x, y in p)


def header(title, sub, color="#fff", subcolor="#ddd", font="Trebuchet MS, Segoe UI, sans-serif"):
    return (f'<text x="{W/2}" y="62" text-anchor="middle" font-family="{font}" font-size="40" font-weight="700" fill="{color}" letter-spacing="2">{title}</text>'
            f'<text x="{W/2}" y="96" text-anchor="middle" font-family="{font}" font-size="18" fill="{subcolor}">{sub}</text>')


def labels(names, gy, color, sub, font="Trebuchet MS, Segoe UI, sans-serif"):
    s = ""
    for cx, (n, r) in zip(XS, names):
        s += (f'<text x="{cx}" y="{gy}" text-anchor="middle" font-family="{font}" font-size="28" font-weight="700" fill="{color}">{n}</text>'
              f'<text x="{cx}" y="{gy + 28}" text-anchor="middle" font-family="{font}" font-size="16" fill="{sub}">{r}</text>')
    return s


def svg(body, path):
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{body}</svg>', encoding="utf-8")
    print("skrev", path)


# ---------------------------------------------------------------- A: söta & runda
def style_a():
    G = 700
    O = 'stroke="#3b2a20" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"'

    def base(cx, skin, tunic, hair, wide=1.0, robe=False):
        s = f'<ellipse cx="{cx}" cy="{G + 6}" rx="{90*wide}" ry="13" fill="#000" opacity=".12"/>'
        if not robe:
            for dx in (-30, 30):
                s += f'<ellipse cx="{cx + dx*wide}" cy="{G - 14}" rx="27" ry="16" fill="#6b4a32" {O}/>'
        w = 124 * wide
        h = 150 if robe else 128
        s += f'<ellipse cx="{cx - 66*wide}" cy="{G - 96}" rx="19" ry="33" fill="{skin}" transform="rotate(22 {cx - 66*wide} {G - 96})" {O}/>'
        s += f'<ellipse cx="{cx + 66*wide}" cy="{G - 96}" rx="19" ry="33" fill="{skin}" transform="rotate(-22 {cx + 66*wide} {G - 96})" {O}/>'
        s += f'<rect x="{cx - w/2}" y="{G - 22 - h + (0 if not robe else 22)}" width="{w}" height="{h}" rx="44" fill="{tunic}" {O}/>'
        s += f'<path d="M{cx - w/2 + 8},{G - 60} L{cx - w/4},{G - 40} L{cx},{G - 60} L{cx + w/4},{G - 40} L{cx + w/2 - 8},{G - 60}" fill="none" stroke="#3b2a20" stroke-width="3" opacity=".35"/>'
        hy = G - 250
        s += f'<circle cx="{cx}" cy="{hy}" r="100" fill="{skin}" {O}/>'
        s += f'<path d="M{cx - 100},{hy} A100,100 0 0 1 {cx + 100},{hy} Q{cx + 64},{hy - 46} {cx + 20},{hy - 34} Q{cx - 10},{hy - 58} {cx - 40},{hy - 36} Q{cx - 70},{hy - 50} {cx - 100},{hy} Z" fill="{hair}" {O}/>'
        for ex in (-36, 36):
            s += f'<ellipse cx="{cx + ex}" cy="{hy + 18}" rx="15" ry="21" fill="#2a1a12"/>'
            s += f'<circle cx="{cx + ex + 5}" cy="{hy + 9}" r="6" fill="#fff"/>'
            s += f'<ellipse cx="{cx + ex*1.65}" cy="{hy + 46}" rx="15" ry="9" fill="#ff7a8a" opacity=".45"/>'
        s += f'<path d="M{cx - 14},{hy + 52} Q{cx},{hy + 66} {cx + 14},{hy + 52}" fill="none" stroke="#3b2a20" stroke-width="5" stroke-linecap="round"/>'
        return s, hy

    # Jägaren
    cx = XS[0]
    s, hy = base(cx, "#f2c29b", "#a8744a", "#5a3720")
    hunter = s
    hunter += f'<line x1="{cx + 92}" y1="{G - 10}" x2="{cx + 92}" y2="{G - 330}" stroke="#8a5a32" stroke-width="12" stroke-linecap="round"/>'
    hunter += f'<polygon points="{pts(cx, G, [(76, -322), (108, -322), (92, -380)])}" fill="#7c8a9a" {O}/>'
    hunter += f'<path d="M{cx - 108},{hy + 8} A108,108 0 0 1 {cx + 108},{hy + 8} L{cx + 92},{hy - 22} Q{cx},{hy - 70} {cx - 92},{hy - 22} Z" fill="#a9b0b8" {O}/>'
    hunter += f'<polygon points="{pts(cx, hy, [(-86, -46), (-62, -128), (-30, -86)])}" fill="#a9b0b8" {O}/>'
    hunter += f'<polygon points="{pts(cx, hy, [(86, -46), (62, -128), (30, -86)])}" fill="#a9b0b8" {O}/>'
    hunter += f'<polygon points="{pts(cx, hy, [(-70, -62), (-62, -108), (-44, -80)])}" fill="#f0b7b7"/>'
    hunter += f'<polygon points="{pts(cx, hy, [(70, -62), (62, -108), (44, -80)])}" fill="#f0b7b7"/>'
    for dy in (34, 46):
        hunter += f'<line x1="{cx - 74}" y1="{hy + dy}" x2="{cx - 52}" y2="{hy + dy - 4}" stroke="#d9473a" stroke-width="5" stroke-linecap="round"/>'
        hunter += f'<line x1="{cx + 52}" y1="{hy + dy - 4}" x2="{cx + 74}" y2="{hy + dy}" stroke="#d9473a" stroke-width="5" stroke-linecap="round"/>'
    # Byggaren
    cx = XS[1]
    s, hy = base(cx, "#b8794e", "#6f8a4a", "#2e1d14", wide=1.25)
    b = s
    b += f'<path d="M{cx - 64},{hy + 40} Q{cx},{hy + 140} {cx + 64},{hy + 40} Q{cx + 30},{hy + 70} {cx},{hy + 62} Q{cx - 30},{hy + 70} {cx - 64},{hy + 40} Z" fill="#2e1d14" {O}/>'
    b += f'<path d="M{cx - 14},{hy + 56} Q{cx},{hy + 66} {cx + 14},{hy + 56}" fill="none" stroke="#f2c29b" stroke-width="4" stroke-linecap="round"/>'
    b += f'<rect x="{cx - 102}" y="{hy - 38}" width="204" height="18" rx="9" fill="#d9a03a" {O}/>'
    b += f'<g transform="rotate(-12 {cx} {G - 150})"><rect x="{cx - 170}" y="{G - 178}" width="250" height="44" rx="22" fill="#9a6a40" {O}/>'
    b += f'<ellipse cx="{cx - 150}" cy="{G - 156}" rx="14" ry="20" fill="#e6c48e" {O}/><ellipse cx="{cx - 150}" cy="{G - 156}" rx="5" ry="8" fill="#b88b55"/></g>'
    # Shamanen
    cx = XS[2]
    s, hy = base(cx, "#d9a27a", "#7a5aa6", "#eeeae0", robe=True)
    sh = s
    for sx in (-1, 1):
        sh += f'<path d="M{cx + sx*40},{hy - 88} Q{cx + sx*70},{hy - 150} {cx + sx*60},{hy - 200} M{cx + sx*56},{hy - 130} Q{cx + sx*100},{hy - 140} {cx + sx*112},{hy - 176} M{cx + sx*64},{hy - 166} Q{cx + sx*30},{hy - 186} {cx + sx*26},{hy - 214}" fill="none" stroke="#3b2a20" stroke-width="16" stroke-linecap="round"/>'
        sh += f'<path d="M{cx + sx*40},{hy - 88} Q{cx + sx*70},{hy - 150} {cx + sx*60},{hy - 200} M{cx + sx*56},{hy - 130} Q{cx + sx*100},{hy - 140} {cx + sx*112},{hy - 176} M{cx + sx*64},{hy - 166} Q{cx + sx*30},{hy - 186} {cx + sx*26},{hy - 214}" fill="none" stroke="#f3dfb5" stroke-width="8" stroke-linecap="round"/>'
    sh += f'<line x1="{cx - 96}" y1="{G}" x2="{cx - 96}" y2="{G - 300}" stroke="#7b5530" stroke-width="12" stroke-linecap="round"/>'
    sh += f'<circle cx="{cx - 96}" cy="{G - 330}" r="32" fill="#fbf6ea" {O}/>'
    for ex in (-108, -84):
        sh += f'<circle cx="{cx + ex}" cy="{G - 332}" r="8" fill="#3b2a20"/>'
    sh += f'<circle cx="{cx - 96}" cy="{G - 286}" r="9" fill="#59c2b8" {O}/>'
    for i in range(-3, 4):
        sh += f'<circle cx="{cx + i*15}" cy="{G - 150 + abs(i)*-3}" r="7" fill="#fbf6ea" {O}/>'
    sh += f'<path d="M{cx - 60},{hy + 10} L{cx + 60},{hy + 10}" stroke="#fff" stroke-width="14" stroke-linecap="round" opacity=".6"/>'

    sparkle = "".join(f'<circle cx="{random.randint(40, W - 40)}" cy="{random.randint(130, 640)}" r="{random.choice((3, 4, 6))}" fill="#fff" opacity=".7"/>' for _ in range(40))
    body = (f'<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bfe6e0"/><stop offset="1" stop-color="#f7ecd2"/></linearGradient></defs>'
            f'<rect width="{W}" height="{H}" fill="url(#bg)"/>{sparkle}'
            f'<path d="M0,{G} Q{W/4},{G - 40} {W/2},{G} T{W},{G} V{H} H0 Z" fill="#9fd08a"/>'
            f'<path d="M0,{G + 20} Q{W/4},{G - 10} {W/2},{G + 20} T{W},{G + 20} V{H} H0 Z" fill="#86c072"/>'
            + header("Alternativ A – Söta &amp; runda", "Stora huvuden, mjuka former, tjocka konturer · Lekfullt och familjevänligt", "#3b2a20", "#5d4a3a")
            + hunter + b + sh
            + labels([("Jägaren", "Vargluva + spjut"), ("Byggaren", "Skägg + stock"), ("Shamanen", "Horn + skallstav")], G + 80, "#3b2a20", "#3f5a33"))
    svg(body, OUT / "alternativ_a.svg")


# ---------------------------------------------------------------- B: mörka & råa
def style_b():
    G = 760
    def figure(cx, extra, broad=1.0):
        b = broad
        parts = [
            [(-32*b, -270), (-8, -270), (-14, 0), (-38*b, 0)],
            [(8, -270), (32*b, -270), (38*b, 0), (14, 0)],
            [(-62*b, -470), (62*b, -470), (54*b, -250), (38*b, -230), (20*b, -252), (0, -226), (-20*b, -252), (-38*b, -230), (-54*b, -250)],
            [(-60*b, -462), (-82*b, -450), (-96*b, -320), (-80*b, -312)],
            [(60*b, -462), (82*b, -450), (96*b, -320), (80*b, -312)],
            [(-14, -500), (14, -500), (14, -470), (-14, -470)],
            [(-21, -560), (21, -560), (25, -522), (12, -496), (-12, -496), (-25, -522)],
            [(-90*b, -480), (-40, -500), (40, -500), (90*b, -480), (100*b, -400), (70*b, -440), (40*b, -405), (10, -445), (-30*b, -400), (-60*b, -445), (-100*b, -398)],
        ] + extra
        return "".join(f'<polygon points="{pts(cx, G, p)}"/>' for p in parts)

    def render(cx, fig_id, shapes):
        return (f'<g id="{fig_id}">{shapes}</g>' if False else '') + \
            f'<g fill="#ff8a3a" transform="translate(6,-3)" opacity=".95">{shapes}</g>' + \
            f'<g fill="#ffd0a0" transform="translate(-3,-2)" opacity=".35">{shapes}</g>' + \
            f'<g fill="#120d0c">{shapes}</g>'

    # Jägaren: vargskalle-mask + långt spjut
    cx = XS[0]
    ex = [[(84, -20), (92, -20), (92, -620), (84, -620)], [(78, -620), (98, -620), (88, -690)],
          [(-30, -560), (-24, -600), (-12, -566)], [(30, -560), (24, -600), (12, -566)]]
    h = render(cx, "h", figure(cx, ex))
    h += f'<polygon points="{pts(cx, G, [(-20, -556), (20, -556), (22, -530), (8, -508), (-8, -508), (-22, -530)])}" fill="#d9d2c0" opacity=".92"/>'
    for e in (-9, 9):
        h += f'<polygon points="{pts(cx, G, [(e - 6, -538), (e + 6, -538), (e, -532)])}" fill="#ff5a2a"/>'
    h += f'<polygon points="{pts(cx, G, [(-4, -526), (4, -526), (0, -516)])}" fill="#120d0c"/>'
    h += f'<path d="M{cx - 20},{G - 420} l14,22 l-14,22 m30,-44 l14,22 l-14,22" stroke="#b0302a" stroke-width="5" fill="none"/>'
    # Byggaren: bred, stor stenklubba
    cx = XS[1]
    ex = [[(-150, -350), (-130, -360), (-60, -320), (-70, -306)],
          [(-200, -330), (-160, -380), (-120, -372), (-130, -318), (-180, -300)]]
    b = render(cx, "b", figure(cx, ex, broad=1.35))
    b += f'<polygon points="{pts(cx, G, [(-200, -330), (-160, -380), (-120, -372), (-130, -318), (-180, -300)])}" fill="#5a5450" opacity=".85"/>'
    b += f'<polygon points="{pts(cx, G, [(-26, -530), (26, -530), (24, -520), (-24, -520)])}" fill="#ff5a2a" opacity=".85"/>'
    b += f'<polygon points="{pts(cx, G, [(-22, -516), (22, -516), (14, -490), (0, -478), (-14, -490)])}" fill="#2b1f1a"/>'
    # Shamanen: höga grenade horn, trasig mantel, stav med eld
    cx = XS[2]
    ex = [[(-112, 0), (-104, 0), (-104, -600), (-112, -600)]]
    for sx in (-1, 1):
        ex += [[(sx*8, -556), (sx*14, -556), (sx*70, -700), (sx*62, -702)],
               [(sx*40, -630), (sx*44, -634), (sx*100, -660), (sx*98, -666)],
               [(sx*56, -670), (sx*60, -672), (sx*50, -740), (sx*46, -738)],
               [(sx*28, -600), (sx*32, -602), (sx*4, -660), (sx*0, -656)]]
    ex += [[(-80, -470), (80, -470), (110, -40), (60, -90), (30, -20), (0, -80), (-30, -20), (-60, -90), (-110, -40)]]
    s = render(cx, "s", figure(cx, ex))
    s += f'<circle cx="{cx - 108}" cy="{G - 620}" r="26" fill="#59c2b8" opacity=".25"/><circle cx="{cx - 108}" cy="{G - 620}" r="12" fill="#bff7ef"/>'
    s += f'<polygon points="{pts(cx, G, [(-21, -548), (21, -548), (24, -522), (0, -500), (-24, -522)])}" fill="#ebe4d4"/>'
    for e in (-9, 9):
        s += f'<circle cx="{cx + e}" cy="{G - 532}" r="4.5" fill="#59c2b8"/>'
    for i in range(-4, 5):
        s += f'<polygon points="{pts(cx, G, [(i*12 - 3, -470), (i*12 + 3, -470), (i*12, -450 + abs(i)*3)])}" fill="#ebe4d4" opacity=".9"/>'

    trees = ""
    rnd = random.Random(3)
    for i in range(30):
        x = rnd.randint(0, W); hgt = rnd.randint(120, 300)
        trees += f'<polygon points="{x - hgt*0.18},{G} {x},{G - hgt} {x + hgt*0.18},{G}" fill="#1d1a22" opacity=".9"/>'
    body = (f'<defs><radialGradient id="glow" cx=".5" cy="1" r=".8"><stop offset="0" stop-color="#ff7a2a" stop-opacity=".55"/><stop offset="1" stop-color="#ff7a2a" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#07070c"/><stop offset="1" stop-color="#2b2230"/></linearGradient></defs>'
            f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
            f'<circle cx="1180" cy="230" r="120" fill="#e8e4da" opacity=".85"/><circle cx="1180" cy="230" r="190" fill="#e8e4da" opacity=".06"/>'
            f'{trees}<rect y="{G - 120}" width="{W}" height="120" fill="#4a4050" opacity=".35"/>'
            f'<rect width="{W}" height="{H}" fill="url(#glow)"/>'
            f'<rect y="{G}" width="{W}" height="{H - G}" fill="#0b0909"/>'
            + header("Alternativ B – Mörka &amp; råa", "Realistiska proportioner, siluetter i eldsken, masker · Spänning och skräck à la Far Cry Primal", "#ffd0a0", "#b8a090")
            + "".join(f'<g transform="translate({x},{G}) scale(.78) translate({-x},{-G})">{part}</g>' for x, part in zip(XS, (h, b, s)))
            + labels([("Jägaren", "Vargskallemask, 2 m spjut"), ("Byggaren", "Stenklubba, björnkraft"), ("Shamanen", "Hjorthorn, andlig stav")], G + 50, "#ffd0a0", "#a08070"))
    svg(body, OUT / "alternativ_b.svg")


# ---------------------------------------------------------------- C: grottmålning
def style_c():
    rnd = random.Random(7)
    RED, BLK, OCH = "#8e2f1c", "#2a1d16", "#b5651d"
    G = 690
    L = 'stroke-linecap="round" stroke-linejoin="round" fill="none"'

    def stroke(d, c=RED, w=14):
        return f'<path d="{d}" stroke="{c}" stroke-width="{w}" {L}/>'

    # bakgrund: sten
    bg = f'<rect width="{W}" height="{H}" fill="#cfa679"/>'
    for _ in range(140):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        c = rnd.choice(("#b98c5e", "#ddb98d", "#c49a6c", "#a87c50"))
        bg += f'<ellipse cx="{x}" cy="{y}" rx="{rnd.randint(30, 160)}" ry="{rnd.randint(14, 70)}" fill="{c}" opacity="{rnd.uniform(.15, .45):.2f}" transform="rotate({rnd.randint(-30, 30)} {x} {y})"/>'
    for _ in range(18):
        x = rnd.randint(0, W); y = rnd.randint(0, H)
        bg += f'<path d="M{x},{y} q{rnd.randint(-60, 60)},{rnd.randint(20, 80)} {rnd.randint(-40, 40)},{rnd.randint(80, 200)}" stroke="#8c6a48" stroke-width="2" fill="none" opacity=".45"/>'

    def hand(x, y, rot, c=RED, op=.35):
        h = f'<g transform="translate({x},{y}) rotate({rot})" opacity="{op}" fill="{c}"><ellipse cx="0" cy="0" rx="30" ry="34"/>'
        for fx, fy, r in ((-26, -48, -18), (-10, -62, -6), (6, -64, 4), (22, -56, 14), (36, -16, 50)):
            h += f'<ellipse cx="{fx}" cy="{fy}" rx="8" ry="24" transform="rotate({r} {fx} {fy})"/>'
        return h + "</g>"

    deco = hand(120, 200, -10) + hand(1390, 260, 20, BLK, .22) + hand(1330, 560, -25) + hand(80, 560, 15, BLK, .18)
    # mammut
    mx, my = 920, 560
    deco += stroke(f"M{mx},{my} q60,-70 150,-40 q40,20 40,70 l0,60 m-30,-60 l0,60 m-110,-60 l0,60 m-30,-50 l0,50 "
                   f"M{mx},{my} q-30,30 -20,80 m10,-60 q-30,10 -50,-10", BLK, 8)
    deco += stroke(f"M{mx + 8},{my + 22} q-40,40 -10,50", "#f0e2c8", 6)
    # prickrader

    # Jägaren – kastar spjut
    cx = XS[0]
    h = f'<circle cx="{cx - 10}" cy="{G - 380}" r="26" fill="{RED}"/>'
    h += f'<polygon points="{pts(cx, G, [(-40, -350), (30, -350), (-6, -200)])}" fill="{RED}"/>'
    h += stroke(f"M{cx - 6},{G - 210} L{cx - 70},{G - 110} L{cx - 110},{G - 20} M{cx - 6},{G - 210} L{cx + 50},{G - 110} L{cx + 110},{G - 50}")
    h += stroke(f"M{cx + 20},{G - 340} L{cx + 70},{G - 420} L{cx + 50},{G - 480} M{cx - 30},{G - 330} L{cx - 90},{G - 270}")
    h += stroke(f"M{cx - 60},{G - 300} L{cx + 120},{G - 540}", BLK, 8)
    h += f'<polygon points="{cx + 120},{G - 540} {cx + 106},{G - 512} {cx + 136},{G - 518}" fill="{BLK}"/>'
    h += stroke(f"M{cx - 30},{G - 404} l-14,-28 m34,22 l6,-30", RED, 8)
    # Byggaren – bär stock över huvudet
    cx = XS[1]
    b = f'<circle cx="{cx}" cy="{G - 360}" r="28" fill="{BLK}"/>'
    b += f'<polygon points="{pts(cx, G, [(-62, -330), (62, -330), (40, -190), (-40, -190)])}" fill="{BLK}"/>'
    b += stroke(f"M{cx - 30},{G - 196} L{cx - 80},{G - 100} L{cx - 90},{G - 10} M{cx + 30},{G - 196} L{cx + 80},{G - 100} L{cx + 90},{G - 10}", BLK)
    b += stroke(f"M{cx - 56},{G - 320} L{cx - 100},{G - 400} L{cx - 90},{G - 450} M{cx + 56},{G - 320} L{cx + 100},{G - 400} L{cx + 90},{G - 450}", BLK)
    b += stroke(f"M{cx - 210},{G - 462} L{cx + 210},{G - 462}", RED, 34)
    b += f'<circle cx="{cx - 210}" cy="{G - 462}" r="17" fill="none" stroke="{BLK}" stroke-width="5"/>'
    for i in range(-4, 5, 2):
        b += f'<circle cx="{cx + i*12}" cy="{G - 270}" r="5" fill="{OCH}"/>'
    # Shamanen – dansar med horn
    cx = XS[2]
    s = f'<circle cx="{cx}" cy="{G - 380}" r="26" fill="{RED}"/>'
    s += stroke(f"M{cx - 12},{G - 402} L{cx - 50},{G - 470} L{cx - 60},{G - 520} M{cx - 34},{G - 440} L{cx - 80},{G - 456} M{cx - 52},{G - 494} L{cx - 30},{G - 520} "
                f"M{cx + 12},{G - 402} L{cx + 50},{G - 470} L{cx + 60},{G - 520} M{cx + 34},{G - 440} L{cx + 80},{G - 456} M{cx + 52},{G - 494} L{cx + 30},{G - 520}", BLK, 9)
    s += f'<path d="M{cx - 44},{G - 352} L{cx + 44},{G - 352} L{cx + 80},{G - 170} L{cx - 80},{G - 170} Z" fill="{RED}"/>'
    for r in range(4):
        for i in range(-3, 4):
            s += f'<circle cx="{cx + i*18 + (r % 2)*9}" cy="{G - 320 + r*36}" r="4.5" fill="#f0e2c8" opacity=".8"/>'
    s += stroke(f"M{cx - 30},{G - 176} L{cx - 70},{G - 90} L{cx - 50},{G - 10} M{cx + 30},{G - 176} L{cx + 90},{G - 110} L{cx + 130},{G - 70}")
    s += stroke(f"M{cx - 40},{G - 340} L{cx - 110},{G - 390} L{cx - 130},{G - 470} M{cx + 40},{G - 340} L{cx + 110},{G - 390} L{cx + 140},{G - 460}")

    font = "Georgia, 'Times New Roman', serif"
    body = (bg + deco
            + header("Alternativ C – Grottmålning", "Platta figurer i ockra och kol, som målade på grottväggen · Unik konststil, billig att producera", BLK, "#4a3424", font)
            + h + b + s
            + labels([("Jägaren", "i kastögonblicket"), ("Byggaren", "bär stammens timmer"), ("Shamanen", "dansar fram andarna")], G + 70, BLK, "#5a2a1a", font))
    svg(body, OUT / "alternativ_c.svg")


# ---------------------------------------------------------------- D: djurstammen
def style_d():
    G = 720

    def body(cx, fur, tunic, broad=1.0, belly=None):
        b = broad
        s = f'<ellipse cx="{cx}" cy="{G + 4}" rx="{80*b}" ry="12" fill="#000" opacity=".2"/>'
        s += f'<polygon points="{pts(cx, G, [(-40*b, -190), (-8, -190), (-12, -30), (-44*b, -30)])}" fill="{fur}"/>'
        s += f'<polygon points="{pts(cx, G, [(8, -190), (40*b, -190), (44*b, -30), (12, -30)])}" fill="{fur}"/>'
        s += f'<polygon points="{pts(cx, G, [(-50*b, -36), (-6, -36), (-2, 0), (-58*b, 0)])}" fill="#3a2a20"/>'
        s += f'<polygon points="{pts(cx, G, [(6, -36), (50*b, -36), (58*b, 0), (2, 0)])}" fill="#3a2a20"/>'
        s += f'<polygon points="{pts(cx, G, [(-56*b, -320), (-78*b, -312), (-96*b, -200), (-78*b, -194)])}" fill="{fur}"/>'
        s += f'<polygon points="{pts(cx, G, [(56*b, -320), (78*b, -312), (96*b, -200), (78*b, -194)])}" fill="{fur}"/>'
        s += f'<circle cx="{cx - 88*b}" cy="{G - 188}" r="14" fill="{fur}"/><circle cx="{cx + 88*b}" cy="{G - 188}" r="14" fill="{fur}"/>'
        s += f'<polygon points="{pts(cx, G, [(-60*b, -330), (60*b, -330), (70*b, -170), (-70*b, -170)])}" fill="{fur}"/>'
        if belly:
            s += f'<ellipse cx="{cx}" cy="{G - 250}" rx="{40*b}" ry="70" fill="{belly}"/>'
        s += f'<polygon points="{pts(cx, G, [(-70*b, -210), (70*b, -210), (74*b, -150), (50*b, -130), (25*b, -152), (0, -126), (-25*b, -152), (-50*b, -130), (-74*b, -150)])}" fill="{tunic}"/>'
        s += f'<polygon points="{pts(cx, G, [(-70*b, -214), (70*b, -214), (70*b, -200), (-70*b, -200)])}" fill="#4a2f1a"/>'
        return s

    # Vargen – jägaren
    cx = XS[0]
    w = body(cx, "#8d939c", "#8a5a34", belly="#c9ccd1")
    w += f'<polygon points="{pts(cx, G, [(-60, -330), (60, -330), (40, -300), (-40, -300)])}" fill="#6b4a2e"/>'
    hy = G - 400
    w += f'<polygon points="{pts(cx, hy, [(-58, -40), (-46, -112), (-14, -60)])}" fill="#7a8089"/><polygon points="{pts(cx, hy, [(-48, -50), (-42, -94), (-24, -62)])}" fill="#e8b4b4"/>'
    w += f'<polygon points="{pts(cx, hy, [(58, -40), (46, -112), (14, -60)])}" fill="#7a8089"/><polygon points="{pts(cx, hy, [(48, -50), (42, -94), (24, -62)])}" fill="#e8b4b4"/>'
    w += f'<polygon points="{pts(cx, hy, [(-62, -40), (0, -70), (62, -40), (70, 10), (40, 50), (0, 80), (-40, 50), (-70, 10)])}" fill="#8d939c"/>'
    w += f'<polygon points="{pts(cx, hy, [(-28, 6), (28, 6), (20, 60), (0, 82), (-20, 60)])}" fill="#e3e5e8"/>'
    w += f'<polygon points="{pts(cx, hy, [(-12, 48), (12, 48), (0, 62)])}" fill="#1a1a1a"/>'
    for ex in (-26, 26):
        w += f'<polygon points="{pts(cx, hy, [(ex - 13, -4), (ex + 13, -8), (ex + 9, 6), (ex - 11, 6)])}" fill="#f2c12e"/><circle cx="{cx + ex}" cy="{hy}" r="4" fill="#111"/>'
    w += f'<polygon points="{pts(cx, hy, [(-62, 20), (-90, 40), (-60, 44)])}" fill="#8d939c"/><polygon points="{pts(cx, hy, [(62, 20), (90, 40), (60, 44)])}" fill="#8d939c"/>'
    w += f'<rect x="{cx + 92}" y="{G - 560}" width="9" height="540" fill="#7b5530"/><polygon points="{pts(cx, G, [(86, -560), (107, -560), (96.5, -620)])}" fill="#3e3d44"/>'
    w += f'<polygon points="{pts(cx, G, [(86, -556), (107, -556), (107, -546), (86, -546)])}" fill="#c43b2e"/>'
    # Björnen – byggaren
    cx = XS[1]
    br = body(cx, "#7a4f2e", "#5f7a4a", broad=1.4, belly="#a87a52")
    hy = G - 395
    br += f'<circle cx="{cx - 56}" cy="{hy - 48}" r="24" fill="#7a4f2e"/><circle cx="{cx - 56}" cy="{hy - 48}" r="12" fill="#5a3820"/>'
    br += f'<circle cx="{cx + 56}" cy="{hy - 48}" r="24" fill="#7a4f2e"/><circle cx="{cx + 56}" cy="{hy - 48}" r="12" fill="#5a3820"/>'
    br += f'<ellipse cx="{cx}" cy="{hy}" rx="76" ry="70" fill="#7a4f2e"/>'
    br += f'<ellipse cx="{cx}" cy="{hy + 28}" rx="36" ry="28" fill="#c49a6c"/><ellipse cx="{cx}" cy="{hy + 16}" rx="14" ry="10" fill="#1a1210"/>'
    br += f'<path d="M{cx},{hy + 26} v12 m-12,6 q12,8 24,0" stroke="#1a1210" stroke-width="4" fill="none" stroke-linecap="round"/>'
    for ex in (-30, 30):
        br += f'<circle cx="{cx + ex}" cy="{hy - 12}" r="8" fill="#1a1210"/><circle cx="{cx + ex + 3}" cy="{hy - 15}" r="2.5" fill="#fff"/>'
    br += f'<polygon points="{pts(cx, hy, [(-76, -16), (76, -16), (76, -2), (-76, -2)])}" fill="#d9a03a" opacity=".9"/>'
    br += f'<polygon points="{pts(cx, G, [(70, -380), (160, -400), (210, -330), (180, -260), (100, -250), (60, -300)])}" fill="#8f8c86"/>'
    br += f'<polygon points="{pts(cx, G, [(70, -380), (160, -400), (140, -330), (60, -300)])}" fill="#a8a59e"/>'
    # Ugglan – shamanen
    cx = XS[2]
    ow = f'<ellipse cx="{cx}" cy="{G + 4}" rx="80" ry="12" fill="#000" opacity=".2"/>'
    ow += f'<polygon points="{pts(cx, G, [(-30, -60), (-8, -60), (-14, -10), (-36, -10)])}" fill="#d9a03a"/><polygon points="{pts(cx, G, [(8, -60), (30, -60), (36, -10), (14, -10)])}" fill="#d9a03a"/>'
    for dx in (-44, -24, 12, 32):
        ow += f'<polygon points="{pts(cx, G, [(dx, -12), (dx + 6, 0), (dx + 12, -12)])}" fill="#3a2a20"/>'
    ow += f'<path d="M{cx - 90},{G - 60} Q{cx - 110},{G - 330} {cx},{G - 380} Q{cx + 110},{G - 330} {cx + 90},{G - 60} Z" fill="#8a6a4a"/>'
    ow += f'<ellipse cx="{cx}" cy="{G - 190}" rx="60" ry="110" fill="#d8c7a6"/>'
    for r in range(5):
        for i in range(-2, 3):
            ow += f'<path d="M{cx + i*22 - 8},{G - 270 + r*34} q8,10 16,0" stroke="#8a6a4a" stroke-width="4" fill="none"/>'
    ow += f'<path d="M{cx - 92},{G - 300} Q{cx - 170},{G - 220} {cx - 140},{G - 80} L{cx - 120},{G - 120} L{cx - 110},{G - 70} L{cx - 92},{G - 120} Z" fill="#5a4a70"/>'
    ow += f'<path d="M{cx + 92},{G - 300} Q{cx + 170},{G - 220} {cx + 140},{G - 80} L{cx + 120},{G - 120} L{cx + 110},{G - 70} L{cx + 92},{G - 120} Z" fill="#5a4a70"/>'
    hy = G - 420
    ow += f'<polygon points="{pts(cx, hy, [(-70, -40), (-60, -100), (-30, -54)])}" fill="#6e5236"/><polygon points="{pts(cx, hy, [(70, -40), (60, -100), (30, -54)])}" fill="#6e5236"/>'
    ow += f'<ellipse cx="{cx}" cy="{hy}" rx="86" ry="74" fill="#8a6a4a"/>'
    for ex in (-36, 36):
        ow += f'<circle cx="{cx + ex}" cy="{hy}" r="38" fill="#efe2c4"/><circle cx="{cx + ex}" cy="{hy}" r="22" fill="#f29a2e"/><circle cx="{cx + ex}" cy="{hy}" r="11" fill="#111"/><circle cx="{cx + ex + 5}" cy="{hy - 5}" r="4" fill="#fff"/>'
    ow += f'<polygon points="{pts(cx, hy, [(-10, 24), (10, 24), (0, 50)])}" fill="#3a2a20"/>'
    for i in range(-3, 4):
        ow += f'<circle cx="{cx + i*15}" cy="{G - 340 + abs(i)*-4}" r="6" fill="#59c2b8"/>'
    ow += f'<rect x="{cx - 168}" y="{G - 520}" width="10" height="510" fill="#6b4a2a"/>'
    ow += f'<polygon points="{pts(cx, G, [(-163, -600), (-140, -540), (-163, -510), (-186, -540)])}" fill="#59c2b8"/><polygon points="{pts(cx, G, [(-163, -600), (-140, -540), (-163, -540)])}" fill="#a8eee6"/>'
    ow += f'<circle cx="{cx - 163}" cy="{G - 550}" r="46" fill="#59c2b8" opacity=".18"/>'

    jungle = ""
    rnd = random.Random(11)
    for _ in range(16):
        x = rnd.randint(0, W); r = rnd.randint(60, 140)
        jungle += f'<circle cx="{x}" cy="{G - rnd.randint(140, 380)}" r="{r}" fill="#2f5d3a" opacity=".55"/>'
    for _ in range(14):
        x = rnd.randint(0, W)
        jungle += f'<rect x="{x}" y="{G - 400}" width="{rnd.randint(16, 30)}" height="400" fill="#3b2a20" opacity=".55"/>'
    bodyy = (f'<defs><linearGradient id="bgd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f5d78a"/><stop offset="1" stop-color="#7fb06a"/></linearGradient></defs>'
             f'<rect width="{W}" height="{H}" fill="url(#bgd)"/>{jungle}'
             f'<rect y="{G}" width="{W}" height="{H - G}" fill="#4a6b32"/>'
             + header("Alternativ D – Djurstammen", "Varje roll är ett djur med stenåldersutrustning · Lätt att känna igen, stark identitet", "#2a1d16", "#3a3020")
             + w + br + ow
             + labels([("Vargen", "Jägaren"), ("Björnen", "Byggaren"), ("Ugglan", "Shamanen")], G + 70, "#f6efd8", "#d8e8c0"))
    svg(bodyy, OUT / "alternativ_d.svg")


if __name__ == "__main__":
    random.seed(5)
    style_a(); style_b(); style_c(); style_d()
