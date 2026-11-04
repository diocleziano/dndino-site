# Connecting to DnDino: a player's guide

Use DnDino Hero on iPhone or iPad to send your sheet to the DM and, when enabled, share game values during play. Hero remains usable without a connection.

The DM's instructions are in the [DnDino guide](../sections/hero-sync.md).

!!! info "Versions and availability"
    The new reconnection comparison is prepared for the next update and needs versions of **both apps that support it**. Live requires **iOS/iPadOS 26 or later**. Older systems can send a sheet manually but cannot synchronize automatically, even outside combat.

## First connection

1. Select your character in Hero and check the sheet.
2. Connect the devices to the same local network, keep Wi-Fi and Bluetooth enabled, and allow Local Network access.
3. Ask the DM to open the adventure in DnDino and start the Hero connection.
4. In Hero, open **Settings → DnDino Connection**, press **Find DnDino**, and choose the session after checking the DM and adventure.
5. Wait for authorization. If needed, press **Send Character to DnDino**: the DM chooses whether to import a new sheet or link an existing one.

Authorization and sending a sheet **do not mean live is already active**.

## Who enables automatic updates?

**Only the DM** enables or disables automatic synchronization, separately for each player. There is no second switch to enable in Hero: the status tells you whether live is active or waiting for the DM.

Normally the DM must enable it again after each new connection. They can choose an automatic-start setting for already-authorized devices.

## What happens when you reconnect?

With the new versions, Hero sends the complete sheet when connecting, even if it was linked before. Sheet structure, levels, and configuration come from Hero.

If the states differ, the DM can compare and keep DnDino or Hero values for current/maximum/temporary HP, AC, inspiration, conditions, remaining resources, and used spell slots. **Hero values are selected initially**, but the DM can choose each field individually. Conditions are not automatically combined.

Hero shows that alignment is pending. Avoid repeatedly changing the same values during this phase: changes may require the comparison to refresh. After confirmation, the selected values are aligned; live starts only if the DM has enabled it.

Example: you corrected HP in Hero after the game, while DnDino still has an earlier value. The DM can keep your new HP without losing a condition they want to retain from DnDino.

## During the session

With live active, supported values such as HP, temporary HP, AC, inspiration, and conditions can travel in both directions. The DM can also change supported resource and slot counters.

- Consumable resources show **remaining out of total**; fixed progressions are reference information.
- Slots show total and used, separated by source when needed.
- Descriptions, resource maxima, new levels, and configuration changes require a **complete sheet update**, not merely live counters.
- Notifications help distinguish incoming damage, healing, conditions, and sheet updates.

The player remains responsible for the sheet. Live does not grant the DM unrestricted editing of every Hero field.

## Manual sending and chat

**Send Character to DnDino** sends the complete sheet, useful after changing levels, spells, or other structural information. The DM must check where it is imported. Compatible versions also let the DM request the already-linked sheet using their download button. Neither action enables live by itself or replaces a backup.

**Private chat with the DM** is available while live is active. It is separate from sheet transfers and game notifications.

## If the connection drops

Keep Hero visible during play: locking the device or switching apps can interrupt local communication. Hero can attempt reconnection when it returns to the foreground; **Reconnect** is also available in Settings. If automatic attempts run out, press Reconnect again.

If the status says connected but values do not update, ask the DM to check live, association, and alignment. For discovery issues, check the network, permissions, and that the Mac is accepting connections. **Test connection** checks communication but does not enable live or send a new sheet.

**Disconnect** ends the current connection, not your character. To find these instructions in the app, open **Settings → Support → Open online guide**.
