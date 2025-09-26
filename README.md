# Health Data Analysis Project

A comprehensive analysis of health datasets examining the impact of lifestyle factors on diabetes, heart disease, and sleep health outcomes.

## 📊 Project Overview

This project analyzes three health datasets to understand how various lifestyle factors influence health outcomes. The analysis focuses on identifying key relationships between physical activity, BMI, stress levels, and other health indicators across different medical conditions.

## 🎯 Key Insights Discovered

### Diabetes Analysis
- **BMI Impact**: Higher BMI is strongly associated with diabetes progression
- **Physical Activity**: Regular physical activity decreases with diabetes progression
- **Prevalence**: Significant diabetes prevalence in the dataset population

### Heart Disease Analysis
- **Cholesterol Levels**: Higher cholesterol levels are associated with heart disease presence
- **Age Factor**: Heart disease risk increases significantly with age
- **Blood Pressure**: Elevated blood pressure correlates with heart disease risk

### Sleep Health Analysis
- **Stress Correlation**: Strong negative correlation between stress levels and sleep duration
- **BMI Categories**: Different BMI categories show distinct sleep duration patterns
- **Physical Activity**: Positive correlation between physical activity and sleep quality

### Combined Analysis
- **Cross-Dataset Insights**: Physical activity emerges as a protective factor across multiple health conditions
- **Holistic Health View**: Demonstrates how lifestyle factors impact various aspects of health simultaneously

## 📁 Project Structure

```
├── raw_data/                          # Original datasets
│   ├── diabetes_012_health_indicators_BRFSS2015.csv
│   ├── Heart_Disease_Prediction.csv
│   └── Sleep_health_and_lifestyle_dataset.csv
├── cleaned_data/                      # Processed datasets
│   ├── clean_diabetes.csv
│   ├── clean_heart.csv
│   └── clean_sleep.csv
├── clean_dataset.py                   # Data cleaning script
├── diabetes_analysis.py              # Diabetes-specific analysis
├── heart_analysis.py                 # Heart disease analysis
├── sleep_analysis.py                 # Sleep health analysis
├── combine_analysis.py               # Cross-dataset analysis
└── *.png                            # Generated visualizations
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pandas
- matplotlib
- numpy

### Installation
1. Clone the repository:
```bash
git clone <your-repo-url>
cd Data1002-Project-1-code
```

2. Install required packages:
```bash
pip install pandas matplotlib numpy
```

### Running the Analysis

1. **Clean the datasets**:
```bash
python clean_dataset.py
```

2. **Run individual analyses**:
```bash
python diabetes_analysis.py
python heart_analysis.py
python sleep_analysis.py
```

3. **Run combined analysis**:
```bash
python combine_analysis.py
```

## 📈 Generated Visualizations

The analysis produces several key visualizations:

- `diabetes_health_insights.png` - BMI distribution by diabetes stage
- `heart_disease_insights.png` - Cholesterol, age, and blood pressure analysis
- `sleep_health_insights.png` - Stress vs sleep duration and BMI impact
- `combined_physical_activity_impact.png` - Cross-dataset physical activity analysis

## 📊 Datasets Used

### 1. Diabetes Dataset (BRFSS 2015)
- **Source**: Behavioral Risk Factor Surveillance System 2015
- **Records**: ~253,000 individuals
- **Key Variables**: BMI, physical activity, diabetes status, demographics

### 2. Heart Disease Dataset
- **Records**: ~270 individuals
- **Key Variables**: Age, cholesterol, blood pressure, heart disease status

### 3. Sleep Health Dataset
- **Records**: ~370 individuals
- **Key Variables**: Sleep duration, stress levels, physical activity, BMI categories

## 🔍 Analysis Methods

- **Statistical Analysis**: Correlation analysis, group comparisons, summary statistics
- **Data Visualization**: Box plots, scatter plots, bar charts
- **Data Cleaning**: Handling missing values, removing duplicates, standardizing categories

## 📋 Key Findings Summary

1. **Physical Activity** is consistently associated with better health outcomes across all three conditions
2. **BMI** shows strong relationships with diabetes progression and sleep quality
3. **Age** is a significant risk factor for heart disease
4. **Stress levels** have a strong negative impact on sleep duration
5. **Lifestyle factors** demonstrate interconnected effects on multiple health outcomes

## 🛠️ Technical Details

- **Data Processing**: Automated cleaning pipeline with duplicate removal and missing value handling
- **Visualization**: High-resolution plots (300 DPI) with professional formatting
- **Statistical Analysis**: Correlation coefficients, group means, and distribution analysis
- **Code Structure**: Modular design with separate scripts for each analysis component

## 📝 Future Enhancements

- Machine learning models for health outcome prediction
- Additional statistical tests and confidence intervals
- Interactive visualizations
- Expanded dataset integration
- Longitudinal analysis capabilities

## 📄 License

This project is for educational use. Please ensure proper attribution when using the datasets or analysis methods.

---

**Note**: This analysis is for educational and research purposes. Always consult healthcare professionals for medical advice.
