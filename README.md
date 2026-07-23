# 🚀 Suvom Media Downloader

A modern, modular Python desktop application for managing media download tasks with a clean architecture, plugin support, and automated testing.

---

## Features

- 📥 Download task management
- ⚡ Multi-worker queue system
- 🔄 Pause, Resume, Cancel downloads
- 📊 Download progress tracking
- 📝 Download history
- 🔔 Notification system
- 🔌 Plugin support
- 🔄 Auto update framework
- ⚙️ Settings management
- 🧪 190+ automated tests

---

## Project Structure

```
core/
services/
plugins/
updater/
gui/
config/
tests/
```

---

## Requirements

- Python 3.12+
- Windows 10/11

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/SuvomMediaDownloader.git

cd SuvomMediaDownloader

pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

---

## Run Tests

```bash
python -m pytest
```

---

## Code Quality

Format code

```bash
python -m black .
```

Lint

```bash
python -m ruff check .
```

Coverage

```bash
python -m pytest --cov=. --cov-report=html
```

---

## Technologies

- Python
- Pytest
- Black
- Ruff
- mypy
- GitHub Actions

---

## License

MIT License

---

## Author

**Suvom Das**