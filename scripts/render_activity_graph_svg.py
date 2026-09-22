#!/usr/bin/env python3
"""
Render data/contributions.json as a line/area "activity graph" SVG covering the
last 31 days -- a self-hosted replacement for github-readme-activity-graph
(whose public deployment went down).

Run by .github/workflows/update-profile-art.yml after fetch_contributions.py.
"""
import datetime
import json
import os

HERE = os.path.dirname(__file__)
IN_PATH = os.path.join(HERE, "..", "data", "contributions.json")
OUT_PATH = os.path.join(HERE, "..", "activity-graph.svg")

DAYS = 31
W, H = 880, 300
PAD_L, PAD_R, PAD_T, PAD_B = 56, 24, 52, 48

BG = "#0d1117"
LINE = "#1cadfb"
GRID = "#21262d"
MUTED = "#7d8590"
TEXT = "#e6edf3"


def nice_max(v):
    # 4 gridlines, each a whole "nice" step
    for step in (1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000):
        if v <= step * 4:
            return step * 4
    return v


def render(data):
    days = data["days"][-DAYS:]
    counts = [d["count"] for d in days]
    ymax = nice_max(max(counts) or 1)

    pw, ph = W - PAD_L - PAD_R, H - PAD_T - PAD_B
    x = lambda i: PAD_L + pw * i / (len(days) - 1)
    y = lambda c: PAD_T + ph * (1 - c / ymax)
    pts = [(x(i), y(c)) for i, c in enumerate(counts)]

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">',
        f'<defs><linearGradient id="fill" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{LINE}" stop-opacity="0.35"/>'
        f'<stop offset="1" stop-color="{LINE}" stop-opacity="0"/></linearGradient></defs>',
        f'<rect width="{W}" height="{H}" rx="8" fill="{BG}"/>',
        f'<text x="{W / 2}" y="30" text-anchor="middle" fill="{LINE}" font-size="18" '
        f'font-weight="600">{data["username"]}\'s Contribution Graph</text>',
    ]

    # horizontal grid + y labels
    for k in range(5):
        v = ymax * k / 4
        gy = y(v)
        out.append(f'<line x1="{PAD_L}" y1="{gy:.1f}" x2="{W - PAD_R}" y2="{gy:.1f}" '
                   f'stroke="{GRID}" stroke-dasharray="3 3"/>')
        out.append(f'<text x="{PAD_L - 10}" y="{gy + 4:.1f}" text-anchor="end" '
                   f'fill="{MUTED}" font-size="11">{v:g}</text>')

    # x labels (day of month)
    for i, d in enumerate(days):
        if i % 2 == 0 or i == len(days) - 1:
            day = datetime.date.fromisoformat(d["date"]).day
            out.append(f'<text x="{x(i):.1f}" y="{H - PAD_B + 18}" text-anchor="middle" '
                       f'fill="{MUTED}" font-size="11">{day}</text>')
    out.append(f'<text x="{W / 2}" y="{H - 8}" text-anchor="middle" fill="{MUTED}" '
               f'font-size="11">Days</text>')
    out.append(f'<text x="16" y="{PAD_T + ph / 2}" text-anchor="middle" fill="{MUTED}" '
               f'font-size="11" transform="rotate(-90 16 {PAD_T + ph / 2})">Contributions</text>')

    line = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    base = PAD_T + ph
    out.append(f'<polygon points="{pts[0][0]:.1f},{base} {line} {pts[-1][0]:.1f},{base}" '
               f'fill="url(#fill)"/>')
    out.append(f'<polyline points="{line}" fill="none" stroke="{LINE}" stroke-width="2" '
               f'stroke-linejoin="round"/>')
    for (px, py), d in zip(pts, days):
        out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3" fill="{LINE}">'
                   f'<title>{d["date"]}: {d["count"]}</title></circle>')

    out.append("</svg>")
    return "\n".join(out)


def main():
    with open(IN_PATH) as f:
        data = json.load(f)
    with open(OUT_PATH, "w") as f:
        f.write(render(data))
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
