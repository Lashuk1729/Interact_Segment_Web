# Interactive Segmentation Tool

We introduce an interactive segmentation technique using a pre-trained semantic segmentation network, without any additional architectural modifications to accurately segment 2D and 3D medical images with help from a medical expert.

The first step in our framework is to obtain an initial segmentation using the pre-trained deep learning network. The user then examines the segmentation and adds scribbles where the desired correction is required. This is then used to refine the weights of the network and the improved segmentation is obtained.
