"""Genererar art/grottmalning_roller.svg – alla 6 roller i grottmålningsstil (spelets stil).

Varje roll skiljer sig åt på fyra sätt så den känns igen direkt, även på avstånd:
  färg · kroppsform · siluett (huvudbonad/utrustning) · symbol
Kör:  python art/make_grottmalning.py
"""
import math
import random
from pathlib import Path

W, H = 1800, 920
G = 640
RED, YEL, BLK, WHT, BRN = "#9a321e", "#c98a1f", "#231812", "#f3e8cf", "#6b3f22"
L = 'stroke-linecap="round" stroke-linejoin="round" fill="none"'
FONT = "Georgia, 'Times New Roman', serif"
XS = [150 + i * 300 for i in range(6)]


def st(d, c, w=14):
    return f'<path d="{d}" stroke="{c}" stroke-width="{w}" {L}/>'


def ost(d, w=12):
    """Vit linje med svart kontur (Hantverkarens kritvita stil)."""
    return st(d, BLK, w + 8) + st(d, WHT, w)


def poly(cx, p, c, extra=""):
    return f'<polygon points="{" ".join(f"{cx + x:.1f},{G + y:.1f}" for x, y in p)}" fill="{c}" {extra}/>'


def circ(x, y, r, c, extra=""):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}" {extra}/>'


def spiral(x, y, turns, r, c, w=5):
    pts = []
    for i in range(turns * 24 + 1):
        a = i / 24 * math.tau
        rr = r * i / (turns * 24)
        pts.append(f"{x + math.cos(a) * rr:.1f},{y + math.sin(a) * rr:.1f}")
    return f'<polyline points="{" ".join(pts)}" stroke="{c}" stroke-width="{w}" {L}/>'


# ---------------------------------------------------------------- roller
def jagaren(cx):
    """RÖD · lång och smal · omvänd triangel · vargöron · spjut i kast."""
    s = st(f"M{cx - 70},{G - 330} L{cx + 130},{G - 560}", BLK, 8)
    s += f'<polygon points="{cx + 130},{G - 560} {cx + 112},{G - 528} {cx + 146},{G - 534}" fill="{BLK}"/>'
    s += poly(cx, [(-46, -400), (34, -400), (-6, -240)], RED)
    for i in range(3):  # sicksack-ränder
        y = -385 + i * 34
        w = 34 - i * 9
        s += st(f"M{cx - 6 - w},{G + y} l{w/2:.0f},10 l{w/2:.0f},-10 l{w/2:.0f},10 l{w/2:.0f},-10", BLK, 4)
    s += circ(cx - 6, G - 432, 24, RED)
    s += poly(cx, [(-28, -446), (-22, -486), (-8, -452)], RED)
    s += poly(cx, [(16, -446), (10, -486), (-4, -452)], RED)
    s += st(f"M{cx - 6},{G - 250} L{cx - 70},{G - 150} L{cx - 120},{G - 30} M{cx - 6},{G - 250} L{cx + 50},{G - 140} L{cx + 90},{G - 4}", RED)
    s += st(f"M{cx + 22},{G - 390} L{cx + 74},{G - 470} L{cx + 70},{G - 520} M{cx - 36},{G - 384} L{cx - 96},{G - 320} L{cx - 80},{G - 300}", RED)
    return s


