# iMessage tap (Mac)

Lets the TC assistant count **texts with work contacts** as evidence, the way it already uses
email and DocuSign. Adapted from the tap built for Lauren's EA (`LoanArkAI/lauren-ea-portal`),
but local-only: no server, no network.

- **Reads** `~/Library/Messages/chat.db` **read-only**, every 20 minutes while the Mac is on.
- **Writes** one file, `imessage-threads.json`, into the TC Assistant folder in Google Drive.
  Drive for desktop syncs it; the skills read it through the Google Drive connector.
- **Never sends** a text. There is no send code in it.
- **Only work contacts.** A thread is written only if the contact is in `work-contacts.csv`
  (same folder) with a work category. Friends, family and unknown numbers are dropped
  before anything is written — not their texts, not their names, not their numbers.
  Group chats are never read.

## When the Mac is asleep or off
Nothing is lost. Messages sync to the Mac from iCloud when it wakes, and each run looks back
14 days, so the first run after wake catches up. Until then the skills see an older
snapshot, check its `generated_at`, and say "texts as of <time>" rather than implying they're
current. Email, DocuSign, Drive and Follow Up Boss checks don't depend on the Mac at all.

## Install (once, ~10 minutes, on Ernie's Mac)
1. **Python** — install the python.org build for macOS (3.11 or newer):
   https://www.python.org/downloads/macos/ — the "universal2" installer. No packages needed.
2. **Google Drive for desktop** running, with the TC Assistant folder synced.
3. Get this repo onto the Mac (clone, or unzip it), then:
   ```bash
   cd tc-assistant/mac-tap
   ./install.sh "$HOME/Library/CloudStorage/GoogleDrive-<his email>/My Drive/TC Assistant"
   ```
4. The first time, it stops and asks for **Full Disk Access** for that Python
   (System Settings → Privacy & Security → Full Disk Access → +). Grant it, run the
   same command again.
5. Fill the allowlist — in Claude: *"set up texts"* / *"refresh my work contacts"*. The setup
   skill builds `work-contacts.csv` from the people on his open Follow Up Boss deals.

Check it: `cat "$HOME/Library/Logs/TC Assistant/tap.out.log"` and look for
`wrote N work threads`. Uninstall: `./install.sh --uninstall`.

## Developing
Zero dependencies. Tests (`tests/`) build synthetic `chat.db` files; run with
`python3 -m pytest` from this folder.
