# Soultopia Game Design Document

"Soultopia" is a dark fantasy MMORPG set in a world torn by eternal war between four races: Vampires, Werewolves, Elves, and Humans. This document outlines the core design pillars, world building, character concepts, and major gameplay systems for a AAA-quality implementation.
The directory also includes a small Panda3D demo showcasing a simple environment and race selection.

## Core Pillars
- **Dark Fantasy Setting** with rich lore and morally grey conflicts.
- **Soulslike Combat** emphasizing skillful dodging, parrying, and timing.
- **PvP Territory Warfare** where races vie for control of regions to gain buffs.
- **Living World** featuring dynamic day/night cycles and environmental reactions.

## Playable Races
### Vampires
- **Theme:** Predators of the night that drain life from foes.
- **Abilities:** Heal on hit, temporary bat-form dash, sunlight damage debuff, blood magic spells.
- **Customization:** Gothic armor, blood-themed weapons, pale skin tones.
- **Story Hook:** Seeking the origin of the vampire curse and dominance over the other races.

### Werewolves
- **Theme:** Bestial warriors embracing primal fury.
- **Abilities:** Transform into a hulking wolf form at night, increased strength and speed, vulnerable to silver.
- **Customization:** Tribal tattoos, fur patterns, dual-wield claws.
- **Story Hook:** Ancient pact with the moon spirits and internal struggle to control the beast within.

### Elves
- **Theme:** Agile masters of elemental magic and swift movement.
- **Abilities:** Fast sprinting, high jumps, powerful ranged spells, affinity with nature.
- **Customization:** Elegant armor, glowing runes, sleek weapons.
- **Story Hook:** Defending sacred forests from the encroaching darkness and discovering lost magical relics.

### Humans
- **Theme:** Resourceful strategists with advanced technology.
- **Abilities:** Deploy gadgets (turrets, traps), balanced stats, leadership buffs when grouped.
- **Customization:** Diverse armor styles, mechanical weapons, steampunk influences.
- **Story Hook:** Uniting fractured kingdoms to survive in a world of monsters.

## Example Biomes
1. **Enchanted Forests** – Home to the Elves, filled with luminous flora and hidden ruins.
2. **Gothic Castles** – Vampire strongholds with shadowy corridors and grand halls.
3. **Ancient Ruins** – Scattered relics from an extinct civilization, harboring powerful artifacts.
4. **Haunted Villages** – Cursed settlements with restless spirits that attack by night.
5. **Underground Lairs** – Labyrinthine tunnels where Werewolves perform dark rituals.

## Boss Battles
1. **Blood Queen Sarra** – A vampire matriarch wielding blood magic that drains player health and summons swarms of bats. Requires careful dodging and sunlight-based mechanics to defeat.
2. **The Silver Juggernaut** – An armored golem powered by pure silver. Its massive swings and area attacks punish reckless players; Werewolves must rely on allies to avoid massive debuffs.
3. **Elderwood Colossus** – A gigantic tree guardian in the Enchanted Forest. Uses root snares, devastating slams, and summons dryad minions. Players must coordinate to break its armor before it regrows.

## Territory Control System
- Regions across the world can be captured by members of a race.
- Holding a territory grants global buffs such as increased resource gain or improved combat stats.
- Siege events occur on a schedule, leading to large-scale PvP battles.

## Day/Night Cycle
- **Day:** Vampires suffer debuffs and take passive damage in direct sunlight; Werewolf transformations are weaker.
- **Night:** Werewolves gain enhanced strength and speed. Vampires roam freely with bonus life-steal.
- **Dynamic Events:** Certain quests, enemies, and bosses only appear at specific times of day.

## Character Customization
- Detailed appearance editor with race-specific features (fangs, fur, elven ears, etc.).
- Armor and weapon skins tied to achievements and crafting.
- Skill trees offering unique builds and playstyles per race.

## Social Features
- Player trading and auction houses in major cities.
- Guilds with shared territory holdings and progression.
- Leaderboards for PvP rankings and world events.
- Global chat channels, emotes, and seasonal festivals.

## Main Story Arc
The world of Soultopia is threatened by **Malachar, the Voidbringer**, an ancient entity manipulating the four races toward endless war. Players unravel the truth behind their origins, forging uneasy alliances to stop Malachar's return. Dramatic cutscenes depict pivotal moments—betrayals, heroic sacrifices, and the final battle in the shattered realm between worlds.

## Prompts for Asset Creation
- *Landscape Concept Art:* "Dark fantasy panorama of a moonlit battlefield where towering castles loom over haunted woods, detailed and atmospheric, trending on artstation."
- *Character Design:* "AAA game character sheet of a vampiric knight in ornate armor, 4k resolution, dramatic lighting, realistic yet stylized."
- *Boss Creature:* "Colossal tree guardian bursting from an enchanted forest, roots entwined with glowing runes, cinematic scale."
- *Environment Modeling:* "Handcrafted gothic castle interior with sweeping staircases and flickering torches, optimized for real-time rendering."

---
This design document provides a foundation for developing Soultopia into a compelling, competitive MMORPG where every decision shapes the world.

## Demo

Install dependencies using the repository's requirements file:

```zsh
python3 -m pip install -r ../requirements.txt
```

If Panda3D fails to install automatically, run:

```zsh
python3 -m pip install panda3d==1.10.14
```

For a minimal local demonstration using Panda3D, run:

```zsh
python3 main.py <race>
```

Replace `<race>` with one of `vampire`, `werewolf`, `elf`, or `human`. The demo shows a basic environment with a day/night cycle and displays your chosen race.