def samlaren(cx):
    """GUL · liten och rund · cirkelkropp · blomkrona · korg på ryggen."""
    s = f'<path d="M{cx - 130},{G - 330} L{cx - 40},{G - 312} L{cx - 56},{G - 210} L{cx - 124},{G - 222} Z" fill="none" stroke="{BLK}" stroke-width="8" stroke-linejoin="round"/>'
    for i in range(4):
        s += st(f"M{cx - 126 + i*2},{G - 306 + i*24} L{cx - 46 - i*3},{G - 292 + i*24}", BLK, 4)
    for dx, dy in ((-110, -340), (-92, -346), (-74, -336), (-100, -356)):
        s += circ(cx + dx, G + dy, 7, BLK)
    s += circ(cx, G - 190, 66, YEL)
    s += f'<circle cx="{cx}" cy="{G - 190}" r="38" fill="none" stroke="{BLK}" stroke-width="4"/>'
    s += f'<circle cx="{cx}" cy="{G - 190}" r="16" fill="none" stroke="{BLK}" stroke-width="4"/>'
    s += circ(cx + 8, G - 290, 26, YEL)
    for a in (-60, -20, 20, 60):  # blomkrona
        r = math.radians(a - 90)
        x2, y2 = cx + 8 + math.cos(r) * 48, G - 290 + math.sin(r) * 48
        s += st(f"M{cx + 8 + math.cos(r)*24:.0f},{G - 290 + math.sin(r)*24:.0f} L{x2:.0f},{y2:.0f}", BLK, 4)
        s += circ(x2, y2, 8, RED)
    s += st(f"M{cx - 26},{G - 132} L{cx - 36},{G - 4} M{cx + 26},{G - 132} L{cx + 36},{G - 4}", YEL, 18)
    s += st(f"M{cx + 56},{G - 220} L{cx + 110},{G - 160} L{cx + 128},{G - 120}", YEL)
    s += st(f"M{cx - 50},{G - 230} L{cx - 20},{G - 150}", YEL)
    s += st(f"M{cx + 120},{G} L{cx + 126},{G - 90} M{cx + 124},{G - 60} l22,-18 m-24,48 l-20,-14", BLK, 6)
    for dx, dy in ((138, -100), (150, -82), (112, -92)):
        s += circ(cx + dx, G + dy, 7, RED)
    return s


def byggaren(cx):
    """SVART · kort och bred · rektangelkropp · stock över huvudet."""
    s = poly(cx, [(-80, -290), (80, -290), (80, -150), (-80, -150)], BLK)
    for i in range(3):
        s += poly(cx, [(-80, -270 + i*40), (80, -270 + i*40), (80, -260 + i*40), (-80, -260 + i*40)], YEL, 'opacity=".9"')
    s += circ(cx, G - 326, 30, BLK)
    s += poly(cx, [(-76, -150), (-30, -150), (-42, 0), (-96, 0)], BLK)
    s += poly(cx, [(30, -150), (76, -150), (96, 0), (42, 0)], BLK)
    s += st(f"M{cx - 72},{G - 284} L{cx - 116},{G - 360} L{cx - 104},{G - 420} M{cx + 72},{G - 284} L{cx + 116},{G - 360} L{cx + 104},{G - 420}", BLK, 22)
    s += st(f"M{cx - 140},{G - 436} L{cx + 140},{G - 436}", RED, 40)
    s += f'<circle cx="{cx - 140}" cy="{G - 436}" r="19" fill="{WHT}" stroke="{BLK}" stroke-width="5"/>'
    s += f'<circle cx="{cx - 140}" cy="{G - 436}" r="7" fill="none" stroke="{BLK}" stroke-width="3"/>'
    return s


def hantverkaren(cx):
    """VIT med svart kontur · på knä · rombkropp · spretig hårknut · flinta och gnistor."""
    s = poly(cx, [(70, -70), (140, -78), (150, -10), (64, 0)], "#7d6a58")  # städsten
    s += poly(cx, [(84, -96), (122, -104), (126, -74), (92, -70)], BLK)    # flintkärna
    for dx, dy, a in ((100, -150, -60), (130, -140, -30), (70, -140, -110), (150, -116, -10)):
        r = math.radians(a)
        s += st(f"M{cx + dx},{G + dy} l{math.cos(r)*18:.0f},{math.sin(r)*18:.0f}", RED, 5)
    s += ost(f"M{cx - 20},{G - 140} L{cx - 90},{G - 70} L{cx - 20},{G - 10} M{cx + 10},{G - 140} L{cx + 40},{G - 50} L{cx}, {G - 6}", 14)
    s += poly(cx, [(-10, -330), (50, -240), (-10, -140), (-70, -240)], WHT, f'stroke="{BLK}" stroke-width="5" stroke-linejoin="round"')
    s += st(f"M{cx - 10},{G - 300} L{cx - 10},{G - 170}", BLK, 4)
    s += ost(f"M{cx + 30},{G - 270} L{cx + 70},{G - 230} L{cx + 96},{G - 270}", 12)
    s += f'<ellipse cx="{cx + 100}" cy="{G - 284}" rx="22" ry="15" fill="{BLK}"/>'
    s += ost(f"M{cx - 50},{G - 250} L{cx + 20},{G - 170} L{cx + 86},{G - 110}", 12)
    s += f'<circle cx="{cx - 10}" cy="{G - 362}" r="26" fill="{WHT}" stroke="{BLK}" stroke-width="5"/>'
    for a in range(-150, -20, 26):  # spretig hårknut
        r = math.radians(a)
        s += st(f"M{cx - 10 + math.cos(r)*26:.0f},{G - 362 + math.sin(r)*26:.0f} l{math.cos(r)*22:.0f},{math.sin(r)*22:.0f}", BLK, 5)
    s += poly(cx, [(-140, -6), (-96, -22), (-86, 0)], BLK)
    s += poly(cx, [(-60, -4), (-30, -16), (-24, 0)], BLK)
    return s


