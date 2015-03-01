from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _

class TestMenu(Menu):
    def get_nodes(self, request):
        return [NavigationNode(_('sample root page'), "/", 'root'),
                NavigationNode(_('sample settings page'), "/bye/", 'bye'),
                NavigationNode(_('sample account page'), "/hello/", 'hello'),
                NavigationNode(_('sample hi page'), "/hi/", 'hi'),
                NavigationNode(_('sample my profile page'), "/hello/world/",
                               'world', 'hello')]

menu_pool.register_menu(TestMenu)
