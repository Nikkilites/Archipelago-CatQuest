from dataclasses import dataclass
from Options import Choice, Toggle, PerGameCommonOptions, StartInventoryPool

class Goal(Choice):
    """Choose the end goal.
    Main Quest: Complete the main quest"""
    display_name = "Goal"
    option_main_quest = 0
    default = 0

class ProgressiveSkills(Toggle):
    """When enabled, skills will no longer level up by purchasing them in the Arcane Temples, but instead through progressive Archipelago items."""
    display_name = "Progressive Skills"
    default = True

# """Chests
# Chestsanity: All chests are included and all items that can be found in chests are added to the itempool
# Golden Chests: Only golden chests are included, and items that can be found in these chests are added to the itempool
# No Chests: No chests are included and weapons and armor will not be found in the itempool"""

# """Side Quests
# Yes: All quests are added as locations
# No: Only the main quests are added as locations"""

# """Progressive Levelup
# Yes: EXP will be given to youSkills and all upgrades will appear in the item pool, and you cannot upgrade skills by purchasing them in the Arcane Temples
# No: Skills will appear in the item pool once, and will be purchaseable in the Arcane Temples hereafter"""

# """Weapons and Armor slots
# Yes: Being able to equip weapons and armor is unlocked through archipelago
# No: You can equip any weapons and armor"""

# """Caves
# Yes: Completing caves are added as locations
# No: No caves are added as locations"""

# """Exploration
# Explorer: All monuments and temples are added as locations
# Temples: Only temples are added as locations
# Monuments: Only monuments are added as locations
# No exploration: No monuments or temples are added as locations"""


@dataclass
class CatQuestOptions(PerGameCommonOptions):
    goal: Goal
    progressive_skills: ProgressiveSkills