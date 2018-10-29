*** Settings ***
Library   SeleniumLibrary
Library   Resources/APP_Resource.py

*** Test Cases ***

Start Test
    Start Test
User can input First and Last name
    enter name
Gender radio button is selectable
    radio button
Language checkbox is selectable
    check box
Age List drop down can be specified
    select age list
Submit option is selectable
    submit
Alert box javascript is selectable and cleared
    get alert
Window 2 can be triggered
    switch window2
Window 2 confirmation drop down confirmed
    select list 2
Window 3 can be triggered
    switch window3
Window 3 confirmation drop down confirmed
    select list 3
End Test
    end test


