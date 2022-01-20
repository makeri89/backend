*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${SERVER}  localhost:3000
${BROWSER}  Firefox
${DELAY}  0
${HOME URL}  http://${SERVER}

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}  service_log_path=${{os.path.devnull}}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Open Browser To Index Page
    Location Should Be  ${HOME URL}

Main Page Should Be Open
    Title Should Be  React App

Go To Main Page
    Go To  ${HOME URL}
