import pandas as pd
import matplotlib.pyplot as plt

# Load data
diabetes_df = pd.read_csv('cleaned_data/clean_diabetes.csv')

print("Diabetes Health Analysis: Impact of Life Factors on Health Outcomes")
print("="*60)

# Focus on 1 meaningful insight
plt.figure(figsize=(8, 5))

# 1. BMI IMPACT ON DIABETES 
plt.subplot(1, 1, 1)
diabetes_df.boxplot(column='BMI', by='Diabetes_012', ax=plt.gca())
plt.suptitle('')  # Remove default title
plt.title('BMI Distribution by Diabetes Stage')
plt.xlabel('Diabetes Stage (0=No, 1=Prediabetes, 2=Diabetes)')
plt.ylabel('BMI')

plt.tight_layout()
plt.savefig('diabetes_health_insights.png', dpi=300, bbox_inches='tight')
plt.show()

# Summary statistics
print(f"\nKey Insights:")
print(f"1. BMI increases with diabetes progression")

# Statistical summary
diabetes_summary = diabetes_df.groupby('Diabetes_012').agg({
    'BMI': 'mean'
}).round(2)
print(f"\nAverage BMI by Diabetes Stage:")
print(diabetes_summary)

# Additional insights
print(f"\nDataset Overview:")
print(f"• Total Records: {len(diabetes_df)}")
print(f"• Diabetes Prevalence: {(diabetes_df['Diabetes_012'] > 0).mean()*100:.1f}%")
print(f"• Average BMI: {diabetes_df['BMI'].mean():.1f}")