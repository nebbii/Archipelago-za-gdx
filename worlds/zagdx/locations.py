from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ZagdxWorld

LOCATION_NAME_TO_ID = {
    "Overworld D24 Boomerang": 1,
    "Overworld E20 Full Pitcher": 2,
    "Overworld F26 Candle": 14,
    "Overworld F26 Magic Shield": 15,
    "Overworld F28 Ladder": 3,
    "Overworld H23 Wand": 4,
    "Overworld J22 Firestorm": 5,
    "Overworld J22a Dagger": 6,
    "Overworld J24 Empty Pitcher": 7,
    "Overworld J24 Vial of Wind": 8,

    "Shrine of Earth S104 1st Underworld Map": 9,
    "Shrine of Earth S105 Compass": 10,
    "Shrine of Earth S108 Jade Ring": 11,
    "Shrine of Earth S116 Red Boots": 12,
    "Shrine of Earth S122 1st Celestial Sign": 13,

    "Overworld Enemy in D24 #1 slain": 1001,
    "Overworld Enemy in E21 #0 slain": 1002,
    "Overworld Enemy in E21 #1 slain": 1003,
    "Overworld Enemy in E22 #0 slain": 1004,
    "Overworld Enemy in E22 #1 slain": 1005,
    "Overworld Enemy in E22 #2 slain": 1006,
    "Overworld Enemy in E22 #3 slain": 1007,
    "Overworld Enemy in E23 #0 slain": 1008,
    "Overworld Enemy in E23 #1 slain": 1009,
    "Overworld Enemy in E23 #2 slain": 1010,
    "Overworld Enemy in E24 #0 slain": 1011,
    "Overworld Enemy in E24 #1 slain": 1012,
    "Overworld Enemy in F21 #0 slain": 1013,
    "Overworld Enemy in F21 #1 slain": 1014,
    "Overworld Enemy in F21 #2 slain": 1015,
    "Overworld Enemy in F21 #3 slain": 1016,
    "Overworld Enemy in F21 #4 slain": 1017,
    "Overworld Enemy in F25 #0 slain": 1018,
    "Overworld Enemy in F25 #1 slain": 1019,
    "Overworld Enemy in F25 #2 slain": 1020,
    "Overworld Enemy in F27 #0 slain": 1021,
    "Overworld Enemy in F27 #1 slain": 1022,
    "Overworld Enemy in F27 #2 slain": 1023,
    "Overworld Enemy in G21 #0 slain": 1024,
    "Overworld Enemy in G21 #1 slain": 1025,
    "Overworld Enemy in G21 #2 slain": 1026,
    "Overworld Enemy in G25 #0 slain": 1027,
    "Overworld Enemy in G25 #1 slain": 1028,
    "Overworld Enemy in G25 #2 slain": 1029,
    "Overworld Enemy in G26 #0 slain": 1030,
    "Overworld Enemy in G26 #1 slain": 1031,
    "Overworld Enemy in G26 #2 slain": 1032,
    "Overworld Enemy in G27 #0 slain": 1033,
    "Overworld Enemy in G27 #1 slain": 1034,
    "Overworld Enemy in G28 #0 slain": 1035,
    "Overworld Enemy in G28 #1 slain": 1036,
    "Overworld Enemy in G29 #0 slain": 1037,
    "Overworld Enemy in G29 #1 slain": 1038,
    "Overworld Enemy in G30 #0 slain": 1039,
    "Overworld Enemy in G30 #1 slain": 1040,
    "Overworld Enemy in G30 #2 slain": 1041,
    "Overworld Enemy in G31 #0 slain": 1042,
    "Overworld Enemy in G31 #1 slain": 1043,
    "Overworld Enemy in G31 #2 slain": 1044,
    "Overworld Enemy in G31 #3 slain": 1045,
    "Overworld Enemy in H21 #0 slain": 1046,
    "Overworld Enemy in H21 #1 slain": 1047,
    "Overworld Enemy in H21 #2 slain": 1048,
    "Overworld Enemy in H21 #3 slain": 1049,
    "Overworld Enemy in H21 #4 slain": 1050,
    "Overworld Enemy in H25 #0 slain": 1051,
    "Overworld Enemy in H25 #1 slain": 1052,
    "Overworld Enemy in H25 #2 slain": 1053,
    "Overworld Enemy in H26 #0 slain": 1054,
    "Overworld Enemy in H26 #1 slain": 1055,
    "Overworld Enemy in H26 #2 slain": 1056,
    "Overworld Enemy in H27 #0 slain": 1057,
    "Overworld Enemy in H27 #1 slain": 1058,
    "Overworld Enemy in H27 #2 slain": 1059,
    "Overworld Enemy in H28 #0 slain": 1060,
    "Overworld Enemy in H28 #1 slain": 1061,
    "Overworld Enemy in H28 #2 slain": 1062,
    "Overworld Enemy in I21 #0 slain": 1063,
    "Overworld Enemy in I22 #0 slain": 1064,
    "Overworld Enemy in I22 #1 slain": 1065,
    "Overworld Enemy in I22 #2 slain": 1066,
    "Overworld Enemy in I22 #3 slain": 1067,
    "Overworld Enemy in I22 #4 slain": 1068,
    "Overworld Enemy in I23 #0 slain": 1069,
    "Overworld Enemy in I23 #1 slain": 1070,
    "Overworld Enemy in I23 #2 slain": 1071,
    "Overworld Enemy in I24 #0 slain": 1072,
    "Overworld Enemy in I24 #1 slain": 1073,
    "Overworld Enemy in I24 #2 slain": 1074,
    "Overworld Enemy in I24 #3 slain": 1075,
    "Overworld Enemy in I24 #4 slain": 1076,
    "Overworld Enemy in I25 #0 slain": 1077,
    "Overworld Enemy in I25 #1 slain": 1078,
    "Overworld Enemy in I25 #2 slain": 1079,
    "Overworld Enemy in I25 #3 slain": 1080,
    "Overworld Enemy in I26 #0 slain": 1081,
    "Overworld Enemy in I26 #1 slain": 1082,
    "Overworld Enemy in I26 #2 slain": 1083,
    "Overworld Enemy in J23 #0 slain": 1084,
    "Overworld Enemy in J23 #1 slain": 1085,
    "Overworld Enemy in J23 #2 slain": 1086,
    "Overworld Enemy in J23 #3 slain": 1087,
    "Overworld Enemy in J25 #0 slain": 1088,
    "Overworld Enemy in J25 #1 slain": 1089,
    "Overworld Enemy in J26 #0 slain": 1090,
    "Overworld Enemy in J26 #1 slain": 1091,
    "Overworld Enemy in S101A #0 slain": 1092,

    "Shrine of Earth Enemy in S103 #0 slain": 2001,
    "Shrine of Earth Enemy in S103 #1 slain": 2002,
    "Shrine of Earth Enemy in S104 #0 slain": 2003,
    "Shrine of Earth Enemy in S104 #1 slain": 2004,
    "Shrine of Earth Enemy in S105 #0 slain": 2005,
    "Shrine of Earth Enemy in S105 #1 slain": 2006,
    "Shrine of Earth Enemy in S105 #2 slain": 2007,
    "Shrine of Earth Enemy in S106 #0 slain": 2008,
    "Shrine of Earth Enemy in S106 #1 slain": 2009,
    "Shrine of Earth Enemy in S110 #0 slain": 2010,
    "Shrine of Earth Enemy in S110 #1 slain": 2011,
    "Shrine of Earth Enemy in S110 #2 slain": 2012,
    "Shrine of Earth Enemy in S110 #3 slain": 2013,
    "Shrine of Earth Enemy in S111 #0 slain": 2014,
    "Shrine of Earth Enemy in S115 #0 slain": 2015,
    "Shrine of Earth Enemy in S115 #1 slain": 2016,
    "Shrine of Earth Enemy in S116 #1 slain": 2017,
    "Shrine of Earth Enemy in S116 #2 slain": 2018,
    "Shrine of Earth Enemy in S116 #3 slain": 2019,

    "Shrine of Earth Enemy in S107 #0 slain": 2020,
    "Shrine of Earth Enemy in S112 #0 slain": 2021,
    "Shrine of Earth Enemy in S120 #0 slain": 2022,
    "Shrine of Earth Enemy in S121 #0 slain": 2023,
}

