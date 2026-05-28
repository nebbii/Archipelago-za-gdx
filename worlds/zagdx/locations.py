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

    overworld_region_1_locations = get_location_names_with_ids(
        [
            "Overworld D24 Goriya Boomerang Drop",
            "Overworld E20 Full Pitcher",
            "Overworld F28 Ladder",
            "Overworld H23 Wand",
            "Overworld J24 Empty Pitcher",
            "Overworld J24 Vial of Wind",
        ]
    )
    overworld_region_1.add_locations(overworld_region_1_locations, ZagdxLocation)

    shrine_of_earth_locations = get_location_names_with_ids(
        [
            "Shrine of Earth S104 1st Underworld Map",
            "Shrine of Earth S105 Compass",
            "Shrine of Earth S108 Jade Ring",
            "Shrine of Earth S116 Red Boots",
            "Shrine of Earth S122 1st Celestial Sign",
        ]
    )
    shrine_of_earth.add_locations(shrine_of_earth_locations, ZagdxLocation)


def create_events(world: ZagdxWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    overworld_region_1 = world.get_region("Overworld Region 1 (Below Andor)")
    overworld_region_2 = world.get_region("Overworld Region 2 (Above Andor)")
    shrine_of_earth = world.get_region("Shrine of Earth")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    shrine_of_earth_chasm = ZagdxLocation(world.player, "Shrine of Earth Chasm Ladder", None, shrine_of_earth)
    shrine_of_earth.locations.append(shrine_of_earth_chasm)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    ladder_placed = items.ZagdxItem("Shrine of Earth Ladder Placed", ItemClassification.progression, None, world.player)
    overworld_region_1.place_locked_item(ladder_placed)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
