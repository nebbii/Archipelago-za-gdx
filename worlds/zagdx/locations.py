from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ZagdxWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "Overworld D24 Goriya Boomerang Drop": 1,
    "Overworld E20 Full Pitcher": 2,
    "Overworld F28 Ladder": 3,
    "Overworld H23 Wand": 4,
    "Overworld J24 Empty Pitcher": 5,
    "Overworld J24 Vial of Wind": 6,

    "Shrine of Earth S104 1st Underworld Map": 7,
    "Shrine of Earth S105 Compass": 8,
    "Shrine of Earth S108 Jade Ring": 9,
    "Shrine of Earth S116 Red Boots": 10,
    "Shrine of Earth S122 1st Celestial Sign": 11,
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class ZagdxLocation(Location):
    game = "Zagdx"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ZagdxWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: ZagdxWorld) -> None:
    overworld_region_1 = world.get_region("Overworld Region 1 (Below Andor)")
    overworld_region_2 = world.get_region("Overworld Region 2 (Above Andor)")
    shrine_of_earth = world.get_region("Shrine of Earth")

    overworld_region_1_item_locations = get_location_names_with_ids(
        [
            "Overworld D24 Goriya Boomerang Drop",
            "Overworld E20 Full Pitcher",
            "Overworld F28 Ladder",
            "Overworld H23 Wand",
            "Overworld J24 Empty Pitcher",
            "Overworld J24 Vial of Wind",
        ]
    )
    overworld_region_1.add_locations(overworld_region_1_item_locations, ZagdxLocation)

    shrine_of_earth_item_locations = get_location_names_with_ids(
        [
            "Shrine of Earth S104 1st Underworld Map",
            "Shrine of Earth S105 Compass",
            "Shrine of Earth S108 Jade Ring",
            "Shrine of Earth S116 Red Boots",
            "Shrine of Earth S122 1st Celestial Sign",
        ]
    )
    shrine_of_earth.add_locations(shrine_of_earth_item_locations, ZagdxLocation)

    if world.options.enemysanity:

