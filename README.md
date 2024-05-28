# Sprint_5
В тестах используются:
- фикстуры для вызова драйвера и генерации данных для регистрации
- данные для аутентификации
- локаторы

### Файл **tests_authorization**
1. Вход по кнопке «Войти в аккаунт» на главной (**test_auth_through_main_page_visible_button_order**)
2. Вход через кнопку «Личный кабинет» (**test_auth_through_profile_visible_button_order**) 
3. Вход через кнопку в форме регистрации (**test_auth_through_registration_page_visible_button_order**)
4. Вход через кнопку в форме восстановления пароля (**test_auth_through_forgot_password_visible_button_order**)
5. Выход по кнопке «Выйти» в личном кабинете (**test_logout_through_profile_visible_button_login**)

### Файл **tests_registration**
1. Успешная регистрация (**test_registration_full_data_success_registration**)
2. Ошибка некорректного пароля при попытке зарегистрироваться с пароелм менее 6 символов (**test_registration_password_less_than_6_show_text_incorrect_password**)

### Файл test_open_pages
1. Переход в «Личный кабинет» по клику на «Личный кабинет» (**test_open_profile_visible_button_logout**)
2. Переход из личного кабинета в конструктор клику на «Конструктор» (**test_open_constructor_from_profile_click_constructor_visible_button_order**)
3. Переход из личного кабинета в конструктор клику на логотип (**test_open_constructor_from_profile_click_logo_visible_button_order**)
4. Переход к разделу "Начинки" (**test_switch_between_section_filling**)
5. Переход к разделу "Соусы" (**test_switch_between_section_sauce**)
6. Переход к разделу "Булки" (**test_switch_between_section_bakery**)