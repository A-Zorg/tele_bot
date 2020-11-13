@sd_test12_bot
Feature: finbot_spd_operation_MoneyTransferTicket

  Background: reaching button - "Банк"
    Given client clicks a set of buttons
      | button_name     | element_code|
      | Операції по СПД |             |
      | Банк            |             |


  Scenario Outline: Transfer money to bank card
    Given client click the button -<button>-
     And client click the button -Створити тікет на поточну тему-
    When client send message -123, 3456 4567 9467 1234-
    Then agent get message -123, 3456 4567 9467 1234-
    Examples: transfer types
        |  button                                              |   element_code     |
        |  Обмін валюти і перерахування на картку Приватбанк   |                    |
#        |  Обмін валюти і перерахування на картку інших банків |                    |
#        |  Перерахування грн на картку Приватбанк              |                    |
#        |  Перерахування грн на картку іншого банку            |                    |
