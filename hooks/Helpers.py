from typing import Optional, Any
import re
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    if any("17." in s for s in item["category"]):
        from ..Helpers import get_option_value
        if "Twitch Drop" in item["name"]:
            return get_option_value(multiworld, player, "enable_twitch_drops")
        else:
            return get_option_value(multiworld, player, "enable_expedition_rewards")
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    # Remove excess missions and standings from the location pool
    if "mission_count" in location:
        from ..Helpers import get_option_value
        mission_num = location["mission_count"]
        max_missions = int(get_option_value(multiworld, player, "max_missions"))
        mission_step = int(get_option_value(multiworld, player, "mission_steps"))
        return mission_num <= max_missions and (mission_num <= 3 or mission_num % mission_step == 0 or mission_num == max_missions)
    if "standing_count" in location:
        from ..Helpers import get_option_value
        if any("Species" in s for s in location["category"]):
            max_standing = int(get_option_value(multiworld, player, "species_standing_maximum"))
            standing_step = int(get_option_value(multiworld, player, "species_standing_steps"))
        if any("Factions" in s for s in location["category"]):
            standing_step = int(get_option_value(multiworld, player, "faction_standing_steps"))
            if any("Outlaws" in s for s in location["category"]):
                max_standing = int(get_option_value(multiworld, player, "outlaw_standing_maximum"))
            else:
                max_standing = int(get_option_value(multiworld, player, "faction_standing_maximum"))
        standing_num = location["standing_count"]
        return standing_num <= max_standing and (standing_num <= 3 or standing_num % standing_step == 0 or standing_num == max_standing)

    # Remove unwanted milestones from the location pool
    if any("Milestones " in s for s in location["category"]):
        milestone_category_pattern = r"-\s*(.*?)\s*$"
        milestone_name = re.search(milestone_category_pattern, location["category"][0])
        cleaned_milestone_name = re.sub(r"[\s-]+", "_", milestone_name.group(1).strip())
        from ..Helpers import get_option_value
        milestone_max_star = int(get_option_value(multiworld, player, "{}_milestone_max_star".format(cleaned_milestone_name.lower())))
        return int(location["name"].split(" ")[0]) <= milestone_max_star
    
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
