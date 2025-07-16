## Ideation and Objectives

#### Utility parameters
1. Electricity - voltage and current - early fault detection in pumps and motors
2. temperature
3. pressure - filter clogging detection
4. Vibration for motors and pumps - predictive maintenance
5. thermal imaging for hotspots (faulty wiring, steam leaks)
6. Steam
7. fuel gas
8. compressed air
9. nitrogen
10. flare system
11. peak hours (time)
12. feed consumption, product and byproduct - fault detection [efficiency]
13. flow rate
14. level - water, oxygen, carbon dioxide and methane (any by products), tank (overfilling prediction, inventory )
15. cooling water
16. noise level - future 

----
#### Objectives

###### Emission of green house gases
- Detection Emission of green house gases
- Anomaly detection of emissions and efficiency
	- Alerts - mail, SMS, maintanence system (admin panel)
- Prevention and recommendations - AI models (voice detection)
###### Miscellaneous
- fault detection of equipments (pumps and motors)
- filter clogging detection in filteration equipments
- thermal imagines of wires, switch boards, and steam leaks
- tank overfilling prediction and inventory
- noise level
- level of $O_2$ --> fermentation reactors, combustion efficieny and explosion prevention
	- partial combustion using $\frac{1}{2} O_2$ producing $CO$ which can be converted to useful products - detection using AI models [future scope]

#### Target
- green house gas emissions, 
	- $CH_4$ 
	- $CO_2$
- equipment fault occurence - 8 main equipments (approximately)
- thermal imaging - contour maps
- level prediction 
- noise detection - turns off the system in case of extreme sounds

----

#### Visualization

| **Parameter**                                                                         | **Best Graph Type(s)**                                                            | **Purpose**                            |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------- |
| **Voltage & Current**                                                                 | - Line chart (real-time)- Heatmap (for multiple machines)                         | Early fault detection in pumps/motors  |
| **Temperature / Pressure / Flow rate / Steam / Fuel gas / Compressed air / Nitrogen** | - Time series line graph- Gauge chart (for live status)- Threshold indicator bars | Monitor for anomalies, safe ranges     |
| **Thermal Imaging**                                                                   | - Infrared heatmaps- Contour plots                                                | Visualize hot spots in real-time       |
| **Peak hours (time-based consumption)**                                               | - Bar chart (hour vs usage)- Heatmap calendar (day/time)                          | Identify high-usage periods            |
| **Feed, Product, Byproduct Consumption**                                              | - Sankey diagram (input → output)- Stacked bar chart                              | Detect inefficiencies                  |
| **Tank Levels (O₂, CO₂, CH₄, Water)**                                                 | - Line chart- Area chart- Predictive fill time (regression overlay)               | Predict overfilling, monitor inventory |
| **Cooling Water**                                                                     | - Line chart- Status gauge                                                        | System cooling efficiency check        |
| **Noise Level**                                                                       | - Real-time waveform- Spectrogram plot                                            | Detect alarming sounds (future scope)  |


| **Objective**                                | **Graph/Visualization**                                                            | **Purpose**                                         |
| -------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------- |
| **GHG Emissions (CO₂, CH₄)**                 | - Line chart (trend)- Pie/donut (proportion per source)- Area chart (stacked)      | Emission source identification, compliance tracking |
| **AI-based Fault Detection (motors, pumps)** | - Timeline with fault flags- Pareto chart (most frequent faults)- Status dashboard | Fault frequency and root cause analysis             |
| **Filter Clogging Detection**                | - Line chart (pressure drop vs time)- Status indicators                            | Early clogging detection                            |
| **Tank Inventory / Overfill Prediction**     | - Predictive fill trend- Remaining time gauge                                      | Avoid losses due to overflows                       |
| **Noise Level Alerts**                       | - Audio spectrogram- Peak sound detector                                           | Future feature for acoustic fault detection         |
