# TeleBot_Artist
## Задание
Создать сервис по рекомендации исполителей песен на основе текстов песен. На вход подается исполнитель. Выход представляет собой список из 10 исполнителей похожих по синтансу слов в своих песнях.
Система рекомендации построена на методе TF/IDF меры.

## Алгоритм решения задания
Главный алгоритм выолнения находится в файле musicrecomend/bot/api/main.py
1. Для создания первичной TF/IDF матрицы, с помощью парсинга сайта http://www.genius.com/, по спику исполнителей составляем словарь, где ключом явялется исполнитель, а значение - 20 его песен.
2. Слова песен преобразуются с помщью чистки песен от лишних слов, которые бы создавали шум, и лемматизации. Далее, с помощью метода TfidfVectorizer из библиотек Sklearn преобразум наши значения матрицы в вектора и вычислим из близость мерой TF/IDF.
3. Получаем на вход исполнителя и проверяем правильность его написания на сайте http://www.genius.com/, при необходимости производим исправление текста. Смотрим если ли такой исполнитель у нас в базе данных исполнителей.
4. Если такой исполнитель есть, то смотрим на TF/IDF матрицу и выводим Топ-10 рекоммендованных исполнителей.
5. Если такого артиста нет, но производим парсинг 20 песен этого артиста(если они имеются).
6. Далее производим преобразования, описанные в пунктах 2-4 и выводим пользователю Топ-10 рекоммендованных испольнителей.
7. При этом все данные о новом исполнителе сохраняются в нашу базу данных. Так же сохраняются логи об имени пользователя, его ID и запрос в файл log.log. 

## Способ проверки работоспособности бота
1. Запустить файл musicrecimend/bot/_bot.py .
2. В Телеграме открыть бота @PolundraHack и отправить ему запрос.
