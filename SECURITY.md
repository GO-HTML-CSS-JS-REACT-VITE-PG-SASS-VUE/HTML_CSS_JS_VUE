https://go-html-css-js-react-vite-pg-sass-vue.github.io/HTML_CSS_JS_VUE/

git add .
git commit -m "роки - задания с решением"
git push origin main


git remote add origin https://github.com/GO-HTML-CSS-JS-REACT-VITE-PG-SASS-VUE/HTML_CSS_JS_VUE.git
git pull origin main
git status
git add .
git commit -m "Мои изменения"
git push origin 

# HTML_CSS_JS_VUE
Пример 1: Базовое создание БД, таблицы и операции CRUD
Это основа основ. Показывает, как подключиться к БД, создать таблицу и выполнять основные операции (Create, Read, Update, Delete).

```python
import sqlite3

# 1. Подключение к БД (создает файл, если его нет)
def create_connection():
    conn = sqlite3.connect('my_database.db')
    return conn

# 2. Создание таблицы
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        )
    ''')
    conn.commit()
    print("Таблица 'users' создана или уже существует.")

# 3. Вставка данных (Create)
def insert_user(conn, name, age, email):
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (name, age, email)
            VALUES (?, ?, ?)
        ''', (name, age, email))
        conn.commit()
        print(f"Пользователь {name} добавлен.")
    except sqlite3.IntegrityError:
        print(f"Ошибка: email {email} уже существует.")

# 4. Чтение данных (Read)
def get_all_users(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# 5. Обновление данных (Update)
def update_user_age(conn, user_id, new_age):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users
        SET age = ?
        WHERE id = ?
    ''', (new_age, user_id))
    conn.commit()
    print(f"Возраст пользователя с id={user_id} обновлен.")

# 6. Удаление данных (Delete)
def delete_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    print(f"Пользователь с id={user_id} удален.")

# Запуск примера
if __name__ == "__main__":
    conn = create_connection()
    create_table(conn)
    
    insert_user(conn, "Анна", 28, "anna@mail.com")
    insert_user(conn, "Иван", 35, "ivan@mail.com")
    
    print("\nВсе пользователи:")
    get_all_users(conn)
    
    update_user_age(conn, 1, 29)
    delete_user(conn, 2)
    
    print("\nПосле изменений:")
    get_all_users(conn)
    
    conn.close()
```
Пример 2: Анализ данных с агрегацией и фильтрацией
Показывает, как использовать SQL для вычислений — агрегирующие функции, группировка и фильтрация.

```python
import sqlite3

# Создаем тестовые данные о продажах
def setup_sales_data(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            product TEXT,
            category TEXT,
            amount REAL,
            sale_date DATE
        )
    ''')
    
    # Очищаем и добавляем тестовые данные
    cursor.execute("DELETE FROM sales")
    test_data = [
        ('Ноутбук', 'Электроника', 50000.0, '2024-01-15'),
        ('Мышь', 'Электроника', 2500.0, '2024-01-15'),
        ('Книга', 'Книги', 800.0, '2024-01-16'),
        ('Ноутбук', 'Электроника', 45000.0, '2024-01-17'),
        ('Книга', 'Книги', 1200.0, '2024-01-17'),
    ]
    cursor.executemany('INSERT INTO sales (product, category, amount, sale_date) VALUES (?, ?, ?, ?)', test_data)
    conn.commit()

# Аналитические запросы
def run_sales_analysis(conn):
    cursor = conn.cursor()
    
    # 1. Общая выручка
    cursor.execute('SELECT SUM(amount) FROM sales')
    total_revenue = cursor.fetchone()[0]
    print(f"Общая выручка: {total_revenue:.2f} руб.")
    
    # 2. Выручка по категориям (GROUP BY)
    print("\nВыручка по категориям:")
    cursor.execute('''
        SELECT category, SUM(amount), COUNT(*)
        FROM sales 
        GROUP BY category
    ''')
    for category, total, count in cursor.fetchall():
        print(f"  {category}: {total:.2f} руб. ({count} продаж)")
    
    # 3. Товары с продажами > 30000 (HAVING)
    print("\nКрупные продажи (>30000 руб.):")
    cursor.execute('''
        SELECT product, SUM(amount)
        FROM sales 
        GROUP BY product
        HAVING SUM(amount) > 30000
    ''')
    for product, total in cursor.fetchall():
        print(f"  {product}: {total:.2f} руб.")

if __name__ == "__main__":
    conn = sqlite3.connect('sales.db')
    setup_sales_data(conn)
    run_sales_analysis(conn)
    conn.close()
```
Пример 3: Продвинутые запросы с JOIN и подзапросами
Демонстрирует работу со связанными таблицами и сложными запросами.

