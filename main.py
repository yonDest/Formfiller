from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# initialize selenium chrome driver
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

# function code
def gchInvestigationDetails(driver):
    # Complaint allege Failure : Yes  Required : Yes and so on.... for reportable complaint
    complaintFailure = driver.find_element(By.XPATH, value='//*[@id="C24_W76_V78_V80_V81_btcustomerh_ext.zzafld000005"]')
    complaintFailure.click()
    complaintFailureSelect = driver.find_element(By.XPATH, value='//*[@id="C24_W76_V78_V80_V81_btcustomerh_ext.zzafld000005__items"]/ul/li[2]/a')
    complaintFailureSelect.click()
    required = driver.find_element(By.XPATH, value='//*[@id="C24_W76_V78_V80_V81_btcustomerh_struct.zzcustomer_h0503"]')
    required.click()
    requiredSelect = driver.find_element(By.XPATH, value='//*[@id="C24_W76_V78_V80_V81_btcustomerh_struct.zzcustomer_h0503__items"]/ul/li[2]')
    requiredSelect.click()
options = webdriver.ChromeOptions()
options.add_argument('--remote-debugging-port=9222')
options.add_experimental_option('debuggerAddress', 'localhost:9222')
driver = webdriver.Chrome(options=options)

# navigate to the URL
driver.get("") # insert URL here
def gchInvestigationDetails(driver)
#-------------------------------------------------------------------------------------------------------
# no access to localhost: 8989, open using cd C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=9222
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# initialize selenium chrome driver
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://facebook.com")
#--------------------------------------------------------------------------------------------------------
# no binary file??
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

o = Options()
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://facebook.com")
