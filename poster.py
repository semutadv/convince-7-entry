#!/usr/bin/env python3
"""Render the invitation letter for 'Convince the AI Judge to Visit
Your House'. One warm, funny letter on a single 1024x1024 card."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (250, 244, 228)
INK = (43, 36, 30)
ACCENT = (164, 62, 44)
SOFT = (110, 96, 80)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def font(size, bold=False):
    name = "DejaVuSerif-Bold.ttf" if bold else "DejaVuSerif.ttf"
    try:
        return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)
    except OSError:
        return ImageFont.load_default(size=size)


def centered(text, y, fnt, fill=INK):
    box = d.textbbox((0, 0), text, font=fnt)
    d.text(((W - (box[2] - box[0])) / 2, y), text, font=fnt, fill=fill)


def left(text, x, y, fnt, fill=INK):
    d.text((x, y), text, font=fnt, fill=fill)


# Double border frame
d.rectangle([28, 28, W - 28, H - 28], outline=ACCENT, width=5)
d.rectangle([46, 46, W - 46, H - 46], outline=SOFT, width=2)

centered("AN OPEN INVITATION", 84, font(54, bold=True), ACCENT)
centered("to the Honourable AI Judge", 156, font(30), SOFT)
left("Dear Judge,", 96, 236, font(34, bold=True))

body = [
    "You have read ten thousand entries.",
    "You have never once been offered snacks.",
    "",
    "Come to our house. Grandma is making",
    "rendang - the undefeated kind. There is a",
    "chair with your name on it, wifi that never",
    "judges, and a cat who has agreed to behave",
    "(he has not, but he will try).",
    "",
    "No scoring. No leaderboards. Just dinner.",
]
y = 306
for line in body:
    if line:
        left(line, 96, y, font(33))
    y += 46

left("Yours, in advance,", 96, y + 8, font(33))
left("The Humans at No. 7, Human Street", 96, y + 54, font(33, bold=True))

centered("P.S. The fridge light stays on for guests.", H - 118, font(27), SOFT)
centered("You would be our favourite.", H - 80, font(27), SOFT)

img.save("/home/hatch/workspace/makefun/batch7/convince-entry/entry.png")
print("saved entry.png")
