# The RobotriX

[c0]: https://placehold.it/15/000000/000000?text=+
[c1]: https://placehold.it/15/0000ff/000000?text=+
[c2]: https://placehold.it/15/00ff00/000000?text=+
[c3]: https://placehold.it/15/00ffff/000000?text=+
[c4]: https://placehold.it/15/ff0000/000000?text=+
[c5]: https://placehold.it/15/ff00ff/000000?text=+
[c6]: https://placehold.it/15/ffff00/000000?text=+
[c7]: https://placehold.it/15/ffffff/000000?text=+
[c8]: https://placehold.it/15/000080/000000?text=+
[c9]: https://placehold.it/15/008000/000000?text=+
[c10]: https://placehold.it/15/008080/000000?text=+
[c11]: https://placehold.it/15/800000/000000?text=+
[c12]: https://placehold.it/15/800080/000000?text=+

[c13]: https://placehold.it/15/808000/000000?text=+
[c14]: https://placehold.it/15/808080/000000?text=+
[c15]: https://placehold.it/15/ff6000/000000?text=+
[c16]: https://placehold.it/15/ffd7b4/000000?text=+
[c17]: https://placehold.it/15/aa6e28/000000?text=+
[c18]: https://placehold.it/15/e6beff/000000?text=+
[c19]: https://placehold.it/15/d2f53c/000000?text=+
[c20]: https://placehold.it/15/aaffc3/000000?text=+
[c21]: https://placehold.it/15/e6194b/000000?text=+
[c22]: https://placehold.it/15/fffac8/000000?text=+
[c23]: https://placehold.it/15/0082c8/000000?text=+
[c24]: https://placehold.it/15/3cb94b/000000?text=+
[c25]: https://placehold.it/15/f58230/000000?text=+

[c26]: https://placehold.it/15/cdcd00/000000?text=+
[c27]: https://placehold.it/15/ffc125/000000?text=+

[c28]: https://placehold.it/15/ff6000/000000?text=+

[c29]: https://placehold.it/15/717162/000000?text=+
[c30]: https://placehold.it/15/cae1ff/000000?text=+
[c31]: https://placehold.it/15/5f9ea0/000000?text=+
[c32]: https://placehold.it/15/00fa9a/000000?text=+
[c33]: https://placehold.it/15/cdba96/000000?text=+
[c34]: https://placehold.it/15/8b4500/000000?text=+
[c35]: https://placehold.it/15/ff4500/000000?text=+
[c36]: https://placehold.it/15/8e388e/000000?text=+
[c37]: https://placehold.it/15/c67185/000000?text=+
[c38]: https://placehold.it/15/c5c1aa/000000?text=+

[seq0]: ./img/seq0.jpg
[seq0_depth]: ./img/seq0_depth.jpg
[seq0_mask]: ./img/seq0_mask.jpg
[seq1]: ./img/seq1.jpg
[seq1_depth]: ./img/seq1_depth.jpg
[seq1_mask]: ./img/seq1_mask.jpg
[seq2]: ./img/seq2.jpg
[seq2_depth]: ./img/seq2_depth.jpg
[seq2_mask]: ./img/seq2_mask.jpg



Enter the RobotriX, an extremely photorealistic indoor dataset designed to enable the application of deep learning techniques to a wide variety of robotic vision problems. The RobotriX consists of hyperrealistic indoor scenes which are explored by robot agents which also interact with objects in a visually realistic manner in that simulated world. Photorealistic scenes and robots are rendered by Unreal Engine into a virtual reality headset which captures gaze so that a human operator can move the robot and use controllers for the robotic hands; scene information is dumped on a per-frame basis so that it can be reproduced offline using UnrealCV to generate raw data and ground truth labels. By taking this approach we were able to generate a dataset of 38 semantic classes across 512 sequences totaling 8M stills recorded at +60 frames per second with full HD resolution. For each frame, RGB-D and 3D information is provided with full annotations in both spaces. Thanks to the high quality and quantity of both raw information and annotations, the RobotriX will serve as a new milestone for investigating 2D and 3D robotic vision tasks with large-scale data-driven techniques.

![seq0]
![seq0_depth]
![seq0_mask]
![seq1]
![seq1_depth]
![seq1_mask]
![seq2]
![seq2_depth]
![seq2_mask]

## Contents

