# LWM-Warehouse-Scene
This Sample was developed during the Learn With Me livestream Series.

Learn With Me streams every Monday and Wednesday at 1pm EST on the NVIDIA Omniverse Twitch and YouTube channels

https://www.youtube.com/@NVIDIAOmniverse/streams

Playlist of the previously recorded streams:

https://youtube.com/playlist?list=PLPR2h_elPvVKH9HLtdgfXNUxGeN6QAlc7


This USD works in Omniverse USD Composer (fka Create) and Isaac Sim 2022.2.0 and later versions.

Check out the Tests folder for simple test scenes.

Contributors/Inspired Authors:

Alberto Arenas / Omniverse Ambassador- Camera Constraint ActionGraph

Mathew Schwartz / NJIT - Behavior Scripts for Detecting Collision

Eric Craft / Mead & Hunt - Collision Detection OmniGraph


____________________________________________
Notes:

For the full sample scene to work, please download all of the .usd files in that folder as the main scene, Warehouse_Detect_Coll_OG, uses payloads of the graphs. If the graphs are not working, please ensure they are connected to the payload. 

You must have Physx Graph enabled from the Extension Manager in order for the Counter graph to work.

If you add more packages to the scene, a Rigidbody with Colliders preset must be added, if not already on the package, then remove the Colliders from the Decal Mesh and the Scotch Mesh. 


Questions? Join me on Discord at discord.gg/nvidiaomniverse or email me at agoldstein@nvidia.com