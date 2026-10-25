#!/usr/bin/env python3
"""渲染 profile README 的统计块。

设计要点（对齐"降级不失败 + 失败要响"）：
- 标记块不存在 → 报错退出，不改文件（fail-closed，避免静默无效）
- star 总数为 0 → 不渲染 0 值徽章（0★ 是负资产），改渲染一行事实
- 无变化 → 不写盘

用法：
    STARS=0 FOLLOWERS=0 REPOS=12 LATEST=2026-09-30 python render_stats.py README.md
"""
import os
import re
import sys

USER = "gavenna"
START = "<!-- STATS-START -->"
END = "<!-- STATS-END -->"


def fmt(n: int) -> str:
    """1234 -> 1.2k ; 1000 -> 1k ; 52 -> 52"""
    if n >= 1000:
        s = f"{n / 1000:.1f}k"
        return s.replace(".0k", "k")
    return str(n)


def badge(label: str, value: str, color: str, url: str) -> str:
    label_q = label.replace(" ", "%20")
    return (
        f"[![{label}](https://img.shields.io/badge/{label_q}-{value}-{color}"
        f"?style=flat&logo=github&logoColor=white)]({url})"
    )


def render(stars: int, followers: int, repos: int, latest: str) -> str:
    if stars > 0:
        body = "\n".join([
            badge("Total Stars", fmt(stars), "FFD93D", f"https://github.com/{USER}"),
            badge("Followers", fmt(followers), "4C8BF5", f"https://github.com/{USER}?tab=followers"),
            badge("Public Repos", str(repos), "2EA44F", f"https://github.com/{USER}?tab=repositories"),
        ])
    else:
        # 0 star 阶段：徽章是负资产，换成一行可核实的事实
        body = f"🛠 {repos} 个公开仓库 · 最近推送 {latest}"
    return f"{START}\n{body}\n{END}"


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    stars = int(os.environ.get("STARS", "0"))
    followers = int(os.environ.get("FOLLOWERS", "0"))
    repos = int(os.environ.get("REPOS", "0"))
    latest = os.environ.get("LATEST", "").strip() or "—"

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    n_start, n_end = text.count(START), text.count(END)
    if n_start != 1 or n_end != 1:
        print(f"ERROR: markers must appear exactly once (found start={n_start} end={n_end}); file left unchanged")
        return 2

    block = render(stars, followers, repos, latest)
    new_text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.DOTALL)

    if new_text == text:
        print("No changes.")
        return 0

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"Rendered: stars={stars} followers={followers} repos={repos} latest={latest} mode={'badges' if stars > 0 else 'text'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
