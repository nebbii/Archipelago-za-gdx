from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ZagdxWorld

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
ITEM_NAMES = [
    "Blue Ruby",
    "Boomerang",
    "Celestial Sign 1",
    "Compass 1",
    "Dagger",
    "Empty Pitcher",
    "Firestorm",
    "Full Pitcher",
    "Jade Ring",
    "Ladder",
    "Red Boots",
    "Underworld Map 1",
    "Vial of Wind",
    "Wand",
    "Yellow Ruby",
]

def build_item_name_to_id(item_names: list[str]) -> dict[str, int]:
    return {
        item_name: item_id
        for item_id, item_name in enumerate(sorted(item_names))
    }

ITEM_NAME_TO_ID = build_item_name_to_id(ITEM_NAMES)

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Blue Ruby": ItemClassification.filler,
    "Boomerang": ItemClassification.useful,
    "Celestial Sign 1": ItemClassification.progression,
    "Compass 1": ItemClassification.useful,
    "Dagger": ItemClassification.useful,
    "Empty Pitcher": ItemClassification.progression | ItemClassification.filler,
    "Firestorm": ItemClassification.useful,
    "Full Pitcher": ItemClassification.progression | ItemClassification.filler,
    "Jade Ring": ItemClassification.progression,
    "Ladder": ItemClassification.progression,
    "Red Boots": ItemClassification.progression,
    "Underworld Map 1": ItemClassification.useful,
    "Vial of Wind": ItemClassification.progression,
    "Yellow Ruby": ItemClassification.filler,
    "Wand": ItemClassification.progression,
}


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class ZagdxItem(Item):
    game = "Zelda's Adventure GDX"

def get_random_filler_item_name(world: ZagdxWorld) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        return "Blue Ruby"
    return "Yellow Ruby"


def create_item_with_correct_classification(world: ZagdxWorld, name: str) -> ZagdxItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return ZagdxItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: ZagdxWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Boomerang"),
        world.create_item("Compass 1"),
        world.create_item("Dagger"),
        world.create_item("Empty Pitcher"),
        world.create_item("Firestorm"),
        world.create_item("Full Pitcher"),
        world.create_item("Jade Ring"),
        world.create_item("Ladder"),
        world.create_item("Red Boots"),
        world.create_item("Underworld Map 1"),
        world.create_item("Vial of Wind"),
        world.create_item("Wand"),
    ]

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
