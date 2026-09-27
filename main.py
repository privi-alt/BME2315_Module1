from patient import Patient

import matplotlib.pyplot as plt
import statistics
from scipy import stats

# Load patient data from the CSV file
Patient.instantiate_from_csv("Metadata and Protein Data for Module 1.csv")
# Print the number of patients and one example patient
print(len(Patient.all_patients))
print(Patient.all_patients[0])
# Sort and print patients by age at death
sorted_patients = sorted(
    Patient.all_patients,
    key=lambda patient: patient.age_at_death
)
for patient in sorted_patients:
    print(patient)
female_dementia = Patient.filter("Female", "Dementia")# Filter female patients with dementia

for patient in female_dementia:
    print(patient)

print("Number of female patients with dementia:", len(female_dementia))
male_dementia = Patient.filter("Male", "Dementia")# Calculate mean and standard deviation of pTAU by sex
female_ptau = [patient.ptau for patient in female_dementia]
male_ptau = [patient.ptau for patient in male_dementia]
female_mean = statistics.mean(female_ptau)
male_mean = statistics.mean(male_ptau)
female_sd = statistics.stdev(female_ptau)
male_sd = statistics.stdev(male_ptau)
groups = ["Female", "Male"]
means = [female_mean, male_mean]
standard_deviations = [female_sd, male_sd]

# Compare female and male pTAU levels using an independent t-test
t_statistic, p_value = stats.ttest_ind(female_ptau, male_ptau)

print("Female vs. Male pTAU t-statistic:", t_statistic)
print("Female vs. Male pTAU p-value:", p_value)

plt.bar(groups, means, yerr=standard_deviations, capsize=5)

plt.xlabel("Sex")
plt.ylabel("Mean pTAU (pg/ug)")
plt.title("Mean pTAU in Dementia Patients by Sex")

plt.savefig("ptau_bar_graph.png", dpi=300, bbox_inches="tight")
plt.show()



ages = [patient.age_at_death for patient in Patient.all_patients]
ptau_values = [patient.ptau for patient in Patient.all_patients]

# Calculate linear regression for age at death vs. pTAU
slope, intercept, r_value, p_value, std_err = stats.linregress(ages, ptau_values)

regression_line = [slope * age + intercept for age in ages]

print("Age vs. pTAU slope:", slope)
print("Age vs. pTAU intercept:", intercept)
print("Age vs. pTAU R-squared:", r_value ** 2)
print("Age vs. pTAU p-value:", p_value)

plt.figure()
plt.scatter(ages, ptau_values)
plt.plot(ages, regression_line)

plt.xlabel("Age at Death")
plt.ylabel("pTAU (pg/ug)")
plt.title("Age at Death vs. pTAU with Linear Regression")

plt.savefig("age_vs_ptau_scatter.png", dpi=300, bbox_inches="tight")
plt.show()



# Filter patients by cognitive status
dementia = Patient.filter("any", "Dementia")
no_dementia = Patient.filter("any", "No dementia")

# Get pTAU values for each cognitive status group
dementia_ptau = [patient.ptau for patient in dementia]
no_dementia_ptau = [patient.ptau for patient in no_dementia]

t_statistic, p_value = stats.ttest_ind(dementia_ptau, no_dementia_ptau)

print("Dementia vs. No dementia pTAU t-statistic:", t_statistic)
print("Dementia vs. No dementia pTAU p-value:", p_value)

# Calculate mean and standard deviation of pTAU for each group
dementia_mean = statistics.mean(dementia_ptau)
no_dementia_mean = statistics.mean(no_dementia_ptau)

dementia_sd = statistics.stdev(dementia_ptau)
no_dementia_sd = statistics.stdev(no_dementia_ptau)

# Create bar graph
groups = ["Dementia", "No dementia"]
means = [dementia_mean, no_dementia_mean]
standard_deviations = [dementia_sd, no_dementia_sd]

plt.figure()
plt.bar(groups, means, yerr=standard_deviations, capsize=5)

plt.xlabel("Cognitive Status")
plt.ylabel("Mean pTAU (pg/ug)")
plt.title("Mean pTAU by Cognitive Status")

plt.savefig("ptau_cognitive_status_bar_graph.png", dpi=300, bbox_inches="tight")
plt.show()