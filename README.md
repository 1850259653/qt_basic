# PySide6 + uv 客户端示例库

该项目用于快速复用客户端开发代码片段，包含常见 UI 元素与数据交互场景。

## 1. 环境准备

```bash
uv python install 3.11
uv sync
```

## 2. 运行应用

```bash
uv run qt-snippets
```

## 3. 项目结构

- `src/app/ui/`：常见 UI 组件示例
- `src/app/data/`：数据交互示例（JSON / SQLite / HTTP / 线程）
- `src/app/snippets/`：可直接复制的最小片段
- `tests/`：数据层基础测试

## 4. 示例列表

- 基础控件：按钮、输入框、标签、布局
- 高级视图：表格、列表、树
- 交互组件：对话框、通知、进度条、分页、主题切换
- 数据交互：JSON 读写、SQLite CRUD、HTTP 请求、后台线程

## 5. 片段复用建议

1. 先在左侧导航打开对应示例。
2. 再到 `src/app/snippets/` 复制最小片段。
3. 按需替换数据模型、字段与 API 地址。
