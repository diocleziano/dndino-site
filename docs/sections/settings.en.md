# Settings

The **Settings** section gathers DnDino’s global preferences. You are not working on a single adventure or a single character here. Instead, this is where you define **how the app should behave as a whole**.

Settings mostly affect:

- the overall look of the interface
- top bar behavior
- the `Places` workflow
- the behavior of `Combat`
- image, backup, and snapshot management
- database support and diagnostics

## Content, help and additional themes

**General → Official content** shows or hides SRD libraries without deleting personal data or breaking existing references. The control is shared with the lists. See [Official Content](official-content.md).

Guide **?** buttons can be disabled globally and are enabled by default. **Halloween** joins the other themes; **System** continues to follow macOS's actual appearance. The top bar, contextual buttons and menus use consistent layouts that keep icons and text readable.

## How the Screen Is Organized

The page is divided into two areas:

- a **left sidebar** with categories
- a **main panel** on the right with the options for the selected section

Available categories are:

- `General`
- `Top Bar`
- `Places`
- `Combat`
- `Media`
- `Theme`
- `Database`
- `Diagnostics`
- `Support`
- `Licenses`

This structure separates daily-use preferences from more technical areas such as backups and diagnostics.

## General

The `General` section gathers the base preferences of the app.

### DM Profile

Here you can customize your profile with:

- `User name`
- `Gender`

The name is reused in other parts of the app, such as the welcome message on the `Home` screen.

### Interface Language

You can choose whether to:

- follow the system language
- force a specific app language

### Keep the screen awake

In **Settings > General**, enable **Keep the screen awake** to prevent the display from turning off automatically while DnDino is in the foreground. This is useful during a session when you are reading notes or presenting content without constantly using the mouse or keyboard.

The option is **off by default**. It also works on battery power, but increases energy use. Your choice is remembered between launches: switching to another app releases the request; returning to DnDino restores it if the option is still enabled. You can turn it off at any time using the same control.

No special permissions are required, and macOS security settings are not changed. It does not prevent manual locking, user-requested sleep, closing the lid, or system protections; it does not guarantee that independent screensaver or security policies will be prevented.

If macOS cannot activate the feature, a warning appears: turn the option off and on again to retry. Resetting all settings turns it off again.

### Global Confirmations

The `Ask for confirmation before deletions` option adds a confirmation step before destructive actions such as removals and deletions.

### Metadata

Inside `General` you also find:

- `Show metadata in app`

This controls whether metadata panels should be shown in the screens that support them.

### Adventure Dashboard Panel Layout

This part is important if you use the `Adventure Dashboard` often.

You can:

- drag panels
- reorder them inside the left or right column
- move them from one column to the other

### Active Theme

Inside `General`, the **currently selected theme** is also shown as a quick summary. The actual theme change is made in the `Theme` section.

### Introductory Guides

From here you can restore the app’s first-use behavior.

The `Reset First Use` button tells DnDino to consider contextual guides and onboarding flows as unseen again.

## Top Bar

The `Top Bar` section defines how the quick tools in the top bar behave. For a full explanation of each button, see the `Top Bar` page.

### Top Bar Look

You can choose whether the top bar is displayed:

- with icons only
- or with icons and labels underneath

### Default Die

Here you can choose the **default die type** shown by the dice roller inside `Quick Tools`.

### Quick Character Opening

Each result has two circular buttons on the right: **View** opens the compact sheet and **Edit** opens the editor. The row itself no longer opens a sheet, and there is no global preference choosing between these actions. [Topbar](topbar.md).

### Quick Rules Opening

This setting controls quick opening of `Rules`.

Here you can decide whether that shortcut should open:

- the full editor
- or a smaller consultation-oriented window

### Players Window Controls in the Top Bar

The `Show players window controls in the top bar` option shows quick controls to manually open or close the `Players Window`.

## Places

The `Places` section contains global preferences used as default behavior in the places dashboard.

### Default Occupant Role

When you add an occupant to a place, DnDino can propose a default starting role.

### Show Parent Place Maps by Default

If enabled, inherited maps from parent places start visible in the `Places` screen.

### Remember Last Visited Place

If enabled, when you come back to the `Places` screen the app tries to restore the last selected place for that adventure.

### Automatically Close the Previous Place

This setting applies during an **active live session**.

When a place is marked as `Being visited`, the place that was previously `Being visited` is automatically marked as `Visited`.

## Combat

