# Cat Quest Multiworld Setup Guide

## Required Software

- Cat Quest from: [Steam](https://store.steampowered.com/app/593280/Cat_Quest/)
    - Games from other storefronts may work, but only if it's the 32 bit version. (EGS, Amazon and GOG are confirmed to be the 64 bit version unfortunately)
    - Only the english version of the game works
    - Cat Quest has been reported as working on Windows, Linux and Steam Deck *(when played in Desktop Mode)*
- BepInEx from: [GitHub](https://github.com/BepInEx/BepInEx/releases)
- Cat Quest Randomizer from: [GitHub](https://github.com/Nikkilites/CatQuest-Randomizer/releases)
- Cat Quest World from: [GitHub](https://github.com/Nikkilites/Archipelago-CatQuest/releases)
- (Optional) Cat Quest PopTracker from: [GitHub](https://github.com/Apheayenne/Cat_Quest_Poptracker/releases)

## Installation

1. Download and install BepInEx 5 (x86, version 5.4.20 or newer) into your Cat Quest root folder. (Don't use the pre-release of 6) (Installation guide for BepInEx can be found [here](https://docs.bepinex.dev/articles/user_guide/installation/index.html))

3. Start Cat Quest once, so that BepInEx can create its required configuration files.

4. After BepInEx has been installed and configured, download the Cat Quest Randomizer zip file, move it to the Cat Quest root folder alongside Cat Quest.exe, right click and select "Extract Here" or the equivalent for your extraction software.
   After this, you can delete the .zip file

## Connecting

When you open your game, you should see the archipawlago menu screen and the randomizer version.

Depending on how much you've played the game beforehand, the menu may look different.

- If you have the 'New Game +' button, click it, and you should have a button called Start New Archipelago Game. Type in your room info and click confirm to start the game
- If you have save data already (the continue button is lit up), then simply click 'New Game' and do as above.
- if you do not have save data, click 'New Game', play the game until it saves for the first time, return to the menu and click 'New Game' again. Do as above.

You can continue your saved game by clicking Continue like in vanilla Cat Quest. This will automatically connect you to the slot you last played on.

## Known Bugs
- It is possible to land in water by landing on specific pieces of land or the edge of the water, when you have only received the Royal Art of Flight.
- Going back and forth between the in game menu and AP gameplay, without closing the game down entirely inbetween, can create an issue where multiple sessions are running at once. If you close down the game inbetween sessions it shouldn't happen, but if it has happened to you, it's possible that some items have been either duplicated or lost, including spells and the ability to walk on water or fly.
    - If this has already happened to you, and you are missing an important item, you can get it by doing the following:
        - check the on-site tracker to see the `Last Order Received` of the item that is missing.
        - Go to `...Cat Quest\ArchipelagoRandomizer\SaveData\ItemIndex.json` and change the number within it to the items `Last Order Received`, but subtract one.
        - Reopen the game, connect to the slot, and the item you were missing should be given to you.

## Troubleshooting Checklist!

Go through this checklist if you __do not__ see the archipawlago menu screen when you open the game
- Make sure you have a 32-bit version of Cat Quest
- Make sure installed the correct version of BepInEx (x86, version 5.4.20 or newer. not x64 and not version 6.0.0+. Also make sure you installed the version that matches your OS)
- Make sure the contents of the mod zip file are put directly in the root cat quest folder, not wrapped in a folder by the name of the downloaded Zip file.
- Make sure your game is in English.

Go through this checklist if you __do__ see the archipawlago menu screen and are unable to log in
- Make sure your login info is case sensitive and otherwise correct
- Make sure the server and room is open and available
- Verify that c-wspp.dll is in your mod installation located here `...Cat Quest\BepInEx\plugins\c-wspp.dll`.
    - If this is not there, your antivirus may have deleted it when you installed the mod. Make sure it is kept in the folder, then try to log in again!
- Verify that you can connect to the server and slot through the standard AP Text client. If this also fails, this is highly likely a form of network or server issue, and not related to Cat Quest
- If you are returning to an AP slot you have previously played, but are now unable to connect to using the "continue" button, check whether your port number/server address has changed.
    - If it has, find the RoomInfo.json file located here: `...Cat Quest\ArchipelagoRandomizer\SaveData\RoomInfo.json`, and change it to the correct login info. After this you can reopen the game and try to click continue again

Still having issues? Ask away!
