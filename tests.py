# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python import run_python_file

class MainTest:
    def __init__(self, test_cases):
        self.runTestCases(test_cases)
    
    def runTestCases(self, test_cases):
        for case in test_cases:
            print(run_python_file(case[0], case[1]))
        return

if __name__ == "__main__":
    test_cases = [
        ["calculator", "main.py"],
        ["calculator", "tests.py"],
        # ["calculator", "../main.py"],
        # ["calculator", "nonexistent.py"]
    ]

    main_test = MainTest(test_cases)