def spejaren(cx):
    """BRUN · längst och tunnast · bara streck · tre fjädrar · slunga · fotspår."""
    s = st(f"M{cx + 14},{G - 480} L{cx - 4},{G - 290}", BRN, 16)
    s += st(f"M{cx - 4},{G - 300} L{cx - 90},{G - 200} L{cx - 160},{G - 230} M{cx - 4},{G - 300} L{cx + 70},{G - 180} L{cx + 60},{G - 4}", BRN, 10)
    s += st(f"M{cx + 10},{G - 450} L{cx + 90},{G - 410} L{cx + 130},{G - 470} M{cx + 6},{G - 440} L{cx - 70},{G - 390} L{cx - 120},{G - 410}", BRN, 10)
    s += circ(cx + 18, G - 506, 20, BRN)
    for i, (dx, c) in enumerate(((-46, RED), (-40, BLK), (-30, RED))):  # tre fjädrar bakåt
        s += st(f"M{cx + 6},{G - 518 + i*6} q{dx/2:.0f},{-30 + i*8} {dx * 2},{-40 + i*14}", c, 7)
    s += f'<ellipse cx="{cx + 140}" cy="{G - 560}" rx="70" ry="20" fill="none" stroke="{RED}" stroke-width="5" stroke-dasharray="10 10"/>'
    s += st(f"M{cx + 130},{G - 470} L{cx + 166},{G - 540}", BLK, 4)
    s += circ(cx + 172, G - 550, 10, BLK)
    return s


def shamanen(cx):
    """RÖD med vita prickar · bred mantel (triangel uppåt) · jättehorn · spiraler."""
    s = spiral(cx - 120, G - 470, 3, 34, BLK, 4) + spiral(cx + 124, G - 250, 3, 30, BLK, 4)
    s += poly(cx, [(-24, -372), (24, -372), (100, -110), (-100, -110)], RED)
    for r in range(5):
        n = 2 + r
        for i in range(n):
            x = (i - (n - 1) / 2) * 26
            s += circ(cx + x, G - 340 + r * 46, 6, WHT)
    s += st(f"M{cx - 36},{G - 112} L{cx - 50},{G - 4} M{cx + 36},{G - 112} L{cx + 50},{G - 4}", RED)
    s += st(f"M{cx - 20},{G - 360} L{cx - 90},{G - 400} L{cx - 110},{G - 480} M{cx + 20},{G - 360} L{cx + 90},{G - 400} L{cx + 110},{G - 480}", RED)
    for sx in (-1, 1):
        s += circ(cx + sx * 112, G - 494, 9, RED)
    s += circ(cx, G - 398, 26, RED)
    for sx in (-1, 1):  # stora grenade horn
        s += st(f"M{cx + sx*12},{G - 420} L{cx + sx*40},{G - 490} L{cx + sx*48},{G - 580} "
                f"M{cx + sx*30},{G - 466} L{cx + sx*82},{G - 480} "
                f"M{cx + sx*42},{G - 530} L{cx + sx*84},{G - 556} "
                f"M{cx + sx*46},{G - 560} L{cx + sx*24},{G - 600}", BLK, 8)
    return s


