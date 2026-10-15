# Referral Pipeline

A networking and referral tracker: companies, contacts (LinkedIn and email outreach, follow-ups, keep-warm reminders) and job applications. One static page, no framework, no build dependencies.

## Files

- `src/app.html` – the source of truth (markup, styles, script).
- `build.py` – wraps the source into a complete page: `python3 build.py`.
- `index.html` – the built page that GitHub Pages serves. Commit it.
- `.nojekyll` – tells Pages to serve the files as they are.

## Deploy to GitHub Pages

1. Push this folder to a GitHub repo. Name it `<username>.github.io` for a site at `https://<username>.github.io`, or any other name for `https://<username>.github.io/<repo>`.
2. Settings, then Pages. Source: "Deploy from a branch", branch `main`, folder `/ (root)`.
3. Free accounts need a public repo. The repo holds only code; your data never goes into it.

After editing `src/app.html`, run `python3 build.py` and commit both files.

## Login (passphrase lock)

The site is public, so the lock protects your data rather than the page itself. On first visit you create a passphrase. From then on:

- Everything in this browser's storage is encrypted with AES-GCM; the key is derived from your passphrase with PBKDF2 (310,000 rounds). Nothing readable is stored.
- Each page load asks for the passphrase. The app also locks after 15 minutes without activity, or when you choose Add, then Lock now.
- Anyone else who opens the site sees an empty setup screen and can only create their own separate, empty tracker in their own browser. They cannot reach your data, which lives in your browser and your private gist.
- **Recovery code (failsafe):** when you create the passphrase you also get a recovery code. It opens the same data, so if you forget the passphrase you choose "Forgot passphrase? Use recovery code" on the lock screen, enter it, and set a new passphrase. You can view it again any time while unlocked (Add, then Recovery code). Store it outside this browser, for example in a password manager.
- On a new device with sync turned on, if the synced data is locked with a passphrase you no longer have, the app asks for the recovery code and restores from the gist.
- Without both the passphrase and the recovery code the data cannot be opened. "Erase this browser" clears the local copy so you can start fresh.
- Exported JSON files are plain text. Keep them somewhere private.

## Where your data lives

- **This browser:** saved (encrypted) in localStorage automatically. It survives closing the tab and restarting the browser, but not clearing site data, and it is per browser.
- **Sync across devices (optional):** Add, then Sync across devices. Paste a GitHub classic token that has only the `gist` scope. The app keeps your pipeline in a private gist (`referral-pipeline.json`), encrypted with your passphrase, and merges it when you unlock, switch back to the tab, and about 1.5 seconds after each change. Use the same token and passphrase on another device to see the same data. If two devices edit before syncing, the most recent save wins.
- **Backup:** Add, then Export data, downloads a plain JSON file. Import data restores it.

The sync token is stored inside the encrypted storage and is only sent to `api.github.com`. Use a token with just the `gist` scope, and revoke it at github.com/settings/tokens if you lose a device.

## Do not commit your GitHub token

GitHub Pages sites are public on the internet even when the repository is private (only GitHub Enterprise Cloud organizations can restrict a Pages site to people with repository access). Any file in this repo, including a `.env`, is served at the same address as the app, so a token committed here can be read by anyone. Paste the token into the app instead; it is stored encrypted in your browser, and you paste it once per device.
