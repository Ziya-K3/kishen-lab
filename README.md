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

## Deploy

Cloudflare Workers hosts the site and can use a domain such as kishenlab.com.

On the Workers “Create an app” screen for this GitHub repo:

- Project name: `kishen-lab`
- Build command: leave empty
- Deploy command: `npx wrangler deploy`

Then attach the domain under the project’s Custom domains settings. The contact form on your own computer still saves notes in `instance/messages.json`. On Cloudflare, that disk does not exist, so the public form points people to the lab email.

## What is in here

- Home, about, research, people, publications, awards, media, and contact
- Publication search that works with or without JavaScript
- Site search across pages, people, papers, awards, and news (`/` in the search field, or the Search button)
- A contact form that stores messages locally in `instance/messages.json`
