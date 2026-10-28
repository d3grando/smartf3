// native_hooks::Game::native_settings (a hook point): SmarterF3's settings page.
fn smarterf3_page(game: &mut crate::game::Game<'_>, mod_id: &str, buttons: &mut Vec<String>) {
    if mod_id == crate::game::smarterf3::ID {
        buttons.extend(game.smarterf3_settings());
    }
}
