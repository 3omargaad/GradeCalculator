# raw mark boundaries (kept for reference)
Maths_Boundaries = {
    "A*": 251,
    "A": 205,
    "B": 167,
    "C": 130,
    "D": 93,
    "E": 56,
    "U": 0
}
CS_Boundaries = {
    "A*": 292,
    "A": 256,
    "B": 215,
    "C": 174,
    "D": 133,
    "E": 93,
    "U": 0
}
Phys_Boundaries = {
    "A*": 198,
    "A": 171,
    "B": 143,
    "C": 116,
    "D": 89,
    "E": 62,
    "U": 0
}
FM_Boundaries = {
    "A*": 270,
    "A": 246,
    "B": 206,
    "C": 166,
    "D": 126,
    "E": 86,
    "U": 0
}

# maximum marks per subject
MATHS_MAX = 300
CS_MAX    = 350
PHYS_MAX  = 250
FM_MAX    = 300

# convert raw mark boundaries into percentage boundaries
def percentify(boundaries, max_marks):
    return {grade: (mark / max_marks) * 100 for grade, mark in boundaries.items()}

Maths_Pct_B = percentify(Maths_Boundaries, MATHS_MAX)
CS_Pct_B    = percentify(CS_Boundaries,    CS_MAX)
Phys_Pct_B  = percentify(Phys_Boundaries,  PHYS_MAX)
FM_Pct_B    = percentify(FM_Boundaries,    FM_MAX)


def calculate_grade(subject, scored, total):
    # pick the right percentage-boundary dict
    if subject == "A":
        pct_boundaries, subject_name = Maths_Pct_B, "Maths"
    elif subject == "B":
        pct_boundaries, subject_name = CS_Pct_B, "Computer Science"
    elif subject == "C":
        pct_boundaries, subject_name = Phys_Pct_B, "Physics"
    elif subject == "D":
        pct_boundaries, subject_name = FM_Pct_B, "Further Maths"
    else:
        print("❌ Invalid subject choice.")
        return

    # calculate percentage
    percentage = (scored / total) * 100

    # determine grade by percentage thresholds
    for grade in ["A*", "A", "B", "C", "D", "E", "U"]:
        if percentage >= pct_boundaries[grade]:
            final_grade = grade
            break

    # output
    print(f"\nSubject: {subject_name}")
    print(f"Marks:   {scored}/{total}")
    print(f"Score:   {percentage:.2f}%")
    print(f"Grade:   {final_grade}")

    return final_grade, percentage


if __name__ == "__main__":
    print("Welcome to the Grade Calculator!")
    print("Pick your subject:")
    print("A) Maths")
    print("B) Computer Science")
    print("C) Physics")
    print("D) Further Maths\n")

    subject = input("Enter your choice (A/B/C/D): ").strip().upper()
    marks_str = input("Enter your marks in the form X/Y (e.g. 54/68): ").strip()
    scored, total = map(int, marks_str.split("/"))

    calculate_grade(subject, scored, total)