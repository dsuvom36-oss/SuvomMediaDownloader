import customtkinter as ctk

from core.database import initialize_database
from core.settings import load_settings

from core.task_manager import TaskManager
from core.task_queue import TaskQueue

from core.event_bus import event_bus
from core.event_types import Event

from gui.pages.home import HomePage
from gui.pages.search import SearchPage
from gui.pages.downloads import DownloadsPage
from gui.pages.history import HistoryPage
from gui.pages.notifications import NotificationsPage
from gui.pages.activity import ActivityPage
from gui.pages.settings import SettingsPage
from gui.about import AboutPage

from gui.widgets.sidebar import Sidebar
from gui.widgets.status_bar import StatusBar


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ==========================================
        # Initialize Application
        # ==========================================

        initialize_database()

        self.settings = load_settings()

        ctk.set_appearance_mode(self.settings.get("theme", "Dark"))

        ctk.set_default_color_theme("blue")

        self.title("Suvom Media Downloader")
        self.geometry("1450x850")

        # ==========================================
        # Core Managers
        # ==========================================

        self.task_manager = TaskManager()

        self.task_queue = TaskQueue(self.task_manager)

        # ==========================================
        # Sidebar
        # ==========================================

        self.sidebar = Sidebar(self, self.show_page)

        self.sidebar.pack(side="left", fill="y")

        # ==========================================
        # Main Container
        # ==========================================

        self.container = ctk.CTkFrame(self, fg_color="transparent")

        self.container.pack(side="right", fill="both", expand=True)

        # ==========================================
        # Pages
        # ==========================================

        self.pages = {
            "Home": HomePage(self.container, self.task_manager),
            "Search": SearchPage(self.container),
            "Downloads": DownloadsPage(
                self.container, self.task_manager, self.task_queue
            ),
            "History": HistoryPage(self.container),
            "Notifications": NotificationsPage(self.container),
            "Activity": ActivityPage(self.container),
            "Settings": SettingsPage(self.container),
            "About": AboutPage(self.container),
        }

        for page in self.pages.values():

            page.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ==========================================
        # Status Bar
        # ==========================================

        self.status_bar = StatusBar(self)

        self.status_bar.pack(side="bottom", fill="x")

        # ==========================================
        # Show Default Page
        # ==========================================

        self.show_page("Home")

        # ==========================================
        # Application Started
        # ==========================================

        event_bus.publish(Event.APPLICATION_STARTED)

        # ==========================================
        # Close Event
        # ==========================================

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    # ==========================================

    def show_page(self, page_name):

        page = self.pages.get(page_name)

        if page:

            page.tkraise()

            event_bus.publish(Event.PAGE_CHANGED, page=page_name)

    # ==========================================

    def on_close(self):

        event_bus.publish(Event.APPLICATION_CLOSED)

        self.destroy()


if __name__ == "__main__":

    app = App()

    app.mainloop()
