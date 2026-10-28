// native_hooks::Game::native_mods (a hook point): SmarterF3's row in Options > Mods.
fn smarterf3_listed(mods: &mut Vec<crate::game::native_hooks::NativeMod>) {
    use crate::game::smarterf3 as sf;
    mods.push(crate::game::native_hooks::NativeMod {
        id: sf::ID.into(),
        title: format!("{} {}", sf::NAME, sf::VERSION),
        description: sf::DESCRIPTION.into(),
        keys: Vec::new(),
    });
}
