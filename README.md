# Anti-plagiarism
Machine Learning Весна'23

Write an anti-plagiarism program that compares two Python program texts and evaluates their similarity.

To solve this problem, I used the Wagner-Fischer algorithm

![image](https://user-images.githubusercontent.com/83032359/211209946-95e446d2-108c-4d68-97e5-f6d87184193a.png)


# Интерфейс
Нужно реализовать скрипт compare.py, который принимает файл со списком пар документов и путь до выходного файла. Скрипт должен сравнить пары документов и записать в выходной файл оценки похожести текстов программ.

## Данные
plagiat.zip был распакован и извлечен в то же место, куда и compare.py  

![image](https://user-images.githubusercontent.com/83032359/211210386-7f7629ab-b596-4e6b-8df2-01c42d3df8e7.png)


### Пример входного файла input.txt
![image](https://user-images.githubusercontent.com/83032359/211210521-ff40f662-65ba-490c-b8cb-c7030206c570.png)

### Пример выходного файла scores.txt
![image](https://user-images.githubusercontent.com/83032359/211210574-1680338d-1939-4f82-87c4-215ea420ea39.png)

### Вызов через консоль
![image](https://user-images.githubusercontent.com/83032359/211210776-b0273fe5-83e4-4d5e-91ec-fd1a2a42027c.png)


# Особенности

• Реализовать консольный интерфейс через argparse  
•	Для анализа кода использовал ast  
• Использовал библиотеку регулярных выражений re  
• Алгоритм Вагнера-Фишера и нормализация были реализованы в functions.py
