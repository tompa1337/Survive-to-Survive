"""Genererar art/karaktarer.svg – konceptbild på stammens 6 roller.

Kör:  python art/make_characters.py
Ändra färger/utrustning i ROLES längst ner och kör igen.
"""
from pathlib import Path

W, H = 1800, 980
GROUND = 800


def poly(pts, fill, extra=""):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" {extra}/>'


class Fig:
    """Bygger en lågpolyfigur. (0,0) = mellan fötterna, y uppåt är negativt."""

    def __init__(self, cx, broad=1.0, slim=1.0):
        self.cx, self.parts, self.bx = cx, [], broad * slim

    def t(self, pts):
        return [(self.cx + x, GROUND + y) for x, y in pts]

    def p(self, pts, fill, extra=""):
        self.parts.append(poly(self.t(pts), fill, extra))

    def raw(self, s):
        self.parts.append(s)

    def X(self, x):
        return x * self.bx

    def body(self, skin, tunic, legs, boots, hair, shade="#000"):
        b = self.X
        # ben
        self.p([(-34, -178), (-6, -178), (-10, -26), (-34, -26)], legs)
        self.p([(6, -178), (34, -178), (34, -26), (10, -26)], legs)
        self.p([(-34, -178), (-20, -178), (-22, -26), (-34, -26)], shade, 'opacity=".12"')
        self.p([(-42, -34), (-6, -34), (-2, 0), (-48, 0)], boots)
        self.p([(6, -34), (42, -34), (48, 0), (2, 0)], boots)
        # armar
        self.p([(b(-44), -292), (b(-64), -286), (b(-82), -192), (b(-66), -186)], skin)
        self.p([(b(44), -292), (b(64), -286), (b(82), -192), (b(66), -186)], skin)
        self.raw(f'<circle cx="{self.cx + b(-74):.1f}" cy="{GROUND - 180}" r="12" fill="{skin}"/>')
        self.raw(f'<circle cx="{self.cx + b(74):.1f}" cy="{GROUND - 180}" r="12" fill="{skin}"/>')
        # tunika
        self.p([(b(-48), -302), (b(48), -302), (b(58), -160), (b(42), -132), (b(-42), -132), (b(-58), -160)], tunic)
        self.p([(0, -302), (b(48), -302), (b(58), -160), (b(42), -132), (0, -132)], shade, 'opacity=".16"')
        self.p([(b(-42), -132), (b(-30), -112), (b(-14), -132), (0, -110), (b(14), -132), (b(30), -112), (b(42), -132)], tunic)
        # hals + huvud
        self.p([(-12, -320), (12, -320), (12, -298), (-12, -298)], skin)
        head = [(-30, -372), (30, -372), (37, -342), (27, -312), (0, -302), (-27, -312), (-37, -342)]
        self.p(head, skin)
        self.p([(0, -372), (30, -372), (37, -342), (27, -312), (0, -302)], shade, 'opacity=".13"')
        # ansikte
        for ex in (-12, 12):
            self.raw(f'<ellipse cx="{self.cx + ex}" cy="{GROUND - 344}" rx="4" ry="4.5" fill="#1d130c"/>')
        self.p([(-19, -354), (-5, -352), (-5, -349), (-19, -350)], "#2a1a10")
        self.p([(5, -352), (19, -354), (19, -350), (5, -349)], "#2a1a10")
        self.p([(-2, -342), (4, -330), (-4, -330)], shade, 'opacity=".2"')
        self.p([(-8, -320), (8, -320), (6, -317), (-6, -317)], "#5a2e22")
        # hår
        self.p([(-36, -346), (-33, -382), (-12, -394), (12, -394), (33, -382), (36, -346), (28, -366), (-28, -366)], hair)

    def svg(self):
        return "\n".join(self.parts)


