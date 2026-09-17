import csv
class Patient:
    all_patients = []
    def __init__(
        self,
        donor_id,
        age_at_death,
        sex,
        apoe_genotype,
        cognitive_status,
        abeta42,
        ptau
    ):
        self.donor_id = donor_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.apoe_genotype = apoe_genotype
        self.cognitive_status = cognitive_status
        self.abeta42 = abeta42
        self.ptau = ptau
        Patient.all_patients.append(self)
    def __repr__(self):
        return f"{self.donor_id} | Age: {self.age_at_death} | {self.sex} | {self.cognitive_status} | pTAU: {self.ptau}"
    @classmethod
    def instantiate_from_csv(cls, filename):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                Patient(
                    donor_id=row["Donor ID"],
                    age_at_death=int(row["Age at Death"]),
                    sex=row["Sex"],
                    apoe_genotype=row["APOE Genotype"],
                    cognitive_status=row["Cognitive Status"],
                    abeta42=float(row["ABeta42 pg/ug"]),
                    ptau=float(row["pTAU pg/ug"])
                )
    @classmethod
    def filter(cls, sex, cognitive_status):
        filtered_patients = []

        for patient in cls.all_patients:
            if patient.sex == sex and patient.cognitive_status == cognitive_status:
                filtered_patients.append(patient)

        return filtered_patients