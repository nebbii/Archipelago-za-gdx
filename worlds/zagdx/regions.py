from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import ZagdxWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: ZagdxWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ZagdxWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.

    overworld_region_1 = Region("Overworld Region 1 (Below Andor)", world.player, world.multiworld)
    overworld_region_2 = Region("Overworld Region 2 (Above Andor)", world.player, world.multiworld)
    shrine_of_earth = Region("Shrine of Earth", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [overworld_region_1, overworld_region_2, shrine_of_earth]

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: ZagdxWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    #overworld = world.get_region("Overworld")
    #top_left_room = world.get_region("Top Left Room")
    #bottom_right_room = world.get_region("Bottom Right Room")
    #right_room = world.get_region("Right Room")
    #final_boss_room = world.get_region("Final Boss Room")

    overworld_region_1 = world.get_region("Overworld Region 1 (Below Andor)")
    overworld_region_2 = world.get_region("Overworld Region 2 (Above Andor)")
    shrine_of_earth = world.get_region("Shrine of Earth")

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    #overworld_to_bottom_right_room = Entrance(world.player, "Overworld to Bottom Right Room", parent=overworld)
    #overworld.exits.append(overworld_to_bottom_right_room)

    overworld_region_1.connect(shrine_of_earth, "Overworld Region 1 to Shrine of Earth", lambda state: state.has("Shrine of Earth Ladder Placed", world.player))
    overworld_region_1.connect(overworld_region_2, "Overworld Region 1 to Overworld Region 2", lambda state: state.has("Red Boots", world.player))

    # You can then connect the Entrance to the target region.
    #overworld_to_bottom_right_room.connect(bottom_right_room)

    # An even easier way is to use the region.connect helper.
    #overworld.connect(right_room, "Overworld to Right Room")
    #right_room.connect(final_boss_room, "Right Room to Final Boss Room")

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    #overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    #if world.options.hammer:
    #    top_middle_room = world.get_region("Top Middle Room")
    #    overworld.connect(top_middle_room, "Overworld to Top Middle Room")
