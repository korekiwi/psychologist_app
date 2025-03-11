def menu_items(request):
    menu = [
        {"title": "Копилка", "url_name": "materials"},
        {"title": "Главная", "url_name": "home"},
        {"title": "Консультирование", "url_name": "questions"},
    ]

    current_url_name = request.resolver_match.view_name

    for item in menu:
        item['is_active'] = current_url_name == item['url_name']

    return {'menu_items': menu}