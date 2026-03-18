from __future__ import annotations

from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class AdvancedViewsDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        root = QVBoxLayout(self)

        title = QLabel("表格 / 列表 / 树形视图")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        root.addWidget(title)

        line = QHBoxLayout()
        line.addWidget(self._table_group(), stretch=2)
        line.addWidget(self._list_group(), stretch=1)
        line.addWidget(self._tree_group(), stretch=2)
        root.addLayout(line)

    def _table_group(self) -> QGroupBox:
        group = QGroupBox("QTableWidget")
        layout = QVBoxLayout(group)

        table = QTableWidget(4, 3)
        table.setHorizontalHeaderLabels(["ID", "姓名", "状态"])
        rows = [
            ("1", "Alice", "Active"),
            ("2", "Bob", "Pending"),
            ("3", "Cindy", "Active"),
            ("4", "David", "Disabled"),
        ]
        for r, row in enumerate(rows):
            for c, value in enumerate(row):
                table.setItem(r, c, QTableWidgetItem(value))

        layout.addWidget(table)
        return group

    def _list_group(self) -> QGroupBox:
        group = QGroupBox("QListWidget")
        layout = QVBoxLayout(group)

        lst = QListWidget()
        lst.addItems(["首页", "用户", "订单", "设置", "日志"])
        layout.addWidget(lst)
        return group

    def _tree_group(self) -> QGroupBox:
        group = QGroupBox("QTreeWidget")
        layout = QVBoxLayout(group)

        tree = QTreeWidget()
        tree.setHeaderLabels(["模块", "说明"])

        ui_root = QTreeWidgetItem(["UI", "界面相关"])
        ui_root.addChild(QTreeWidgetItem(["basic_widgets", "基础控件"]))
        ui_root.addChild(QTreeWidgetItem(["advanced_views", "高级视图"]))

        data_root = QTreeWidgetItem(["Data", "数据交互"])
        data_root.addChild(QTreeWidgetItem(["json_demo", "本地 JSON"]))
        data_root.addChild(QTreeWidgetItem(["sqlite_demo", "SQLite CRUD"]))

        tree.addTopLevelItem(ui_root)
        tree.addTopLevelItem(data_root)
        tree.expandAll()

        layout.addWidget(tree)
        return group
