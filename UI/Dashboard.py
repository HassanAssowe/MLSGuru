from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivymd.uix.tab import MDTabsBase
import WebScrapper.Standings_Data

Window.size = (1000, 800)
Window.minimum_width, Window.minimum_height = Window.size



class ContentNavigationDrawer(MDBoxLayout):
    pass

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MLSGuru(MDApp):
    global easternConference
    global westernConference
    westernConference = []

    easternConference, westernConference = WebScrapper.Standings_Data.parseData()


    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.load_kv("Dashboard.kv")

    def on_start(self):
        for i in range(14):
            if i < 9:
                rank = str(i+1).center(10,' ')
            else:
                rank = str(i+1).center(8, ' ')
            east_team_name = str(easternConference[i].get_name())
            west_team_name = str(westernConference[i].get_name())

            self.root.ids.east_container.add_widget(
            OneLineListItem(text=rank + f"{east_team_name :<0}")
            )

            self.root.ids.west_container.add_widget(
            OneLineListItem(text=rank + f"{west_team_name :<0}")
            )


            self.root.ids.form.add_widget(
            Label(text = "W")
            )

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