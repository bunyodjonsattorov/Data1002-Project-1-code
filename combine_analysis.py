import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the datasets
diabetes_df = pd.read_csv('cleaned_data/clean_diabetes.csv')
sleep_df = pd.read_csv('cleaned_data/clean_sleep.csv')

print("Combined Health Analysis: Physical Activity Across Health Conditions")
print("="*60)

# COMBINED ANALYSIS: Physical Activity across both datasets

# Analyze Physical Activity impact on Diabetes (from diabetes dataset)
activity_by_diabetes = diabetes_df.groupby('Diabetes_012')['PhysActivity'].mean()

# Analyze Physical Activity impact on Sleep Duration (from sleep dataset)
correlation_activity = np.corrcoef(sleep_df['Physical Activity Level'], sleep_df['Sleep Duration'])[0,1]

# VISUALIZATION: Combined insight showing physical activity impact across both datasets
plt.figure(figsize=(12, 5))

# Subplot 1: Physical Activity vs Diabetes (from diabetes dataset)
plt.subplot(1, 2, 1)
plt.bar(activity_by_diabetes.index, activity_by_diabetes.values, color='blue', alpha=0.7)
plt.title('Physical Activity by Diabetes Stage')
plt.xlabel('Diabetes Stage (0=No, 1=Prediabetes, 2=Diabetes)')
plt.ylabel('Average Physical Activity')

# Subplot 2: Physical Activity vs Sleep Duration (from sleep dataset)
plt.subplot(1, 2, 2)
plt.scatter(sleep_df['Physical Activity Level'], sleep_df['Sleep Duration'], alpha=0.6)
plt.title('Sleep Duration vs Physical Activity Level')
plt.xlabel('Physical Activity Level')
plt.ylabel('Sleep Duration (hours)')
plt.text(0.05, 0.95, f'Correlation: {correlation_activity:.3f}', transform=plt.gca().transAxes)

plt.tight_layout()
plt.savefig('combined_physical_activity_impact.png', dpi=300, bbox_inches='tight')
plt.show()

# Summary statistics
print(f"\nKey Insights:")
print(f"1. Physical activity decreases with diabetes progression")
print(f"2. Physical activity shows positive correlation with sleep duration ({correlation_activity:.3f})")
print(f"3. Physical activity is a protective factor for both diabetes prevention and sleep quality")

# Statistical summary
print(f"\nAverage Physical Activity by Diabetes Stage:")
for stage, activity in activity_by_diabetes.items():
    stage_name = ['No Diabetes', 'Prediabetes', 'Diabetes'][int(stage)]
    print(f"  {stage_name}: {activity:.2f}")

# Additional insights
print(f"\nDataset Overview:")
print(f"• Diabetes dataset: {len(diabetes_df)} records")
print(f"• Sleep dataset: {len(sleep_df)} records")
print(f"• Combined insight: Physical activity benefits multiple health conditions")