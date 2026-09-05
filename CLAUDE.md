# CLAUDE.md

Orientation for future Claude sessions working in this repo. It's small — read this and you've read most of it.

## Response style

Be extremely concise. Sacrifice grammar for the sake of concision.

## What this is

The public support site for **Budgie**, a personal budgeting app. Jekyll on GitHub Pages (`pages-themes/minimal` via `remote_theme`, see `_config.yml`), served at `https://etienneptl2.github.io/budgie-support/`. Four documents and two workflows; no app code.

```
README.md            # the support/FAQ landing page
privacy.md           # Privacy Policy — numbered sections, the app links to privacy.html
terms.md             # Terms of Use / EULA — the source of truth
terms-appstore.txt   # GENERATED from terms.md; never hand-edit
scripts/             # build-eula-text.py, the generator
.github/workflows/   # site.yml (Jekyll build), eula.yml (generated-text freshness)
```

## This repository is public

**Everything here is world-readable: the files, the commit messages, the pull request titles and bodies, and every comment.** The app it documents lives in a separate **private** repo. Writing about the work therefore has one hard rule:

> Describe what the app *does*. Never name the app's repository, its files, its symbols, or its pull requests.

So: "the app's Settings screen has a Privacy options row" — never a source path. "The app carries a legal-version number" — never the constant's name or the file holding it. "The app now points at these Terms" — never a link to the pull request that did it.

Cross-repo links are the worst offender and the easiest to type without thinking. A link to a private pull request **confirms both the repository name and the number** to anyone who reads it, even though it 404s for them. `owner/repo#123` renders as one of these too.

Three things make this hard to undo, which is why it's a rule rather than a preference:

- **Pull request bodies keep an edit history**, visible to anyone who can see the pull request. Scrubbing after the fact leaves the original one dropdown away. The only complete remedy is deleting and recreating the pull request, which throws away its review history.
- **A merged commit message can't be edited** without rewriting public history. What saves us today is that merges here are squashes taking the *pull request title only*, not the body — keep merging that way.
- **This has gone wrong here before.** It goes wrong while you're explaining something genuinely useful — the detail feels like good citation practice right up until you remember where it's published. Assume the rule is easier to break than to follow.

Nothing about this is secret-handling — no keys or credentials belong in either repo. It's that a private repo's file names, symbols and pull request numbers describe a codebase its owner chose not to publish.

## The generated EULA

`terms-appstore.txt` is rendered from `terms.md` by `scripts/build-eula-text.py`. It exists because App Store Connect's custom licence agreement is a **plain-text field, not a URL** — it strips markup, so the Markdown can't be pasted as-is without users reading literal `**bold**` and `[text](./file.md)`.

- **Any change to `terms.md` means running the script and committing both files.** `eula.yml` runs `--check` and fails otherwise.
- **The check never regenerates and pushes.** That's deliberate: the generated text is what users actually read, so it belongs in the diff under review rather than appended by a bot after approval.
- **CI can only prove the two files agree in git.** Whether the text has been pasted into App Store Connect (Apps → Budgie → General → App Information → License Agreement) is outside anything CI can see. Re-pasting is a manual step after every merge that touches `terms.md`.
- Don't edit `terms-appstore.txt` by hand — the next run overwrites it.

## Both workflows run on every pull request, unfiltered by path

`site.yml` and `eula.yml` deliberately carry no `paths:` filter. They're required status checks, and GitHub treats a required check that never reports as **permanently pending** — a path filter would block every pull request that happens not to touch the filtered files. Each job is a checkout plus one command, so running them always is cheaper than that failure mode.

`site.yml` builds the Jekyll site on the pull request because Pages' own "pages build and deployment" only runs *after* a push to main — it can report a broken site but never prevent one.

## Document conventions

- **Bump `_Last updated:` whenever you change a document.** Both files carry one under the title.
- **The app shows a one-time legal notice** keyed to a version number baked into its build. A *material* change here — a new processor, a new category of data sharing, a new promise — must be **live on this site before** the app build announcing it ships, or the notice points at a policy that doesn't yet say what the notice claims. Non-material edits (naming something more precisely, a carve-out in the user's favour) need no bump; say which you think it is in the pull request.
- **In-app paths are written as `Settings → Export`, `Profile → AI insights`.** Verify them against the current app before writing them — several already-published paths were corrected this way. A group *heading* on a screen isn't a screen you push into, so it doesn't get its own arrow.
- **Typography is not plain ASCII.** Both documents use non-breaking hyphens (`‑`), curly quotes and em dashes throughout. Match the surrounding text; the generator normalises them for the plain-text copy.
- `privacy.md` sections are **numbered and cross-referenced** ("see Section 7"). Renumbering means fixing every reference, including the ones in `README.md`.
- Markdown tables render fine (kramdown). `privacy.md` already uses one.

## Jurisdictions

`privacy.md` §7 carries a block per market the app is actually distributed in — currently **Australia, Canada (PIPEDA + Quebec Law 25), and the United States**, plus a catch-all. Add a block when a market is added, not before: a policy claiming compliance with a regime you aren't in is worse than silence.

**Europe is deliberately not a distribution territory.** App Store availability excludes the EEA, so there are no GDPR sections and no Article 27 representative. A full draft exists on the retained branch `add-eea-uk-privacy-section` (see the closed pull request #7) if that ever changes — along with the two blockers that come with it: appointing EU **and** UK representatives, and confirming the third-party data processing agreements are actually executed before claiming Standard Contractual Clauses.

The EEA/UK mentions in §2.4 and §5 are correct and should stay: the ad consent form resolves geography at runtime, so a user travelling in Europe really can be shown it.

**Don't link the EU ODR platform** — it shut down in July 2025, and stale references to it are common in policies of this vintage.

## Not a lawyer

Neither are you. These documents make legal claims about a real business; draft them to be structurally complete and honest about what the app does, flag what needs professional review, and don't invent a fact (an address, a certification, a retention period) to fill a gap. A `TODO` in a live policy is worse than an omission.
