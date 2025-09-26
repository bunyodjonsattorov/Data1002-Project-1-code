import pandas as pd

# File paths for raw datasets
sleep_file = 'raw_data/Sleep_health_and_lifestyle_dataset.csv'  
diabetes_file = 'raw_data/diabetes_012_health_indicators_BRFSS2015.csv'  
heart_file = 'raw_data/Heart_Disease_Prediction.csv' 

print("DATA CLEANING PROCESS STARTED")
print("="*40)

# SLEEP DATASET CLEANING
print("\n1. SLEEP DATASET")
sleep_df = pd.read_csv(sleep_file)
print(f"Original: {sleep_df.shape[0]} records, {sleep_df.shape[1]} columns")

sleep_df['Sleep Disorder'] = sleep_df['Sleep Disorder'].fillna('None')
sleep_df['BMI Category'] = sleep_df['BMI Category'].replace({'Normal Weight': 'Normal'})
sleep_df.to_csv('cleaned_data/clean_sleep.csv', index=False)
print(f"✅ Sleep dataset cleaned and saved: {sleep_df.shape}")

# DIABETES DATASET CLEANING
print("\n2. DIABETES DATASET")
diabetes_df = pd.read_csv(diabetes_file)
print(f"Original: {diabetes_df.shape[0]} records, {diabetes_df.shape[1]} columns")

diabetes_df = diabetes_df.drop_duplicates()
diabetes_df.to_csv('cleaned_data/clean_diabetes.csv', index=False)
print(f"✅ Diabetes dataset cleaned and saved: {diabetes_df.shape}")

# HEART DATASET CLEANING
print("\n3. HEART DATASET")
heart_df = pd.read_csv(heart_file)
print(f"Original: {heart_df.shape[0]} records, {heart_df.shape[1]} columns")

heart_df = heart_df.drop_duplicates()
heart_df.to_csv('cleaned_data/clean_heart.csv', index=False)
print(f"✅ Heart dataset cleaned and saved: {heart_df.shape}")

print("\n🚀 ALL DATASETS ARE NOW CLEANED AND READY FOR ANALYSIS!")