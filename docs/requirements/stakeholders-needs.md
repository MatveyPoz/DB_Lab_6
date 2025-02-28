# Запити зацікавлених осіб

## <span id = "introduction">Вступ</span>

Цей документ містить опис концепцій, методів та підходів, пов'язаних із розробкою системи організації та управління опитуваннями експертів. Він охоплює ключові терміни, методології експертних опитувань, аналіз існуючих методів та підходів до вирішення завдань, а також рекомендації для створення ефективної інформаційної системи управління опитуваннями. Документ має на меті дати повне уявлення про етапи планування, проведення та аналізу експертних опитувань, враховуючи найкращі світові практики в цій сфері.

### <span id = "target">Мета</span> 

Метою проекту є розробка та впровадження інформаційної системи для організації та управління експертними опитуваннями. Ця система повинна полегшити процес збору, обробки та аналізу експертних оцінок для підтримки прийняття рішень у різних галузях. Основними завданнями проекту є забезпечення анонімності учасників, автоматизація багатократних раундів опитувань, статистична обробка результатів та надання інструментів для візуалізації й аналізу зібраних даних. Проект спрямований на підвищення точності, об’єктивності та зручності проведення експертних оцінок, що дозволить швидко і якісно отримувати узгоджені висновки для вирішення складних питань.

### <span id = "context">Контекст</span>

Цей документ описує вимоги та рекомендації для розробки інформаційної системи, призначеної для організації та управління експертними опитуваннями. Він встановлює ключові функціональні можливості, методи опитувань та підходи до оцінки експертних висновків та служить базою для створення системи, яка автоматизує процеси збору, обробки та аналізу експертних думок.


### <span id = "glossary">Основні визначення та скорочення</span>

1. Предметна область - це сукупність об'єктів, понять та процесів, які пов'язані з певною сферою людської діяльності чи знання

2. Зацікавлені особи (stakeholders) - фізичні та юридичні особи, які мають легітимний інтерес у діяльності організації, тобто певною мірою залежать від неї або можуть впливати на її діяльність.

3. Бізнес-сценарій (сценарій використання, use case) - опис спостережуваної взаємодії між актором (або акторами) та рішенням, яка відбувається, коли актор використовує систему для досягнення певної мети.

4. FURPS — акронім, який використовується для класифікації вимог до програмного забезпечення. Він розшифровується як:
    - Functionality (Функціональність): основні функції системи, коректність, безпека.
    - Usability (Зручність використання): інтерфейс, документація.
    - Reliability (Надійність): частота збоїв, відмовостійкість.
    - Performance (Продуктивність): час відгуку, ресурсомісткість.
    - Supportability (Підтримуваність): можливість обслуговування, розширюваність, тестування.
FURPS допомагає систематизувати як функціональні, так і нефункціональні вимоги до програмних продуктів.

5. REST (REpresentational State Transfer, «передача репрезентативного стану») — підхід до архітектури мережевих протоколів, які надають доступ до інформаційних ресурсів.

6. API (Application Programming Interface “прикладний програмний інтерфейс”) - підхід до архітектури мережевих протоколів, які надають доступ до інформаційних ресурсів.

7. SOLID — це набір з п'яти принципів об'єктно-орієнтованого програмування, які допомагають розробникам створювати гнучкі та підтримувані системи:
    - Single Responsibility Principle (Принцип єдиної відповідальності) — кожен клас повинен мати лише одну причину зміни.
    - Open/Closed Principle (Принцип відкритості/закритості) — класи мають бути відкриті для розширення, але закриті для модифікації.
    - Liskov Substitution Principle (Принцип підстановки Барбари Лисков) - підкласи повинні замінювати батьківські класи без порушення функціональності.
    - Interface Segregation Principle (Принцип поділу інтерфейсу) — клієнти не повинні залежати від інтерфейсів, які вони не використовують.
    - Dependency Inversion Principle (Принцип інверсії залежностей) — високорівневі модулі не повинні залежати від низькорівневих, обидві групи мають залежати від абстракцій.

