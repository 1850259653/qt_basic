from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QListWidget,
    QMainWindow,
    QMessageBox,
    QStackedWidget,
    QStatusBar,
    QToolBar,
    QWidget,
)

from app.data.http_demo import HttpDemoWidget
from app.data.json_demo import JsonDemoWidget
from app.data.sqlite_demo import SqliteDemoWidget
from app.data.threading_demo import ThreadingDemoWidget
from app.ui.advanced_views import AdvancedViewsDemo
from app.ui.basic_widgets import BasicWidgetsDemo
from app.ui.interaction_widgets import InteractionWidgetsDemo


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PySide6 + uv 客户端示例库")
        self.resize(1200, 760)

        self._setup_menus()
        self._setup_toolbar()
        self._setup_statusbar()
        self._setup_central()

    def _setup_menus(self) -> None:
        file_menu = self.menuBar().addMenu("文件")
        about_menu = self.menuBar().addMenu("帮助")

        exit_action = file_menu.addAction("退出")
        exit_action.triggered.connect(self.close)

        about_action = about_menu.addAction("关于")
        about_action.triggered.connect(self._show_about)

    def _setup_toolbar(self) -> None:
        toolbar = QToolBar("主工具栏")
        toolbar.setMovable(False)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        refresh_action = toolbar.addAction("刷新提示")
        refresh_action.triggered.connect(
            lambda: self.statusBar().showMessage("示例已就绪，可直接浏览左侧菜单", 3000)
        )

    def _setup_statusbar(self) -> None:
        bar = QStatusBar()
        bar.showMessage("欢迎使用客户端示例库")
        self.setStatusBar(bar)

    def _setup_central(self) -> None:
        container = QWidget()
        root = QHBoxLayout(container)

        self.nav = QListWidget()
        self.nav.setFixedWidth(240)
        self.stack = QStackedWidget()

        pages: list[tuple[str, QWidget]] = [
            ("UI - 基础控件", BasicWidgetsDemo()),
            ("UI - 高级视图", AdvancedViewsDemo()),
            ("UI - 交互组件", InteractionWidgetsDemo()),
            ("Data - JSON", JsonDemoWidget()),
            ("Data - SQLite", SqliteDemoWidget()),
            ("Data - HTTP", HttpDemoWidget()),
            ("Data - 线程", ThreadingDemoWidget()),
        ]

        for title, page in pages:
            self.nav.addItem(title)
            self.stack.addWidget(page)

        self.nav.currentRowChanged.connect(self.stack.setCurrentIndex)
        self.nav.setCurrentRow(0)

        root.addWidget(self.nav)
        root.addWidget(self.stack, stretch=1)

        self.setCentralWidget(container)

    def _show_about(self) -> None:
        QMessageBox.information(
            self,
            "关于",
            "该项目用于沉淀可复用的 PySide6 客户端代码片段。",
        )
