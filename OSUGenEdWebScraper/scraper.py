from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://courses.erppub.osu.edu/psc/ps/EMPLOYEE/PUB/c/COMMUNITY_ACCESS.OSR_CAT_SRCH.GBL?PortalActualURL=https%3a%2f%2fcourses.erppub.osu.edu%2fpsc%2fps%2fEMPLOYEE%2fPUB%2fc%2fCOMMUNITY_ACCESS.OSR_CAT_SRCH.GBL&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fcourses.erppub.osu.edu%2fpsp%2fps%2f&PortalURI=https%3a%2f%2fcourses.erppub.osu.edu%2fpsc%2fps%2f&PortalHostNode=CAMP&NoCrumbs=yes&PortalKeyStruct=yes")
courseAttribute = driver.find_element(By.NAME, "OSR_CAT_SRCH_WK_CRSE_ATTR")
courseAttribute.send_keys("GE2")
courseAttributeValue = driver.find_element(By.NAME, "OSR_CAT_SRCH_WK_CRSE_ATTR_VALUE")
courseAttributeValue.send_keys("F7")
driver.find_element(By.NAME, "OSR_CAT_SRCH_WK_BUTTON1").click()

