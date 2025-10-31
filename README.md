
# PTCG-SM-Campaign
### Pokemon Trading Card Game - Sun and Moon - Campaign
#### README is still a WIP


## **Summary**


### What
This project aims to make a video game version of the PTCG (Pokemon Trading Card Game,) not entirely unlike the original PTCGs for the Gameboy Color. The implementation will be flexible and **customizable** (by the user.) The intent is to create a high quality base game **worth playing out-of-the-box,** but with an accessible collection of assets that can be **changed or added with as little overhead and difficulty as reasonably achievable**. 

### Why
The current, official video game implementation of the PTCG (PTCG Live) is cloud-based. At the time of writing this, it **lacks a campaign** and has **little to no support for CPU opponents**. Since it is solely a PvP experience, it is not customizable. The latest mobile game is no exception to this rule, being solely PvP and sporting some rule tweaks to accommodate faster mobile play.

### How
This project is built on Pygame with Python3 and emphasizes object-oriented solutions. Implementation is still flexible and the overall trajectory is developing organically. 


## **Development Trajectory**
The original plan was to create an almost completed backend for gameplay --including deck building, menu navigating, and the actual card mechanics-- before moving onto UI/graphics, which would steadily merge into story/game-design elements. This is still the general idea, however it is subject to change and some basic shell of a UI will likely appear for testing that will either be the backbone for the UI or a stand-in.




## **Dataflow**
#### Using this section to help manage the flow of data during development.

### Maps
An ingest_list json that gets fed into the Tile_Ingester class. This returns the k:v 'tiles' needed to instantiate an Area type, which is basically an in-game map with all of it's inanimate sprites, like floors, walls, tables, etc.. The tiles represent both the structure of the map and the 'objects' on it. The Area converts the tiles to Inanimates and gives them positions. The positions are derived from 'map_data' which gets passed into the Area type. The map_data is just a list of lists, so row/col, that contains strings. The strings will correspond to items defined in the ingest_list, which should define all the tiles available to that map. 

In other words, to create or alter a map, it is as simple as altering that list, making new areas extremely easy to make and change. The Tile_Ingester gets the actual sprites themselves from the path provided. *TODO: Describe how the Tile_Ingester actually knows what to ingest and explain what it expects to run smoothly* 

### Sprites
All characters, including the player, are members of the Entity class. This class inherits from pygame.sprite.Sprite, so it's children will work with the intended pygame objects, but it also takes in a custom Sprite object -- either a VisualSprite, or it's child, an AnimatedSprite -- which is used solely for representing the *physical characteristics* of the sprite *except for collision*. This includes position, the representing visual/image, and the movement animation if appropriate. These sprites all have positions that are tied to their stored rectangles values; the ones that they get upon being assigned a pygame.Surface and/or Image. These sprites are composed inside of Entity types, but the Entity types have their own position information for handling collision. They have both a visual_position and a collision_position which correspond to their sprite's position and their own collision_rect, respectively. The good news is that when setting just 'position' for an Entity subclass, it will update both at the same time; the bad news is the access delegation via getters/setters is a bit confusing, so modifying them can be touchy.

All entities are added to pygame.sprite.Groups upon creation. These groups are currently the soul source of collision management. 

### Collision
Collision is officially supported and I'm hoping the core doesn't need too many more changes as development progresses, though I suspect some new ways to actually detect might be warranted, rather than relying solely on groups and a pygame method which requires the arg being tested to have a rect property. Thanks to the addition of a collision_position to the Entity class, the collision areas can now be freely altered without affecting the visual itself. This can currently be seen in the player's ability to clip over objects that would not be in the way were the space 3D. I believe this is traditionally referred to as a T value?

### Cards
I did some work with the cards when I first started this project, but it has been awhile. When I am able to actually get to a state where a card game might feasibly be started in-game, I'll return to it.



