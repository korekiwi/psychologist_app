def menu_items(request):
    menu = [
        {"title": "Главная", "url_name": "home", "icon": "bi-house"},
        {"title": "Консультирование", "url_name": "questions", "icon": 'bi-chat-right-dots'},
        {"title": "Записаться на прием", "url_name": "appointment", "icon": 'bi-pencil-square'},
    ]

    current_url_name = request.resolver_match.view_name

    for item in menu:
        item['is_active'] = current_url_name == item['url_name']

    return {'menu_items': menu}
