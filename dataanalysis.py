import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#New Comment
# Load the Iris dataset from Seaborn
iris = sns.load_dataset("iris")

# Print the first 5 rows for initial inspection
print("First 5 rows of the Iris dataset:")
print(iris.head())

# Check for missing values
print("\nMissing values:")
print(iris.isnull().sum())

# Exploratory Data Analysis (EDA)

# Descriptive statistics for numerical columns
print("\nDescriptive statistics:")
print(iris.describe())

# Distribution of each feature
sns.histplot(data=iris, x="sepal_length", hue="species")
plt.title("Distribution of Sepal Length by Species")
plt.show()

sns.histplot(data=iris, x="sepal_width", hue="species")
plt.title("Distribution of Sepal Width by Species")
plt.show()

sns.histplot(data=iris, x="petal_length", hue="species")
plt.title("Distribution of Petal Length by Species")
plt.show()

sns.histplot(data=iris, x="petal_width", hue="species")
plt.title("Distribution of Petal Width by Species")
plt.show()

# Pair plot to visualize relationships between features
sns.pairplot(data=iris, hue="species")
plt.show()

# Correlation matrix to explore relationships between numerical features
numerical_features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
numerical_correlation = iris[numerical_features].corr()


# Create a heatmap to visualize correlations
sns.heatmap(numerical_correlation, annot=True)
plt.title("Correlation Matrix (Numerical Features)")
plt.show()

# Example: Group by species and calculate mean values
species_means = iris.groupby("species").mean()
print("\nMean values for each species:")
print(species_means)

# Visualizations (tailored based on insights from EDA and correlation matrix)

# Example: Boxplots to compare distributions between species for petal features
sns.boxplot(
    x="species",
    y="petal_length",
    showmeans=True,
    data=iris
)
plt.title("Boxplot of Petal Length by Species")
plt.show()

sns.boxplot(
    x="species",
    y="petal_width",
    showmeans=True,
    data=iris
)
plt.title("Boxplot of Petal Width by Species")
plt.show()

# Additional visualizations can be created based on findings

# Correlation Calculations (already explored in EDA)

# The correlation matrix provides insights into relationships between features

print("\nCorrelation matrix (refer to heatmap for visualization):")
print(numerical_correlation)
