from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.request
from pathlib import Path


def _safe_filename_from_url(url: str) -> str:
    # Use the last path segment; keep the trailing id to avoid collisions.
    segment = re.sub(r"[?#].*$", "", url).rstrip("/").split("/")[-1]
    segment = re.sub(r"[^A-Za-z0-9._-]+", "-", segment).strip("-")
    if not segment:
        segment = "page"
    return segment + ".html"


def fetch(url: str, *, timeout: float = 30.0, sleep_s: float = 0.25) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "nl-NL,nl;q=0.9,en;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()

    if sleep_s:
        time.sleep(sleep_s)

    return data


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Download HelloFresh recipe pages as HTML files")
    ap.add_argument("--out", dest="out_dir", default="raw/hellofresh", help="Output directory")
    ap.add_argument("--urls-file", dest="urls_file", default="", help="Text file with URLs (one per line)")
    ap.add_argument("urls", nargs="*", help="Recipe URLs")
    args = ap.parse_args(argv)

    urls: list[str] = []
    if args.urls_file:
        urls.extend([line.strip() for line in Path(args.urls_file).read_text(encoding="utf-8").splitlines() if line.strip()])
    urls.extend([u.strip() for u in args.urls if u.strip()])

    if not urls:
        print("No URLs provided", file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    ok = 0
    for url in urls:
        fn = _safe_filename_from_url(url)
        out_path = out_dir / fn
        try:
            data = fetch(url)
        except Exception as e:
            print(f"FAILED {url}: {e}", file=sys.stderr)
            continue
        out_path.write_bytes(data)
        ok += 1
        print(f"saved {out_path}")

    return 0 if ok == len(urls) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
