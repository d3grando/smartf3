"""Draws icon.png, the registry icon: a debug screen's panel of coloured lines of text and an F3 key cap in front of
it, in a vanilla tooltip's frame (the frame LookAt's icon uses, so the mods look like one family). 32 x 32 pixel art
scaled 8 times to 256 x 256. Needs Pillow.

    python tools/icon.py [icon.png]
"""
import sys

from PIL import Image

SIZE, SCALE = 32, 8
BACKGROUND = (0x10, 0x00, 0x10, 0xF0)
FRAME_TOP = (0x50, 0x00, 0xFF, 0xFF)
FRAME_BOTTOM = (0x28, 0x00, 0x7F, 0xFF)


def lerp(a, b, t):
    return tuple(round(ca + (cb - ca) * t) for ca, cb in zip(a, b))


class Canvas:
    """A 32 x 32 tooltip; drawing stays inside its frame."""

    def __init__(self):
        self.img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
        self.px = self.img.load()
        for y in range(SIZE):
            for x in range(SIZE):
                if x in (0, SIZE - 1) and y in (0, SIZE - 1):
                    continue
                edge = x in (0, SIZE - 1) or y in (0, SIZE - 1)
                frame = x in (1, SIZE - 2) or y in (1, SIZE - 2)
                self.px[x, y] = lerp(FRAME_TOP, FRAME_BOTTOM, (y - 1) / (SIZE - 3)) if frame and not edge else BACKGROUND

    def set(self, x, y, c):
        if not (2 <= x < SIZE - 2 and 2 <= y < SIZE - 2) or c is None:
            return
        if len(c) == 4 and c[3] < 255:
            under, a = self.px[x, y], c[3] / 255
            c = tuple(round(u + (v - u) * a) for u, v in zip(under[:3], c[:3])) + (under[3],)
        self.px[x, y] = c if len(c) == 4 else c + (255,)

    def sprite(self, x0, y0, art, palette):
        for dy, row in enumerate(art):
            for dx, ch in enumerate(row):
                if ch not in ". ":
                    self.set(x0 + dx, y0 + dy, palette[ch])

    def save(self, path):
        self.img.resize((SIZE * SCALE, SIZE * SCALE), Image.NEAREST).save(path, optimize=True)


PALETTE = {
    # the panel: its fill and its lighter top edge
    "P": (0x3A, 0x3A, 0x46), "p": (0x52, 0x52, 0x60),
    # the text: labels in white, values in colour
    "W": (0xF0, 0xF0, 0xF0), "Y": (0xFF, 0xD8, 0x40), "G": (0x6C, 0xE0, 0x5C), "C": (0x5C, 0xD0, 0xF0),
    "R": (0xFF, 0x70, 0x58),
    # the key cap: outline, its top face, the face's light edge, its sides; the legend
    "K": (0x18, 0x14, 0x1C), "F": (0xD8, 0xD8, 0xE0), "f": (0xF8, 0xF8, 0xFF), "S": (0x8C, 0x8C, 0x9C),
    "s": (0x6C, 0x6C, 0x7C), "L": (0x2A, 0x26, 0x34),
}

# The lines of the debug screen: (colour, length) runs, a gap between runs.
LINES = [
    [("W", 4), ("G", 6)],
    [("W", 3), ("Y", 3), ("Y", 4)],
    [("W", 5), ("C", 5)],
    [("W", 3), ("R", 4)],
    [("W", 4), ("G", 2), ("Y", 3)],
]

# The key cap, 13 x 12, its legend drawn on later.
KEY = [
    ".KKKKKKKKKKK.",
    "KffffffffffFK",
    "KfFFFFFFFFFFK",
    "KfFFFFFFFFFFK",
    "KfFFFFFFFFFFK",
    "KfFFFFFFFFFFK",
    "KfFFFFFFFFFFK",
    "KfFFFFFFFFFFK",
    "KFFFFFFFFFFFK",
    "KSSSSSSSSSSSK",
    "KsssssssssssK",
    ".KKKKKKKKKKK.",
]

LEGEND = [
    "###.###",
    "#.....#",
    "##..##.",
    "#.....#",
    "#...###",
]


def draw():
    c = Canvas()
    # the panel, the debug screen's grey box
    for y in range(3, 23):
        for x in range(3, 24):
            c.set(x, y, PALETTE["p" if y == 3 else "P"])
    # its text, two pixels a line
    for row, runs in enumerate(LINES):
        y, x = 5 + row * 3 + (row > 2) * 0, 5
        for colour, length in runs:
            for dx in range(length):
                c.set(x + dx, y, PALETTE[colour])
                c.set(x + dx, y + 1, PALETTE[colour])
            x += length + 1
    # the key cap in front of the panel's corner
    c.sprite(16, 17, KEY, PALETTE)
    for dy, row in enumerate(LEGEND):
        for dx, ch in enumerate(row):
            if ch == "#":
                c.set(19 + dx, 19 + dy, PALETTE["L"])
    return c


if __name__ == "__main__":
    draw().save(sys.argv[1] if len(sys.argv) > 1 else "icon.png")
