# This script makes course swap requests by clicking through the QUEST menu

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Connect to selenium Chrome
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

def perform_swap():
    try:
        print("Attempting swap...")

        driver.switch_to.default_content()
        driver.switch_to.frame("main_target_win0")

        # STEP 1: Click Swap button
        swap_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="win0divDERIVED_SSTSNAV_SSTS_NAV_SUBTABS"]/div/table/tbody/tr/td[26]/a')))
        swap_link.click()
        time.sleep(1)

        # STEP 2: Select PD 1: Career Fundamentals
        pd_element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(), 'PD 1: Career Fundamentals')]")))
        pd_element.click()
        time.sleep(0.5)

        # STEP 3: Select CHEM 200
        chem_element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(), 'CHEM 200')]")))
        chem_element.click()
        time.sleep(0.5)

        # STEP 4: Enter class number
        class_input = wait.until(EC.presence_of_element_located(
            (By.ID, "DERIVED_REGFRM1_CLASS_NBR")))
        class_input.clear()
        class_input.send_keys("7727")
        time.sleep(1)

        # STEP 5: Click Enter button
        enter_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$106$"]')))
        enter_button.click()
        time.sleep(2)

        # STEP 6 & 7: Click Next button twice
        for _ in range(2):
            next_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="DERIVED_CLS_DTL_NEXT_PB"]')))
            next_button.click()
            time.sleep(2)

        # STEP 8: Click Finish Swapping button
        finish_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]')))
        finish_button.click()
        time.sleep(2)

        # STEP 9: Check result message
        message_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="win0divDERIVED_REGFRM1_SS_MESSAGE_LONG$0"]/div')))
        message_text = message_box.text.strip()

        driver.switch_to.default_content()

        if "Class 7727 is full" in message_text:
            print("❌ Class full curse this life")
            return False
        else:
            print("✅ BLESS MY LIFE HELLO SECTION 002")
            return True

    except Exception as e:
        print(f"⚠️ Error during swap: {e}")
        driver.switch_to.default_content()
        return False

#  Main loop with fail count
fail_count = 0

while True:
    success = perform_swap()
    if success:
        print(f"that took {fail_count} attempts holy od.")
        break
    fail_count += 1
    print(f"# of attemps: {fail_count}")
    time.sleep(2)