# SmarterF3

A **native** [Horizon](https://github.com/horizon-rust/horizon) mod (a horizon-mixins source bundle, `.hnmod`): a
tidier, configurable F3 debug screen. The same information as the vanilla screen, grouped into **modules**
(FPS, server, coordinates, chunk, facing, world, biome, light, chart keys, system, rendering, targeted block, fluid
and entity), each with its own label and value colours, shown or hidden, in the left or right column, in the order
you choose. Optional text shadow and background, a compact layout, and the vanilla F3 screen one click away.

Inspired by BetterF3 (https://modrinth.com/mod/betterf3); not affiliated, no code from it.

> **Native mods are not sandboxed.** A native mod is Rust source compiled into your own Horizon game, and runs with
> your rights. Read the source (`mixins/smarterf3/`) before you build it.

## What it shows

Press F3 as usual. Each line is `Label: value`, the label in the module's label colour, the value in its value
colour. Modules with nothing to show (nothing targeted, no world) leave no gap.

| Module | Full layout | Compact layout |
| --- | --- | --- |
| FPS | `FPS: 112 (T: 120 (fifo) @165Hz)`: frames per second, the frame-rate limit, the present mode, the monitor's refresh rate | `FPS: 112` |
| Server | `Minecraft: 26.3 (26.3/horizon)`, `Server: integrated @ 6.6/50.0 ms, 28 tx, 492 rx` (or the server's brand) | `Server: 6.6 ms/tick` |
| Coordinates | `XYZ: 108.500 / 104.00000 / -51.500`, `Block: 108 104 -52` | `XYZ: 108.5 / 104.0 / -51.5` |
| Chunk | `Chunk: 6 6 -4`, `Region: r.0.-1.mca [6 28]`, `Section-relative: 12 08 12` | `Chunk: 6 6 -4 in r.0.-1` |
| Facing | `Facing: south (+Z) (-1.0 / 7.1)` (yaw / pitch) | `Facing: south (+Z)` |
| World | `Dimension: minecraft:overworld`, `Forced chunks: 0`, `Day: 1 (12:00)` | `World: overworld, day 1 12:00` |
| Biome | `Biome: minecraft:plains` (at your feet) | `Biome: plains` |
| Light | `Light: 15 sky, 3 block` (at your feet) | `Light: 15 (15/3)` |
| Chart keys | the vanilla screen's `Debug charts: ...` and `To edit: ...` lines | (hidden) |
| System | `Memory`, `CPU`, `GPU`, `Driver`, `Display`, `Window` | `Memory`, `GPU` |
| Rendering | clouds and biome blend, filtering, terrain rendering, the shader pack's GPU passes | (hidden) |
| Targeted block | `Targeted Block: 108, 103, -52`, `minecraft:oak_log`, then each property (`axis: y`) | `Block: oak_log @ 108 103 -52` |
| Targeted fluid | `Targeted Fluid: x, y, z`, `minecraft:water` / `flowing_water` / `lava` / `flowing_lava`, `amount`, `falling` | `Fluid: water @ x y z` |
| Targeted entity | `Targeted Entity: minecraft:zombie` | `Entity: zombie` |

The left column holds where you are, the right one the machine and what you look at, as in the vanilla screen. The
targeted block and fluid are looked for 20 blocks ahead, as vanilla F3 does; the targeted entity is the one an
attack would hit (mobs, armour stands, paintings, item frames, boats, minecarts, the dragon, LAN players).

The F3 charts (F3+1, F3+2, the lightmap) are drawn exactly as the game draws them. When debug info is reduced (the
`reducedDebugInfo` game rule or the accessibility option), the coordinates, facing and targeted modules are left out
and the chunk module shows only the section-relative position, as vanilla hides where you are.

**Memory** is the game's resident memory (Horizon has no Java heap): read every 2 seconds on a thread of its own
while the System module shows; on Windows by asking `tasklist` (no window opens), on Linux and macOS as Horizon's
benchmark does.

## Settings

**Options > Mods** lists SmarterF3 with its **Settings** button. The row's own button turns the mod off (it then does
nothing at all and F3 shows the vanilla screen; the launcher's next build leaves it out) and on again. Each click on
the settings page moves a setting to its next value; it is saved and applies at once.

| Button | Does |
| --- | --- |
| Debug screen: SmarterF3 / vanilla F3 | **The vanilla toggle**: vanilla F3 is one click (or `/smarterf3 off`) away |
| Layout: full / compact | Compact: one short line per module, no chart keys, no rendering lines |
| Text shadow: ON / OFF | |
| Background: grey (vanilla) / dark / none | The box behind each line |
| Gap between modules: ON / OFF | An empty line between two modules |
| Module 3/14: Coordinates (click for the next) | Picks the module the five buttons below change |
| &nbsp;&nbsp;Coordinates: shown / hidden | |
| &nbsp;&nbsp;Label colour: Red | Steps through the 16 chat colours and the F3 grey |
| &nbsp;&nbsp;Value colour: F3 Grey | Same |
| &nbsp;&nbsp;Column: left / right | |
| &nbsp;&nbsp;Move up (3rd of 9 in the left column) | One place up among the modules of its column (hidden ones count) |
| &nbsp;&nbsp;Move down | One place down |
| Reset to defaults | Every setting back to its default |

## Command

| Command | Does |
| --- | --- |
| `/smarterf3` or `/smarterf3 status` | Says which screen F3 shows |
| `/smarterf3 on` / `off` (or `vanilla`) / `toggle` | SmarterF3's screen / the vanilla one |
| `/smarterf3 compact` | Switches between the full and compact layouts |
| `/smarterf3 reload` | Reads `config.json` again |

It is a client command: it runs in your window, in single player and on servers alike, and never reaches the server.

## Configuration file

The settings page writes, and the mod reads, `horizon-mods/.horizon-mod-data/smarterf3/config.json` (beside the
game's `options.txt`, in the instance that plays the native build). Every key is optional; modules the file leaves out
keep their defaults and come after the listed ones. An unknown key, module or value makes the mod step aside (F3
shows the vanilla screen; the settings page shows the error with a button to read the file again and a reset) until
the file is fixed.

```json
{
  "enabled": true,
  "compact": false,
  "shadow": true,
  "background": "vanilla",
  "spacing": true,
  "modules": [
    { "id": "fps", "shown": true, "column": "left", "label": "green", "value": "f3_gray" },
    { "id": "coordinates", "shown": true, "column": "left", "label": "#FF8800", "value": "white" }
  ]
}
```

| Key | Values |
| --- | --- |
| `enabled` | `true`: SmarterF3 draws F3. `false`: the vanilla screen |
| `compact` | Compact layout |
| `shadow` | Text shadow |
| `background` | `"vanilla"` (ARGB `#90505050`), `"dark"` (`#A0000000`), `"none"` |
| `spacing` | An empty line between modules |
| `modules` | Their drawing order. `id`: `fps`, `server`, `coordinates`, `chunk`, `facing`, `world`, `biome`, `light`, `charts`, `system`, `rendering`, `target_block`, `target_fluid`, `target_entity`. `column`: `left`, `right`. Colours: a chat colour name (`white`, `gray`, `dark_gray`, `black`, `red`, `gold`, `yellow`, `green`, `aqua`, `blue`, `light_purple`, `dark_red`, `dark_green`, `dark_aqua`, `dark_blue`, `dark_purple`), `f3_gray` (the vanilla screen's `#E0E0E0`), or any `#RRGGBB` |

## Compatibility

Horizon's native mods can use **hook points** (`game/native_hooks.rs`, `NATIVE_HOOKS_API`): functions kept stable from
release to release. SmarterF3 uses them for everything they cover:

- `native_mods`, `native_settings`, `native_settings_click`: the row in Options > Mods and the settings page, with
  the helpers `native_setting` / `native_set_setting` for the file and `native_on` for the row's off switch;
- `native_command`: `/smarterf3` (answered with the `native_chat` helper).

There is no hook point for the debug screen, so one game function is hooked directly and the mod is **pinned**:

| Hook | Kind | Why it is not a hook point |
| --- | --- | --- |
| `Game::hud` | cancellable HEAD | SmarterF3's screen replaces the vanilla one. `native_hud` can't do it: it is drawn under menus, chat and toasts, isn't drawn under F1 while a menu is open, and nothing would stop the vanilla text from being drawn as well. The vanilla screen's own function, `debug_keys::Game::draw_debug_overlay`, can't be hooked: its body has macros (`format!`), which horizon-mixins refuses (`E_UNSUPPORTED_MACRO`). So the hook is on its caller `Game::hud` (six calls, no macros): **only while F3 is open** and SmarterF3 is on, it builds the HUD with the same calls in the same order (`hud_layers`, dialog, pack prompt, link prompt, the debug screen, the frame graph, the controller cursor) with SmarterF3's screen in place of `draw_debug_overlay`, so it is drawn where the vanilla screen is: over everything, menus included, at the debug GUI scale. Otherwise the game's own `hud` runs. |

The adapter (`native.rs`) also reads the game's internals the vanilla screen reads (renderer and window info, the
tick clock, chunks, light, the block registry, the crosshair hit tests), another reason it builds on one commit only.
No `native_tick` hook: SmarterF3 is client-only, keeps no per-tick state, and checks Options > Mods' switch where it
acts (it only ever acts in the window's game, `native_window`).

Pinned: Horizon `142388e1c136e622652ec7505af15d8ad195e041`, horizon-mixins `0d6b103c70633d8fd9443d8d0acd3aadaacedb06`,
game 26.3, the same pins as TreeFall 0.3.0 and Mason 0.2.0, so the three build together into one game. Checked with
horizon-mixins `plan` and `apply` on that commit, alone and together with TreeFall and Mason (21 injections, 14
modules, no conflict; neither of them hooks `Game::hud`).

## Build and try

SmarterF3 is a source bundle; the launcher compiles it into a game of its own:

```sh
horizon-launcher native-build C:\Users\degrando\projects\smarterf3 --version v0.2.97 --trust-native-code
```

`--version` is the installed version whose game files the build reuses; the build compiles the pinned commit. To build
it with TreeFall and Mason, put the three bundles in one folder, one subfolder each, and build that folder.

## Development

`mixins/smarterf3/`:

- `horizon-mixin.toml`: two support modules and five HEAD hooks (one pinned, four on hook points).
- `runtime.rs`: everything that can be decided without the game (the modules and their lines, full and compact,
  the columns and where each line goes, colours, the file, the settings page's buttons and clicks, the command),
  with unit tests. It is both this repository's Cargo library and the injected `crate::game::smarterf3` module.
- `native.rs`: the adapter to the game (`crate::game::smarterf3_native`): reads a `Snapshot` and draws.
- `hud.rs`, `command.rs`, `list.rs`, `settings.rs`, `click.rs`: the hook helpers.

`tests/format.rs` declares the game-side files (never compiled here) so `cargo fmt` checks them too.

```sh
cargo test
cargo fmt --check
cargo clippy --all-targets -- -D warnings
python tools/pack_hnmod.py   # dist/smarterf3-0.1.0.hnmod
```

Written with [Claude Code](https://claude.com/claude-code).

## License

[MIT](LICENSE)
