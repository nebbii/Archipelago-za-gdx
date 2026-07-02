from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule
from rule_builder.rules import Has, HasAny, Rule

if TYPE_CHECKING:
    from .world import ZagdxWorld


def set_all_rules(world: ZagdxWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: ZagdxWorld) -> None:
    overworld_region_1_to_shrine_of_earth = world.get_entrance("Overworld Region 1 to Shrine of Earth")
    overworld_region_1_to_overworld_region_2 = world.get_entrance("Overworld Region 1 to Overworld Region 2")

    has_ladder_been_placed_over_chasm: Rule = Has("Shrine of Earth Ladder Placed")

    world.set_rule(overworld_region_1_to_shrine_of_earth, has_ladder_been_placed_over_chasm)

    can_cross_andor = Has("Red Boots")
    world.set_rule(overworld_region_1_to_overworld_region_2, can_cross_andor)

def set_all_location_rules(world: ZagdxWorld) -> None:
    can_defeat_basic_enemy: Rule = HasAny("Wand", "Dagger", "Boomerang", "Jade Ring")
    goriya_boomerang_drop = world.get_location("Overworld D24 Boomerang")

    world.set_rule(can_defeat_basic_enemy, goriya_boomerang_drop)

    shrine_of_earth_chasm = world.get_location("Shrine of Earth Chasm")

    world.set_rule(shrine_of_earth_chasm, Has("Ladder"))

    if world.options.enemysanity:
        for location in world.get_locations():
            if "slain" in location.name.lower():
                world.set_rule(location, can_defeat_basic_enemy)

    shrine_of_earth_underground_map = world.get_location("Shrine of Earth S104 1st Underworld Map")
    world.set_rule(shrine_of_earth_underground_map, can_defeat_basic_enemy)

    shrine_of_earth_compass = world.get_location("Shrine of Earth S105 Compass")
    world.set_rule(shrine_of_earth_compass, can_defeat_basic_enemy)

    boss_sardak_red = world.get_location("Shrine of Earth Enemy in S107 #0 slain")
    world.set_rule(boss_sardak_red, Has("Jade Ring"))

    boss_sardak_blue = world.get_location("Shrine of Earth Enemy in S112 #0 slain")
    world.set_rule(boss_sardak_blue, Has("Jade Ring"))

    boss_sardak_yellow = world.get_location("Shrine of Earth Enemy in S120 #0 slain")
    world.set_rule(boss_sardak_yellow, Has("Jade Ring"))

    boss_llort = world.get_location("Shrine of Earth Enemy in S121 #0 slain")
    world.set_rule(boss_llort, Has("Wand"))

    shrine_of_earth_celestial_sign_1 = world.get_location("Shrine of Earth S122 1st Celestial Sign")
    world.set_rule(shrine_of_earth_celestial_sign_1, Has("Wand") & Has("Jade Ring"))

def set_completion_condition(world: ZagdxWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Celestial Sign 1", world.player)
