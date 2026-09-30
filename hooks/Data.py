# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table
# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:
    return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_location_file(location_table: list) -> list:
    BASE_LOCATION_ID = 900000
    MAX_RANGE_END = 100

    for count in range(1, MAX_RANGE_END + 1):
        location_table.append({
            "name": f"Complete {count} Mission{'s' if count > 1 else ''} from a Space Station",
            "id": BASE_LOCATION_ID + count,
            "region": "Open Galaxy (Yellow Systems)",
            "category": ["13e. Activities - Missions"],
            "mission_count": count
        })

    # (ID offset, name suffix, category)
    standings = [
        (1000, "Gek", "15a. Standings - Species - Gek"),
        (2000, "Korvax", "15b. Standings - Species - Korvax"),
        (3000, "Vy'keen", "15c. Standings - Species - Vy'keen"),
        (4000, "Explorers Guild", "15d. Standings - Factions - Explorers Guild"),
        (5000, "Merchants Guild", "15e. Standings - Factions - Merchants Guild"),
        (6000, "Mercenaries Guild", "15f. Standings - Factions - Mercenaries Guild"),
        (7000, "Outlaws", "15g. Standings - Factions - Outlaws"),
    ]
    for id_offset, standing_with, category in standings:
        for count in range(1, MAX_RANGE_END + 1):
            location_table.append({
                "name": f"Reach Standing Rating {count} with the {standing_with}",
                "id": BASE_LOCATION_ID + id_offset + count,
                "region": "Open Galaxy (Yellow Systems)",
                "category": [category],
                "standing_count": count
            })
    return location_table

# called after the events.json file has been loaded, before any processing has occurred
# If you need access to the events after processing, you should use the hooks in World.py
def after_load_event_file(event_table: list) -> list:
    return event_table

# called after the regions.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:
    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
    return category_table

# called after the categories.json file has been loaded
def after_load_option_file(option_table: dict) -> dict:
    # option_table["core"] is the dictionary of modification of existing options
    # option_table["user"] is the dictionary of custom options
    return option_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table
