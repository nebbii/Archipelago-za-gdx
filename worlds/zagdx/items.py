from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ZagdxWorld

ITEM_NAME_TO_ID = {
    "Blue Ruby": 1,
    "Boomerang": 2,
    "Celestial Sign 1": 3,
    "Compass 1": 4,
    "Dagger": 5,
    "Empty Pitcher": 6,
    "Firestorm": 7,
    "Full Pitcher": 8,
    "Jade Ring": 9,
    "Ladder": 10,
    "Red Boots": 11,
    "Underworld Map 1": 12,
    "Vial of Wind": 13,
    "Wand": 14,
    "Yellow Ruby": 15,
}

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
