
from dataclasses import dataclass
import pandas as pd
import numpy as np

@dataclass
class Patient:
    RecordID: int = 0
    Age: float = -1
    Gender: int = -1
    ICUType: int = -1
    Height: int = -1
    Albumin: float = -1
    ALP: float = -1
    ALT: float = -1
    AST: float = -1
    Bilirubin: float = -1
    BUN: float = -1
    Cholesterol: float = -1
    Creatinine: float = -1
    DiasABP: float = -1
    FiO2: float = -1
    GCS: int = -1
    Glucose: float = -1
    HCO3: float = -1
    HCT: float = -1
    HR: int = -1
    K: float = -1
    Lactate: float = -1
    Mg: float = -1
    MAP: float = -1
    MechVent: bool = False
    Na: float = -1
    NIDiasABP: float = -1
    NIMAP: float = -1
    NISysABP: float = -1
    PaCO2: float = -1
    PaO2: float = -1
    pH: float = -1
    Platelets: float = -1
    RespRate: int = -1
    SaO2: float = -1
    SysABP: float = -1
    Temp: float = -1
    TroponinI: float = -1
    TroponinT: float = -1
    Urine: float = -1
    WBC: float = -1
    Weight: int = -1

def raw_to_df(patient_data):
    """
    Convert patient data to a pandas DataFrame.

    Parameters:
        patient_data (Any): Raw patient data after being read as a df from read_csv function

    Returns:
        pd.DataFrame: Structured patient data as a DataFrame.
    """
    not_to_be_added = [
    'Age',              # Fixed, does not change
    'Gender',           # Binary, constant
    'ICUType',          # Constant for the patient's ICU stay
    'Height',           # Fixed, does not change
    'RecordID',         # Unique identifier, does not change
    'MechVent',         # Binary, should not be summed
    'GCS',              # Score, should not be summed
    'Temp',             # Single measurement at each time point
    'PaCO2',            # Arterial gas, not cumulative
    'PaO2',             # Arterial gas, not cumulative
    'pH',               # Arterial gas, not cumulative
    'Platelets',        # Blood count, should not be summed
    'Weight'            # Fixed for most cases
    ]
    Patient_info = [Patient() for _ in range(len(patient_data))]
    for index, patient in enumerate(Patient_info):
        for _, row in patient_data[index].iterrows():
            param = row['Parameter']
            value = row['Value'] 
            if hasattr(patient, param):
                current = getattr(patient, param)
                if current == -1:
                    current = 0
                if param not in not_to_be_added:
                    setattr(patient, param, current + value)
                else:
                    setattr(patient, param, value)
            else:
                print(f"Warning: Patient {patient.RecordID} has no attribute '{param}'")
    for patient in Patient_info:
        for field in patient.__dataclass_fields__:
            value = getattr(patient, field)
            if value == -1:
                setattr(patient, field, None)
    # we make the value None to mask the data, -1 would cause very severe inaccuracies
    df = pd.DataFrame([patient.__dict__ for patient in Patient_info])
    return df