def label(cx, name, role, desc, color):
    y = GROUND + 52
    return f'''
<rect x="{cx - 130}" y="{y - 30}" width="260" height="128" rx="14" fill="#1b120b" opacity=".55"/>
<rect x="{cx - 30}" y="{y - 30}" width="60" height="5" rx="2" fill="{color}"/>
<text x="{cx}" y="{y + 6}" text-anchor="middle" font-size="28" font-weight="700" fill="#f6e7cf">{name}</text>
<text x="{cx}" y="{y + 34}" text-anchor="middle" font-size="16" fill="{color}" letter-spacing="1">{role}</text>
<text x="{cx}" y="{y + 60}" text-anchor="middle" font-size="14" fill="#d9c7aa">{desc[0]}</text>
<text x="{cx}" y="{y + 80}" text-anchor="middle" font-size="14" fill="#d9c7aa">{desc[1]}</text>'''


SKINS = ["#c68a5e", "#e0b08a", "#8d5a3b", "#d79f74", "#6e4429", "#b97a50"]


def jagaren(cx):
    f = Fig(cx)
    # pälskappa bakom
    f.p([(-62, -300), (62, -300), (78, -120), (-78, -120)], "#6d6a66")
    f.body(SKINS[0], "#7a5233", "#5b3d24", "#4a4440", "#3a2416")
    # spjut
    f.p([(70, -40), (78, -40), (78, -470), (70, -470)], "#7b5530")
    f.p([(66, -470), (82, -470), (74, -520)], "#3e3d44")
    f.p([(68, -462), (80, -462), (80, -455), (68, -455)], "#b8a27a")
    # vargskalle-huva
    f.p([(-40, -350), (-36, -392), (-18, -404), (18, -404), (36, -392), (40, -350), (46, -300), (30, -340), (-30, -340), (-46, -300)], "#8a8782")
    f.p([(-30, -396), (-24, -426), (-12, -400)], "#77746f")
    f.p([(30, -396), (24, -426), (12, -400)], "#77746f")
    f.p([(-16, -404), (16, -404), (10, -384), (-10, -384)], "#9a9792")
    # krigsmålning
    for dy in (0, 9):
        f.p([(-28, -336 + dy), (-14, -338 + dy), (-14, -334 + dy), (-28, -332 + dy)], "#b0302a")
        f.p([(14, -338 + dy), (28, -336 + dy), (28, -332 + dy), (14, -334 + dy)], "#b0302a")
    # tandhalsband
    for i in range(-3, 4):
        f.p([(i * 9 - 3, -300), (i * 9 + 3, -300), (i * 9, -288)], "#efe6d2")
    return f.svg()


def samlaren(cx):
    f = Fig(cx, slim=0.95)
    # korg på ryggen (bakom)
    f.p([(-70, -330), (-20, -340), (-14, -170), (-66, -160)], "#a5753e")
    for i in range(6):
        y = -320 + i * 28
        f.p([(-70, y), (-18, y - 6), (-17, y - 2), (-69, y + 4)], "#7d5527")
    f.p([(-60, -350), (-50, -372), (-40, -346)], "#6b8f3a")
    f.p([(-44, -352), (-30, -380), (-26, -346)], "#7fa443")
    f.body(SKINS[1], "#9c8a52", "#6e5a35", "#5a4128", "#b8742e")
    # axelrem
    f.p([(-40, -300), (-30, -300), (36, -150), (26, -150)], "#5a3d1f")
    # grävpinne
    f.p([(70, -60), (77, -60), (82, -330), (75, -330)], "#8a6136")
    f.p([(68, -62), (79, -62), (72, -20)], "#6b4626")
    # hårband med blommor
    f.p([(-36, -360), (36, -360), (36, -354), (-36, -354)], "#c74b3c")
    for x, c in ((-20, "#f2d34a"), (-6, "#f0f0f0"), (10, "#e47fb0")):
        f.raw(f'<circle cx="{cx + x}" cy="{GROUND - 362}" r="6" fill="{c}"/>')
    # flätor
    f.p([(-36, -350), (-28, -350), (-30, -270), (-38, -272)], "#b8742e")
    f.p([(28, -350), (36, -350), (38, -272), (30, -270)], "#b8742e")
    # liten påse med bär
    f.raw(f'<circle cx="{cx + 46}" cy="{GROUND - 150}" r="16" fill="#7c6a3d"/>')
    for dx, dy in ((-5, -6), (5, -4), (0, 3)):
        f.raw(f'<circle cx="{cx + 46 + dx}" cy="{GROUND - 166 + dy}" r="5" fill="#5b2a8c"/>')
    return f.svg()