def create_events(world: ZagdxWorld) -> None:
    overworld_region_1 = world.get_region("Overworld Region 1 (Below Andor)")
    overworld_region_2 = world.get_region("Overworld Region 2 (Above Andor)")
    shrine_of_earth = world.get_region("Shrine of Earth")

    overworld_shrine_of_earth_chasm = ZagdxLocation(world.player, "Shrine of Earth Chasm", None, overworld_region_1)
    overworld_region_1.locations.append(overworld_shrine_of_earth_chasm)

    ladder_placed = items.ZagdxItem("Shrine of Earth Ladder Placed", ItemClassification.progression, None, world.player)
    overworld_shrine_of_earth_chasm.place_locked_item(ladder_placed)

    celestial_sign_1_pedestal = world.get_location("Shrine of Earth S122 1st Celestial Sign")
    celestial_sign_1 = world.create_item("Celestial Sign 1")
    celestial_sign_1_pedestal.place_locked_item(celestial_sign_1)

    # Enemy sanity
    if world.options.enemysanity:
        overworld_enemy_d24_1_slain = ZagdxLocation(world.player, "Overworld Enemy D24 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_d24_1_slain)

        overworld_enemy_e21_0_slain = ZagdxLocation(world.player, "Overworld Enemy E21 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e21_0_slain)
        overworld_enemy_e21_1_slain = ZagdxLocation(world.player, "Overworld Enemy E21 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e21_1_slain)

        overworld_enemy_e22_0_slain = ZagdxLocation(world.player, "Overworld Enemy E22 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e22_0_slain)
        overworld_enemy_e22_1_slain = ZagdxLocation(world.player, "Overworld Enemy E22 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e22_1_slain)
        overworld_enemy_e22_2_slain = ZagdxLocation(world.player, "Overworld Enemy E22 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e22_2_slain)
        overworld_enemy_e22_3_slain = ZagdxLocation(world.player, "Overworld Enemy E22 #3 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e22_3_slain)

        overworld_enemy_e23_0_slain = ZagdxLocation(world.player, "Overworld Enemy E23 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e23_0_slain)
        overworld_enemy_e23_1_slain = ZagdxLocation(world.player, "Overworld Enemy E23 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e23_1_slain)
        overworld_enemy_e23_2_slain = ZagdxLocation(world.player, "Overworld Enemy E23 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e23_2_slain)

        overworld_enemy_e24_0_slain = ZagdxLocation(world.player, "Overworld Enemy E24 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e24_0_slain)
        overworld_enemy_e24_1_slain = ZagdxLocation(world.player, "Overworld Enemy E24 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_e24_1_slain)

        overworld_enemy_f21_0_slain = ZagdxLocation(world.player, "Overworld Enemy F21 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f21_0_slain)
        overworld_enemy_f21_1_slain = ZagdxLocation(world.player, "Overworld Enemy F21 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f21_1_slain)
        overworld_enemy_f21_2_slain = ZagdxLocation(world.player, "Overworld Enemy F21 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f21_2_slain)
        overworld_enemy_f21_3_slain = ZagdxLocation(world.player, "Overworld Enemy F21 #3 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f21_3_slain)
        overworld_enemy_f21_4_slain = ZagdxLocation(world.player, "Overworld Enemy F21 #4 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f21_4_slain)

        overworld_enemy_f25_0_slain = ZagdxLocation(world.player, "Overworld Enemy F25 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f25_0_slain)
        overworld_enemy_f25_1_slain = ZagdxLocation(world.player, "Overworld Enemy F25 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f25_1_slain)
        overworld_enemy_f25_2_slain = ZagdxLocation(world.player, "Overworld Enemy F25 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f25_2_slain)

        overworld_enemy_f27_0_slain = ZagdxLocation(world.player, "Overworld Enemy F27 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f27_0_slain)
        overworld_enemy_f27_1_slain = ZagdxLocation(world.player, "Overworld Enemy F27 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f27_1_slain)
        overworld_enemy_f27_2_slain = ZagdxLocation(world.player, "Overworld Enemy F27 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_f27_2_slain)

        overworld_enemy_g21_0_slain = ZagdxLocation(world.player, "Overworld Enemy G21 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g21_0_slain)
        overworld_enemy_g21_1_slain = ZagdxLocation(world.player, "Overworld Enemy G21 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g21_1_slain)
        overworld_enemy_g21_2_slain = ZagdxLocation(world.player, "Overworld Enemy G21 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g21_2_slain)

        overworld_enemy_g25_0_slain = ZagdxLocation(world.player, "Overworld Enemy G25 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g25_0_slain)
        overworld_enemy_g25_1_slain = ZagdxLocation(world.player, "Overworld Enemy G25 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g25_1_slain)
        overworld_enemy_g25_2_slain = ZagdxLocation(world.player, "Overworld Enemy G25 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g25_2_slain)

        overworld_enemy_g26_0_slain = ZagdxLocation(world.player, "Overworld Enemy G26 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g26_0_slain)
        overworld_enemy_g26_1_slain = ZagdxLocation(world.player, "Overworld Enemy G26 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g26_1_slain)
        overworld_enemy_g26_2_slain = ZagdxLocation(world.player, "Overworld Enemy G26 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g26_2_slain)

        overworld_enemy_g27_0_slain = ZagdxLocation(world.player, "Overworld Enemy G27 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g27_0_slain)
        overworld_enemy_g27_1_slain = ZagdxLocation(world.player, "Overworld Enemy G27 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g27_1_slain)

        overworld_enemy_g28_0_slain = ZagdxLocation(world.player, "Overworld Enemy G28 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g28_0_slain)
        overworld_enemy_g28_1_slain = ZagdxLocation(world.player, "Overworld Enemy G28 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g28_1_slain)

        overworld_enemy_g29_0_slain = ZagdxLocation(world.player, "Overworld Enemy G29 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g29_0_slain)
        overworld_enemy_g29_1_slain = ZagdxLocation(world.player, "Overworld Enemy G29 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g29_1_slain)

        overworld_enemy_g30_0_slain = ZagdxLocation(world.player, "Overworld Enemy G30 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g30_0_slain)
        overworld_enemy_g30_1_slain = ZagdxLocation(world.player, "Overworld Enemy G30 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g30_1_slain)
        overworld_enemy_g30_2_slain = ZagdxLocation(world.player, "Overworld Enemy G30 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g30_2_slain)

        overworld_enemy_g31_0_slain = ZagdxLocation(world.player, "Overworld Enemy G31 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g31_0_slain)
        overworld_enemy_g31_1_slain = ZagdxLocation(world.player, "Overworld Enemy G31 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g31_1_slain)
        overworld_enemy_g31_2_slain = ZagdxLocation(world.player, "Overworld Enemy G31 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g31_2_slain)
        overworld_enemy_g31_3_slain = ZagdxLocation(world.player, "Overworld Enemy G31 #3 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_g31_3_slain)

        overworld_enemy_h21_0_slain = ZagdxLocation(world.player, "Overworld Enemy H21 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h21_0_slain)
        overworld_enemy_h21_1_slain = ZagdxLocation(world.player, "Overworld Enemy H21 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h21_1_slain)
        overworld_enemy_h21_2_slain = ZagdxLocation(world.player, "Overworld Enemy H21 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h21_2_slain)
        overworld_enemy_h21_3_slain = ZagdxLocation(world.player, "Overworld Enemy H21 #3 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h21_3_slain)
        overworld_enemy_h21_4_slain = ZagdxLocation(world.player, "Overworld Enemy H21 #4 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h21_4_slain)

        overworld_enemy_h25_0_slain = ZagdxLocation(world.player, "Overworld Enemy H25 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h25_0_slain)
        overworld_enemy_h25_1_slain = ZagdxLocation(world.player, "Overworld Enemy H25 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h25_1_slain)
        overworld_enemy_h25_2_slain = ZagdxLocation(world.player, "Overworld Enemy H25 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h25_2_slain)

        overworld_enemy_h26_0_slain = ZagdxLocation(world.player, "Overworld Enemy H26 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h26_0_slain)
        overworld_enemy_h26_1_slain = ZagdxLocation(world.player, "Overworld Enemy H26 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h26_1_slain)
        overworld_enemy_h26_2_slain = ZagdxLocation(world.player, "Overworld Enemy H26 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h26_2_slain)

        overworld_enemy_h27_0_slain = ZagdxLocation(world.player, "Overworld Enemy H27 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h27_0_slain)
        overworld_enemy_h27_1_slain = ZagdxLocation(world.player, "Overworld Enemy H27 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h27_1_slain)
        overworld_enemy_h27_2_slain = ZagdxLocation(world.player, "Overworld Enemy H27 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h27_2_slain)

        overworld_enemy_h28_0_slain = ZagdxLocation(world.player, "Overworld Enemy H28 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h28_0_slain)
        overworld_enemy_h28_1_slain = ZagdxLocation(world.player, "Overworld Enemy H28 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h28_1_slain)
        overworld_enemy_h28_2_slain = ZagdxLocation(world.player, "Overworld Enemy H28 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_h28_2_slain)

        overworld_enemy_i21_0_slain = ZagdxLocation(world.player, "Overworld Enemy I21 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i21_0_slain)

        overworld_enemy_i22_0_slain = ZagdxLocation(world.player, "Overworld Enemy I22 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i22_0_slain)
        overworld_enemy_i22_1_slain = ZagdxLocation(world.player, "Overworld Enemy I22 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i22_1_slain)
        overworld_enemy_i22_2_slain = ZagdxLocation(world.player, "Overworld Enemy I22 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i22_2_slain)
        overworld_enemy_i22_3_slain = ZagdxLocation(world.player, "Overworld Enemy I22 #3 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i22_3_slain)
        overworld_enemy_i22_4_slain = ZagdxLocation(world.player, "Overworld Enemy I22 #4 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i22_4_slain)

        overworld_enemy_i23_0_slain = ZagdxLocation(world.player, "Overworld Enemy I23 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i23_0_slain)
        overworld_enemy_i23_1_slain = ZagdxLocation(world.player, "Overworld Enemy I23 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i23_1_slain)
        overworld_enemy_i23_2_slain = ZagdxLocation(world.player, "Overworld Enemy I23 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i23_2_slain)

        overworld_enemy_i24_0_slain = ZagdxLocation(world.player, "Overworld Enemy I24 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i24_0_slain)
        overworld_enemy_i24_1_slain = ZagdxLocation(world.player, "Overworld Enemy I24 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i24_1_slain)
        overworld_enemy_i24_2_slain = ZagdxLocation(world.player, "Overworld Enemy I24 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i24_2_slain)
        overworld_enemy_i24_3_slain = ZagdxLocation(world.player, "Overworld Enemy I24 #3 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i24_3_slain)
        overworld_enemy_i24_4_slain = ZagdxLocation(world.player, "Overworld Enemy I24 #4 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i24_4_slain)

        overworld_enemy_i25_0_slain = ZagdxLocation(world.player, "Overworld Enemy I25 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i25_0_slain)
        overworld_enemy_i25_1_slain = ZagdxLocation(world.player, "Overworld Enemy I25 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i25_1_slain)
        overworld_enemy_i25_2_slain = ZagdxLocation(world.player, "Overworld Enemy I25 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i25_2_slain)
        overworld_enemy_i25_3_slain = ZagdxLocation(world.player, "Overworld Enemy I25 #3 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i25_3_slain)

        overworld_enemy_i26_0_slain = ZagdxLocation(world.player, "Overworld Enemy I26 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i26_0_slain)
        overworld_enemy_i26_1_slain = ZagdxLocation(world.player, "Overworld Enemy I26 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i26_1_slain)
        overworld_enemy_i26_2_slain = ZagdxLocation(world.player, "Overworld Enemy I26 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_i26_2_slain)

        overworld_enemy_j23_0_slain = ZagdxLocation(world.player, "Overworld Enemy J23 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_j23_0_slain)
        overworld_enemy_j23_1_slain = ZagdxLocation(world.player, "Overworld Enemy J23 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_j23_1_slain)
        overworld_enemy_j23_2_slain = ZagdxLocation(world.player, "Overworld Enemy J23 #2 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_j23_2_slain)
        overworld_enemy_j23_3_slain = ZagdxLocation(world.player, "Overworld Enemy J23 #3 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_j23_3_slain)

        overworld_enemy_j25_0_slain = ZagdxLocation(world.player, "Overworld Enemy J25 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_j25_0_slain)
        overworld_enemy_j25_1_slain = ZagdxLocation(world.player, "Overworld Enemy J25 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_j25_1_slain)

        overworld_enemy_j26_0_slain = ZagdxLocation(world.player, "Overworld Enemy J26 #0 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_j26_0_slain)
        overworld_enemy_j26_1_slain = ZagdxLocation(world.player, "Overworld Enemy J26 #1 slain", None, overworld_region_1)
        overworld_region_1.locations.append(overworld_enemy_j26_1_slain)

        shrine_of_earth_enemy_s101a_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S101A #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s101a_0_slain)

        shrine_of_earth_enemy_s103_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S103 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s103_0_slain)
        shrine_of_earth_enemy_s103_1_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S103 #1 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s103_1_slain)

        shrine_of_earth_enemy_s104_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S104 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s104_0_slain)
        shrine_of_earth_enemy_s104_1_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S104 #1 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s104_1_slain)

        shrine_of_earth_enemy_s105_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S105 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s105_0_slain)
        shrine_of_earth_enemy_s105_1_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S105 #1 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s105_1_slain)
        shrine_of_earth_enemy_s105_2_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S105 #2 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s105_2_slain)

        shrine_of_earth_enemy_s106_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S106 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s106_0_slain)
        shrine_of_earth_enemy_s106_1_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S106 #1 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s106_1_slain)

        shrine_of_earth_enemy_s107_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S107 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s107_0_slain)

        shrine_of_earth_enemy_s110_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S110 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s110_0_slain)
        shrine_of_earth_enemy_s110_1_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S110 #1 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s110_1_slain)
        shrine_of_earth_enemy_s110_2_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S110 #2 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s110_2_slain)
        shrine_of_earth_enemy_s110_3_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S110 #3 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s110_3_slain)

        shrine_of_earth_enemy_s111_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S111 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s111_0_slain)

        shrine_of_earth_enemy_s112_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S112 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s112_0_slain)

        shrine_of_earth_enemy_s115_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S115 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s115_0_slain)
        shrine_of_earth_enemy_s115_1_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S115 #1 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s115_1_slain)

        shrine_of_earth_enemy_s116_1_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S116 #1 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s116_1_slain)
        shrine_of_earth_enemy_s116_2_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S116 #2 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s116_2_slain)
        shrine_of_earth_enemy_s116_3_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S116 #3 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s116_3_slain)

        shrine_of_earth_enemy_s120_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S120 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s120_0_slain)

        shrine_of_earth_enemy_s121_0_slain = ZagdxLocation(world.player, "Shrine of Earth Enemy S121 #0 slain", None, shrine_of_earth)
        shrine_of_earth.locations.append(shrine_of_earth_enemy_s121_0_slain)
