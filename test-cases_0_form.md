### test-case: 0.1  
## Разблокирование кнопки  
Проверка разблокировки кнопки регистрации после заполнения чекбокса 
#### Test:  
test_0_form.py::  
test_register_btn_unblocked  
#### Предусловие:  
Открыть url: https://victoretc.github.io/webelements_information/  
Пустые поля формы  
#### Шаги:  
1. Ввести 'John Doe' в 'Name'  
2. Ввести '@pass12345*!' в 'Password'  
3. Отметить чекбокс  
#### Ожидаемый результат:   
Кнопка 'Register' разблокирована  
#### Постусловие:  
Перейти на стартовую страницу:  
https://victoretc.github.io/webelements_information/  

----------------------------------------------------------------
