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
[video_preview]: ./img/video_demo.png


[![video_preview]](https://www.youtube.com/watch?v=CiRc5tCtCak)


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
2. [UnrealROX](#unrealrox)
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

Due to the huge size of the data (~7 TiB), we are currently distributing part of it via private links to our FTP server to avoid excessive traffic (drop a mail to [agarcia@dtic.ua.es](mailto:agarcia@dtic.ua.es) for them). However, half of the dataset is available through [AcademicTorrents](http://academictorrents.com/). We have created various `.torrent` files that can be obtained by cloning this repo which allow the distributed download of the dataset. We have divided the whole dataset into multiple `.torrent`files as we will describe in the following sections to make it easier to download and fetch whichever information you prefer.

### Cargo Manifest

| Sequence | Scene | Interactable Objects | Cameras | Frames | Torrent |
| - | - | - | - | - | - |
| hamburghaus_000 | HamburgHaus | 5 | 0 | 39.190 | data/000_hamburghaus.torrent |
| hamburghaus_001 | HamburgHaus | 5 | 1 | 35.110 | data/000_hamburghaus.torrent |
| hamburghaus_002 | HamburgHaus | 5 | 1 | 27.770 | data/000_hamburghaus.torrent |
| hamburghaus_003 | HamburgHaus | 5 | 3 | 48.930 | data/000_hamburghaus.torrent |
| hamburghaus_004 | HamburgHaus | 5 | 5 | 53.520 | data/000_hamburghaus.torrent |
| hamburghaus_005 | HamburgHaus | 5 | 2 | 51.345 | data/000_hamburghaus.torrent |
| hamburghaus_006 | HamburgHaus | 5 | 0 | 32.410 | data/000_hamburghaus.torrent |
| hamburghaus_007 | HamburgHaus | 5 | 0 | 30.295 | data/000_hamburghaus.torrent |

TODO

### Sequences

Each sequence is recorded as a TXT file that describes it and allows its offline playback to generate the aforementioned data. As a matter of fact, those TXT files are processed and converted into JSON files for improved readability and to make them easier to parse. Those sequence descriptor files contain all the information needed to generate the images and extract ground truth. They are available for download using the `.torrent` file inside *robotrix/recordings*. We provide one individual `.torrent` file for each pack of sequences on a per-scene basis.

### Raw Data

For each frame, we provide the following data:

* 3D poses for the cameras, objects, and robot joints.
* RGB image at 1920x1080 resolution in 24-bit JPG(95%) format (instead of PNG for reduced size).
* Depth map at 1920x1080 resolution in 16-bit grayscale PNG format.
* 2D instance mask at 1920x1080 resolution in RGB 24-bit PNG format.

### Ground Truth

For each frame, we provide the tools to generate the following annotations:

* 2D class mask at 1920x1080 resolution in RGB 24-bit PNG format.
* 2D/3D object instance bounding boxes in XML format.
* 3D point cloud in PLY format with RGB color.
* 3D instance/class mask in PLY format with RGB color.

Due to the excessive size of that large-scale ground truth, we provide the needed tools and instructions so that anyone can generate the annotations they need locally using the aforementioned raw data.

## UnrealROX

** IMPORTANT **

The data for this paper was generated using a deprecated tool which extended UnrealCV to generate all the data we needed. This tool has been superseded by UnrealROX, a compatible and home-brewed C++ solution for UnrealEngine that allows efficient and flexible data recording in virtual reality and offline generation with annotations. Since this tool is better suited for our purposes (more efficient, flexible, and complete), we have removed all previous references in this repository to old RobotriX tools that we mention in the paper (although they can be obtained through commit history).

UnrealROX is described in detail at the following [arXiv](https://arxiv.org/abs/1810.06936) paper and it is released at the following [GitHub/3dperceptionlab/unrealrox](https://github.com/3dperceptionlab/unrealrox) repository.

** IMPORTANT **

## Assets

Assets for this project are originated from two sources: [UE4Arch](https://ue4arch.com/) and [Unreal Engine Marketplace](https://www.unrealengine.com/marketplace/store) so they can be acquired from there. At this moment, we are still in conversations with both parties to release the modified assets as we used them in our scenes.

## Troubleshooting

For any kind of problems, configurations, or instructions, please read carefully [UnrealROX's documentation](https://unrealrox.readthedocs.io/en/master/).

We encourage any user to submit any issue related to the data itself using GitHub's built-in issue system within this repository. For any other issue related to the data generation process or tool, please submit the adequate issue to [UnrealROX's repository](https://github.com/3dperceptionlab/unrealrox). Improvements and critics are welcome at all fronts!

## License

Both the data for The RobotriX and the code for UnrealROX are released under the [MIT license](LICENSE).

## Contact

Please contact Albert Garcia at [agarcia@dtic.ua.es](mailto:agarcia@dtic.ua.es) if you have any questions or requests.