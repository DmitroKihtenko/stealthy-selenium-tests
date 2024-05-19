from driver import DriverManager
from fixtures import UserData
from pages import SignUpPage, SignInPage, UserSpacePage

APP_BASE_URL = "http://localhost:4200/stealthy/ui"
CHROME_LOCATION = "/snap/chromium/2851/usr/lib/chromium-browser"
FILE_LOCATION = "/home/pacman/Data/Projects/Python/stealthy-selenium-tests/Pipfile"


def test_sign_up_sign_out(
    manager: DriverManager, user_data: UserData
):
    sign_up_page = SignUpPage(manager, user_data)
    sign_up_page.navigate().type_login().type_password().submit()
    sign_up_page.assert_sign_up_success()
    sign_up_page.sign_out().assert_sign_out_success()


def test_sign_in_sign_out(
    manager: DriverManager, user_data: UserData
):
    sign_in_page = SignInPage(manager, user_data)
    sign_in_page.navigate().type_login().type_password().submit()
    sign_in_page.assert_sign_in_success()
    sign_in_page.sign_out().assert_sign_out_success()


def test_upload_download_file(
    manager: DriverManager, user_data: UserData
):
    sign_in_page = SignInPage(manager, user_data)
    sign_in_page.navigate().type_login().type_password().submit()
    sign_in_page.assert_sign_in_success()
    try:
        files_page = UserSpacePage(
            manager, user_data, 2, FILE_LOCATION
        )
        files_page.navigate().type_file().upload_file()
        files_page.check_file_uploaded()
        files_page.download_file()
        files_page.check_no_errors_on_page()
    finally:
        sign_in_page.sign_out().assert_sign_out_success()


def main():
    user_data = UserData()
    manager = DriverManager(APP_BASE_URL, CHROME_LOCATION)

    try:
        test_sign_up_sign_out(manager, user_data)
        test_sign_in_sign_out(manager, user_data)
        test_upload_download_file(manager, user_data)
    finally:
        manager.close()


if __name__ == "__main__":
    main()
