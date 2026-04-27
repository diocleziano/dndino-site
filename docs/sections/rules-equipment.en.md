# Rules and Equipment

This section covers the app reference areas: **Rules**, **Feats**, **Glossary**, **Spells**, and **Equipment**.

Fields are intentionally flexible, so you can adapt them to your campaign. For cleaner filters and better grouping, though, use consistent, tidy values.

## How Search Works

The top bar quick search checks several fields at once.

For **rules**, it searches:

- name
- category
- prerequisites
- rule type
- school
- description

For **equipment**, it searches:

- name
- category
- AC
- damage
- properties
- use
- description

## Feats

For feats, the most useful grouping field is **category**.

Examples:

- `Origin`
- `General`
- `Combat`
- `Magic`

Use **prerequisites** to quickly show who can take the feat. Keep them short, for example `Level 4`, `Strength 13+`, `Spellcaster`.

## Glossary

The glossary is useful for terms, conditions, recurring rules, and table reminders.

Use **rule type** or **category** to group similar entries.

Examples:

- `Condition`
- `Action`
- `Movement`
- `Saving throw`

Descriptions should stay clear and direct, so entries remain useful during play.

## Spells

Spells are more structured because they are also used in combat when linked to characters.

For reliable grouping:

- for **cantrips**, choose `Cantrip` from the level menu
- for other spells, choose a level from `1` to `9`
- in **classes**, separate class names with commas, for example `Wizard, Cleric, Druid`
- in **school**, enter only the school name, for example `Conjuration`

Avoid values like `3rd-level Conjuration` in the school field: level already has its own field, and school works best when it stays clean.

### Useful Fields

Fill these carefully:

- **casting time**
- **range**
- **components**
- **duration**
- **description**
- **higher levels**

These details appear in the spell detail window and help you reference the spell without opening external books.

## Spells in Combat

If spells are linked to a character, they appear in that character's combat sheet, grouped by level.

The section also shows spellcasting information when available, such as spell attack bonus, spell save DC, and available spell slots.

For **NPCs and monsters**, the `Use` button on a spell increases the used-slot counter for that spell level. The counter is a GM reminder: it does not block casting, but it clearly shows when the expected maximum has been reached.

Cantrips do not consume slots.

## Equipment

Equipment is split into:

- weapons
- armor
- tools
- adventuring gear

Fields are flexible here too, but consistent data makes search much more useful.

## Weapons

For weapons, the most important fields are **category**, **damage**, and **properties**.

Examples:

- category: `Simple`, `Martial`, `Ranged`
- damage: `1d8 piercing`
- properties: `Versatile, Thrown`

If you reuse the same property names, it becomes easier to find every weapon with a shared trait.

## Armor

For armor, keep **category** and **AC** tidy.

Examples:

- category: `Light`, `Medium`, `Heavy`, `Shield`
- AC: `14 + Dex max 2`

The description can include notes, requirements, disadvantage, or special rules.

## Tools and Gear

For tools and adventuring gear, the most useful fields are **category**, **use**, and **description**.

Examples:

- category: `Artisan's tools`
- use: `Dexterity or Intelligence checks`
- category: `Exploration gear`
- use: `Travel, dungeon, survival`

Prefer short, reusable categories instead of long sentences.

## Good Practices

To keep the database readable:

- use the same names for similar categories
- separate lists of values with commas when you want them to read as groups
- avoid repeating information in text when it already has a dedicated field
- keep descriptions complete, but filtering fields short and clean
