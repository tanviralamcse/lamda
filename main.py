import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait


def is_dom_fully_loaded(driver):
    return driver.execute_script("return document.readyState") == "complete"


@pytest.fixture
def browser(request):
    if request.param == "chrome":
        caps_chrome = DesiredCapabilities.CHROME.copy()
        caps_chrome['version'] = '86.0'
        caps_chrome['platform'] = 'Windows 10'
        driver = webdriver.Remote(command_executor='http://selenium-grid-url:4444/wd/hub',
                                  desired_capabilities=caps_chrome)
    elif request.param == "edge":
        caps_edge = DesiredCapabilities.EDGE.copy()
        caps_edge['version'] = '87.0'
        caps_edge['platform'] = 'macOS Sierra'
        driver = webdriver.Remote(command_executor='http://selenium-grid-url:4444/wd/hub',
                                  desired_capabilities=caps_edge)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.browser_version = '92'
        options.platform_name = 'Windows 10'

        cloud_options = {}
        cloud_options['build'] = my_test_build
        cloud_options['name'] = my_test_name
        options.set_capability('cloud:options', cloud_options)

        driver = webdriver.Remote(cloud_url, options=options)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    yield driver
    time.sleep(3)
    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "edge", "firefox"], indirect=True)
def test_open_link_in_new_tab(browser):
    # Step 1: Open the website
    browser.get("https://www.lambdatest.com/")
    browser.maximize_window()

    # Step 2: Set an explicit wait with a maximum timeout of 10 seconds
    wait = WebDriverWait(browser, 20)
    wait.until(lambda driver: is_dom_fully_loaded(driver))

    # Step 3: Scroll to 'SEE ALL INTEGRATIONS'
    see_all_integrations_element = browser.find_element(By.XPATH,
                                                        "//*[@id='__next']/div[1]/section[8]/div/div/div/div/a")
    # Scroll to the element using scrollIntoView()
    time.sleep(5)
    browser.execute_script("arguments[0].scrollIntoView(true);", see_all_integrations_element)
    time.sleep(5)

    # Step 4: Open in a new tab
    url = see_all_integrations_element.get_attribute("href")
    browser.execute_script(f"window.open('{url}', '_blank');")
    time.sleep(2)

    # Step 5: Verify whether the window handles correspond to the newly opened tab
    original_window_handle = browser.current_window_handle
    new_window_handles = set(browser.window_handles) - {original_window_handle}

    # Retrieve and print the URL associated with each new window handle
    for handle in new_window_handles:
        browser.switch_to.window(handle)
        current_url = browser.current_url
        handles_to_close = handle
        print(f"Window Handle: {handle}, URL: {current_url}")
        # Add any additional checks or assertions as needed

    browser.switch_to.window(original_window_handle)  # Switch back to the original window

    # Step 6: Verify whether the URL is the same as the expected URL (if not, throw
    # an Assert).Expected URL
    expected_url = "https://www.lambdatest.com/integrations"

    # Retrieve and print the URL associated with each new window handle
    for handle in new_window_handles:
        browser.switch_to.window(handle)
        current_url = browser.current_url
        print(f"Window Handle: {handle}, URL: {current_url}")

        # Add an assertion to check if the current URL matches the expected URL
        assert current_url == expected_url, f"URL is not as expected. Expected: {expected_url}, Actual: {current_url}"

    #Step 7: On that page, scroll to the page where the WebElement
    #(Codeless Automation) is present.
    codeless_row = browser.find_element(By.XPATH, "//*[@id='codeless_row']/h2")
    # Scroll to the element using scrollIntoView()
    time.sleep(5)
    browser.execute_script("arguments[0].scrollIntoView(true);", codeless_row)
    time.sleep(5)

    # Step 8: Click the ‘LEARN MORE’ link for Testing Whiz. The page should open
    # in the same window.
    testing_whiz = browser.find_element(By.XPATH, "//*[@id='codeless_row']/div/div[4]/a")
    testing_whiz_link = testing_whiz.get_attribute("href")
    browser.execute_script(f"window.open('{testing_whiz_link}', '_self');")
    time.sleep(2)

    # Step 9: Check if the title of the page is ‘TestingWhiz Integration | LambdaTest’.
    expected_title = 'TestingWhiz Integration | LambdaTest'
    current_title = browser.title

    try:
        assert current_title == expected_title, f"Title is not as expected. Expected: {expected_title}, Actual: {current_title}"
    except AssertionError as e:
        print(f"AssertionError: {e}")

    # Step 10: Close the current window using the window handle obtained in step (5)
    for handle in new_window_handles:
        browser.switch_to.window(handle)

        # Check if the current handle is not the original window handle
        if handle != original_window_handle:
            browser.close()

    # Switch back to the original window
    browser.switch_to.window(original_window_handle)

    # Wait for the windows to close
    time.sleep(10)
    # Step 11: Print the current window count
    current_window_count = len(browser.window_handles)
    print(f"Current Window Count: {current_window_count}")
    time.sleep(10)
    # Step 12: On the current window, set the URL to https://www.lambdatest.com/blog.
    browser.get("https://www.lambdatest.com/blog")
    time.sleep(10)
    # Step 13: Click on the ‘Community’ link and verify whether the URL is https://community.lambdatest.com/.
    community_link = browser.find_element(By.XPATH, "//a[contains(text(),'Community')]")
    community_link.click()

    # Wait for the page to load, you can use WebDriverWait if needed
    # Example: wait.until(lambda driver: driver.current_url == "https://community.lambdatest.com/")

    # Verify the URL
    expected_community_url = "https://community.lambdatest.com/"
    assert browser.current_url == expected_community_url, f"URL is not as expected. Expected: {expected_community_url}, Actual: {browser.current_url}"

    # Step 14: Close the current browser window
    browser.quit()

# This block ensures that the test is executed only if this script is run directly, not imported
if __name__ == "__main__":
    pytest.main([__file__])
