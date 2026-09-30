# No Man's Sky – Manual Archipelago

A community-maintained **No Man's Sky** game for [Archipelago](https://archipelago.gg), the multiworld randomizer.

> **This is a "Manual" game.** There is no mod to install for No Man's Sky itself. You play the game normally and use the Archipelago **Manual Client** to mark checks as complete and see which items you've received. The game runs on the honor system: don't use a blueprint or item until the client says you've received it.

## Goals

Choose one in your YAML:

| Goal | What you do |
|---|---|
| Mine activated indium | Mine activated indium in a blue system. *Good for synced game* |
| Fusion ignitor or stasis device | Obtain a fusion ignitor or a stasis device |
| Indium + ignitor/stasis | Do both of the above |
| Mine activated indium & Fusion ignitor or stasis device | Mine activated indium in a blue system AND Obtain a fusion ignitor or a stasis device. *Good for asynced game* |
| Quantum processor | Obtain a quantum processor *Good for synced game* |

---

## Quick start

### 1. Install the apworld

1. Download `manual_nomanssky_zinx.apworld` from the [Releases page](https://github.com/gitzinx/manual_nomanssky_zinx/releases/latest).
2. **Double-click it.** Archipelago should install it automatically.
   - If that doesn't work, open the **Archipelago Launcher**, click **Install APWorld**, and select the file.
   - Or copy the file into the `custom_worlds` folder inside your Archipelago install directory.
3. Restart the Archipelago Launcher if it was open.

### 2. Set up your YAML

The YAML is your settings file. It tells Archipelago how you want your game configured.

1. Download `Manual_NoMansSky_Zinx.yaml` from the [Releases page](https://github.com/gitzinx/manual_nomanssky_zinx/releases/latest).
2. Open it in any text editor (Notepad is fine).
3. Change `name:` to your player name (16 characters max, no spaces recommended).
4. Set your options. Each option has a comment explaining what it does. Key ones:
   - **`goal`**: your win condition. Put `50` on the goal you want and `0` on the rest.
   - **`starting_blueprints`**: blueprints you begin with to help you leave the first system.
   - **`max_missions`** and **`mission_steps`**: how many space station mission checks exist.
   - **`*_milestone_max_star`**: how many stars of each milestone category (Overall Journey, Alien Encounters, Words Collected, and so on) count as checks. `0` turns that category off.
   - **`species_standing_maximum`**, **`faction_standing_maximum`**, **`outlaw_standing_maximum`**: how much standing counts as checks. `0` turns them off.
   - **`enable_fishing_checks`**, **`enable_cooking_checks`**, **`enable_freighter_checks`**, **`enable_archaeology_checks`**: optional check groups (all off by default).
   - **`enable_twitch_drops`** and **`enable_expedition_rewards`**: add those item types to the pool (off by default).
5. You can check your file at [archipelago.gg/check](https://archipelago.gg/check) before sending it in.

**Weights:** each option is a list of choices with numbers next to them. A higher number means a higher chance. `50` on one choice and `0` on the others always picks that choice. You don't need to touch the numbers unless you want randomness.

---

## Tips

- **Honor system.** The game can't lock blueprints for you, so hold off on crafting or using anything until it's been sent to you.
- **New to Archipelago?** See the [official setup guide](https://archipelago.gg/tutorial/Archipelago/setup/en).

## Downloads and versions

Every version of this manual is on the [Releases page](https://github.com/gitzinx/manual_nomanssky_zinx/releases), with patch notes for each. **Always grab the apworld and YAML from the same release.**

## Contribution

Found a bug, or have an idea for new checks or items? Open an [issue](https://github.com/gitzinx/manual_nomanssky_zinx/issues). Contributors are welcome.

## Credits

Original manual by **Zinx**, with updates from community contributors. Built on the [Manual for Archipelago](https://github.com/ManualForArchipelago/Manual) framework.

No Man's Sky is a trademark of Hello Games. This is an unofficial fan project and is not affiliated with or endorsed by Hello Games.
