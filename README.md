# Automated Farnsworth Fusor
## Background
This repository contains the design (in progress) of a Farnsworth Fusor supervisory control and power supply design supporting automatic control of operations from startup to neutron production to shutdown. 

The repository is divided into a directory containing Python code for a Supervisory Control and Data Acquisition (SCADA) and a directory documenting the progress of the power supply. 

## System Block Diagram
This is the original system block diagram made for our Capstone project. Several updates have been made since this was produced, see the sub-directories for more information. 

<img src="images/FusorTasks_TopDown - System.png" width="800" />

## Supervisory Controller Logic (Finite State Machine)
The SCADA contains a supervisory FSM which sequences startup and shutdown actions like opening valves, turning on rotary vane/turbo pumps, and turning on the power supply. This is implemented in Python, and will be coupled with an MPC that calculates voltage and pressure setpoints. These setpoints will then be transmitted to the desired peripherals via and Raspberry Pi. 

Several updates must be made to this diagram. The current design focus is on the power supply, where much of the architecture has changed. Once the power supply is complete, the FSM can be updated relatively easily in the Python software.

<img src="images/FusorTasks_TopDown - Software.png" width="500" />
