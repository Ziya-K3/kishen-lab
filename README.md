# Kishen Lab

A research-studio redesign of the public Kishen Lab site. Flask serves the pages, the publication index, and site search. Layout, motion, and illustration are original HTML, CSS, and JavaScript.

The copy follows the public record at [thekishenlab.org](https://thekishenlab.org/): the lab’s mission, research themes, people, selected papers, patents, awards, and media. It is an independent redesign, not the official WordPress theme.

## Run

PowerShell on this machine blocks `Activate.ps1`, so start the app with the virtual environment’s Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Or double-click `run.bat`, or from this folder run `.\run.bat`.

Open [http://127.0.0.1:5050](http://127.0.0.1:5050).

## Deploy for free

[Render](https://render.com) can run this Flask app from the GitHub repo at no cost. The free instance sleeps after about 15 minutes without visitors and takes about a minute to wake. Messages saved by the contact form live on that temporary disk, so they disappear when the service sleeps or redeploys.

1. Sign in to Render with GitHub and create a new Web Service from this repository.
2. Runtime: Python.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --threads 2`
5. Choose the free instance and deploy.

A `Procfile` with that start command is already in the repo. Render also gives the site HTTPS.

[PythonAnywhere](https://www.pythonanywhere.com) has a free Beginner account with one web app. It does not sleep, but the free app has to be extended about once a month and it cannot use a custom domain.

## What is in here

- Home, about, research, people, publications, awards, media, and contact
- Publication search that works with or without JavaScript
- Site search across pages, people, papers, awards, and news (`/` in the search field, or the Search button)
- A contact form that stores messages locally in `instance/messages.json`
