"""Genererar art/grottmalning_roller.svg – alla 6 roller i grottmålningsstil.

Stilen används för menyer, rollval, karta och laddningsskärmar.
Lågpolystilen (art/karaktarer.svg) används för karaktärerna i själva spelet.
Kör:  python art/make_grottmalning.py
"""
import random
from pathlib import Path

W, H = 1800, 900
G = 700
RED, BLK, OCH, CREAM = "#8e2f1c", "#2a1d16", "#b5651d", "#f0e2c8"
L = 'stroke-linecap="round" stroke-linejoin="round" fill="none"'
FONT = "Georgia, 'Times New Roman', serif"
XS = [150 + i * 300 for i in range(6)]


def st(d, c=RED, w=14):
    return f'<path d="{d}" stroke="{c}" stroke-width="{w}" {L}/>'


def poly(cx, p, c):
    return f'<polygon points="{" ".join(f"{cx + x},{G + y}" for x, y in p)}" fill="{c}"/>'


def circ(x, y, r, c, extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {extra}/>'


def jagaren(cx):
    s = circ(cx - 10, G - 380, 26, RED)
    s += poly(cx, [(-40, -350), (30, -350), (-6, -200)], RED)
    s += st(f"M{cx - 6},{G - 210} L{cx - 70},{G - 110} L{cx - 110},{G - 20} M{cx - 6},{G - 210} L{cx + 50},{G - 110} L{cx + 110},{G - 50}")
    s += st(f"M{cx + 20},{G - 340} L{cx + 70},{G - 420} L{cx + 50},{G - 480} M{cx - 30},{G - 330} L{cx - 90},{G - 270}")
    s += st(f"M{cx - 60},{G - 300} L{cx + 110},{G - 530}", BLK, 8)
    s += f'<polygon points="{cx + 110},{G - 530} {cx + 96},{G - 502} {cx + 126},{G - 508}" fill="{BLK}"/>'
    s += st(f"M{cx - 30},{G - 404} l-14,-28 m34,22 l6,-30", RED, 8)
    return s


def samlaren(cx):
    # böjer sig fram och plockar, korg på ryggen
    s = circ(cx + 40, G - 300, 24, OCH)
    s += poly(cx, [(-60, -330), (30, -300), (10, -220), (-50, -230)], OCH)
    s += st(f"M{cx - 30},{G - 228} L{cx - 50},{G - 120} L{cx - 60},{G - 20} M{cx - 10},{G - 226} L{cx + 20},{G - 120} L{cx + 30},{G - 20}", OCH)
    s += st(f"M{cx + 20},{G - 290} L{cx + 70},{G - 200} L{cx + 90},{G - 120}", OCH)
    # korg
    s += f'<path d="M{cx - 110},{G - 400} L{cx - 30},{G - 380} L{cx - 50},{G - 300} L{cx - 110},{G - 310} Z" fill="none" stroke="{BLK}" stroke-width="8" stroke-linejoin="round"/>'
    for i in range(3):
        s += st(f"M{cx - 106 + i*4},{G - 375 + i*24} L{cx - 40 - i*4},{G - 360 + i*24}", BLK, 4)
    # bär och plantor
    for dx, dy in ((80, -100), (100, -84), (88, -70), (112, -110)):
        s += circ(cx + dx, G + dy, 7, BLK)
    s += st(f"M{cx + 90},{G - 10} L{cx + 96},{G - 80} M{cx + 96},{G - 60} l18,-14 m-20,40 l-16,-12", BLK, 6)
    return s


def byggaren(cx):
    s = circ(cx, G - 360, 28, BLK)
    s += poly(cx, [(-62, -330), (62, -330), (40, -190), (-40, -190)], BLK)
    s += st(f"M{cx - 30},{G - 196} L{cx - 80},{G - 100} L{cx - 90},{G - 10} M{cx + 30},{G - 196} L{cx + 80},{G - 100} L{cx + 90},{G - 10}", BLK)
    s += st(f"M{cx - 56},{G - 320} L{cx - 100},{G - 400} L{cx - 90},{G - 450} M{cx + 56},{G - 320} L{cx + 100},{G - 400} L{cx + 90},{G - 450}", BLK)
    s += st(f"M{cx - 140},{G - 462} L{cx + 140},{G - 462}", RED, 34)
    s += f'<circle cx="{cx - 140}" cy="{G - 462}" r="17" fill="none" stroke="{BLK}" stroke-width="5"/>'
    for i in range(-4, 5, 2):
        s += circ(cx + i * 12, G - 270, 5, OCH)
    return s


def hantverkaren(cx):
    # sitter på knä och knackar flinta
    s = circ(cx - 20, G - 300, 26, RED)
    s += poly(cx, [(-60, -272), (20, -272), (10, -130), (-50, -130)], RED)
    s += st(f"M{cx - 40},{G - 136} L{cx - 90},{G - 60} L{cx - 20},{G - 20} M{cx},{G - 136} L{cx + 40},{G - 60} L{cx + 10},{G - 16}")
    s += st(f"M{cx + 10},{G - 260} L{cx + 60},{G - 220} L{cx + 80},{G - 280}")
    s += st(f"M{cx - 50},{G - 250} L{cx + 10},{G - 180} L{cx + 70},{G - 150}")
    s += f'<ellipse cx="{cx + 84}" cy="{G - 292}" rx="20" ry="14" fill="{BLK}"/>'
    s += poly(cx, [(60, -160), (110, -170), (100, -130), (70, -126)], BLK)
    for dx, dy in ((96, -200), (120, -190), (110, -220), (130, -214)):
        s += st(f"M{cx + dx},{G + dy} l8,-8", BLK, 4)
    # färdiga verktyg på marken
    s += poly(cx, [(70, -10), (130, -16), (110, 0)], BLK)
    s += poly(cx, [(-120, -6), (-80, -20), (-70, 0)], BLK)
    return s


def spejaren(cx):
    # springer med slunga över huvudet, fjäder i håret
    s = circ(cx + 20, G - 400, 22, BLK)
    s += st(f"M{cx + 26},{G - 420} q10,-40 30,-60", RED, 6)
    s += st(f"M{cx + 18},{G - 380} L{cx},{G - 240}", BLK, 22)
    s += st(f"M{cx},{G - 250} L{cx - 80},{G - 170} L{cx - 140},{G - 190} M{cx},{G - 250} L{cx + 60},{G - 150} L{cx + 50},{G - 40}", BLK)
    s += st(f"M{cx + 10},{G - 360} L{cx + 80},{G - 330} L{cx + 120},{G - 380} M{cx + 6},{G - 350} L{cx - 60},{G - 300} L{cx - 110},{G - 320}", BLK)
    s += f'<ellipse cx="{cx + 130}" cy="{G - 470}" rx="70" ry="22" fill="none" stroke="{RED}" stroke-width="5" stroke-dasharray="10 10"/>'
    s += st(f"M{cx + 120},{G - 380} L{cx + 160},{G - 450}", RED, 5)
    s += circ(cx + 166, G - 460, 9, RED)
    for i in range(4):
        s += st(f"M{cx - 140 - i*30},{G - 40 - i*4} l-16,0", BLK, 5)
    return s


def shamanen(cx):
    s = circ(cx, G - 380, 26, RED)
    s += st(f"M{cx - 12},{G - 402} L{cx - 50},{G - 470} L{cx - 60},{G - 520} M{cx - 34},{G - 440} L{cx - 80},{G - 456} M{cx - 52},{G - 494} L{cx - 30},{G - 520} "
            f"M{cx + 12},{G - 402} L{cx + 50},{G - 470} L{cx + 60},{G - 520} M{cx + 34},{G - 440} L{cx + 80},{G - 456} M{cx + 52},{G - 494} L{cx + 30},{G - 520}", BLK, 9)
    s += f'<path d="M{cx - 44},{G - 352} L{cx + 44},{G - 352} L{cx + 80},{G - 170} L{cx - 80},{G - 170} Z" fill="{RED}"/>'
    for r in range(4):
        for i in range(-3, 4):
            s += circ(cx + i * 18 + (r % 2) * 9, G - 320 + r * 36, 4.5, CREAM, 'opacity=".8"')
    s += st(f"M{cx - 30},{G - 176} L{cx - 70},{G - 90} L{cx - 50},{G - 10} M{cx + 30},{G - 176} L{cx + 90},{G - 110} L{cx + 130},{G - 70}")
    s += st(f"M{cx - 40},{G - 340} L{cx - 110},{G - 390} L{cx - 130},{G - 470} M{cx + 40},{G - 340} L{cx + 110},{G - 390} L{cx + 130},{G - 460}")
    return s


ROLES = [(jagaren, "Jägaren", "i kastögonblicket"), (samlaren, "Samlaren", "plockar bär och örter"),
         (byggaren, "Byggaren", "bär stammens timmer"), (hantverkaren, "Hantverkaren", "knackar flinta"),
         (spejaren, "Spejaren", "springer före stammen"), (shamanen, "Shamanen", "dansar fram andarna")]


def hand(x, y, rot, c=RED, op=.35):
    h = f'<g transform="translate({x},{y}) rotate({rot})" opacity="{op}" fill="{c}"><ellipse cx="0" cy="0" rx="30" ry="34"/>'
    for fx, fy, r in ((-26, -48, -18), (-10, -62, -6), (6, -64, 4), (22, -56, 14), (36, -16, 50)):
        h += f'<ellipse cx="{fx}" cy="{fy}" rx="8" ry="24" transform="rotate({r} {fx} {fy})"/>'
    return h + "</g>"


def main():
    rnd = random.Random(7)
    out = f'<rect width="{W}" height="{H}" fill="#cfa679"/>'
    for _ in range(170):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        c = rnd.choice(("#b98c5e", "#ddb98d", "#c49a6c", "#a87c50"))
        out += f'<ellipse cx="{x}" cy="{y}" rx="{rnd.randint(30, 160)}" ry="{rnd.randint(14, 70)}" fill="{c}" opacity="{rnd.uniform(.15, .45):.2f}" transform="rotate({rnd.randint(-30, 30)} {x} {y})"/>'
    for _ in range(22):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        out += f'<path d="M{x},{y} q{rnd.randint(-60, 60)},{rnd.randint(20, 80)} {rnd.randint(-40, 40)},{rnd.randint(80, 200)}" stroke="#8c6a48" stroke-width="2" fill="none" opacity=".45"/>'
    out += hand(70, 210, -10) + hand(1740, 230, 20, BLK, .22) + hand(1750, 600, -25, RED, .3) + hand(60, 620, 15, BLK, .18)
    out += (f'<text x="{W/2}" y="64" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="700" fill="{BLK}" letter-spacing="3">SURVIVE TO SURVIVE</text>'
            f'<text x="{W/2}" y="100" text-anchor="middle" font-family="{FONT}" font-size="20" fill="#4a3424">Stammen – målad på grottväggen · för menyer, rollval och laddningsskärmar</text>')
    for cx, (fn, name, sub) in zip(XS, ROLES):
        out += f'<g transform="translate({cx},{G}) scale(.8) translate({-cx},{-G})">{fn(cx)}</g>'
        out += (f'<text x="{cx}" y="{G + 80}" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="{BLK}">{name}</text>'
                f'<text x="{cx}" y="{G + 110}" text-anchor="middle" font-family="{FONT}" font-size="17" fill="#5a2a1a">{sub}</text>')
    path = Path(__file__).with_name("grottmalning_roller.svg")
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{out}</svg>', encoding="utf-8")
    print("skrev", path)


if __name__ == "__main__":
    main()
