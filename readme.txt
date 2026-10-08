HARBORFLOW DISPATCH CONSOLE - TEAM README

Run instructions
----------------
Command:
Python version tested: 3.14.7 

Team members and concrete contributions
---------------------------------------
Name: Anton Johansson
Contribution: Developed the main functionality for Task 4 (Consolidate parcel labels), Task 6 (Classify service performance) and Task 8 (Input validation and console resilience).
This includes parcel-label processing, service-performance classification, and input validation across the console.
When a group member left, I also reviewed the existing implementations of Task 3 and Task 9, corrected and adapted the code where needed, and integrated both features into the final HarborFlow Dispatch Console.
I also contributed to testing and making sure the different functions worked correctly together.

Name: Nils-Oskar Arnell
Contribution: Task_02, Task_05, exception handling/bug fixes for whole program

Name: Vladyslav Pryshchep
Contribution: Building dispatch console menu and producing weekly dispatch report

Name (if applicable): Bojan Petric (left half way through)
Contribution: Started with Task 3 and Task 9.

Design notes
------------
Main function boundaries: main() handles the menu and dispatches the user to the correct service. 
Each task is separated into its own function, with helper functions used for repeated logic such as quote calculations and input validation. 
Functions receive arguments and return values where appropriate instead of relying on global variables.

How input validation is organized: Validation is divided between main() and the task functions. 
try/except is used to catch invalid numeric input, while functions perform additional range and format checks. 
Invalid values produce an error message and prevent the affected calculation from continuing.
When invalid input is detected, an error message is printed and the program either uses continue to return to the menu loop or the function returns None to stop that calculation.

How shared calculations are reused: Reusable functions are used for calculations that appear in more than one task. 
For example, calculate_quote() is used both for the normal delivery quote and for comparing all three service levels in Task 9. 
This avoids duplicating the pricing formula and keeps the logic consistent. 
Therefore the program is easier to maintain, because if the quote formula changes, it only needs to be updated in one place.

Known limitations: The weekly report (option 7) requiers 7 inputs and input can't end with a ",".
-----------------
Write "None known" or describe each known limitation.
