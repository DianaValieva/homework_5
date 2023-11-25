from selene.support.shared import browser
from selene import be, have, by
import os

def test_practice_form(open_browser):
    browser.open('https://app.qa.guru/automation-practice-form/')
    browser.element('.MuiBox-root .css-1vpe9z').click()
    browser.element('#\:r0\:').type("Diana")
    browser.element('#\:r1\:').type("Valieva")
    browser.all('.MuiInputBase-input').element_by(have.attribute('data-testid','email')).type("di7051@gmail.com")
    browser.element('#\:r3\:').type("9999999999")
    browser.element('#\:r4\:').click().type('30121991')
    browser.all('[role=button]')[0].element('..').click()
    browser.element('[data-value=English]').click()
    browser.all('[name=gender]').element_by(have.value('Female')).click()
    browser.all('.PrivateSwitchBase-input').element_by(have.attribute("value","Reading")).click()
    browser.all('[data-testid=hobbies]').element_by(have.value('Sports')).click()
    browser.all('[role=button]')[1].element('..').click()
    browser.element('[data-value=Arts]').press_enter()
    browser.element('[data-value="English"]').press_enter().press_escape()
    browser.all('[role=button]')[4].element('..').click()
    browser.element('[data-value=Alaska]').press_enter()
    browser.all('[role=button]')[5].element('..').click()
    browser.element('[data-value=Anchorage]').press_enter()
    browser.element('[type = submit]').press_enter()

    browser.all('h4.MuiTypography-root')[1].should(have.text('Thank you for submitting the form'))
    browser.all('p.MuiTypography-root')[2].should(have.text('Diana'))

