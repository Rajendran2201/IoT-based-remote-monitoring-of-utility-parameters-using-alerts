# Models and Parameters

### **1. Prediction of the Emission of Greenhouse Gases**

**Goal:** Estimate emissions of CO₂, CH₄, N₂O based on operational data.

**Relevant Utility Parameters:**

- **Level** of:
    
    - CO₂
        
    - CH₄
        
    - Oxygen
        
- **Feed consumption, product, byproduct** (affects emissions intensity)
    
- **Steam** (energy usage metric)
    
- **Fuel gas** (combustion source)
    
- **Flare system** (emergency emissions source)
    
- **Flow rate** (gas flow = emission output)
    
- **Cooling water** (indirectly related to efficiency & emissions)
    
- **Temperature** (affects combustion/emission efficiency)
    
- **Pressure** (in reactors/pipes, affects emissions)
    
- **Peak hours (time)** (load variation affects emission patterns)
    

---

### **2. Fault Detection in Equipment (Pumps and Motors)**

**Goal:** Detect early-stage faults or performance degradation.

**Relevant Utility Parameters:**

- **Electricity (voltage & current)** (motor health & load)
    
- **Vibration** (bearing issues, imbalance)
    
- **Noise level** (future input - acoustic anomalies)
    
- **Temperature** (overheating)
    
- **Feed consumption, product, byproduct** (abnormal process flow)
    
- **Thermal imaging** (hotspots indicating faults)
    
- **Cooling water** (if used to regulate motor/pump temperature)
    

---

### **3. Filter Clogging Detection in Filtration Equipment**

**Goal:** Detect pressure or flow anomalies that indicate clogging.

**Relevant Utility Parameters:**

- **Pressure** (increase indicates clogging)
    
- **Flow rate** (reduction = blockage)
    
- **Temperature** (may rise due to flow restriction)
    
- **Feed consumption, product, byproduct** (to analyze material causing clogging)
    
- **Cooling water** (may affect viscosity/clogging if applicable)
    

---

### **4. Tank Overfilling Prediction & Inventory Management**

**Goal:** Predict when tanks may overfill and monitor inventory levels.

**Relevant Utility Parameters:**

- **Level** of tank contents (primary)
    
- **Flow rate** (inflow/outflow)
    
- **Feed consumption, product, byproduct** (net accumulation)
    
- **Peak hours (time)** (production cycle insight)
    
- **Pressure** (may correlate with tank filling)
    
- **Temperature** (density changes may affect level measurement)
    
- **Nitrogen/Oxygen/CO₂/Methane levels** (if stored in tanks)
    

---

### **Summary Table**

| **Objective**                      | **Key Utility Parameters**                                                                                                              |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Greenhouse Gas Emission**        | CO₂, CH₄, O₂ levels, steam, fuel gas, flare system, flow rate, feed/product/byproduct, pressure, temperature, cooling water, peak hours |
| **Fault Detection (Pumps/Motors)** | Voltage, current, vibration, noise level, thermal imaging, temperature, feed/product/byproduct, cooling water                           |
| **Filter Clogging Detection**      | Pressure, flow rate, temperature, feed/product/byproduct, cooling water                                                                 |
| **Tank Overfilling & Inventory**   | Level (various), flow rate, feed/product/byproduct, pressure, temperature, peak hours, nitrogen/CO₂/CH₄                                 |
