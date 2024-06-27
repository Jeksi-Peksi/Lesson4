from testpage import OperationsHelper

def test_step1(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("Dusha1")
    testpage.enter_pass("dd666a4b5a")
    testpage.click_login_button()
    assert testpage.get_login_text() == "Hello, Dusha1"
