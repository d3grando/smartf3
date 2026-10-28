// native_hooks::Game::native_settings_click (a hook point): a click on
// SmarterF3's settings page changes the setting, keeps it and applies it.
fn smarterf3_click(game: &mut crate::game::Game<'_>, mod_id: &str, button: usize) {
    if mod_id == crate::game::smarterf3::ID {
        game.smarterf3_settings_click(button);
    }
}
