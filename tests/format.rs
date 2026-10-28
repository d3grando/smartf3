// The game-side files, never compiled here (`cfg(any())` is never true) but
// declared so that `cargo fmt` formats and checks them too: the adapter, and
// each hook's helper (one function each, injected into a game function). They
// only compile inside Horizon. runtime.rs, the library, is tested in itself.

#[cfg(any())]
#[path = "../mixins/smarterf3/click.rs"]
mod hook_click;
#[cfg(any())]
#[path = "../mixins/smarterf3/command.rs"]
mod hook_command;
#[cfg(any())]
#[path = "../mixins/smarterf3/hud.rs"]
mod hook_hud;
#[cfg(any())]
#[path = "../mixins/smarterf3/list.rs"]
mod hook_list;
#[cfg(any())]
#[path = "../mixins/smarterf3/settings.rs"]
mod hook_settings;
#[cfg(any())]
#[path = "../mixins/smarterf3/native.rs"]
mod smarterf3_native;
