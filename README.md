# MSDS GenAI away-day: Workshop on AI assistants

A single-page, pick-your-own-exercise tutorial for making everyday university administrative work easier with UU AI-Chat.

## Structure

- `index.qmd` — page introduction, navigation and exercise includes.
- `exercises/_*.md` — one collapsible section per exercise; 13 in total.
- `materials/*.md` and `materials/*.csv` — fictional material, linked from the exercises.
- `scripts/build_tutorial.py` — thin wrapper around Quarto's `render` command.
- `_quarto.yml`, `styles.css` — layout, left table of contents, copy buttons, publishing to `/docs`.
- `docs/` — generated site; commit this to publish. Quarto will refresh it when you render.
- `slides/` — optional introductory presentation.
- `instructor/` — local facilitator notes, **excluded by `.gitignore`**. They must not be committed to the public repository. **If uploading through GitHub’s website rather than `git add`, manually omit this folder; `.gitignore` does not protect web uploads.**

Keep each exercise heading (`##`) outside its collapsible callout so that it is always shown in the left contents menu. The materials are fictional and are **not** official UU policy or live forms.

### Materials and uploads

Files are Markdown/CSV as requested. If your UU AI-Chat interface does not accept `.md`, open the linked file and paste its contents into chat. The same sample documents are reused across related exercises; they aren't duplicated.
"# msds-awayday-tutorial" 
