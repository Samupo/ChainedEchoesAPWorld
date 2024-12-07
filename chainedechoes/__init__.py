from worlds.AutoWorld import World
from .Regions import create_regions
from .Locations import create_locations, location_table
from .Items import create_items, item_table

class ChainedEchoesWorld(World):
    """
    Chained Echoes world integration for Archipelago.
    Regions and locations are created in `create_regions` (including a call to `create_locations`).
    Items are created in `create_items`.
    """
    game = "Chained Echoes"
    location_name_to_id = location_table
    item_name_to_id = item_table
    topology_present = True
    
    def create_regions(self):
        """
        Creates regions and locations for the world.
        `create_regions` internally calls `create_locations`.
        """
        create_regions(self)
        create_locations(self)

    def create_items(self):
        """
        Populates the item pool with items for the world.
        """
        create_items(self)