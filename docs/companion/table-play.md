# Combat and Table Play

DnDino Hero is designed to support the player during the session.

The sheet can be used without DnDino, but some features are intended for local table play.

## During Combat

The **Combat** section collects the information you usually need most:

- hit points
- temporary HP
- armor class
- initiative
- speed
- Heroic Inspiration
- conditions
- saving throws
- attacks
- prepared spells
- spell slots
- consumable features and resources
- death saving throws, when the character is at 0 HP

## Attacks

Attacks are currently designed for weapons.

Each attack can have:

- name
- icon
- properties
- mastery
- proficiency
- ability used for the attack roll
- attack roll bonuses
- main damage
- additional damage
- damage bonuses
- class progressions used in damage or bonuses

The view shows the total attack bonus and a summary of its modifiers.

If the weapon has active mastery, the sheet shows it compactly. The full description can be opened without filling the attack card.

## Spells

Character spells are grouped by level.

Cantrips are always available. Other spells can be marked as:

- **Prepared**
- **Not Prepared**

The main sheet and combat section show only prepared spells.

## Spell Slots

Spell slots are separated by class or subclass when multiple sources provide magic.

For each source, the sheet shows:

- spellcasting ability
- spell attack bonus
- spell save DC
- total slots
- spent slots

Slots reset on a long rest.

## Conditions

Conditions are managed manually.

The app can import the condition list from DnDino, but it does not automatically apply removal logic or mechanical effects. Control remains with the player and the DM.

## Local DnDino Connection

The apps connect over the local network. The player selects the Mac in Hero, and the GM approves from the **Hero** panel in DnDino’s bottom bar. Live, chat and sheet transfer are available on iOS/iPadOS 17 or later.

For pairing, sheet transfer, Live and chat, see the [player guide](dndino-sync.md) or the [GM guide](../sections/hero-sync.md).

Hero notifications try to describe what happened:

- damage taken
- healing received
- temporary HP updated
- Heroic Inspiration gained or removed
- conditions applied
- sheet updated

## Private Chat

Open **Chat** in **Settings → DnDino Connection** after pairing. When a message arrives with the chat closed, the GM sees an unread badge in DnDino’s bottom bar. Each pairing has its own conversation.
