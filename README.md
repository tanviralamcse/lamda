# lamda
Assignment Task: Selenium Advanced

Test Scenario
1. Navigate to https://www.lambdatest.com/.
2. Perform an explicit wait till the time all the elements in the DOM
are available.
3. Scroll to the WebElement ‘SEE ALL INTEGRATIONS’ using the
scrollIntoView() method. You are free to use any of the available
web locators (e.g., XPath, CssSelector, etc.)
4. Click on the link and ensure that it opens in a new Tab.
5. Save the window handles in a List (or array). Print the window handles
of the opened windows (now there are two windows open).
6. Verify whether the URL is the same as the expected URL (if not, throw
an Assert).
7. On that page, scroll to the page where the WebElement
(Codeless Automation) is present.
8. Click the ‘LEARN MORE’ link for Testing Whiz. The page should open
in the same window.
9. Check if the title of the page is ‘TestingWhiz Integration | LambdaTest’.

Selenium Advanced LambdaTest Certifications

If not, raise an Assert.
10. Close the current window using the window handle [which we
obtained in step (5)]
11. Print the current window count.
12. On the current window, set the URL to
https://www.lambdatest.com/blog.
13. Click on the ‘Community’ link and verify whether the URL is
https://community.lambdatest.com/.
14. Close the current browser window.

Execution

The test scenarios should be demonstrated on the following combinations of
browsers and platforms (using Selenium 4 Grid and programming language of
your choice):
1. Chrome + 86.0 + Windows 10 (Test Scenario 1)
2. Microsoft Edge + 87.0 + macOS Sierra (Test Scenario 2)

Selenium Advanced LambdaTest Certifications

Important Notes

1. You can submit the solution using any programming language
and framework of your choice. However, it is recommended to use
the latest version of the framework.
2. If you are using Java and TestNG, then pass the browser and OS
combinations to the test scenario(s) from testng.xml (for Java).
You could also hard code the browser and OS combination in the
implementation.
3. TimeOut of the test duration should be set to 20 seconds (for both
the test scenarios). Parallelism should be at the Class Level (i.e.,
both the tests should be executing in parallel on LambdaTest).
4. Please ensure to use at least 3 different locators while performing
the test.
5. Please ensure that network logs, video recording, screenshots,
and console logs are enabled in all the test runs. Please refer to
the Capability Generator for desired capabilities.
6. Refer to the detailed instructions appended below for
submission guidelines

Selenium Advanced LambdaTest Certifications

Reference Images

Selenium Advanced LambdaTest Certifications

Important Instructions

1. You can submit the solution using any programming language and
framework of your choice. We advise you to keep it as simple and as
lean as possible.
2. You must run the test on LambdaTest Cloud Selenium Grid in
parallel and mention the final Test ID(s) while submitting.
3. Submit the assignment task via Gitpod and make sure you have the
.gitpod.yml file configured on GitHub Repository. Please ensure
that you attach a detailed README.md file along with your GitHub
repository. This should include the instructions to run the test on the
Gitpod dev environment. Learn more about configuring your
single-click Gitpod dev environment.
4. Please ensure that it is a Private Repository shared with
‘LambdaTest-Certifications’ or
admin@lambdatestcertifications.com.
5. Ensure that network logs, video recording, screenshots, & console
logs are enabled through the desired capabilities generator.
6. You are required to submit the final solution within 48 hours of the
deadline.

Setting up your LambdaTest account & running your first test

1. Ensure that you register for your LambdaTest Account with the same
email address used to register for the certification and to appear for the
objective test.

Selenium Advanced LambdaTest Certifications

2. The free account comes with 15 days of automation trial access that
allows 100 minutes of automation testing.
3. If you have used the automation minutes or have exceeded the allotted
trail access time, you can get a 24-hour or more trial access window by
contacting LambdaTest support. You can contact LambdaTest support
from our in-app chat support or by dropping an email at
support@lambdatest.com. You can also drop your request at
admin@lambdatestcertifications.com.
4. You can also refer to our support docs to get started with Automation
testing on the LambdaTest platform.
