"""
BUSINESS OUTCOME Prevent mistyped references from entering customer and
warehouse workflows.
A valid HarborFlow reference has the business format HFL-CCC-NNNN. HFL is fixed, CCC is
a three-letter customer code and NNNN is a four-digit shipment number. The user may type
lowercase letters and spaces around the input. Normalize the reference, test every rule and
print the result.
Rules
• Remove leading and trailing spaces and convert letters to uppercase.
• The normalized reference must contain exactly 12 characters.
• Positions 4 and 8 must contain hyphens.
• The customer code must contain three letters; the shipment part must contain four
digits.
• Do not use regular expressions.
Example A
Booking reference: hfl-nor-2048
Valid reference: HFL-NOR-2048
Example B
Booking reference: HFL-N4R-2048
Invalid booking reference.
EXPECTED DESIGN Implement a function such as validate_reference(reference) that
returns the normalized reference when valid and an empty string when invalid.
"""
def validate_reference(reference):
    oldRef = reference      # copy of old reference
    reference = reference.upper().strip().replace(" ", "")
    # Literally checking everything (i think), and if someting is wrong make reference an empty string
    # Maybe should make a if-block to print what is wrong with reference (only if needed or i feel like it)
    if reference[0:3] != "HFL" or reference[3] != "-" or reference[7] != "-" or reference[4:7].isalpha() == False or reference[9:12].isdigit() == False:
        reference = ""

    if len(reference) != 0:                         # If string isnt empty by this point it is valid
        print(f"Valid reference: {reference}")      #
    else:                                           # If ir is empty it is invalid
        print(f"Invalid reference: {oldRef}")       #
    return reference

if __name__ == "__main__":
    TestReference = "    hfl-no r-2048 "
    validate_reference(TestReference)
