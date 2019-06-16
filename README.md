# IRT for Blender 2.8
## The What and Why
IRT is a blender addon made with the idea of speeding up commonly used tools or tasks when modeling and prototyping for a game engine.


## Features
- Render
  - Intended to be used with Eevee to save a quick "thumbnail" like render from eevee in your home directory
- Hide non-essentials
  - Hides the camera and light gizmos
- Export
  - Export
    - Exports your selection to .fbx and moves it beforehand to 0,0,0 and back to make sure your pivot is where it has to be
  - Export with offset
    - Exports your selection to .fbx without moving i.e. it will have an offset if your object is not centered ( 0, 0, 0 )

## Instalation

Download the init python file and rename it to irt.py ( to be fixed soon )

## Future features
- Defineable names for exported objects, possibly format selection
- Name iteration, currently writes over your rendered thumbnail
- Thumbnail save location options
- Automatic ID map generation