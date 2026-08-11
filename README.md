# Automated Farnsworth Fusor
## Overview
This repository contains the design (in progress) of a Farnsworth Fusor control system and power supply design supporting automatic control of operations from startup to neutron production to shutdown. 

## Power Supply Design 1

<PS1>
## Control System Architecture
A Supervisory Control and Data Acquisition (SCADA) System written in Python allows the user to monitor the fusor and activate emergency shutdown procedures. A manual control panel is included for controller tuning purposes. 
 <scada1> <scada2> <scada3>
The SCADA implements a Finite State Machine (FSM) which iterates through the startup and shutdown process, defining setpoints for the two downstream control loops.

### Controller 1
Controller 1 regulates fusor pressure when the power supply is de-energized. 

<controller1> <legend>
### Controller 2
Controller 2 regulates fusor pressure, current and voltage while the power supply is energized. Each IPOS module will consist of a buck converter feeding an LLC resonator driven at its series resonant frequency. There are 6 control loops with varying bandwidths:
- 10kHz BW Current Loop: regulates buck converter inductor current, to ensure adequate phase and gain margin of the individual bucks. 
- 1kHz BW PLL: ensures the 6 IPOS modules are 60 degrees out of phase with each other, minimizing output ripple.
- 100Hz BW Voltage Loop: regulates aggregate output voltage of all IPOS modules according to a setpoint determined by the 10Hz current loop.
- 10Hz BW Current Loop: configures the IPOS power supply as a current source for the fusor. A feedforward path whose transfer function T(s) is the IV curve of a plasma predicts the power supply output voltage that will result in the intended current. A PI loop minimizes remaining error.
- 0.1Hz BW Pressure Loop: regulates pressure in the fusor chamber to match the setpoint determined by the 0.01Hz BW Voltage Loop. 
- 0.01Hz BW Voltage Loop: uses pressure to regulate the voltage over a long time-horizon. 
## Power Supply Design 2





Several updates must be made to this diagram. The current design focus is on the power supply, where much of the architecture has changed. Once the power supply is complete, the FSM can be updated relatively easily in the Python software.

<img src="images/FusorTasks_TopDown - Software.png" width="500" />
