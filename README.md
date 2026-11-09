# UU AI-Chat: Administrative workshop

A single-page, pick-your-own-exercise tutorial for making everyday university administrative work easier with UU AI-Chat.

## Local build

Requires [Quarto](https://quarto.org/docs/get-started/) and Python 3; no Python packages are needed.

From the repository root, run the same command used in the previous tutorials:

```bash
python scripts/build_tutorial.py --department admin --render
```

Or simply:

```bash
python scripts/build_tutorial.py --render
```

Quarto assembles `index.qmd` and the individual Markdown files in `exercises/` into **`docs/index.html`**. The ZIP contains a working initial HTML preview so the Pages site is immediately viewable; **run the script once locally** to replace it with the canonical Quarto render. After that, edit only Markdown sources; never edit generated HTML manually.

You can preview locally with `quarto preview` (optional). Edit → render → commit → push.

## GitHub Pages

Create a **public repository**, push the files, then choose **Settings → Pages → Deploy from a branch → main → `/docs`**. GitHub Pages serves the generated `docs/index.html`; it does not run Quarto for you. The included `.nojekyll` file prevents Jekyll from processing the generated website.

The page URL will be `https://YOUR-USERNAME.github.io/YOUR-REPO/` (unless you configure a custom domain).

## Structure

- `index.qmd` — page introduction, navigation and exercise includes.
- `exercises/_*.md` — one collapsible section per exercise; 13 in total.
- `materials/*.md` and `materials/*.csv` — fictional material, linked from the exercises.
- `scripts/build_tutorial.py` — thin wrapper around Quarto's `render` command.
- `_quarto.yml`, `styles.css` — layout, left table of contents, copy buttons, publishing to `/docs`.
- `docs/` — generated site; commit this to publish. Quarto will refresh it when you render.
- `slides/` — optional introductory presentation.
- `instructor/` — local facilitator notes, **excluded by `.gitignore`**. They must not be committed to the public repository. **If uploading through GitHub’s website rather than `git add`, manually omit this folder; `.gitignore` does not protect web uploads.**

## Updating the exercises

1. Edit an existing `exercises/_NN-*.md` file, or add one and include it in `index.qmd`.
2. Put new non-sensitive sample material in `materials/`, and link it from the exercise.
3. Run `python scripts/build_tutorial.py --render`.
4. Check the page and `git add`, commit and push.

Keep each exercise heading (`##`) outside its collapsible callout so that it is always shown in the left contents menu. The materials are fictional and are **not** official UU policy or live forms.

### Materials and uploads

Files are Markdown/CSV as requested. If your UU AI-Chat interface does not accept `.md`, open the linked file and paste its contents into chat. The same sample documents are reused across related exercises; they aren't duplicated.
"# msds-awayday-tutorial" 