Presentation and visibility preferences define **defaults for new combats**. To change one combat, use [second-screen management and player visibility](combat.md#player-screen-options), including group actions. Saved choices in other combats are not overwritten.

Enabling the player combat screen and window-opening behavior remain global. Existing unfinished combats store their initial values once, when first opened.

### Enable Combat Screen for Players

These controls appear only when **Enable combat screen for players** is on in **Settings > Combat**. Turning it off hides them in both preparation and active combat, while retaining saved choices. A second monitor does not need to be connected, and the Player Window does not need to be open already.

### Open the Players Window if Closed

If enabled, DnDino automatically opens the `Players Window` when combat starts. If disabled, the presentation is updated only when the window is already open.

### Open the Players Window Even with One Monitor

This setting appears only when automatic opening is enabled. Use it if you want to use the `Players Window` even without a second display.

## Combat Presentation

These options define presentation defaults for new combats; change them within a combat without changing Settings:

- `Show combat intro to players`
- `Show final summary to players`
- `Show round on player screen`
- `Show encounter duration on player screen`
- `Show next turn on player screen`

Encounter duration is shown as a readable timer; if combat is paused, the count stops.

## Hero Information

These define initial visibility for hero-type participants in new combats. Choose whether to show:

- current, maximum, and temporary HP
- active conditions

## NPC Information

These define initial NPC visibility in new combats, including NPCs with the Ally role. Choose separately whether to show:

- current, maximum, and temporary HP
- active conditions
- the NPC's real name

If NPC names are hidden, the `Players Window` uses the generic name `NPC`.

## Monster Information

These define initial monster visibility in new combats. Monster HP and conditions use these options even for allies; non-enemy monster names initially remain visible. Choose separately whether to show:

- current, maximum, and temporary HP
- active conditions
- the real name of enemies

If monster/enemy names are hidden, the `Players Window` uses the generic name `Enemy`.

## Media

The `Media` section gathers preferences for image management and presentation windows.

### Fullscreen Player Images

If enabled, images shown to players open in fullscreen mode.

### DM Images on the Main Monitor

This option makes the DM window open by default on the first available screen.

### Remember DM Window Size

If enabled, when you reopen a new image for the DM, the window keeps:

- the last size
- the last position

## Media Maintenance

The `Media maintenance` area covers the more technical side of image handling.

From here you can launch `Clean unused media`, which checks the image files stored by the app and removes those no longer linked to any entity.

## Theme

The `Theme` section lets you choose the app’s **global palette**.

Each theme shows a small visual preview of its main colors, so you can immediately understand how the interface will change.

## Database

The `Database` section is one of the most important areas for data safety.

Here you can find:

- the path of the data folder
- the path of the SQLite database
- the path of the backup folder
- information about the latest snapshots

### Automatic Backup

You can choose:

- automatic backup frequency
- maximum number of automatic snapshots to keep

### Cloud Snapshots

DnDino also manages cloud snapshot behavior.

From here you can choose how cloud saves should behave and view the current state through the summary text shown in the screen.

### Main Actions

Inside the `Database` panel you find the main maintenance buttons:

- `Open data folder`
- `Open backup folder`
- `Create snapshot...`
- `Restore snapshot...`
- `Restore from iCloud`

### Reset App Data

The `Reset app data` function deletes:

- the app database
- the app media

but keeps already-created backups.

### Latest Snapshots

At the bottom of the `Database` section, DnDino also shows the list of the latest snapshots it found.

For each one, it displays:

- file name
- date
- size

## Diagnostics

The `Diagnostics` section is used to inspect the technical state of the SQLite database used by the app.

Here you can:

- refresh diagnostic data
- see the database path
- check whether the file exists
- verify file size and modification date
- see the SQLite version

### Tables

Diagnostics also shows the list of tables found in the database together with the number of records in each one.

## Support

The `Support` section gathers quick ways to contact the app developer.

Here you find:

- support email
- `Request support` button
- `Send a suggestion` button
- `Copy email` button

## Licenses

The `Licenses` section gathers the legal and attribution references used by the app.

At the moment it includes in particular the material related to the **System Reference Document 5.2** for Dungeons & Dragons, with references to:

- the SRD document
- the `CC-BY-4.0` license

!!! tip
    If you are configuring DnDino for the first time, the most useful sections to check first are `General`, `Top Bar`, `Combat`, and `Database`. Those are usually the ones that affect day-to-day use and data safety the most.
## Version 1.4 additions

The `Database` section is now `Database and Media`.

In release builds, DnDino no longer shows internal technical paths. Instead, the section focuses on useful information: database size, number of saved images, total image size, snapshots, backup export, and media export.

Snapshots and app media can be exported to a user-selected location through the standard macOS save panel. Media files still remain copied inside the app sandbox so DnDino does not lose references if the original files are moved or deleted.

The Diagnostics section is reserved for debug builds and is not shown in the release version.

<!-- guide-coverage: MOD-042 MOD-043 MOD-049 MOD-051 MOD-060 MOD-061 MOD-062 MOD-070 MOD-071 MOD-073 MOD-077 MOD-078 MOD-079 MOD-080 MOD-086 MOD-088 -->

## Themes, backgrounds and opacity

Alongside **System**, which follows the Mac's light/dark appearance, themes include **Halloween**, **Christmas**, **Parchment** and **Winter**. Previews show palette and background; **Decorative background** can be disabled without changing theme. Winter uses a snowy landscape. These are theme backgrounds, not a custom-image background importer for Mac.

The opacity slider immediately changes supported panels and sidebars, including Settings and both Places and Quests panels. Panels that were already opaque are excluded. **Default** restores each panel's original opacity, not one shared 50% value.

Changing theme rebuilds the main screen and returns to **Settings → Theme**. Open secondary windows and unsaved drafts remain intact; the bottom bar follows the new theme. Main buttons and sidebar selection use theme colors with contrast-aware text. **System** retains native macOS control behavior.

For authorizations, device history, optional automatic live startup and the difference between disconnecting, removing an association and forgetting a device, see [Connect with Hero](hero-sync.md).
