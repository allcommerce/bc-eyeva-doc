# bc-eyeva-docs

Documentation for the Eyeva BigCommerce Theme by PapaThemes

## Installation

### Prerequisites

- Python 3.x
- pip

### Install Dependencies

```bash
pip install -r requirements.txt
```

Lệnh này sẽ:
- Cài đặt MkDocs và các dependencies
- Cài đặt MkDocs Material theme
- Cài đặt các plugins
- Đăng ký custom plugin `absolute-paths` với MkDocs (qua `-e .` trong requirements.txt)

## Development

### Local Development Server

```bash
mkdocs serve
```

Truy cập tại: http://127.0.0.1:8000

### Build Site

```bash
mkdocs build
```

Site sẽ được build vào thư mục `site/`

## Deployment

Deploy lên GitHub Pages:

```bash
mkdocs gh-deploy --clean --force
```

Hoặc deploy thư mục `site/` lên web server của bạn.

## Custom Plugin: Absolute Paths

Plugin `absolute-paths` tự động convert tất cả relative URLs thành absolute paths (không có domain).

**Ví dụ:**
- `../update/` → `/update/`
- `./` → `/usage/get-started/`
- `../../` → `/`

**Files liên quan:**
- `absolute_paths_plugin.py` - Plugin implementation
- `setup.py` - Plugin package configuration

### Tại sao cần `pip install -e .`?

Lệnh này (được gọi qua `requirements.txt`) cài đặt custom plugin ở chế độ "editable mode":

1. **Đăng ký plugin**: Đăng ký entry point với MkDocs để có thể dùng `- absolute-paths` trong `mkdocs.yml`
2. **Development mode**: Khi sửa code trong `absolute_paths_plugin.py`, thay đổi có hiệu lực ngay không cần cài lại
3. **Entry point**: Setup.py định nghĩa entry point để MkDocs tìm và load plugin

## Configuration

### URL Structure

- **Site URL**: `https://bc-eyeva-docs.papathemes.com/`
- **URL structure**: Clean URLs với `use_directory_urls: true`
- **Navigation links**: Absolute paths như `/usage/get-started/`
- **Assets**: Giữ relative paths để optimize performance

## Project Structure

```
bc-eyeva-doc/
├── docs/                    # Documentation source files
│   ├── index.md
│   ├── usage/
│   ├── samples/
│   └── ...
├── site/                    # Built documentation (generated)
├── absolute_paths_plugin.py # Custom MkDocs plugin
├── setup.py                 # Plugin configuration
├── mkdocs.yml              # MkDocs configuration
└── requirements.txt        # Python dependencies
```
