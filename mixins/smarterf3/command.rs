// native_hooks::Game::native_command (a hook point): run `/smarterf3`, leave
// everything else to the game (and to other mods).
fn smarterf3_command(game: &mut crate::game::Game<'_>, command: &str, ran: &mut bool) {
    if !*ran && game.smarterf3_command(command) {
        *ran = true;
    }
}
