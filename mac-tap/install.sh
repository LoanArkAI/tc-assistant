#!/bin/bash
# Install the TC assistant iMessage tap on this Mac (per user, no sudo).
#
#   ./install.sh "<Google Drive folder for TC Assistant>"
#
# e.g. ./install.sh "$HOME/Library/CloudStorage/GoogleDrive-ernie@example.com/My Drive/TC Assistant"
#
# Reads iMessage READ-ONLY every 20 minutes and writes imessage-threads.json into
# that folder (work contacts only). Re-run any time; it replaces the old job.
# Uninstall:  ./install.sh --uninstall
set -euo pipefail

LABEL="com.tcassistant.imessage-tap"
AGENT="$HOME/Library/LaunchAgents/$LABEL.plist"
TAP_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="$HOME/Library/Logs/TC Assistant"

if [[ "${1:-}" == "--uninstall" ]]; then
  launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
  rm -f "$AGENT"
  echo "Removed the iMessage tap. The last snapshot file was left where it was."
  exit 0
fi

DRIVE_DIR="${1:?usage: ./install.sh \"<Google Drive folder for TC Assistant>\"}"
[[ -d "$DRIVE_DIR" ]] || { echo "Folder not found: $DRIVE_DIR (is Google Drive for desktop running?)"; exit 1; }

# A python.org framework build: it gets its own Full Disk Access entry, unlike
# the /usr/bin/python3 shim. Newest 3.11+ wins.
PYTHON=""
for v in 3.14 3.13 3.12 3.11; do
  p="/Library/Frameworks/Python.framework/Versions/$v/bin/python3"
  [[ -x "$p" ]] && { PYTHON="$p"; break; }
done
if [[ -z "$PYTHON" ]]; then
  echo "Python 3.11+ from python.org is required (one-time install, ~2 minutes):"
  echo "  https://www.python.org/downloads/macos/  → the macOS 64-bit universal2 installer"
  echo "Then run this script again."
  exit 1
fi
echo "Using $PYTHON"

OUTPUT="$DRIVE_DIR/imessage-threads.json"
CONTACTS_CSV="$DRIVE_DIR/work-contacts.csv"
mkdir -p "$LOG_DIR" "$HOME/Library/LaunchAgents"
[[ -f "$CONTACTS_CSV" ]] || printf 'Category,Name,Contact\n' > "$CONTACTS_CSV"

esc() { printf '%s' "$1" | sed -e 's/[&|]/\\&/g' -e 's/</\&lt;/g' -e 's/>/\&gt;/g'; }
sed -e "s|__PYTHON__|$(esc "$PYTHON")|" \
    -e "s|__TAP_DIR__|$(esc "$TAP_DIR")|" \
    -e "s|__OUTPUT__|$(esc "$OUTPUT")|" \
    -e "s|__CONTACTS_CSV__|$(esc "$CONTACTS_CSV")|" \
    -e "s|__LOG_DIR__|$(esc "$LOG_DIR")|g" \
    "$TAP_DIR/launchd/$LABEL.plist.template" > "$AGENT"
plutil -lint "$AGENT" >/dev/null

echo
echo "Checking access to Messages (dry run, writes nothing)..."
if ! (cd "$TAP_DIR" && TC_TAP_CONTACTS_CSV="$CONTACTS_CSV" "$PYTHON" -m tc_tap.tap --dry-run >/dev/null); then
  echo
  echo "Python can't read Messages yet. Grant it Full Disk Access:"
  echo "  System Settings → Privacy & Security → Full Disk Access → +  → add:"
  echo "  $PYTHON"
  echo "(In the file picker press Cmd-Shift-G and paste that path.) Then run this script again."
  open "x-apple.systempreferences:com.apple.preference.security?Privacy_AllFiles" || true
  exit 1
fi

launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$AGENT"
echo
echo "Installed. Runs every 20 minutes; first run now."
echo "  snapshot:      $OUTPUT"
echo "  work contacts: $CONTACTS_CSV   (only these threads are ever written)"
echo "  logs:          $LOG_DIR"
