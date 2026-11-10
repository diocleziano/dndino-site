# Top Bar

![Top Bar](../images/en_topbar.png){ .img-hero }


The **top bar** is DnDino's global shortcut area. It keeps the tools you use most often close at hand while preparing or running an adventure.

It can show icons only, or icons with labels below, depending on the preference set in **Settings**.

## General Behavior

The buttons on the left are global shortcuts. Some open a full section, while others open a quick panel. Quick panels are meant for fast lookup without losing the place where you are working.

## Home

`Home` returns to the app's start page.

Use it when you want to go back to the general overview or restart from the main entry point.

## Adventures

`Adventures` changes behavior depending on context.

From the **Home** or from sections not tied to a specific adventure, it opens the adventure list.

From an **adventure dashboard**, **places**, or a **combat** tied to an adventure, it returns to that adventure dashboard. It is the fastest way back to the campaign hub.

## Characters

Each result has two circular buttons on the right: **View** opens the compact sheet and **Edit** opens the editor. The row itself no longer opens a sheet, and there is no global preference choosing between these actions.

## Equipment

`Equip` opens quick equipment search.

It searches:

- weapons
- armor
- tools
- adventuring gear

You can search by name, category, AC, damage, properties, use, or description. Results open in a reference window, while the lower buttons open the full equipment sections.

## Rules

`Rules` opens quick rules search.

It searches:

- feats
- glossary
- spells

You can search by name, category, prerequisites, rule type, school, or description. Spells open in a dedicated window; feats and glossary entries can open for reference or editing depending on settings.

The lower buttons open the full feats, glossary, and spells sections.

## Quick Tools

`Quick Tools` brings together the tools you may need immediately while preparing or running a session.

From here you can open:

- the **quick dice roller**
- the **name generator**
- **quick timers**

### Dice Roller

The dice roller lets you choose the number of dice, die type, and modifier.

The default die is configured in **Settings**. Results show each die and the total, making it useful for quick checks and improvised rolls during play.

### Name Generator

Choose ancestry, gender and **full name** or **given name only**. Lock the given name or surname to regenerate only the other part, or regenerate a single suggestion. Copy a result or retrieve it from recent history, shared between the full generator and quick access. You can clear that history.

### Quick Timers

Quick timers help you track table deadlines without leaving the current screen.

You can set a name, choose the duration with a macOS-style control, and run up to four timers at once. Each timer can be paused, resumed, stopped, or removed.

## Settings

`Settings` opens the app preferences.

This is where you manage language, theme, top bar, panel behavior, combat, Player Window, database, diagnostics, and support.

## Live Session in the bottom bar {#live-session-control}

On an adventure page, open **Live Session** in the **bottom bar**, to the left of Hero. Click **Start** and confirm to begin a session for the current adventure.

If a session is already open, the control stays available even outside the adventure. You cannot start a second one in parallel. [Live Session guide](live-session.md#live-session-bottom-bar).

## Player Window in the Center

If enabled in settings, the center of the top bar also shows **Player Window** controls.

They let you manually open or close the player-facing window, useful when showing images, combat, or summaries on a second display.

## When to Use It

Use the top bar when you want to:

- return quickly from places to the adventure dashboard
- look up a rule without changing screen
- consult a character or item on the fly
- make a quick roll, start a timer, or generate an improvised name
- manage a live session from the current section

## Fill the main window {#fill-main-window}

If the macOS title-bar double-click action is **Fill**, double-click an empty part of the title bar. The main window fills the visible area without going full screen. Double-click again to restore the previous size.

<!-- guide-coverage: MOD-023 MOD-024 MOD-025 MOD-034 MOD-038 MOD-039 MOD-044 MOD-045 MOD-048 MOD-054 MOD-067 MOD-069 -->

## Bottom bar and open windows

The bottom bar appears when work windows or return links are available; the Players Window is excluded. Each window has a title and icon distinguishing **Edit** from **View**: click to bring it forward or restore it, or use X to close it. Character sheets/editors are independent and minimizable; Conditions and Full Attack cannot be minimized.

Leaving an unfinished combat pauses it and keeps a return link **first on the left**, with a colored stripe. Click to return. Its X only hides the link: it does not finish or delete the combat. The shortcut is hidden during that combat, while other windows remain listed.

Chats received from Hero appear even with their window closed, without interrupting you; a dot indicates unread messages. Opening and reading the conversation clears it. On the right, the Hero area retains players contacted during the current app run even after disconnection: status, connection test, chat, sheet download, live sync and disconnect. See the [Hero guide](hero-sync.md).
