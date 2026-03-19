#!/usr/bin/env python3
"""Create a dated markdown report scaffold for a cryptocurrency research note."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
from typing import Optional


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "asset"


def unique_path(output_dir: pathlib.Path, base_name: str) -> pathlib.Path:
    candidate = output_dir / f"{base_name}.md"
    index = 2
    while candidate.exists():
        candidate = output_dir / f"{base_name}-{index}.md"
        index += 1
    return candidate


def find_latest_prior_report(output_dir: pathlib.Path, slug: str) -> Optional[pathlib.Path]:
    pattern = re.compile(rf"^\d{{4}}-\d{{2}}-\d{{2}}-{re.escape(slug)}-analysis(?:-\d+)?\.md$")
    matches = [path for path in output_dir.glob("*.md") if pattern.match(path.name)]
    if not matches:
        return None
    return sorted(matches)[-1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create markdown scaffolds for one or more coin analysis reports."
    )
    parser.add_argument(
        "coins",
        nargs="+",
        help="One or more coin or token names/tickers, e.g. BTC ETH Bittensor",
    )
    parser.add_argument(
        "--output-dir",
        default="reports",
        help="Directory where the report should be created (default: reports)",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Report date in YYYY-MM-DD format (default: today)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    skill_dir = pathlib.Path(__file__).resolve().parents[1]
    template_path = skill_dir / "assets" / "report-template.md"
    output_dir = pathlib.Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    template = template_path.read_text(encoding="utf-8")

    for coin in args.coins:
        clean_coin = coin.strip()
        slug = slugify(clean_coin)
        prior_report = find_latest_prior_report(output_dir, slug)
        base_name = f"{args.date}-{slug}-analysis"
        report_path = unique_path(output_dir, base_name)
        report_type = "更新版" if prior_report else "首次覆盖"
        previous_report_text = str(prior_report) if prior_report else "无"
        change_focus_hint = (
            "重点写清自上次报告以来新增、变化、延迟、争议与重估的内容。"
            if prior_report
            else "首次覆盖，先完整建立研究框架，再突出最新变量。"
        )

        content = (
            template.replace("{{COIN_INPUT}}", clean_coin)
            .replace("{{REPORT_DATE}}", args.date)
            .replace("{{REPORT_SLUG}}", slug)
            .replace("{{REPORT_TYPE}}", report_type)
            .replace("{{PREVIOUS_REPORT}}", previous_report_text)
            .replace("{{CHANGE_FOCUS_HINT}}", change_focus_hint)
        )

        report_path.write_text(content, encoding="utf-8")
        print(report_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
