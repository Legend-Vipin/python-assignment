# 8. Association (uses-a)
# Concept: Objects linked but independent
class Stethoscope:
    def __init__(self, brand="MediSound"):
        self.brand = brand

    def listen(self):
        print(f"Listening with {self.brand} stethoscope...")

class Doctor:
    def __init__(self, name):
        self.name = name

    def perform_checkup(self, patient_name, stethoscope_tool: Stethoscope):
        print(f"Dr. {self.name} starting checkup for {patient_name}.")
        stethoscope_tool.listen()
        print("Checkup complete.")

dr_greg = Doctor("Gregory House")
common_stethoscope = Stethoscope()
fancy_stethoscope = Stethoscope("UltraScope")

print("Demonstrating Association:")
dr_greg.perform_checkup("Patient A", common_stethoscope)
print("---")
dr_greg.perform_checkup("Patient B", fancy_stethoscope)
