from fastapi import FastAPI
import uvicorn

app = FastAPI()

EMPLOYEES = [
    {"EmployeeID": 1,  "LastName": "Baxter",     "FirstName": "Michael",  "Title": "Ambulance person", "region": "Norteamérica"},
    {"EmployeeID": 2,  "LastName": "Baker",      "FirstName": "Charles",  "Title": "Loss adjuster, chartered", "region": "Europa"},
    {"EmployeeID": 3,  "LastName": "Rodriguez",  "FirstName": "Helen",    "Title": "Secretary, company", "region": "Asia Pacífico"},
    {"EmployeeID": 4,  "LastName": "Obrien",     "FirstName": "Cindy",    "Title": "Accountant, chartered management", "region": "Latinoamérica"},
    {"EmployeeID": 5,  "LastName": "Clark",      "FirstName": "Jessica",  "Title": "Engineer, mining", "region": "Medio Oriente"},
    {"EmployeeID": 6,  "LastName": "Sullivan",   "FirstName": "Wendy",    "Title": "Fast food restaurant manager", "region": "África"},
    {"EmployeeID": 7,  "LastName": "Estrada",    "FirstName": "Shelly",   "Title": "Actor", "region": "Oceanía"},
    {"EmployeeID": 8,  "LastName": "Dickerson",  "FirstName": "Ralph",    "Title": "Metallurgist", "region": "Norteamérica"},
    {"EmployeeID": 9,  "LastName": "Thompson",   "FirstName": "Sally",    "Title": "Commercial art gallery manager", "region": "Europa"},
    {"EmployeeID": 10, "LastName": "Miranda",    "FirstName": "Stacie",   "Title": "Sports therapist", "region": "Asia Pacífico"},
    {"EmployeeID": 11, "LastName": "Wright",     "FirstName": "Tracy",    "Title": "IT trainer", "region": "Latinoamérica"},
    {"EmployeeID": 12, "LastName": "Holmes",     "FirstName": "Karen",    "Title": "Civil Service fast streamer", "region": "Medio Oriente"},
    {"EmployeeID": 13, "LastName": "Williams",   "FirstName": "Amy",      "Title": "Civil Service fast streamer", "region": "África"},
    {"EmployeeID": 14, "LastName": "Davidson",   "FirstName": "Rebecca",  "Title": "Hydrographic surveyor", "region": "Oceanía"},
    {"EmployeeID": 15, "LastName": "Richardson", "FirstName": "Michael",  "Title": "Biomedical engineer", "region": "Norteamérica"},
    {"EmployeeID": 16, "LastName": "Garcia",     "FirstName": "Daniel",   "Title": "Tourism officer", "region": "Europa"},
    {"EmployeeID": 17, "LastName": "Roth",       "FirstName": "Joseph",   "Title": "Special effects artist", "region": "Asia Pacífico"},
    {"EmployeeID": 18, "LastName": "Allen",      "FirstName": "Tammy",    "Title": "Engineer, broadcasting (operations)", "region": "Latinoamérica"},
    {"EmployeeID": 19, "LastName": "Nguyen",     "FirstName": "Michael",  "Title": "Radiation protection practitioner", "region": "Medio Oriente"},
    {"EmployeeID": 20, "LastName": "Krause",     "FirstName": "Richard",  "Title": "Materials engineer", "region": "África"},
    {"EmployeeID": 21, "LastName": "Byrd",       "FirstName": "Kristopher","Title": "Microbiologist", "region": "Oceanía"},
    {"EmployeeID": 22, "LastName": "Patterson",  "FirstName": "Stephanie","Title": "Quality manager", "region": "Norteamérica"},
    {"EmployeeID": 23, "LastName": "Hill",       "FirstName": "Derek",    "Title": "Media buyer", "region": "Europa"},
    {"EmployeeID": 24, "LastName": "Clayton",    "FirstName": "Kelly",    "Title": "Optometrist", "region": "Asia Pacífico"},
    {"EmployeeID": 25, "LastName": "Perez",      "FirstName": "Chelsea",  "Title": "Energy engineer", "region": "Latinoamérica"},
    {"EmployeeID": 26, "LastName": "Noble",      "FirstName": "Chelsea",  "Title": "Television production assistant", "region": "Medio Oriente"},
    {"EmployeeID": 27, "LastName": "Russell",    "FirstName": "Curtis",   "Title": "Event organiser", "region": "África"},
    {"EmployeeID": 28, "LastName": "Calhoun",    "FirstName": "Justin",   "Title": "Product manager", "region": "Oceanía"},
    {"EmployeeID": 29, "LastName": "Gallagher",  "FirstName": "Juan",     "Title": "Broadcast presenter", "region": "Norteamérica"},
    {"EmployeeID": 30, "LastName": "Adams",      "FirstName": "Michael",  "Title": "Herbalist", "region": "Europa"},
    {"EmployeeID": 31, "LastName": "Herrera",    "FirstName": "Samantha", "Title": "Phytotherapist", "region": "Asia Pacífico"},
    {"EmployeeID": 32, "LastName": "Blevins",    "FirstName": "Lisa",     "Title": "Waste management officer", "region": "Latinoamérica"},
    {"EmployeeID": 33, "LastName": "Carter",     "FirstName": "Richard",  "Title": "Nurse, children's", "region": "Medio Oriente"},
    {"EmployeeID": 34, "LastName": "Chambers",   "FirstName": "Amy",      "Title": "Counsellor", "region": "África"},
    {"EmployeeID": 35, "LastName": "Sherman",    "FirstName": "Jeremy",   "Title": "Investment analyst", "region": "Oceanía"},
    {"EmployeeID": 36, "LastName": "Diaz",       "FirstName": "Alexandra","Title": "Administrator, education", "region": "Norteamérica"},
    {"EmployeeID": 37, "LastName": "Parker",     "FirstName": "Justin",   "Title": "Scientist, forensic", "region": "Europa"},
    {"EmployeeID": 38, "LastName": "Harrison",   "FirstName": "Heidi",    "Title": "Insurance underwriter", "region": "Asia Pacífico"},
    {"EmployeeID": 39, "LastName": "Marquez",    "FirstName": "Melissa",  "Title": "Commercial/residential surveyor", "region": "Latinoamérica"},
    {"EmployeeID": 40, "LastName": "Morrow",     "FirstName": "Tom",      "Title": "Cytogeneticist", "region": "Medio Oriente"},
    {"EmployeeID": 41, "LastName": "Freeman",    "FirstName": "Sherry",   "Title": "Landscape architect", "region": "África"},
    {"EmployeeID": 42, "LastName": "Jones",      "FirstName": "Ronald",   "Title": "Corporate treasurer", "region": "Oceanía"},
    {"EmployeeID": 43, "LastName": "Shaw",       "FirstName": "Michael",  "Title": "Contractor", "region": "Norteamérica"},
    {"EmployeeID": 44, "LastName": "Garcia",     "FirstName": "Valerie",  "Title": "Community education officer", "region": "Europa"},
    {"EmployeeID": 45, "LastName": "Parker",     "FirstName": "Stacy",    "Title": "Professor Emeritus", "region": "Asia Pacífico"},
    {"EmployeeID": 46, "LastName": "Jones",      "FirstName": "Heather",  "Title": "Visual merchandiser", "region": "Latinoamérica"},
    {"EmployeeID": 47, "LastName": "Burke",      "FirstName": "Terri",    "Title": "Information officer", "region": "Medio Oriente"},
    {"EmployeeID": 48, "LastName": "Murphy",     "FirstName": "Robert",   "Title": "Engineering geologist", "region": "África"},
    {"EmployeeID": 49, "LastName": "Jones",      "FirstName": "Victoria", "Title": "Associate Professor", "region": "Oceanía"},
    {"EmployeeID": 50, "LastName": "Russell",    "FirstName": "Amy",      "Title": "Engineer, agricultural", "region": "Norteamérica"},
    {"EmployeeID": 51, "LastName": "Smith",      "FirstName": "John",     "Title": "Data Scientist", "region": "Europa"},
    {"EmployeeID": 52, "LastName": "Johnson",    "FirstName": "Emily",   "Title": "Software Engineer", "region": "Asia Pacífico"},
    {"EmployeeID": 53, "LastName": "Williams",   "FirstName": "David",   "Title": "Product Manager", "region": "Latinoamérica"},
    {"EmployeeID": 54, "LastName": "Jones",      "FirstName": "Sarah",   "Title": "UX Designer", "region": "Medio Oriente"},
    {"EmployeeID": 55, "LastName": "Brown",      "FirstName": "Michael", "Title": "DevOps Engineer", "region": "Europa"},
]

@app.get("/employees/list")
def get_employees():
    return EMPLOYEES

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
