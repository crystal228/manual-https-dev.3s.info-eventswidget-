from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright


URL = "https://dev.3s.info/eventswidget/"
ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"
SCREENSHOTS_DIR = ROOT / "screenshots"


VIEWPORTS = [
    ("desktop", {"width": 1366, "height": 900}),
    ("tablet", {"width": 768, "height": 1024}),
    ("mobile", {"width": 375, "height": 812}),
]


def main() -> None:
    REPORTS_DIR.mkdir(exist_ok=True)
    SCREENSHOTS_DIR.mkdir(exist_ok=True)

    console_messages: list[dict[str, object]] = []
    failed_requests: list[dict[str, str]] = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(viewport=VIEWPORTS[0][1])
        page = context.new_page()

        page.on(
            "console",
            lambda message: console_messages.append(
                {
                    "type": message.type,
                    "text": message.text,
                    "location": message.location,
                }
            ),
        )

        page.on(
            "requestfailed",
            lambda request: failed_requests.append(
                {
                    "method": request.method,
                    "url": request.url,
                    "failure": str(request.failure or ""),
                }
            ),
        )

        page.goto(URL, wait_until="networkidle", timeout=60_000)

        page.screenshot(
            path=str(SCREENSHOTS_DIR / "diagnostic-desktop.png"),
            full_page=True,
        )

        for name, viewport in VIEWPORTS[1:]:
            page.set_viewport_size(viewport)
            page.wait_for_timeout(500)
            page.screenshot(
                path=str(SCREENSHOTS_DIR / f"diagnostic-{name}.png"),
                full_page=True,
            )

        context.close()
        browser.close()

    diagnostics = {
        "url": URL,
        "collected_at": datetime.now().isoformat(timespec="seconds"),
        "note": (
            "This helper only collects diagnostics. It does not search for "
            "defects automatically and does not generate the QA report."
        ),
        "console_messages": console_messages,
        "failed_requests": failed_requests,
    }

    output_path = REPORTS_DIR / "diagnostics.json"
    output_path.write_text(
        json.dumps(diagnostics, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Diagnostics saved to {output_path}")


if __name__ == "__main__":
    main()