def byggaren(cx):
    f = Fig(cx, broad=1.28)
    f.body(SKINS[2], "#5f4a36", "#4b3825", "#3b2c1e", "#1d1410")
    # helskägg
    f.p([(-30, -330), (30, -330), (26, -296), (0, -282), (-26, -296)], "#1d1410")
    f.p([(-10, -322), (10, -322), (6, -317), (-6, -317)], "#5a2e22")
    # stock på axeln
    f.p([(-150, -322), (60, -322), (60, -292), (-150, -292)], "#7a5332")
    f.p([(-150, -322), (60, -322), (60, -314), (-150, -314)], "#8d6440")
    f.raw(f'<ellipse cx="{cx - 150}" cy="{GROUND - 307}" rx="9" ry="15" fill="#c9a26b"/>')
    f.raw(f'<ellipse cx="{cx - 150}" cy="{GROUND - 307}" rx="4" ry="7" fill="#a47c48"/>')
    # stenyxa i handen
    f.p([(92, -100), (100, -100), (104, -250), (96, -250)], "#7b5530")
    f.p([(84, -262), (122, -270), (130, -238), (98, -232)], "#85837c")
    f.p([(84, -262), (98, -264), (98, -232)], "#6a6862")
    f.p([(92, -250), (110, -250), (110, -242), (92, -242)], "#b8a27a")
    # armring
    f.p([(-90, -230), (-70, -232), (-70, -224), (-90, -222)], "#b88a3a")
    return f.svg()


def hantverkaren(cx):
    f = Fig(cx)
    f.body(SKINS[3], "#8a6a4a", "#5c4430", "#46352a", "#6b3b1f")
    # förkläde
    f.p([(-32, -230), (32, -230), (38, -120), (-38, -120)], "#b39a74")
    f.raw(f'<circle cx="{cx - 12}" cy="{GROUND - 170}" r="9" fill="#9a6b45" opacity=".6"/>')
    f.raw(f'<circle cx="{cx + 14}" cy="{GROUND - 150}" r="6" fill="#9a6b45" opacity=".6"/>')
    # verktygsbälte
    f.p([(-58, -186), (58, -186), (58, -172), (-58, -172)], "#4a2f1a")
    for x, c in ((-46, "#6e5233"), (40, "#6e5233")):
        f.p([(x - 10, -176), (x + 10, -176), (x + 8, -146), (x - 8, -146)], c)
    f.p([(-6, -186), (6, -186), (2, -150), (-2, -150)], "#2f2f36")  # flintkniv
    # hårknut
    f.raw(f'<circle cx="{cx}" cy="{GROUND - 400}" r="14" fill="#6b3b1f"/>')
    f.p([(-12, -404), (12, -398), (12, -394), (-12, -400)], "#d9c7aa")
    # knacksten + flintkärna
    f.raw(f'<ellipse cx="{cx + 80}" cy="{GROUND - 192}" rx="16" ry="12" fill="#8d8b84"/>')
    f.p([(-92, -200), (-62, -206), (-56, -182), (-84, -172)], "#2f2f36")
    f.p([(-92, -200), (-76, -204), (-80, -182)], "#4a4a55")
    # lerfläckar i ansiktet
    f.raw(f'<ellipse cx="{cx + 20}" cy="{GROUND - 328}" rx="5" ry="3" fill="#9a6b45" opacity=".7"/>')
    return f.svg()


