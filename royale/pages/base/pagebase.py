from royale.pages.headernav import HeaderNav


class PageBase:
    def __init__(self,driver):
        self.headerNav = HeaderNav(driver)