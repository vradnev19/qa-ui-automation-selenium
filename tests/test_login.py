from pages.login_page import LoginPage

def test_valid_login(driver):
    lp = LoginPage(driver)
    lp.open()
    lp.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_invalid_login(driver):
    lp = LoginPage(driver)
    lp.open()
    lp.login("user", "wrong")
    assert "Username and password do not match any user" in lp.get_error()
