#!/usr/bin/env python3
"""Build index.html (a single static file for GitHub Pages) from src/app.html.

Usage: python3 build.py
"""
import pathlib, re

root = pathlib.Path(__file__).parent
src = (root / "src" / "app.html").read_text(encoding="utf-8")

# Drop the meta tag that only matters inside Claude's artifact viewer.
src = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n?', "", src)

head_end = src.index("</style>") + len("</style>")
head, body = src[:head_end], src[head_end:]

favicon = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 22 22'%3E"
           "%3Ccircle cx='5' cy='11' r='3.5' fill='none' stroke='%23284de0' stroke-width='2'/%3E"
           "%3Ccircle cx='17' cy='11' r='3.5' fill='%23284de0'/%3E"
           "%3Cpath d='M8.5 11h5' stroke='%23284de0' stroke-width='2'/%3E%3C/svg%3E")

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Track companies, LinkedIn and email outreach, referrals and job applications.">
<link rel="icon" href="{favicon}">
<style>:root{{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head}
</head>
<body>
{body.lstrip()}
</body>
</html>
"""
(root / "index.html").write_text(page, encoding="utf-8")
print("Wrote index.html", len(page.encode()), "bytes")
