# myapp/templatetags/menu_tags.py
from django import template
from myapp.models import MenuItem

register = template.Library()

def build_menu(menu_items, current_url):
    menu_html = '<ul>'
    for item in menu_items:
        is_active = current_url == item.url or current_url == item.named_url
        menu_html += f'<li{" class=active" if is_active else ""}><a href="{item.url or item.named_url}">{item.name}</a>'
        children = MenuItem.objects.filter(parent=item)
        if children:
            menu_html += build_menu(children, current_url)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html

@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = MenuItem.objects.filter(name=menu_name, parent=None)
    return build_menu(menu_items, current_url)
