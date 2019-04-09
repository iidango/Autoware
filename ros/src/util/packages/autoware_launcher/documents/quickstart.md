# Quick Start
1. Put map and rosbag file
```
~/.autoware/data/tf/tf.launch
~/.autoware/data/pointcloud_map/*.pcd
~/.autoware/data/vector_map/*.csv
~/.autoware/log/20150324.bag
```
1. Start the Autoware Launcher<br>
```
$ cd Autoware/ros
$ ./run-experimental
```
![quickstart01](./images/quickstart01.png)
1. Load a profile if needed<br>
Window Menu -> File -> Load Profile
1. Show simulation panel<br>
Window Menu -> View -> Simulation
1. Play rosbag<br>
Swtich on Simulation Mode check box, then, push Play button.
1. Push launch buttons<br>
Map, Vehicle, Sensing, and Visualization
![quickstart02](./images/quickstart02.png)
1. Push Localization button on rviz plugin and check the estimated vehicle pose
![quickstart03](./images/quickstart03.png)
1. Push other buttons on rviz plugin<br>
Detection, Prediction, Decision, Mission, and Motion
![quickstart04](./images/quickstart04.png)
![quickstart05](./images/quickstart05.png)
