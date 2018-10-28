*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      http://www.teachmeselenium.com/automation-practice/
${browser}  Chrome

*** Keywords ***
Start Test
    go to  ${url}

End Test
    close browser
