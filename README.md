
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

### Maps
Using this section to help manage the flow of data during development. Current flow is an ingest_list json that gets fed into the Tile_Ingester class. This returns the k:v 'tiles' needed to instantiate an Area type (which will correspond to different maps.) The tiles represent both the structure of the map and the 'objects' on it.

The tiles made by the Tile_Ingester are then input into the MapRenderer class, alongside the pygame screen and some (currently) hard coded map_data, which will act essentially as a key for pickling the Area tiles (see the definition for the TypeDict AreaProps as well as the current ingest_list.json for more details on why a key is needed).

### Sprites
All characters, including the player, are apart of the Entity class. This class inherits from pygame.sprite.Sprite, so it's children will work with the intended pygame objects, but it also takes in a custom Sprite object, which is used solely for representing the *physical characteristics* of the sprite. This includes position, the representing visual, and the movement animation.

As it stands, all entities as well as InanimateSprites will use pygame.sprite. Groups and will be added to appropriate ones upon creation. I still need to do more research on Groups, though, to see if they can handle what I'm hoping for, so this is very subject to change.



