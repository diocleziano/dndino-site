# Connecting DnDino Hero: a guide for the DM

Receive players' character sheets into your adventure and manage supported game values from your Mac. The connection is local and does not require an external server.

For phone and tablet instructions, see the [Hero player's guide](../companion/dndino-sync.md).

!!! info "Availability of new features"
    This page also describes the new connection comparison prepared for the next app update. It requires versions of **both DnDino and DnDino Hero that support it**. Earlier versions may have different options and startup behavior.

## Before you begin

- Open the correct adventure in DnDino.
- Use the same local network and allow Local Network access when prompted. Keep Wi-Fi and Bluetooth enabled and the devices nearby.
- Ask each player to select the correct character in Hero.
- Live synchronization requires **iOS/iPadOS 26 or later** on Hero. Older systems allow **manual sheet sending only**, even outside combat.

**Connected does not mean synchronized:** a device can be connected while automatic synchronization is disabled.

## First connection, step by step

1. On the adventure dashboard, in the **Live Session** panel, press **Start** in the **DnDino Hero** area. You do not need to start a game session to receive a sheet.
2. The player opens **Settings → DnDino Connection**, presses **Find DnDino**, and chooses your adventure.
3. Authorize the device when prompted. Check its name and character before confirming.
4. For an unlinked sheet, choose **Import new** or **Link existing**. The latter can update an existing sheet: read the replacement confirmation to avoid overwriting the wrong one.
5. For real-time updates, enable **Automatic synchronization** for that device. Hero shows the status; the player does not have to enable a second switch.

Links do not depend on the character's name alone. Renaming a linked character does not require creating another copy.

## Which data should be kept?

**Hero supplies the sheet structure:** the player manages levels, abilities, descriptions, spells, and progression configuration. The DM controls live activation and supported game values.

With the new versions, Hero sends a fresh complete sheet at each connection or reconnection before ordinary live updates. Re-enabling synchronization also requires alignment. If the values agree, no comparison appears.

When values differ, **Character alignment** opens:

- compare current, maximum, and temporary HP, AC, heroic inspiration, conditions, remaining resources, and used spell slots;
- choose **Keep** in either the DnDino or Hero column for each difference: **Hero is selected by default**;
- **All from DnDino** and **All from Hero** apply your choice to every difference;
- press **Confirm and align** and wait for the result.

Example: DnDino has 18 HP and Hero has 24. You can keep the DM's 18 HP but choose Hero's conditions. Conditions are selected **as a complete set**, never automatically combined.

Resource maxima and configuration still come from Hero. Incompatible combinations produce a message. Updates for this device are suspended while alignment is pending; other players can continue. If data changes meanwhile, review the refreshed comparison. **Retry** requests fresh data; closing the window or choosing **Disconnect** ends the connection.

Confirming alignment does **not itself enable live synchronization**.

## During play

With live active, supported values update between the apps: current/maximum/temporary HP, AC, inspiration, and conditions. In combat, the linked participant is taken into account.

The PC's detail panel also displays imported progressions and slots:

| Information | Use |
| --- | --- |
| Consumable progressions | **Remaining/Total**, minus to spend and plus to restore |
| Fixed current-level progressions | Reference cards, without spending controls |
| Spell slots | Total and used, separated by source when there are multiple sources |

Counters are stored in DnDino, not merely displayed while connected. During an active live connection, supported DM commands are confirmed by Hero. If a value changes concurrently, read the result and retry after the update; do not assume an unconfirmed click was applied.

New levels and configuration changes require a **complete sheet update**, not just counter synchronization.

## Complete sheet, chat, and bottom bar

The **download character** button, to the right of chat, requests the already-linked sheet from the connected device without asking the player to send it again. It does not enable live automatically. It requires a compatible, connected, authorized Hero and is unavailable while alignment is pending.

The bottom bar's Hero area retains devices connected during the current DnDino app session, including those that disconnect. Check status and identity, run a **connection test**, open **chat**, control live, or disconnect. Testing does not import data. Private chat requires live to be active; unread messages are flagged in the bar.

## Reconnection, disconnection, and troubleshooting

By default, each new connection requires the DM to enable live again. Settings offer optional automatic startup for already-authorized devices; the new alignment is still required.

- **Mac not found:** check the listening adventure, shared network, Local Network permissions, and that both apps are open.
- **Connected without updates:** check authorization, character association, iOS/iPadOS 26+, completed alignment, and the DM's live switch.
- **Connection lost:** keep Hero in the foreground during play. Returning to the app can trigger reconnection; **Reconnect** is also available.
- **Disconnect** ends the current connection; it does not delete the imported sheet.
- **Remove character association** revokes authorization and associations for this adventure; **Forget device** applies across all adventures. Already-imported sheets are not deleted.

!!! tip "Before the session"
    Test the connection and a small HP change with every player. Check the result in both apps before starting combat.
