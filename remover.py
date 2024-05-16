# deleting empty files from dataframe
import pandas as pd
import os
import re

_ICU_TIMESTAMP_HEADER = 'Timestamp'
_PATIENT_TIMESTAMP_HEADER = 'CHARTTIME'
_SUBJECT_ID = 'SUBJECT_ID'
_RESULTS_FILE = 'outputs/intersection_updated.csv'
_CSV_EXTENSION = ".csv"


def _delete(filepath):
    os.remove(filepath)
    print("[DEBUG] removed", filepath)

if __name__ == "__main__":
    icu_vitals_directory = 'without_impute_with_icuid_pred_abp1_test'
    del_count = 0
    tot_count = 0
    
    print("[DEBUG], starting")
    for subdir, _, files in os.walk(icu_vitals_directory):
        
        for icu_data_file in files:
            # print("[DEBUG] trying for", os.path.join(subdir, icu_data_file))
            if icu_data_file.endswith(_CSV_EXTENSION):
                tot_count += 1
                # match = pattern.match(icu_data_file)
                filepath = os.path.join(subdir, icu_data_file)
                #print("[DEBUG] file =",  filepath)
                try:
                    df = pd.read_csv(filepath)
                    if df.empty:
                        del_count += 1
                        _delete(filepath)
                        
                except pd.errors.EmptyDataError as e:
                    # print("[ERROR]", e, filepath)
                    del_count += 1
                    _delete(filepath)
        
    print("[DEBUG] tot_files =", tot_count, "to del =", del_count, "exiting")