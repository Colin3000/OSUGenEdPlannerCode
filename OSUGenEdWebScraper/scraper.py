from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
#Initalizes dictionary to later export as json
genCourseData = {}
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
#Creates a webdriver to manipulate the starting page
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://courses.erppub.osu.edu/psc/ps/EMPLOYEE/PUB/c/COMMUNITY_ACCESS.OSR_CAT_SRCH.GBL?PortalActualURL=https%3a%2f%2fcourses.erppub.osu.edu%2fpsc%2fps%2fEMPLOYEE%2fPUB%2fc%2fCOMMUNITY_ACCESS.OSR_CAT_SRCH.GBL&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fcourses.erppub.osu.edu%2fpsp%2fps%2f&PortalURI=https%3a%2f%2fcourses.erppub.osu.edu%2fpsc%2fps%2f&PortalHostNode=CAMP&NoCrumbs=yes&PortalKeyStruct=yes")
#Creates a webdriverwait to wait for certain elements to load
wait = WebDriverWait(driver, 10)
#Creates the list of courseAttributes needed
courseAttributes = []
for i in range(1, 9):
    courseAttributes.append("F" + str(i))
for i in range(1, 9):
    courseAttributes.append("T" + str(i))
#Finds the input form for the course attribute
courseAttribute = driver.find_element(By.NAME, "OSR_CAT_SRCH_WK_CRSE_ATTR")
courseAttribute.send_keys("GE2")
#Getting the courses of each attribute
for attribute in courseAttributes:
    #Finds element for course attribute and enters data
    courseAttributeValue = driver.find_element(By.NAME, "OSR_CAT_SRCH_WK_CRSE_ATTR_VALUE")
    courseAttributeValue.clear()
    courseAttributeValue.send_keys(attribute)
    #Clicks the search button to load the list of courses
    driver.find_element(By.NAME, "OSR_CAT_SRCH_WK_BUTTON1").click()
    time.sleep(1)
    #Creates a list to store info of courses
    courseInfo = []
    #Check if the courses loaded has more than 1 page
    isPresent = driver.find_elements(By.ID, "OSR_CAT_SRCH_WK_BUTTON_FORWARD")
    #Don't look for a forward buttton if there is only one page
    if len(isPresent) == 0:
        time.sleep(1)
        #Waits until a course loads
        wait.until(EC.presence_of_element_located((By.ID, "OSR_CAT_SRCH_OSR_CRSE_HEADER$0")))
        #Gets course titles
        courseTitles = driver.find_elements(By.CLASS_NAME, "PSQRYTITLE")
        #Converts course title elements to text
        courseTitles = [element.text for element in courseTitles]
        #Pops content header
        courseTitles.pop(0)
        #Gets course descriptions
        courseDescriptions = driver.find_elements(By.CLASS_NAME, "PSLONGEDITBOX")
        #Gets the number of courses through course descriptions list. 
        #The course descriptions list will have double the elements than normal due to the website's formatting. 
        #However, the last element in the list will always show the number of courses
        numCoursesOnPage = courseDescriptions[-1].get_attribute("id")[-2:]
        if (not numCoursesOnPage.isnumeric()):
            numCoursesOnPage = courseDescriptions[-1].get_attribute("id")[-1:]
        numCoursesOnPage = int(numCoursesOnPage)
        #Creates a list to get the text of course units
        courseUnits = []
        #Creates a list to get the text of course descriptions
        courseDescriptionsText = []
        #Finds the number of units and descriptions in each course
        for unitIndex in range(0, numCoursesOnPage + 1):
            idToSearch = "OSR_CAT_SRCH_OSR_UNITS_DESCR$" + str(unitIndex)
            courseUnits.append(driver.find_element(By.ID, idToSearch).text)
            idToSearch = "OSR_CAT_SRCH_DESCRLONG$" + str(unitIndex)
            courseDescriptionsText.append(driver.find_element(By.ID, idToSearch).text)
        #Adds course data to courseInfo
        courseInfo = [{"Title": t, "Description": d, "Units": u} for t, d, u in zip(courseTitles, courseDescriptionsText, courseUnits)]
    else:
        wait.until(EC.presence_of_element_located((By.ID, "OSR_CAT_SRCH_WK_BUTTON_FORWARD")))
        onceMore = iter([True, False])
        #Loop to go through pages as long as the forward button is enabled + one extra iteration
        while driver.find_element(By.ID, "OSR_CAT_SRCH_WK_BUTTON_FORWARD").is_enabled() or next(onceMore):
            time.sleep(1)
            wait.until(EC.presence_of_element_located((By.ID, "OSR_CAT_SRCH_OSR_CRSE_HEADER$0")))
            courseTitles = driver.find_elements(By.CLASS_NAME, "PSQRYTITLE")
            courseTitles = [element.text for element in courseTitles]
            courseTitles.pop(0)
            courseDescriptions = driver.find_elements(By.CLASS_NAME, "PSLONGEDITBOX")
            numCoursesOnPage = courseDescriptions[-1].get_attribute("id")[-2:]
            if (not numCoursesOnPage.isnumeric()):
                numCoursesOnPage = courseDescriptions[-1].get_attribute("id")[-1:]
            numCoursesOnPage = int(numCoursesOnPage)
            courseUnits = []
            courseDescriptionsText = []
            for unitIndex in range(0, numCoursesOnPage + 1):
                idToSearch = "OSR_CAT_SRCH_OSR_UNITS_DESCR$" + str(unitIndex)
                courseUnits.append(driver.find_element(By.ID, idToSearch).text)
                idToSearch = "OSR_CAT_SRCH_DESCRLONG$" + str(unitIndex)
                courseDescriptionsText.append(driver.find_element(By.ID, idToSearch).text)
            #Adds course data of current page and adds to courseInfo
            currentPageInfo = [{"Title": t, "Description": d, "Units": u} for t, d, u in zip(courseTitles, courseDescriptionsText, courseUnits)]
            courseInfo = courseInfo + currentPageInfo
            #Finds and clicks the next page button
            driver.find_element(By.ID, "OSR_CAT_SRCH_WK_BUTTON_FORWARD").click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located((By.ID, "OSR_CAT_SRCH_WK_BUTTON_FORWARD")))
    #Adds courseInfo to genCourseData with attribute as key
    genCourseData[attribute] = courseInfo
    #Go back to the course attribute page
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, "OSR_CAT_SRCH_WK_HYPERLINK")))
    driver.find_element(By.ID, "OSR_CAT_SRCH_WK_HYPERLINK").click()
    time.sleep(1)
#Closes webdriver
driver.close()
#Converts and writes getCourseData to json
course_json = json.dumps(genCourseData, indent = 4)
with open("GECourseData.json", "w") as outfile:
    outfile.write(course_json)
