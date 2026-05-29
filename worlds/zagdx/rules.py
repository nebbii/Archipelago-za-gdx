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
    can_defeat_basic_enemy: Rule = HasAny("Wand", "Boomerang", "Jade Ring")
    goriya_boomerang_drop = world.get_location("Overworld D24 Goriya Boomerang Drop")

    world.set_rule(can_defeat_basic_enemy, goriya_boomerang_drop)

    shrine_of_earth_chasm = world.get_location("Shrine of Earth Chasm")

    world.set_rule(shrine_of_earth_chasm, Has("Ladder"))

def set_completion_condition(world: ZagdxWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Celestial Sign 1", world.player)
