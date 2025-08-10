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

# """Chests (Choice)
# Chestsanity: All chests are included and all items that can be found in chests are added to the itempool
# Golden Chests: Only golden chests are included, and items that can be found in these chests are added to the itempool
# No Chests: No chests are included and weapons and armor will not be found in the itempool"""

# """Side Quests (Toggle)
# Yes: All quests are added as locations
# No: Only the main quests are added as locations"""

# """Levelup (Range)
# If 0 is picked, you will be playing with "lvl 1 cat" modifyer, and exp is not available to gain whatsoever
# Range goes between 0 and 100. Default is the level you'd be at had you done all quests in the vanilla game"""

# """Weapons and Armor slots (Choice)
# Yes: Being able to equip weapons and armor is unlocked through archipelago
# No: You can equip any weapons and armor"""

# """Caves (Choice)
# Yes: Completing caves are added as locations
# No: No caves are added as locations"""

# """Exploration (Choice)
# Explorer: All monuments and temples are added as locations
# Temples: Only temples are added as locations
# Monuments: Only monuments are added as locations
# No exploration: No monuments or temples are added as locations"""


@dataclass
class CatQuestOptions(PerGameCommonOptions):
    goal: Goal
    progressive_skills: ProgressiveSkills