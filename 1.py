for i in range(1, 101):
    with open(f"{i}.html", "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Страница {i}</title>
</head>
<body>
    <h1>Это страница #{i}</h1>
</body>
</html>""")