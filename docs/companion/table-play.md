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

The connection with DnDino is local.

The DM starts the Hero connection from the adventure in DnDino. Hero searches for the session on the local network, shows the found DM and adventure, and lets you send the active character.

On first connection, DnDino can ask for confirmation:

- to authorize the device
- to import the character as new
- to associate it with an existing character

The association uses internal identifiers, not just the character name. This avoids problems if the name changes later.

When the connection has already been authorized, Hero tries to reconnect automatically when it returns to the foreground. The sheet hero area also shows the last connected DnDino session for faster reconnection.

## Sync During Play

Synchronization can be bidirectional, but only the DM enables or disables it, separately for each connected device. Hero displays the status: the player does not need to enable a second switch. By default, the DM enables it again after each connection; optional automatic startup is available for already-authorized devices. Update both apps to use the new flow.

Live synchronization requires iOS/iPadOS 26 or later. Older systems only support sending the character manually, without automatic synchronization even outside combat.

Hero can send DnDino:

- current, maximum, and temporary hit points
- armor class
- conditions
- spent hit dice
- Heroic Inspiration

DnDino can update supported values in Hero; combat takes the linked participant into account. The new reconnection flow instead starts with the Hero sheet: when values differ, the DM chooses which to keep before ordinary live exchanges. The earlier Master state is no longer assumed to take precedence.

For setup, first sending, comparison, progressions, slots, and troubleshooting, see the [player connection guide](dndino-sync.md) and [DM guide](../sections/hero-sync.md). The new alignment requires the next update of both apps, as explained in those guides.

Hero notifications try to describe what happened:

- damage taken
- healing received
- temporary HP updated
- Heroic Inspiration gained or removed
- conditions applied
- sheet updated

## Private Chat

The **Private Message to DM** section is available while live synchronization is active.

The player can write to the DM from there. In DnDino, the DM receives a notification and can open the conversation. The chat remains separate by character and device, so two devices with the same account can use different conversations.
