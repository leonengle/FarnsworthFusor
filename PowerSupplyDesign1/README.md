# Farnsworth Fusor Power Supply

## Overview

Here a design (in progress) is presented for a 400W 120VrmsAC 60Hz -> -33kVDC Power Converter; to power a Farnsworth Fusor. The power converter has four stages: a rectifier, an inverter, a ferrite 1:30 transformer, and an 8x voltage multiplier. 

## Status Update (July 19 2026)

Recently achieved -20kVDC output at open load from 40VAC input (open-loop control), using a VFD borrowed from a professor. Significant corona discharge occured at this voltage, working on re-insulating. Currently redesigning switcher (migrating from IGBTs to SiC and from PIC 18F micro to TI C2000 series), and simulating the i control loop. It is a passion project that takes a backseat to my other commitments, so I am expecting it to take years. 

## Integrated Supply

3D model of the power supply assembly and current build state. 

<table align="center" width="56%">
  <tr>
    <td align="center" width="58%" valign="top">
      <img src="images/Assembly_3D.png" alt="3D model of the power supply assembly" width="100%">
      <br>
      <em>Fig. 1 &mdash; 3D model of the power supply assembly.</em>
    </td>
    <td align="center" width="42%" valign="top">
      <img src="images/Assembly_Real1.png" alt="Current build state of the power supply" width="100%">
      <br>
      <em>Fig. 2 &mdash; Current build state of the power supply.</em>
    </td>
  </tr>
</table>

## LTSpice Transient Model

This model was used to verify output voltage, tune dead time, and determine DC link/voltage multiplier capacitances. 

<table align="center" width="74%">
  <tr>
    <td align="center">
      <img src="images/LTSpice.png" alt="LTSpice transient model of the power converter" width="100%">
      <br>
      <em>Fig. 3 &mdash; LTSpice transient model of the power converter.</em>
    </td>
  </tr>
</table>

## LLC Stage

### Modeling of Transformer

Leakage inductance Lr and magnetizing inductance Lm were derived from an Ansys FEA, and measured with the RidleyBox Frequency Response Analyzer. Ansys FEA results were Lr=11.2uH and Lm=2.63mH. RidleyBox measurements were Lr=200uH and Lm=2.50mH. Measured magnetizing inductance was close to predicted, but Ansys FEA did not correctly account for leakage paths. 

The red RidleyBox sweep is Lm (XF secondary open) and the blue sweep is Lr (XF secondary shorted). 

<table align="center" width="80%">
  <tr>
    <td align="center" width="35%" valign="top">
      <img src="images/ansys.png" alt="Ansys FEA model of the transformer" width="100%">
      <br>
      <em>Fig. 4 &mdash; Ansys FEA model of the transformer.</em>
    </td>
    <td align="center" width="65%" valign="top">
      <img src="images/ridleybox_sweeps.png" alt="RidleyBox frequency response sweeps of the transformer" width="100%">
      <br>
      <em>Fig. 5 &mdash; RidleyBox sweeps of the transformer: Lm (red, XF secondary open) and Lr (blue, XF secondary shorted).</em>
    </td>
  </tr>
</table>

These results were used to simulate LLC gain curves and create a feedforward function for the H-bridge control loop which calculates required frequency for a desired LLC-stage output voltage.

### LLC Gain Curves (Lr and Lm from Ansys FEA)

Two models were used to derive LLC gain curves: a FHA computed with MATLAB and an LTSpice AC analysis. These models were used to determine a suitable resonant capacitor and series L (to add in series with Lr) to achieve desired gain curve. The series L was required since the fusor load is very light, damping series resonant peak. A peaky resonance is desired so the required output voltage range is attainable in a smaller range of frequencies. An L of 800uH (200uH Lr + 600uH series L) and C of 250nF resulted in desired series resonant frequency (fsr).

<table align="center" width="74%">
  <tr>
    <td align="center" width="50%" valign="top">
      <img src="images/matlab_fha.png" alt="LLC gain curve from MATLAB FHA" width="100%">
      <br>
      <em>Fig. 6 &mdash; LLC gain curve from the MATLAB FHA.</em>
    </td>
    <td align="center" width="50%" valign="top">
      <img src="images/ltspice_LLC_ideal.png" alt="LLC gain curve from LTSpice AC analysis" width="100%">
      <br>
      <em>Fig. 7 &mdash; LLC gain curve from the LTSpice AC analysis.</em>
    </td>
  </tr>
