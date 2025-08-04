import re
from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.logout_list_item = SidebarListItemComponent(page, 'logout')


    def check_visible(self):
        self.dashboard_list_item.check_visible('Dashboard')
        self.courses_list_item.check_visible('Courses')
        self.logout_list_item.check_visible('Logout')

    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*//#/auth/login"))

