# Automated Farnsworth Fusor
## Overview
This repository contains the design (in progress) of a Farnsworth Fusor control system and power supply design supporting automatic control of operations from startup to neutron production to shutdown. 

## Power Supply Design 1

## Control System Architecture
A Supervisory Control and Data Acquisition (SCADA) System written in Python allows the user to monitor the fusor and activate emergency shutdown procedures. A manual control panel is included for controller tuning purposes. 

The SCADA implements a Finite State Machine (FSM) which iterates through the startup and shutdown process, defining setpoints for the two downstream control loops.

### Controller 1
Controller 1 regulates fusor pressure when the power supply is de-energized. 

### Controller 2
Controller 2 regulates fusor pressure, current and voltage while the power supply is energized. An inner current loop is included for each LLC module

Controller 2

## Power Supply Design 2





Several updates must be made to this diagram. The current design focus is on the power supply, where much of the architecture has changed. Once the power supply is complete, the FSM can be updated relatively easily in the Python software.

<img src="images/FusorTasks_TopDown - Software.png" width="500" />