1. [Data](#data)
    1. Raw Data
    2. Ground Truth
2. [Tools](#tools)
    1. Server
    2. Scene Parser
    3. Instance Mapper
    4. Client
    5. Generator
    6. Utils
3. [Assets](#assets)
4. [Troubleshooting](#troubleshooting)
5. [License](#license)
6. [Contact](#contact)

## Data

We generated a dataset of 512 sequences recorded on 16 different indoor layouts at +60 FPS with a duration that spans between one and five minutes each. That adds up to a total of approximately eight million individual frames. This initial release of the dataset contains 32 detection and 39 semantic classes. The categories were selected from the most common and useful household goods in indoor environments for social robots. 

| Type | 00 <br> ![c0] | 01 <br> ![c1] | 02 <br> ![c2] | 03 <br> ![c3] | 04 <br> ![c4] | 05 <br> ![c5] | 06 <br> ![c6] | 07 <br> ![c7] | 08 <br> ![c8] | 09 <br> ![c9] | 10 <br> ![c10]  | 11 <br> ![c11]  | 12 <br> ![c12]  |
| - | - | - | - | - | - | - | - | - | - | - | -  | -  | -  |
| Semantic  | void  | wall  | floor | ceiling | window  | door  | table | chair | lamp  | sofa  | cupboard | screen | hand |
| Detection | -     | -     | -     | -       | -       | -     | table | chair | lamp  | sofa  | cupboard | screen | hand |

| Type | 13 <br> ![c13] | 14 <br> ![c14] | 15 <br> ![c15] | 16 <br> ![c16] | 17 <br> ![c17] | 18 <br> ![c18] | 19 <br> ![c19] | 20 <br> ![c20] | 21 <br> ![c21] | 22 <br> ![c22] | 23 <br> ![c23] | 24 <br> ![c24] | 25 <br> ![c25]  |
| - | - | - | - | - | - | - | - | - | - | - | -  | -  | -  |
| Semantic  | frame  | bed   | fridge | whiteboard | book | bottle | plant | furniture | toilet | phone | bathtub | cup | mat |
| Detection | frame  | bed   | fridge | whiteboard | book | bottle | plant | - | lamp  | toilet | phone | bathtub | cup | mat |

| Type | 26 <br> ![c26] | 27 <br> ![c27] | 28 <br> ![c28] | 29 <br> ![c29] | 30 <br> ![c30] | 31 <br> ![c31] | 32 <br> ![c32] | 33 <br> ![c33] | 34 <br> ![c34] | 35 <br> ![c35] | 36 <br> ![c36] | 37 <br> ![c37] | 38 <br> ![c38]  |
| - | - | - | - | - | - | - | - | - | - | - | -  | -  | -  |
| Semantic  | mirror | sink  | box | mouse | keyboard | bin | cushion | shelf | bag | curtain | kitchen_stuff | bath_stuff | prop |
| Detection | mirror | sink  | box | mouse | keyboard | bin | cushion | shelf | bag | - | kitchen_stuff | bath_stuff | prop |

### Raw Data

For each frame, we provide the following data:

* 3D poses for the cameras, objects, and robot joints.
* RGB image at 1920x1080 resolution in 24-bit PNG format.
* Depth map at 1920x1080 resolution in 16-bit grayscale PNG format.
* 2D instance mask at 1920x1080 resolution in RGB 24-bit PNG format.

Public download links to be released.

### Ground Truth

For each frame, we provide the tools to generate the following annotations:

* 2D class mask at 1920x1080 resolution in RGB 24-bit PNG format.
* 2D/3D object instance bounding boxes in XML format.
* 3D point cloud in PLY format with RGB color.
* 3D instance/class mask in PLY format with RGB color.

Due to the excessive size of that large-scale ground truth, we provide the needed tools and instructions so that anyone can generate the annotations they need locally using the aforementioned raw data. Nevertheless, we provide an annotated subset for visualization and demo purposes. Public download links to be released.

## Tools

In this repository, we release all the tools that were used to record and generate our data and ground truth. The reason is twofold: (1) by using the tools anyone can easily reproduce our dataset and (2) anyone can modify or extend our data or generate new datasets for specific problems.

The codebase is divided into different parts:
* data
* server
* scene parser
* instance mapper
* client
* generator
* utils

### Server

The server side contains the code to track all objects, cameras, and bones in an Unreal Engine scene and dump their identifiers, positions, rotations, and bounding boxes. This code implements an Actor in Unreal Engine tack ticks for each rendered frame and gathers all that information by iterating over cameras, actors, and bones.

#### Requirements

* Unreal Engine 4.18
* Visual Studio 2017 with developer tools (for compiling the project).

#### Before Executing

To make the tracker work, we first need to create a new C/C++ class (Actor) in the project content browser. Make sure to name it Tracker and then open the Visual Studio project to copy the content of `./server/Tracker.h` and `./server/Tracker.cpp` into the corresponding project files.

The `.cpp` can be copied directly but for the header file one must take into account that the class name depends on the project name so special attention is required to copy it. For instance, the following code fragment shows the initial part of the `Tracker.h` file for an UE4 project named HamburgHaus (notice the `class HAMBURGHAUS_API` line):

```
#include "Tracker.generated.h"

UCLASS()
class HAMBURGHAUS_API ATracker : public AActor
{
        GENERATED_BODY()
```

That `HAMBURGHAUS_API` prefix must be changed accordingly to the project name, e.g., for a project named InteractiveHouse it would be `INTERACTIVEHOUSE_API`.

After copying the source files, we can modify two important variables in `Tracker.h`, namely `m_save_directory` and `m_file_name`. Those two will control the path to which the tracker will dump the file with the specified name respectively.

Once all the changes are done, just build the scene project either using Visual Studio 2017 or Unreal Engine's button. Once the project has been successfully compiled, drag and drop the newly created actor to the scene.

In addition, in order to be able to make the actor start/stop tracking (dumping the information) it is required that the `R` key is mapped to an action event `SwitchRecord` on the project input configuration.

#### Execution

Play the scene in Standalone mode, hit `R` to start recording and hit it again to stop dumping information or close the window.

#### After Executing

The tracker will generate a `.txt` file in the folder specified by the member variable `m_save_directory` in `Tracker.h`. The name of the file is specified by the corresponding variable `m_file_name`. We encourage changing those variables to a proper path and filename and then recompiling the project if the default values are not satisfactory.

That text file has the following format for each frame:

```
frame_0
timestamp frame_id
camera_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll
object_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll bbox_info
bone_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll bbox_info
[...]
frame_n
timestamp frame_id
camera_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll
object_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll bbox_info
bone_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll bbox_info
```

### Scene Parser

The scene parser is a utility to convert the raw text information dumped by the tracker on the server side into a more structured and interpretable JSON file for later reuse with other tools and data sharing. This is a strictly necessary step for using the client and the generator later.

### Requirements

* Python >= 2.7
  * json

#### Before Executing

The scene parser is contained in `./scenetojson.py`. Before execution, two parameters of that file must be taken into account: `FILE_NAME` and `SEQUENCE_NAME`. The first one is the path to the scene text file generated by the server. The second one is the name we would like to give to that sequence. Other important parameters that might be modified are `drop_frames` (which makes our parser keep every `drop_frames` frame and discard the rest) and `skip_n_frames` (that tells the parser to skip the first `n` frames). By default we keep every frame (`drop_frames=1`) and skip the first one (`skip_n_frames=1`).

#### Execution

To execute the parser, just run `scenetojson.py`.

#### After Executing

After execution, a JSON file describing the sequence will be generated in the `./data/` folder as `./data/SEQUENCE_NAME.json`. That file can be later reused by the client and the generator to reproduce the sequence and extract useful information. That JSON file has the following format:

```
{
  "frames": [
    {
      "timestamp": "319.422211", 
      "camera": {
        "position": {
          "y": "0.000", 
          "x": "165.000", 
          "z": "124.009"
        }, 
        "rotation": {
          "y": "179.999756", 
          "p": "0.000000", 
          "r": "0.000000"
        }
      }, 
      "objects": [
        {
          "position": {
            "y": "105.000", 
            "x": "-210.000", 
            "z": "32.000"
          }, 
          "rotation": {
            "y": "-27.499922", 
            "p": "0.000000", 
            "r": "0.000000"
          }, 
          "name": "Chair"
        }, 
[...]
```

### Instance Mapper

### Client

The client side contains the code to reproduce recorded sequences and issue the needed commands using UnrealCV's client to an Unreal Engine server with UnrealCV's plugin to position the camera, the objects, and the robot on each frame and generate raw visual data: RGB, depth map, and instance segmentation mask.

#### Requirements

The following requirements must be met to execute the client:

* Python >= 2.7
  * json
  * numpy
  * matplotlib
  * pillow
* UnrealCV 0.3.10

#### Before Executing

The client takes three JSON files input for configuration: ```client/config.json```, ```client/classes.json```, and ```client/instance_class.json```. Each one of them must be carefully reviewed before executing it.

The first ```config.json``` file specifies various generic configuration options regarding ```unrealengine``` (host IP and port for the Unreal Engine server), the ```scene``` (path to the sequence recording file, usually to be placed inside ```data/```), and the ```camera``` (calibration parameters ```fx```, ```cx```, ```fy```, ```cy```, ```fov```, and min/max distances in meters for depth generation ```depthmin``` and ```depthmax``` respectively). Make sure to provide the appropriate values for each one of them.

The other two configuration files ```classes.json``` and ```instance_class.json``` are less likely to be modified. The first one provides information for each class of the dataset such as its ```name```, the corresponding semantic (```semantic_class```) and detection (```detection_class```) classes, and the associated ```color``` in RGB format. The second one is just a map that associates each instance name for the objects and meshes in UnrealEngine to a corresponding class. These two files can be modified for various purposes: rearranging classes, adding new ones or removing existing ones, changing their colors...

#### Execution

To execute the client, just execute `python client.py` inside the `client/` directory. It requires the Unreal Engine server to be up and running with the scene in ```Play``` mode (we have detected a performance increase if you do not eject from the window when playing). The client will start replaying the sequence file frame by frame and making the appropriate UnrealCV calls to generate data.

#### After Executing

After the client has finished, three folders (```/rgb```, ```/depth```, and ```/mask```) and three JSON files (```camera.json```, ```sequence.json```, and ```objects.json```) will be created in the ```data/sequence_name``` folder where ```sequence_name``` is the name of the sequence specified in the sequence recording JSON file that was used as input for the client.

The ```/rgb``` folder contains the color maps in 24-bit RGB PNG format. The ```/depth``` directory contains the depth maps in 16-bit grayscale PNGs. The ```/mask``` one contains the instance segmentation masks in 24-bit RGB PNG format. The ```sequence.json``` file is a copy of the original sequence recording file for future reference. ```objects.json``` contains information for each object in the sequence (the given instance name by Unreal Engine ```instance_name```, the class information correlated with the ```classes.json``` and ```instance_class.json``` files, and its instance color given by UnrealCV ```instance_color``` in RGB. The ```camera.json``` contains all the camera information from the previous ```config.json```. 

### Generator

The generator contains the code to produce that extra annotations and data using the raw information obtained by the client and UnrealCV. The generator will take a sequence and load the RGB, depth, and instance masks for each frame to produce 2D class segmentation masks, 2D/3D bounding boxes, 3D point clouds, and 3D class and instance segmentation masks. It also needs certain sequence, camera, and object information that is passed by the respective JSON files generated by the client.

#### Requirements

The following requirements must be met to execute the generator:

* Python >= 2.7
  * json
  * numpy
  * matplotlib
  * pillow
  * plyfile

#### Before Executing

The `generator/generator.py` file contains the generator itself. Before executing it, we must specifiy the `SEQUENCE_DIR` and the `FRAME_START` inside it. The first one indicates the name of the sequence created by the client in the `data` folder so the generator will look for all the needed files in `data/SEQUENCE_DIR`. The second parameter tells the generator to skip the first `FRAME_START` frames (this is a mechanism to restart the generation process in case of failure).

There are also some flags that determine which annotations will be generated: `GENERATE_2DCLASSMASK`, `GENERATE_3DINSTANCEMASK`, `GENERATE_3DCLASSMASK`, `GENERATE_2DBBOX`, `GENERATE_3DBBOX`, and `GENERATE_3DPOINTCLOUD`.

#### Execution

To start the generator, just execute `python generator.py` inside the `generator/` folder. The generator will start loading the frames in `data/SEQUENCE_DIR/rgb`, `data/SEQUENCE_DIR/depth`, and `data/SEQUENCE_DIR/mask` to produce the annotations starting from the `FRAME_START` frame.

#### After Executing

Once the generator is done, folders for the annotations (`/2dclassmask`, `/cloud`, `/2dbbox`, ...) will be created in the `data/SEQUENCE_DIR` directory with all the requested data.

The `/2dclassmask` folder contains the class segmentation masks in 24-bit RGB PNG format. The `/2dbbox` and `/3dbbox` contain bounding boxes for detection in XML format. `/cloud` contains 3D point clouds with color in PLY format. `/3dclassmask` and `/3dmask` contain PLY point clouds with RGB color information representing class and instance segmentation.

### Utils

The `utils` folder contains a set of Python classes and methods that encapsulate functionality that is commonly reused by all the previous tools. Some of the utilities are:

* `utils/camera.py` which defines a Camera class that provides functionality for holding camera information (calibration parameters, FoV, and depth range) and JSON load/store.
* `utils/color.py` for handling RGB colors and interpreting regular expressions.
* `utils/objectclass.py` for encapsulating information about an object class for both semantic and detection problems with their corresponding IDs, names, and colors.
* `utils/sceneobject.py` to hold information about an object in the scene (its class, instance, and instance color assigned by UnrealCV).
* `utils/sequence.py` for handling JSON formatted sequences.
* `utils/ucv.py` contains functions that wrap UnrealCV commands to provide high level procedures such as object placement, camera placement, client connection...

## Assets

To be released...

## Troubleshooting

* UnrealCV 0.3.10 segmentation issues with Unreal Engine >4.16.

## License

Both the data and the code for The RobotriX are released under the [MIT license](LICENSE).

## Contact

Please contact Albert Garcia at [agarcia@dtic.ua.es](mailto:agarcia@dtic.ua.es) if you have any questions or requests.
