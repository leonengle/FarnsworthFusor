# Automated Farnsworth Fusor
## Background
A Farnsworth Fusor (fusor for short) is a machine that produces the conditions for nuclear fusion using the method of electrostatic confinement. At its simplest, a neutron-producing fusor consists of a wire grid connected to the hot terminal of a power supply (usually -20kVDC 200W output or greater) and a grounded vacuum chamber. The energized wire grid is mounted in the center of the grounded vacuum chamber, creating a strong electric field between the center of the chamber and its walls. The electric field ionizes an injected deuterium gas and accelerates the ions to a degree where collisions have a chance to result in fusion.

We are developing a fully digitized 120VAC to -33kVDC power converter (400W) and control system software library compatible with a Farnsworth Fusor. While not a feasible method for power generation, building and operating a Farnsworth Fusor provides students with many opportunities for learning the principles of nuclear fusion and related systems. Our verified designs will be released open source, to provide to universities a feasible pathway to teach students the principles of nuclear fusion in an immersive way. 

Our design enables automatic control of the Farnsworth Fusor operating cycle, requiring user input only to initiate startup and shutdown procedures. This feature is not supported by currently published Farnsworth Fusor designs and will enable students to practice implementing control algorithms on a fusion-capable testbench. Learning activities in these areas will prepare students for design work on frontier fusion machines around the world.

## System Block Diagram
<img src="images/FusorTasks_TopDown - System.png" width="1000" />

## Supervisory Controller Logic (Finite State Machine)
<img src="images/FusorTasks_TopDown - Software.png" width="800" />