</table>

### LLC Gain Curves (Lr and Lm measured with RidleyBox)

LT Spice has been used to simulate the LLC gain curve, including parasitics measured by RidleyBox. Next steps are to update MATLAB state-space model and feedforward function. 

<table align="center" width="52%">
  <tr>
    <td align="center">
      <img src="images/ltspice_LLC_parasitics.png" alt="LTSpice LLC gain curve including measured parasitics" width="100%">
      <br>
      <em>Fig. 8 &mdash; LTSpice LLC gain curve including parasitics measured with the RidleyBox.</em>
    </td>
  </tr>
</table>

## Control System

### Simulink Models

The plan is to use a Simulink model of the power converter to validate the power supply control loop, then use the C2000 Toolbox to flash the control loop onto a TI C2000 microcontroller. The goal is to use the IV curve of a Townsend Avalanche in series with the voltage-to-frequency function to calculate required frequency as a function of i_error. 

<table align="center" width="74%">
  <tr>
    <td align="center">
      <img src="images/simulink_validation.png" alt="Simulink model of the power converter" width="100%">
      <br>
      <em>Fig. 9 &mdash; Simulink model of the power converter for control loop validation.</em>
    </td>
  </tr>
</table>

## Rectifier and Inverter PCB Version 2
For the full quality schematic see the Altium_Exported_PDFs directory.

<table align="center" width="80%">
  <tr>
    <td align="center">
      <img src="images/PCB1v2_Top.png" alt="PCB1v2 top-level schematic" width="100%">
      <br>
      <em>Fig. 10 &mdash; PCB1v2: top-level schematic.</em>
    </td>
  </tr>
</table>

<table align="center" width="80%">
  <tr>
    <td align="center">
      <img src="images/PCB1v2_IPM.png" alt="PCB1v2 IPM schematic" width="100%">
      <br>
      <em>Fig. 11 &mdash; PCB1v2: IPM schematic.</em>
    </td>
  </tr>
</table>

<table align="center" width="80%">
  <tr>
    <td align="center" width="50%" valign="top">
      <img src="images/PCB1v2_Rect.png" alt="PCB1v2 rectifier schematic" width="100%">
      <br>
      <em>Fig. 12 &mdash; PCB1v2: rectifier schematic.</em>
    </td>
    <td align="center" width="50%" valign="top">
      <img src="images/PCB1v2_Sense.png" alt="PCB1v2 sensing schematic" width="100%">
      <br>
      <em>Fig. 13 &mdash; PCB1v2: sensing schematic.</em>
    </td>
  </tr>
</table>

<table align="center" width="80%">
  <tr>
    <td align="center" width="50%" valign="top">
      <img src="images/PCB1v2_Inverter.png" alt="PCB1v2 inverter schematic" width="100%">
      <br>
      <em>Fig. 14 &mdash; PCB1v2: inverter schematic.</em>
    </td>
    <td align="center" width="50%" valign="top">
      <img src="images/PCB1v2_Protection.png" alt="PCB1v2 protection schematic" width="100%">
      <br>
      <em>Fig. 15 &mdash; PCB1v2: protection schematic.</em>
    </td>
  </tr>
</table>

<table align="center" width="80%">
  <tr>
    <td align="center">
      <img src="images/PCB1v2_Control.png" alt="PCB1v2 control schematic" width="100%">
      <br>
      <em>Fig. 16 &mdash; PCB1v2: control schematic.</em>
    </td>
  </tr>
</table>

<table align="center" width="80%">
  <tr>
    <td align="center">
      <img src="images/PCB1v2_Aux.png" alt="PCB1v2 auxiliary supply schematic" width="100%">
      <br>
      <em>Fig. 17 &mdash; PCB1v2: auxiliary supply schematic.</em>
    </td>
  </tr>
</table>

