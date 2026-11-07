# Video Game Management System

A desktop app for cataloguing video games, built with Python, Tkinter/customtkinter and MySQL.

**[▶ Try the live demo](https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/)** (runs in your browser, no setup)

<!-- Add a screenshot: ![Screenshot](docs/screenshot.png) -->

## Features

- Add, update and delete game records
- Search by Game ID, name, year or company
- Sort ascending or descending by ID, rating, year, company or exclusivity
- Compare: histogram of games by release year (matplotlib)
- Click a row in the table to load it into the form

Each record stores: Game ID, name, release year, short ID, Steam rating, company, whether it is exclusive, and platform.

## Browser demo

`index.html` is a standalone, in-browser demo of the interface with sample data. It needs no database, and changes reset on reload. To open it:

- **Live link:** enable GitHub Pages (Settings → Pages → deploy from the `main` branch, root folder). The demo is then at `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`. Replace `YOUR-USERNAME` and `YOUR-REPO-NAME` in the link at the top of this README with your own.
- **Without Pages:** open `https://htmlpreview.github.io/?https://github.com/YOUR-USERNAME/YOUR-REPO-NAME/blob/main/index.html`.
- **Locally:** download the repo and double-click [`index.html`](index.html).

## Requirements

- Python 3.10+ (with Tkinter)
- MySQL 8.0+

## Setup

```bash
git clone https://github.com/<your-username>/video-game-management-system.git
cd video-game-management-system

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create the database and table:

```bash
mysql -u root -p < schema.sql
```

The app connects using the host, user and database name written in
`video_game_management_system12_beta.py` (`localhost`, `root`, and the database
`interactive`). No password is included in the code, so if your MySQL user has
one, add `password='...'` to each `mysql.connector.connect(...)` call before
running (and don't commit it).

## Run

```bash
python video_game_management_system12_beta.py
```

## Notes

- The interface uses Windows fonts (OCR A Extended, Bahnschrift) and a fixed layout sized for a large screen.
- Needs a running MySQL server with the `interactive` database.

## License

[MIT](LICENSE)
