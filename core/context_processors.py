def menu_items(request):
    menu = [
        {"title": "Главная", "url_name": "home", "url_hash": ""},
        {"title": "Обо мне", "url_name": "home", "url_hash": "#inf"},
        {"title": "Копилка", "url_name": "materials", "url_hash": ""},
        {"title": "Консультирование", "url_name": "questions", "url_hash": ""},
        {"title": "Запись на прием", "url_name": "appointment", "url_hash": ""},
    ]

    current_url_name = request.resolver_match.view_name

    for item in menu:
        item['is_active'] = current_url_name == item['url_name'] + item['url_hash']

    return {'menu_items': menu}