def spejaren(cx):
    f = Fig(cx, slim=0.88)
    f.body(SKINS[4], "#a07a4c", "#7a5a38", "#5e4630", "#151515")
    # kort cape
    f.p([(-46, -302), (46, -302), (30, -256), (-30, -256)], "#5f7a4a")
    # fjädrar
    f.p([(24, -380), (34, -380), (52, -438), (46, -440)], "#e8e2d4")
    f.p([(30, -378), (40, -376), (66, -420), (60, -424)], "#c2462e")
    f.p([(18, -382), (26, -382), (32, -446), (26, -446)], "#2d2d2d")
    # slunga
    f.p([(70, -186), (74, -186), (70, -110), (66, -110)], "#c9b28a")
    f.p([(76, -186), (80, -186), (84, -110), (80, -110)], "#c9b28a")
    f.raw(f'<ellipse cx="{cx + 75}" cy="{GROUND - 104}" rx="12" ry="8" fill="#8a6a44"/>')
    # horn på snöre
    f.p([(-40, -300), (-34, -300), (20, -200), (14, -198)], "#c9b28a")
    f.p([(6, -206), (40, -214), (44, -196), (12, -190)], "#e9dcc0")
    f.p([(36, -216), (46, -218), (48, -194), (40, -194)], "#b49a6c")
    # ränder i ansiktet
    f.p([(-30, -330), (30, -330), (30, -324), (-30, -324)], "#e0d6c0", 'opacity=".75"')
    return f.svg()


def shamanen(cx):
    f = Fig(cx)
    # lång mantel bakom
    f.p([(-60, -304), (60, -304), (80, -14), (-80, -14)], "#3d3550")
    f.body(SKINS[5], "#5a4a6e", "#3d3550", "#2a2433", "#d8d2c4")
    # mantelns framkanter
    f.p([(-50, -300), (-34, -300), (-50, -14), (-80, -14)], "#4a4060")
    f.p([(34, -300), (50, -300), (80, -14), (50, -14)], "#4a4060")
    # stav med skalle
    f.p([(-78, -20), (-70, -20), (-70, -470), (-78, -470)], "#6b4a2a")
    f.p([(-94, -500), (-54, -500), (-50, -478), (-60, -462), (-88, -462), (-98, -478)], "#ece4d2")
    for ex in (-84, -64):
        f.raw(f'<circle cx="{cx + ex}" cy="{GROUND - 484}" r="5" fill="#2a2433"/>')
    f.p([(-82, -468), (-66, -468), (-66, -462), (-82, -462)], "#2a2433")
    f.raw(f'<circle cx="{cx - 74}" cy="{GROUND - 440}" r="5" fill="#59c2b8"/>')
    f.p([(-74, -435), (-70, -435), (-60, -400), (-64, -400)], "#c9b28a")
    # hjorthorn
    for s in (-1, 1):
        f.p([(s * 18, -390), (s * 24, -390), (s * 46, -446), (s * 42, -448)], "#d9c49a")
        f.p([(s * 32, -420), (s * 36, -422), (s * 58, -432), (s * 56, -436)], "#d9c49a")
        f.p([(s * 40, -440), (s * 44, -440), (s * 40, -470), (s * 36, -470)], "#d9c49a")
    # vit ansiktsmålning
    f.p([(-30, -352), (30, -352), (26, -336), (-26, -336)], "#f2ede2", 'opacity=".55"')
    for ex in (-12, 12):
        f.raw(f'<ellipse cx="{cx + ex}" cy="{GROUND - 344}" rx="4" ry="4.5" fill="#1d130c"/>')
    # benhalsband
    for i in range(-3, 4):
        f.p([(i * 10 - 3, -300 + abs(i) * -2), (i * 10 + 3, -300 + abs(i) * -2), (i * 10 + 2, -282), (i * 10 - 2, -282)], "#ece4d2")
    # örtpung
    f.raw(f'<circle cx="{cx + 52}" cy="{GROUND - 160}" r="14" fill="#5e7a3a"/>')
    return f.svg()


