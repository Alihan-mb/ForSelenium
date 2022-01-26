import pytest
import self

from AnotherTest.conftest import init_driver


@pytest.mark.usefixtures("init_driver")
class Test_thisthingg:
    pass

class TestingIt(Test_thisthingg):
    def test_this(self):
        self.driver.find_element_by_link_text("Add/Remove Elements").click()
        mama = self.driver.find_elements_by_css_selector("button[onclick='addElement()']")

        number = 1
        while number < 6:
            for mam in mama:
                mam.click()

            number = number+1

        papa = self.driver.find_elements_by_css_selector("button[class='added-manually']")

        i = 1

        while i < 5:
            for pap in papa:
                if pap.is_displayed():
                    pap.click()
            break