<table align="center" width="80%">
  <tr>
    <td align="center" width="50%" valign="top">
      <img src="images/PCB1v2_15V.png" alt="PCB1v2 15V supply schematic" width="100%">
      <br>
      <em>Fig. 18 &mdash; PCB1v2: 15V supply schematic.</em>
    </td>
    <td align="center" width="50%" valign="top">
      <img src="images/PCB1v2_5V.png" alt="PCB1v2 5V supply schematic" width="100%">
      <br>
      <em>Fig. 19 &mdash; PCB1v2: 5V supply schematic.</em>
    </td>
  </tr>
</table>

## Rectifier and Inverter PCB
This PCB includes the rectifier, switcher and series capacitor for LLC stage. The design had several issues that were fixed in V2. For the full quality schematic see the Altium_Exported_PDFs directory.

<table align="center" width="64%">
  <tr>
    <td align="center">
      <img src="images/PCB1_Schematic_Top.png" alt="Rectifier and Inverter PCB top-level schematic" width="100%">
      <br>
      <em>Fig. 20 &mdash; Rectifier and Inverter PCB: top-level schematic.</em>
    </td>
  </tr>
</table>

<table align="center" width="64%">
  <tr>
    <td align="center">
      <img src="images/PCB1_Schematic_RI.png" alt="Rectifier and Inverter PCB rectifier and inverter schematic" width="100%">
      <br>
      <em>Fig. 21 &mdash; Rectifier and Inverter PCB: rectifier and inverter schematic.</em>
    </td>
  </tr>
</table>

<table align="center" width="48%">
  <tr>
    <td align="center">
      <img src="images/PCB1_Schematic_uC.png" alt="Rectifier and Inverter PCB microcontroller schematic" width="100%">
      <br>
      <em>Fig. 22 &mdash; Rectifier and Inverter PCB: microcontroller schematic.</em>
    </td>
  </tr>
</table>

<table align="center" width="80%">
  <tr>
    <td align="center" width="59%" valign="top">
      <img src="images/PCB1_2D.png" alt="Rectifier and Inverter PCB 2D view" width="100%">
      <br>
      <em>Fig. 23 &mdash; Rectifier and Inverter PCB: 2D view.</em>
    </td>
    <td align="center" width="41%" valign="top">
      <img src="images/PCB1_3D.png" alt="Rectifier and Inverter PCB 3D view" width="100%">
      <br>
      <em>Fig. 24 &mdash; Rectifier and Inverter PCB: 3D view.</em>
    </td>
  </tr>
</table>

## Voltage Multiplier PCB
For the full quality schematic see the Altium_Exported_PDFs directory.

<table align="center" width="64%">
  <tr>
    <td align="center">
      <img src="images/PCB2_Schematic.png" alt="Voltage Multiplier PCB top-level schematic" width="100%">
      <br>
      <em>Fig. 25 &mdash; Voltage Multiplier PCB: top-level schematic.</em>
    </td>
  </tr>
</table>

<table align="center" width="80%">
  <tr>
    <td align="center" width="59%" valign="top">
      <img src="images/PCB2_2D.png" alt="Voltage Multiplier PCB 2D view" width="100%">
      <br>
      <em>Fig. 26 &mdash; Voltage Multiplier PCB: 2D view.</em>
    </td>
    <td align="center" width="41%" valign="top">
      <img src="images/PCB2_3D.png" alt="Voltage Multiplier PCB 3D view" width="100%">
      <br>
      <em>Fig. 27 &mdash; Voltage Multiplier PCB: 3D view.</em>
    </td>
  </tr>
</table>

## Transformer Design

Bobbins and equations used to design transformer. UU core, wound non-concentrically to increase leakage inductance for LLC. Litz wire on primary. The transformer is mounted on machined HDPE mounts, since PLA/ABS do not have required dielectric constant to maintain creepage threshold.

<table align="center" width="80%">
  <tr>
    <td align="center" width="65%" valign="top">
      <img src="images/xf_bobbins.png" alt="Transformer bobbins and design equations" width="100%">
      <br>
      <em>Fig. 28 &mdash; Bobbins and equations used to design the transformer.</em>
    </td>
    <td align="center" width="35%" valign="top">
      <img src="images/xf_photo.png" alt="Transformer mounted on machined HDPE mounts" width="100%">
      <br>
      <em>Fig. 29 &mdash; Transformer mounted on machined HDPE mounts.</em>
    </td>
  </tr>
</table>
