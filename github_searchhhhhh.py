from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Wait object
wait = WebDriverWait(driver, 20)

# Repository to search
repo = "tensorflow"

# Open GitHub repository search page
driver.get(f"https://github.com/search?q={repo}&type=repositories")

try:
    # Wait until the page is loaded
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    print("Search Page Opened Successfully")
    print("Search URL :", driver.current_url)

    # Click the first repository
    first_repo = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//a[contains(@href,'/tensorflow/tensorflow')])[1]")
        )
    )
    first_repo.click()

    # Repository Name
    repo_name = wait.until(
        EC.presence_of_element_located((By.XPATH, "//strong/a"))
    ).text

    # Owner Name
    owner = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(@class,'author')]/a")
        )
    ).text

    # Repository URL
    url = driver.current_url

    print("\nRepository Details")
    print("-------------------------")
    print("Repository Name :", repo_name)
    print("Owner           :", owner)
    print("Repository URL  :", url)

    # Verify Public Repository
    try:
        visibility = driver.find_element(
            By.XPATH,
            "//span[text()='Public']"
        ).text

        print("Visibility      :", visibility)
        print("Verification    : PASS")

    except:
        print("Verification    : FAIL")

except Exception as e:
    print("Error :", e)

input("\nPress Enter to close the browser...")
driver.quit()