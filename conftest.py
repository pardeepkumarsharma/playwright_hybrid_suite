import pytest
import os
from datetime import datetime

import pytest_html


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")
            page.screenshot(path=file_name)

            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.image(file_name))