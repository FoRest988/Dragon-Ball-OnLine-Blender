#  DrangonBall OnLine Blender

DrangonBall OnLine Blender is a Blender Addon for import and export of DBO files. 


## Supported Features

The following is a list of supported features by the addon

#### File Types

- [X] Model files
- [ ] Texture Files
- [X] Collision files (including the ones packed in dff)
  - [X] Import
  - [X] Export *(Partial)*
  - [X] Import *(Partial, experimental)*
  - [ ] Export
- [ ] Animation files

#### Model Features

- [X] Skinned mesh support
- [X] Multiple UV Maps
- [X] Mass export
- [X] Material Effects
  - [X] Environment/Normal Maps
  - [X] UV Animation
- [X] Rockstar Specular and Reflection Extensions

## Installation

1. Get a release from the bleeding-edge script by cloning the repository
2. Import the downloaded .zip file by selecting it from *(User) Preferences/Addons/Install from File*
3. Set the addon "Dragon Ball OnLine Blender" to enabled
4. Import dff from Import tab from the panel in *Scene Settings*

## Python Module

The python scripts have been designed with reusability in mind. As of now, the dff module is standalone, and can be used with any other Python instance without the need for Blender API.

#### Dragon Ball OnLine Modules

* [X] - DFF - `dff.py`

