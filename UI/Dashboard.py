from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase

Window.size = (1000, 800)
Window.minimum_width, Window.minimum_height = Window.size



class ContentNavigationDrawer(MDBoxLayout):
    pass

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MLSGuru(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.load_kv("Dashboard.kv")


    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

MLSGuru().run()