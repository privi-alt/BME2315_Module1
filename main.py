from patient import Patient

import matplotlib.pyplot as plt
import statistics
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

plt.bar(groups, means, yerr=standard_deviations, capsize=5)

plt.xlabel("Sex")
plt.ylabel("Mean pTAU (pg/ug)")
plt.title("Mean pTAU in Dementia Patients by Sex")

plt.savefig("ptau_bar_graph.png", dpi=300, bbox_inches="tight")
plt.close()
ages = [patient.age_at_death for patient in Patient.all_patients]
ptau_values = [patient.ptau for patient in Patient.all_patients]
plt.figure()
plt.scatter(ages, ptau_values)
plt.xlabel("Age at Death")
plt.ylabel("pTAU (pg/ug)")
plt.title("Age at Death vs. pTAU")
plt.savefig("age_vs_ptau_scatter.png", dpi=300, bbox_inches="tight")
plt.show()