# ---------------------------------------------------------------- symboler
def glyph(name, x, y, fg):
    if name == "Jägaren":
        return st(f"M{x - 12},{y + 14} L{x + 8},{y - 6}", fg, 5) + f'<polygon points="{x + 4},{y - 18} {x + 16},{y - 14} {x + 14},{y - 2}" fill="{fg}"/>'
    if name == "Samlaren":
        return circ(x - 9, y + 4, 6, fg) + circ(x + 7, y + 6, 6, fg) + circ(x - 1, y - 7, 6, fg) + st(f"M{x},{y - 12} q8,-8 14,-6", fg, 4)
    if name == "Byggaren":
        return st(f"M{x - 12},{y} L{x + 16},{y}", fg, 12) + f'<circle cx="{x - 14}" cy="{y}" r="6" fill="none" stroke="{fg}" stroke-width="3"/>'
    if name == "Hantverkaren":
        s = f'<polygon points="{x - 12},{y + 10} {x - 2},{y - 12} {x + 12},{y + 8}" fill="{fg}"/>'
        return s + st(f"M{x + 10},{y - 14} l6,-6 M{x + 14},{y - 6} l8,-2", fg, 3)
    if name == "Spejaren":
        return (f'<ellipse cx="{x}" cy="{y + 4}" rx="8" ry="11" fill="{fg}"/>'
                + "".join(circ(x - 8 + i * 5.5, y - 12 + abs(i - 1.5) * 2, 2.8, fg) for i in range(4)))
    if name == "Shamanen":
        return spiral(x, y, 2, 15, fg, 3)
    return ""


ROLES = [
    (jagaren, "Jägaren", "röd · lång · vargöron · spjut", RED, WHT),
    (samlaren, "Samlaren", "gul · rund · blomkrona · korg", YEL, BLK),
    (byggaren, "Byggaren", "svart · bred · stock", BLK, WHT),
    (hantverkaren, "Hantverkaren", "vit · på knä · flinta", WHT, BLK),
    (spejaren, "Spejaren", "brun · smal · fjädrar · slunga", BRN, WHT),
    (shamanen, "Shamanen", "röd/vit · mantel · horn", RED, WHT),
]


def hand(x, y, rot, c=RED, op=.35):
    h = f'<g transform="translate({x},{y}) rotate({rot})" opacity="{op}" fill="{c}"><ellipse cx="0" cy="0" rx="30" ry="34"/>'
    for fx, fy, r in ((-26, -48, -18), (-10, -62, -6), (6, -64, 4), (22, -56, 14), (36, -16, 50)):
        h += f'<ellipse cx="{fx}" cy="{fy}" rx="8" ry="24" transform="rotate({r} {fx} {fy})"/>'
    return h + "</g>"


def main():
    rnd = random.Random(7)
    out = f'<rect width="{W}" height="{H}" fill="#c99d72"/>'
    for _ in range(170):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        c = rnd.choice(("#b48659", "#d9b285", "#bf9466", "#a37548"))
        out += f'<ellipse cx="{x}" cy="{y}" rx="{rnd.randint(30, 160)}" ry="{rnd.randint(14, 70)}" fill="{c}" opacity="{rnd.uniform(.15, .45):.2f}" transform="rotate({rnd.randint(-30, 30)} {x} {y})"/>'
    for _ in range(22):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        out += f'<path d="M{x},{y} q{rnd.randint(-60, 60)},{rnd.randint(20, 80)} {rnd.randint(-40, 40)},{rnd.randint(80, 200)}" stroke="#8c6a48" stroke-width="2" fill="none" opacity=".45"/>'
    out += hand(60, 190, -10, RED, .3) + hand(1745, 180, 20, BLK, .2)
    out += (f'<text x="{W/2}" y="62" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="700" fill="{BLK}" letter-spacing="3">SURVIVE TO SURVIVE</text>'
            f'<text x="{W/2}" y="98" text-anchor="middle" font-family="{FONT}" font-size="20" fill="#4a3424">Stammen · varje roll har egen färg, kroppsform, siluett och symbol</text>')
    for cx, (fn, name, sub, col, fg) in zip(XS, ROLES):
        out += f'<g transform="translate({cx},{G}) scale(.8) translate({-cx},{-G})">{fn(cx)}</g>'
        gy = G + 52
        stroke = f'stroke="{BLK}" stroke-width="3"' if col == WHT else ""
        out += f'<circle cx="{cx}" cy="{gy}" r="27" fill="{col}" {stroke}/>' + glyph(name, cx, gy, fg)
        out += (f'<text x="{cx}" y="{G + 122}" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="{BLK}">{name}</text>'
                f'<text x="{cx}" y="{G + 150}" text-anchor="middle" font-family="{FONT}" font-size="16" fill="#5a2a1a">{sub}</text>')
    path = Path(__file__).with_name("grottmalning_roller.svg")
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{out}</svg>', encoding="utf-8")
    print("skrev", path)


if __name__ == "__main__":
    main()
