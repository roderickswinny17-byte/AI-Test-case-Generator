from generator import read_requirement,generate_test_cases
from excel_export import export_to_excel

print("+++++++++-------------------+++++++++++++")
print("AI Test Case Generator")
print("+++++++++-------------------+++++++++++++")

requirement = read_requirement("sample_requirement.txt")

if requirement:
    print("\nRequirement loaded succesfully\n")
    print(requirement)
    print("\n Generating Test Cases\n")
    test_cases = generate_test_cases(requirement)
    print("+++++++++-------------------+++++++++++++")
    print("Generated Test Cases")
    print("+++++++++-------------------+++++++++++++")
    print(test_cases)
    with open("output/generated_test_cases.md","w",encoding="utf-8") as file:
        file.write(test_cases)
        print("+++++++++-------------------+++++++++++++")
    print("\n Test Cases saved to  output/generated_test_cases.md")
    export_to_excel(
        test_cases,
        "output/TestCases.xlsx"
    )
