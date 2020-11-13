@sd_test12_bot
Feature: finbot_spd_charity

  Scenario Outline: st.family
    Given client send message -/start-
     And client click the button -Благодійність-
     And client click the button -<button>-
     And client send message -запит-
     And client click the button -Відмінити тікет-
    When client click the button -Так-
    Then client check message -Тікет скасований-1138-
    Examples: transfer types
        |  button                                         |
        |  ST.FAMILY                                      |
        |  ST.HELP                                        |
        |  Інші проекти                                   |
        |  Створити тікет на іншу тему в поточній категорії|