```python
import sqlite3

def create_related_tables(conn):
    cursor = conn.cursor()
    
    # Таблица сотрудников
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department_id INTEGER
        )
    ''')
    
    # Таблица отделов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            budget REAL
        )
    ''')
    
    # Тестовые данные
    cursor.execute("DELETE FROM departments")
    cursor.execute("DELETE FROM employees")
    
    departments = [(1, 'IT', 100000), (2, 'Sales', 80000)]
    employees = [
        (1, 'Алексей', 1), 
        (2, 'Мария', 2), 
        (3, 'Дмитрий', 1),
        (4, 'Ольга', 2)
    ]
    
    cursor.executemany('INSERT INTO departments VALUES (?, ?, ?)', departments)
    cursor.executemany('INSERT INTO employees VALUES (?, ?, ?)', employees)
    conn.commit()

def run_advanced_queries(conn):
    cursor = conn.cursor()
    
    # INNER JOIN: сотрудники с названиями отделов
    print("Сотрудники и их отделы:")
    cursor.execute('''
        SELECT e.name, d.name 
        FROM employees e
        JOIN departments d ON e.department_id = d.id
    ''')
    for employee_name, department_name in cursor.fetchall():
        print(f"  {employee_name} -> {department_name}")
    
    # Подзапрос: сотрудники отдела с максимальным бюджетом
    print("\nСотрудники в самом богатом отделе:")
    cursor.execute('''
        SELECT e.name 
        FROM employees e
        WHERE e.department_id = (
            SELECT id FROM departments 
            ORDER BY budget DESC 
            LIMIT 1
        )
    ''')
    for (employee_name,) in cursor.fetchall():
        print(f"  {employee_name}")

if __name__ == "__main__":
    conn = sqlite3.connect('company.db')
    create_related_tables(conn)
    run_advanced_queries(conn)
    conn.close()
```
Пример 4: Интеграция Pandas и SQL для анализа
Показывает мощь связки Pandas + SQL для анализа и визуализации данных.

```python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def analyze_with_pandas():
    # Подключение к БД через Pandas
    conn = sqlite3.connect('sales.db')
    
    # Чтение данных прямо в DataFrame
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    
    print("Данные из БД:")
    print(df.head())
    
    # Анализ средствами Pandas
    print("\nСтатистика по продажам:")
    print(df['amount'].describe())
    
    # Группировка и агрегация
    category_stats = df.groupby('category')['amount'].agg(['sum', 'mean', 'count'])
    print(f"\nСтатистика по категориям:\n{category_stats}")
    
    # Визуализация
    df.groupby('category')['amount'].sum().plot(kind='bar', title='Выручка по категориям')
    plt.ylabel('Сумма (руб.)')
    plt.show()
    
    conn.close()

if __name__ == "__main__":
    analyze_with_pandas()
```
Пример 5: Практический проект — Анализ эффективности маркетинга
Мини-проект, объединяющий несколько техник для решения бизнес-задачи.

```python
import sqlite3
import pandas as pd
from datetime import datetime, timedelta

def setup_marketing_data(conn):
    cursor = conn.cursor()
    
    # Таблица рекламных кампаний
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS campaigns (
            campaign_id INTEGER PRIMARY KEY,
            name TEXT,
            cost REAL,
            start_date DATE
        )
    ''')
    
    # Таблица конверсий
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversions (
            conversion_id INTEGER PRIMARY KEY,
            campaign_id INTEGER,
            revenue REAL,
            conversion_date DATE,
            FOREIGN KEY (campaign_id) REFERENCES campaigns (campaign_id)
        )
    ''')
    
    # Генерация тестовых данных
    cursor.execute("DELETE FROM campaigns")
    cursor.execute("DELETE FROM conversions")
    
    campaigns = [
        (1, 'Кампания в соцсетях', 5000, '2024-01-01'),
        (2, 'Email-рассылка', 3000, '2024-01-05'),
    ]
    
    conversions_data = [
        (1, 1, 15000, '2024-01-02'),
        (2, 1, 8000, '2024-01-03'),
        (3, 2, 12000, '2024-01-06'),
        (4, 1, 7000, '2024-01-08'),
    ]
    
    cursor.executemany('INSERT INTO campaigns VALUES (?, ?, ?, ?)', campaigns)
    cursor.executemany('INSERT INTO conversions VALUES (?, ?, ?, ?)', conversions_data)
    conn.commit()

def calculate_roi(conn):
    """Расчет ROI для маркетинговых кампаний"""
    
    query = '''
    SELECT 
        c.name AS campaign_name,
        c.cost,
        SUM(conv.revenue) AS total_revenue,
        (SUM(conv.revenue) - c.cost) AS net_profit,
        ROUND((SUM(conv.revenue) - c.cost) / c.cost * 100, 2) AS roi_percent
    FROM campaigns c
    LEFT JOIN conversions conv ON c.campaign_id = conv.campaign_id
    GROUP BY c.campaign_id
    HAVING total_revenue > 0
    ORDER BY roi_percent DESC
    '''
    
    df = pd.read_sql_query(query, conn)
    
    print("Эффективность маркетинговых кампаний:")
    print(df.to_string(index=False))
    
    # Дополнительный анализ
    print(f"\nОбщая ROI всех кампаний: {df['net_profit'].sum() / df['cost'].sum() * 100:.1f}%")
    
    return df

if __name__ == "__main__":
    conn = sqlite3.connect('marketing.db')
    setup_marketing_data(conn)
    roi_df = calculate_roi(conn)
    conn.close()
```
```
Ключевые навыки, которые охватывают эти примеры:
Основы SQLite в Python - подключение, выполнение запросов, управление транзакциями
SQL операции - CRUD, агрегации, GROUP BY, HAVING, JOIN, подзапросы
Работа с Pandas - чтение SQL в DataFrame, анализ и визуализация
Структуры данных Python - списки, кортежи, словари (в передаче параметров)
Функции и чистая логика - каждая задача в отдельной функции
Аналитическое мышление - от сырых данных к бизнес-метрикам (ROI, эффективность)
Практические кейсы - анализ продаж, маркетинговой эффективности
```