class ZagdxLocation(Location):
    game = "Zelda's Adventure GDX"

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
            "Overworld D24 Boomerang",
            "Overworld E20 Full Pitcher",
            "Overworld F28 Ladder",
            "Overworld H23 Wand",
            "Overworld J22 Firestorm",
            "Overworld J24 Empty Pitcher",
            "Overworld J24 Vial of Wind",
            "Overworld J22a Dagger",
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
        overworld_region_1_enemysanity_locations = get_location_names_with_ids(
            [
                "Overworld Enemy in D24 #1 slain",
                "Overworld Enemy in E21 #0 slain",
                "Overworld Enemy in E21 #1 slain",
                "Overworld Enemy in E22 #0 slain",
                "Overworld Enemy in E22 #1 slain",
                "Overworld Enemy in E22 #2 slain",
                "Overworld Enemy in E22 #3 slain",
                "Overworld Enemy in E23 #0 slain",
                "Overworld Enemy in E23 #1 slain",
                "Overworld Enemy in E23 #2 slain",
                "Overworld Enemy in E24 #0 slain",
                "Overworld Enemy in E24 #1 slain",
                "Overworld Enemy in F21 #0 slain",
                "Overworld Enemy in F21 #1 slain",
                "Overworld Enemy in F21 #2 slain",
                "Overworld Enemy in F21 #3 slain",
                "Overworld Enemy in F21 #4 slain",
                "Overworld Enemy in F25 #0 slain",
                "Overworld Enemy in F25 #1 slain",
                "Overworld Enemy in F25 #2 slain",
                "Overworld Enemy in F27 #0 slain",
                "Overworld Enemy in F27 #1 slain",
                "Overworld Enemy in F27 #2 slain",
                "Overworld Enemy in G21 #0 slain",
                "Overworld Enemy in G21 #1 slain",
                "Overworld Enemy in G21 #2 slain",
                "Overworld Enemy in G25 #0 slain",
                "Overworld Enemy in G25 #1 slain",
                "Overworld Enemy in G25 #2 slain",
                "Overworld Enemy in G26 #0 slain",
                "Overworld Enemy in G26 #1 slain",
                "Overworld Enemy in G26 #2 slain",
                "Overworld Enemy in G27 #0 slain",
                "Overworld Enemy in G27 #1 slain",
                "Overworld Enemy in G28 #0 slain",
                "Overworld Enemy in G28 #1 slain",
                "Overworld Enemy in G29 #0 slain",
                "Overworld Enemy in G29 #1 slain",
                "Overworld Enemy in G30 #0 slain",
                "Overworld Enemy in G30 #1 slain",
                "Overworld Enemy in G30 #2 slain",
                "Overworld Enemy in G31 #0 slain",
                "Overworld Enemy in G31 #1 slain",
                "Overworld Enemy in G31 #2 slain",
                "Overworld Enemy in G31 #3 slain",
                "Overworld Enemy in H21 #0 slain",
                "Overworld Enemy in H21 #1 slain",
                "Overworld Enemy in H21 #2 slain",
                "Overworld Enemy in H21 #3 slain",
                "Overworld Enemy in H21 #4 slain",
                "Overworld Enemy in H25 #0 slain",
                "Overworld Enemy in H25 #1 slain",
                "Overworld Enemy in H25 #2 slain",
                "Overworld Enemy in H26 #0 slain",
                "Overworld Enemy in H26 #1 slain",
                "Overworld Enemy in H26 #2 slain",
                "Overworld Enemy in H27 #0 slain",
                "Overworld Enemy in H27 #1 slain",
                "Overworld Enemy in H27 #2 slain",
                "Overworld Enemy in H28 #0 slain",
                "Overworld Enemy in H28 #1 slain",
                "Overworld Enemy in H28 #2 slain",
                "Overworld Enemy in I21 #0 slain",
                "Overworld Enemy in I22 #0 slain",
                "Overworld Enemy in I22 #1 slain",
                "Overworld Enemy in I22 #2 slain",
                "Overworld Enemy in I22 #3 slain",
                "Overworld Enemy in I22 #4 slain",
                "Overworld Enemy in I23 #0 slain",
                "Overworld Enemy in I23 #1 slain",
                "Overworld Enemy in I23 #2 slain",
                "Overworld Enemy in I24 #0 slain",
                "Overworld Enemy in I24 #1 slain",
                "Overworld Enemy in I24 #2 slain",
                "Overworld Enemy in I24 #3 slain",
                "Overworld Enemy in I24 #4 slain",
                "Overworld Enemy in I25 #0 slain",
                "Overworld Enemy in I25 #1 slain",
                "Overworld Enemy in I25 #2 slain",
                "Overworld Enemy in I25 #3 slain",
                "Overworld Enemy in I26 #0 slain",
                "Overworld Enemy in I26 #1 slain",
                "Overworld Enemy in I26 #2 slain",
                "Overworld Enemy in J23 #0 slain",
                "Overworld Enemy in J23 #1 slain",
                "Overworld Enemy in J23 #2 slain",
                "Overworld Enemy in J23 #3 slain",
                "Overworld Enemy in J25 #0 slain",
                "Overworld Enemy in J25 #1 slain",
                "Overworld Enemy in J26 #0 slain",
                "Overworld Enemy in J26 #1 slain",
                "Overworld Enemy in S101A #0 slain",
            ]
        )

        overworld_region_1.add_locations(overworld_region_1_enemysanity_locations, ZagdxLocation)

        shrine_of_earth_enemysanity_locations = get_location_names_with_ids(
            [
                "Shrine of Earth Enemy in S103 #0 slain",
                "Shrine of Earth Enemy in S103 #1 slain",
                "Shrine of Earth Enemy in S104 #0 slain",
                "Shrine of Earth Enemy in S104 #1 slain",
                "Shrine of Earth Enemy in S105 #0 slain",
                "Shrine of Earth Enemy in S105 #1 slain",
                "Shrine of Earth Enemy in S105 #2 slain",
                "Shrine of Earth Enemy in S106 #0 slain",
                "Shrine of Earth Enemy in S106 #1 slain",
                "Shrine of Earth Enemy in S110 #0 slain",
                "Shrine of Earth Enemy in S110 #1 slain",
                "Shrine of Earth Enemy in S110 #2 slain",
                "Shrine of Earth Enemy in S110 #3 slain",
                "Shrine of Earth Enemy in S111 #0 slain",
                "Shrine of Earth Enemy in S115 #0 slain",
                "Shrine of Earth Enemy in S115 #1 slain",
                "Shrine of Earth Enemy in S116 #1 slain",
                "Shrine of Earth Enemy in S116 #2 slain",
                "Shrine of Earth Enemy in S116 #3 slain",
                "Shrine of Earth Enemy in S107 #0 slain",
                "Shrine of Earth Enemy in S112 #0 slain",
                "Shrine of Earth Enemy in S120 #0 slain",
                "Shrine of Earth Enemy in S121 #0 slain",
            ]
        )

        shrine_of_earth.add_locations(shrine_of_earth_enemysanity_locations, ZagdxLocation)

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