ROLES = [
    (jagaren, "Jägaren", "SPJUT · SPÅRAR", ("+skada mot djur", "Vargpäls och krigsmålning"), "#d9473a"),
    (samlaren, "Samlaren", "KORG · ÖRTER", ("Mer bär och rötter", "Hittar sällsynta örter"), "#e3b23c"),
    (byggaren, "Byggaren", "STENYXA · BÄR TUNGT", ("Bygger snabbare", "Kan bära stockar ensam"), "#c9874a"),
    (hantverkaren, "Hantverkaren", "FLINTA · VERKTYG", ("Tillverkar bättre", "verktyg och vapen"), "#b5a07a"),
    (spejaren, "Spejaren", "SLUNGA · HORN", ("Snabbast i stammen", "Markerar fiender åt laget"), "#6fa35a"),
    (shamanen, "Shamanen", "STAV · HELAR", ("Helar laget, ser i mörker", "Läser vädret"), "#59c2b8"),
]


def main():
    slot = W / len(ROLES)
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Trebuchet MS, Segoe UI, sans-serif">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#2b1a33"/><stop offset=".55" stop-color="#a0472c"/><stop offset="1" stop-color="#e59a4a"/>
  </linearGradient>
  <radialGradient id="glow" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#ffb35c" stop-opacity=".55"/><stop offset="1" stop-color="#ffb35c" stop-opacity="0"/>
  </radialGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<polygon points="0,{GROUND - 160} 220,{GROUND - 300} 420,{GROUND - 190} 640,{GROUND - 340} 900,{GROUND - 200} 1150,{GROUND - 320} 1400,{GROUND - 210} 1620,{GROUND - 330} {W},{GROUND - 220} {W},{GROUND} 0,{GROUND}" fill="#4a2a2e" opacity=".55"/>
<polygon points="0,{GROUND - 90} 300,{GROUND - 170} 600,{GROUND - 110} 950,{GROUND - 190} 1300,{GROUND - 100} 1600,{GROUND - 160} {W},{GROUND - 120} {W},{GROUND} 0,{GROUND}" fill="#2e2224" opacity=".7"/>
<polygon points="1560,{GROUND - 260} 1640,{GROUND - 340} 1700,{GROUND - 300} 1800,{GROUND - 360} 1800,{GROUND - 200} 1560,{GROUND - 200}" fill="#dce9f2" opacity=".35"/>
<rect y="{GROUND}" width="{W}" height="{H - GROUND}" fill="#2a1c12"/>
<rect y="{GROUND}" width="{W}" height="6" fill="#4d3a22"/>
<text x="{W / 2}" y="64" text-anchor="middle" font-size="44" font-weight="700" fill="#ffcf8a" letter-spacing="6">SURVIVE TO SURVIVE</text>
<text x="{W / 2}" y="98" text-anchor="middle" font-size="20" fill="#f3dcc0" letter-spacing="3">STAMMEN · 6 ROLLER I CO-OP · KONCEPT v0.1</text>''']
    for i, (fn, name, role, desc, color) in enumerate(ROLES):
        cx = slot * i + slot / 2
        out.append(f'<ellipse cx="{cx}" cy="{GROUND - 220}" rx="150" ry="230" fill="url(#glow)" opacity=".5"/>')
        out.append(f'<ellipse cx="{cx}" cy="{GROUND + 2}" rx="70" ry="10" fill="#000" opacity=".35"/>')
        out.append(f'<g>{fn(cx)}</g>')
        out.append(label(cx, name, role, desc, color))
    out.append("</svg>")
    path = Path(__file__).with_name("karaktarer.svg")
    path.write_text("\n".join(out), encoding="utf-8")
    print("skrev", path)


if __name__ == "__main__":
    main()
