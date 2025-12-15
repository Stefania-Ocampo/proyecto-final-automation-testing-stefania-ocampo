import pytest
from selenium import webdriver
from datetime import datetime
import os
import pytest_html

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "reports/screens"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"{screenshots_dir}/{item.name}_{timestamp}.png"

            driver.save_screenshot(screenshot_path)

            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.image(screenshot_path))
            else:
                rep.extra = [pytest_html.extras.image(screenshot_path)]





                

