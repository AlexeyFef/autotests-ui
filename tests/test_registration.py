import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.registration
@pytest.mark.regression
@pytest.mark.parametrize('email, username, password',
        [
                ('user.name@gmail.com', 'username', 'password'),
        ]
)

def test_successfull_registration(registration_page: RegistrationPage, email: str, username: str, password: str, dashboard_page: DashboardPage):

        registration_page.vizit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_registration_form(email='user.name@gmail.com', username='username', password='password')
        registration_page.click_registration_button()

        dashboard_page.check_dashboard_title()


