import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load cleaned sleep dataset
sleep_df = pd.read_csv('cleaned_data/clean_sleep.csv')

print("Sleep Health Analysis: Impact of Life Factors on Health Outcomes")
print("="*60)

# Focus on the 2 most meaningful insights
plt.figure(figsize=(12, 5))

# 1. STRESS IMPACT ON SLEEP (Strongest relationship)
plt.subplot(1, 2, 1)
plt.scatter(sleep_df['Stress Level'], sleep_df['Sleep Duration'], alpha=0.6, color='red')
plt.title('Sleep Duration vs Stress Level')
plt.xlabel('Stress Level')
plt.ylabel('Sleep Duration (hours)')
correlation_stress = np.corrcoef(sleep_df['Stress Level'], sleep_df['Sleep Duration'])[0,1]
plt.text(0.05, 0.95, f'Correlation: {correlation_stress:.3f}', transform=plt.gca().transAxes)

# 2. BMI IMPACT ON SLEEP (Clear categorical differences)
plt.subplot(1, 2, 2)
sleep_df.boxplot(column='Sleep Duration', by='BMI Category', ax=plt.gca())
plt.suptitle('')
plt.title('Sleep Duration by BMI Category')
plt.xlabel('BMI Category')
plt.ylabel('Sleep Duration (hours)')

plt.tight_layout()
plt.savefig('sleep_health_insights.png', dpi=300, bbox_inches='tight')
plt.show()

# Summary statistics
print(f"\nKey Insights:")
print(f"1. Stress vs Sleep: Strong negative correlation ({correlation_stress:.3f})")
print(f"2. BMI Categories show distinct sleep duration patterns")

# BMI analysis summary
bmi_summary = sleep_df.groupby('BMI Category')['Sleep Duration'].mean().round(2)
print(f"\nAverage Sleep Duration by BMI:")
print(bmi_summary)