8. DRY (Don`t Repeat Yourself) - це принцип розробки програмного забезпечення, націлений на зниження повторення різного роду інформації, особливо в системах з безліччю шарів абстрагування

9. KISS (Keep It Simple Stupid) - процес і принцип проектування, при якому простота системи декларується як основна мета та/або цінність.






## <span id = "processes">Характеристика ділових процесів</span>

### Процес 1: Створення опитування

| **ID**             | SurveyCreation                     |
|--------------------|------------------------------------|
| **Назва**          | Створення опитування               |
| **Учасники**       | Адміністратор, Система             |
| **Передумови**     | Адміністратор авторизований на платформі та має права для створення опитування. |
| **Результат**      | Створене нове опитування з доданими питаннями. |
| **Виключні ситуації** | Недостатньо прав для створення опитування, відсутні необхідні дані (назва, опис тощо). |
| **Основний сценарій** | 1. Адміністратор входить на платформу. <br> 2. Вибирає опцію створення нового опитування. <br> 3. Вводить назву, опис та додає питання. <br> 4. Зберігає опитування. <br> 5. Опитування стає доступним для експертів. |

---

### Процес 2: Реєстрація експерта на платформі

| **ID**             | UserRegistration                   |
|--------------------|------------------------------------|
| **Назва**          | Реєстрація експерта на платформі   |
| **Учасники**       | Користувач (експерт), Система      |
| **Передумови**     | Користувач не має акаунту на платформі. |
| **Результат**      | Створено акаунт експерта з підтвердженою електронною адресою та спеціалізацією. |
| **Виключні ситуації** | Неправильна або вже зареєстрована електронна адреса, помилки у формі. |
| **Основний сценарій** | 1. Користувач заповнює реєстраційну форму. <br> 2. Підтверджує email через посилання. <br> 3. Отримує доступ до платформи. |

---

### Процес 3: Проходження опитування

| **ID**             | SurveyCompletionProcess            |
|--------------------|------------------------------------|
| **Назва**          | Проходження опитування             |
| **Учасники**       | Користувач (експерт), Система      |
| **Передумови**     | Є активне опитування, експерт зареєстрований або анонімний. |
| **Результат**      | Відповіді збережено в системі.     |
| **Виключні ситуації** | Відсутній доступ до опитування, технічні проблеми з поданням. |
| **Основний сценарій** | 1. Користувач відкриває опитування. <br> 2. Відповідає на питання. <br> 3. Система зберігає відповіді. <br> 4. Після завершення користувач подає відповіді. |

---

### Процес 4: Перегляд результатів опитування

| **ID**             | SurveyResultsReview                |
|--------------------|------------------------------------|
| **Назва**          | Перегляд результатів опитування    |
| **Учасники**       | Адміністратор, Експерт             |
| **Передумови**     | Опитування завершено з достатньою кількістю відповідей. |
| **Результат**      | Згенеровано звіт з результатами.   |
| **Виключні ситуації** | Відсутні відповіді для аналізу, технічні проблеми з відображенням результатів. |
| **Основний сценарій** | 1. Система агрегує відповіді. <br> 2. Генерується звіт. 3. Користувач обирає спосіб отримання результату (завантажити pdf/надіслати на пошту). <br> 4. Результат надходить до користувача. <br><br> *Адміністратор може переглянути звіт у адмін-панелі.|

---

### Процес 5: Редагування опитування

| **ID**             | SurveyEditing                      |
|--------------------|------------------------------------|
| **Назва**          | Редагування опитування             |
| **Учасники**       | Адміністратор, Система             |
| **Передумови**     | Існуюче опитування, яке ще не завершено. |
| **Результат**      | Опитування відредаговане, зміни збережено. |
| **Виключні ситуації** | Опитування вже запущено або завершено, адміністратор не має прав на редагування. |
| **Основний сценарій** | 1. Адміністратор вибирає опитування для редагування. <br> 2. Вносить зміни до деталей або питань. <br> 3. Зберігає зміни. <br> 4. Система оновлює опитування. |

---

### Процес 6: Оцінка опитування

| **ID**             | SurveyReviewByExpertProcess        |
|--------------------|------------------------------------|
| **Назва**          | Оцінка опитування                  |
| **Учасники**       | Користувач (експерт), Система      |
| **Передумови**     | Користувач завершив опитування та авторизований. |
| **Результат**      | Відгук збережено та доступний адміністратору. |
| **Виключні ситуації** | Відгук не збережено через технічні проблеми, користувач не має прав залишити відгук. |
| **Основний сценарій** | 1. Користувач завершує опитування. <br> 2. Залишає відгук та оцінку. <br> 3. Система зберігає відгук. <br> 4. Адміністратор може переглядати відгуки. |


## <span id = "describe">Короткий огляд продукту</span>

### 1. Експерти

**Опис:**  
Експерти – це фахівці з конкретної галузі, які мають досвід і знання, що можуть бути корисними для проведення опитувань. Вони можуть представляти різні сектори: науку, бізнес, освіту, медицину тощо.

**Потреби:**
- **Зручність використання:** Інтуїтивно зрозумілий інтерфейс, який дозволяє легко брати участь в опитуваннях.
- **Анонімність:** Можливість давати відповіді анонімно, щоб забезпечити чесність та відкритість.
- **Часова гнучкість:** Можливість заповнювати опитування у зручний час.
- **Зворотний зв'язок:** Інформація про результати опитувань, щоб відчувати, що їхні думки враховуються.

### 2. Організатори опитувань

**Опис:**  
Це особи або команди, які розробляють, реалізують і керують опитуваннями. Вони можуть працювати в академічних установах, дослідницьких компаніях або організаціях, що займаються консалтингом.

**Потреби:**
- **Інструменти для створення опитувань:** Легкий доступ до шаблонів і можливість налаштування питань.
- **Управління запрошеннями:** Можливість легко запрошувати експертів через електронну пошту або інші канали.
- **Моніторинг:** Інструменти для відстеження участі експертів і статусу заповнення опитувань.
- **Аналіз результатів:** Функції для швидкого перегляду та аналізу зібраних даних, включаючи графіки та діаграми.

### 3. Аналізатори даних

**Опис:**  
Це спеціалісти, які обробляють та аналізують дані, отримані з опитувань. Вони можуть працювати в дослідницьких організаціях або великих компаніях.

**Потреби:**
- **Доступ до звітів:** Можливість генерувати звіти з даними, представленими в зрозумілому форматі.
- **Експорт даних:** Інструменти для експорту даних в різних форматах (Excel, CSV, PDF) для подальшого аналізу.
- **Статистичні інструменти:** Інтеграція з програмами для статистичного аналізу (наприклад, SPSS, R) для глибшого аналізу.

### 4. Менеджери проектів

**Опис:**  
Ці користувачі відповідають за загальну координацію та управління проектами, пов'язаними з опитуваннями. Вони можуть працювати в різних секторах, таких як бізнес, наука або освіта.

**Потреби:**
- **Огляд статусу:** Панель управління для моніторингу прогресу опитувань, термінів виконання завдань і участі експертів.
- **Управління термінами:** Календар для планування важливих дат і дедлайнів.
- **Комунікація:** Інструменти для зв'язку з організаторами та експертами, щоб забезпечити ефективну співпрацю.

### 5. IT-персонал

**Опис:**  
Фахівці, відповідальні за технічну підтримку системи. Вони можуть бути частиною внутрішньої команди або зовнішніх постачальників послуг.

**Потреби:**
- **Управління базами даних:** Інструменти для моніторингу та підтримки бази даних, що зберігає результати опитувань.
- **Безпека:** Забезпечення захисту даних експертів і конфіденційності інформації.
- **Технічна підтримка:** Швидка реакція на проблеми, що виникають, та навчання користувачів.

### 6. Замовники опитувань

**Опис:**  
Це організації або окремі особи, які ініціюють опитування для отримання експертних висновків. Вони можуть бути представниками бізнесу, науки або державних установ.

**Потреби:**
- **Налаштування опитувань:** Можливість адаптувати опитування під свої специфічні потреби і цілі.
- **Отримання звітів:** Легкий доступ до результатів з можливістю глибокого аналізу.
- **Оцінка ефективності:** Інструменти для оцінки корисності отриманих даних для прийняття рішень.

## <span id = "functionality">Функціональність</span>

### Функціональність для користувача (експерта)

1. **Реєстрація та вхід:**
   - Можливість створення облікового запису та входу в систему.
   - Відновлення пароля.

2. **Участь в опитуваннях:**
   - Отримання запрошень на участь в опитуваннях через електронну пошту.
   - Легкий доступ до активних опитувань.
   - Заповнення опитувань у зручному для себе темпі.

3. **Анонімність:**
   - Можливість залишити анонімні відповіді.
   - Інформування про використання даних.

4. **Перегляд результатів:**
   - Доступ до зведених результатів попередніх опитувань.
   - Можливість отримувати зворотний зв'язок щодо своїх відповідей.

5. **Особистий кабінет:**
   - Перегляд історії участі в опитуваннях.
   - Налаштування профілю (персональна інформація, уподобання).

### Функціональність для адміністратора (організатора опитувань)

1. **Управління користувачами:**
   - Додавання, редагування та видалення облікових записів експертів.
   - Управління ролями та доступом користувачів.

2. **Створення та налаштування опитувань:**
   - Інструменти для створення нових опитувань із використанням шаблонів або налаштувань.
   - Налаштування типів питань (вибір, відкриті питання, шкали оцінювання).

3. **Управління запрошеннями:**
   - Надсилання запрошень на участь в опитуваннях.
   - Відстеження статусу запрошень (надіслано, прийнято, відмовлено).

4. **Моніторинг та аналіз:**
   - Панель моніторингу для відстеження участі експертів.
   - Генерація звітів з результатами опитувань.
   - Візуалізація даних (графіки, діаграми).

5. **Налаштування системи:**
   - Керування налаштуваннями платформи (повідомлення, інтерфейс).
   - Встановлення параметрів безпеки та конфіденційності.

6. **Технічна підтримка:**
   - Надання підтримки користувачам у разі виникнення проблем.
   - Моніторинг технічних питань та їх вирішення.


## <span id = "usability">Практичність</span>

1. **Інтуїтивний інтерфейс**; користувач не повинен зіткунтися з проблемою створення хоча б простих опитуваннь

2. **Кастомізація**; необхідно забезпечити можливість змінювати дизайн опитувань згідно з дизайн-кодом організації або уподобаннь користувачів

3. **Підтримка різних засобів опитувань**; користувач або організація повинен мати можливість створювати різні види опитувань (обрати зі списку, оцінка за шкалою, текстова відповідь тощо)

4. **Підтримка якомога більших платформ**; для максимального охвату користувачів сервіс має коректно працювати на максимально можливій кількості платформ та браузерів

5. **Підтримка якомога більших мов**; для макимального охвату користувачів сервіс повинен надавати можливість створювати опитування на зручній для учасника опитування мові

6. **Підтримка користувачів або організацій** 
- максимально швидка технічна підтримка через вбудований чат, електронну пошту або телефон; 
- надання користувачас навчальних матеріалів та FAQ

7. **Візуалізація, аналітка та експорт даних**; 
- можливість відображення отриманної з опитувань інформації за певними правилами (графіки та діаграми); 
- експорт статистичних даних у форматі .csv, .pdf, .json тощо, або засобами REST API

## <span id = "reliability">Надійність</span>

1. **Швидкодія сервісу**; стабільно малий час реакції незалежно від рівня навантаження на систему

2. **Безпека та конфіденційність** 
- викорситання протоколів шифрувань при передачі даних з/на сервер; 
- регулярні оновлення безпеки для захисту від погроз та вразливовістей;
- розділення прав для різних категорій користувачів

3. **Безпека зберігання даних**; регулярне та автоматичне створення резервних копій та їх зберігання на локальних носіях

4. **можливість масштабування**; пітримка можливості вертикального та горизонтального масштабування системи для підтримки зростаючій кількості користувачів, опитуваннь та їх учасників

5. **Відповідність стандартів відповідності щодо надійності та безпеки системи**; система повинна відповідати місцевим стандартам надійності та конфіденційності для можливості роботи в певних країнах

6. **Feedback від користувачів**; користувачі та учасники опитувань повинні мати можливість відправляти відгуки, пропозиції, звіти о несправностях

## <span id = "performance">Продуктивність</span>

1. **Мінімізоване використання системних ресурсів**

2. **Використання оптимізованих SQL скриптів**

3. **Мінімальна швидкість реагування на запити завдяки RESTFull архітектурі**

4. **Мінімалізований дизайн та інтерфейся, який в свою чергу не потребує додаткових відео-ресурсів**

## <span id = "supportability">Експлуатаційна придатність</span>

1. **Регулярні оновлення та виправлення недоліків системи**

2. **Постійна підтримка та моніторинг роботи системи**

3. **Деталізована документація системи для швидкого ознайомлення та розуміння роботи системи**

4. **Відкритий вихідний код**



## Короткий зміст

- [**Вступ**](#introduction)
    - [Мета](#target)
    - [Контекст](#context)
    - [Основні визначення та скорочення](#glossary)
    - [Посилання](#links)

- [**Характеристика ділових процесів**](#processes)

- [**Короткий огляд продукту**](#describe)

- [**Функціональність**](#functionality)

- [**Практичність**](#usability)

- [**Надійність**](#reliability)

- [**Продуктивність**](#performance)

- [**Експлуатаційна придатність**](#supportability)

## Посилання

### <span id = "links"></span>
1. [Предметна область](https://uk.wikipedia.org/wiki/Предметна_область#cite_note-1)
2. [Ворончак І. Соціальна відповідальність бізнесу як соціально-економічний феномен // Відповідальна економіка. — 2009. — № 1. — С. 90–103.](http://www.market-infr.od.ua/journals/2021/62_2021/3.pdf)
3. [BABOK® Guide v3 Glossary - Ukrainian Translation. Український переклад Додатку А: Глосарій до BABOK® Guide v3](https://www.iiba.org/globalassets/standards-and-resources/glossary/files/babok-v3-glossary-ukrainian.pdf)
4. [FURPS](https://uk.wikipedia.org/wiki/FURPS)
5. [REST](https://uk.wikipedia.org/wiki/REST)
6. [API](https://uk.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%BD%D0%B8%D0%B9_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BD%D0%B8%D0%B9_%D1%96%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81)
7. [SOLID](https://en.wikipedia.org/wiki/SOLID)
8. [DRY](https://ru.wikipedia.org/wiki/Don’t_repeat_yourself)
9. [KISS](https://uk.wikipedia.org/wiki/Принцип_«KISS»)