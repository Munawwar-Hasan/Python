# Fix and regenerate the detailed PDF

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("./bit_packing_master_guide.pdf")
styles = getSampleStyleSheet()

content = []

def title(text):
    content.append(Paragraph(f"<b>{text}</b>", styles["Title"]))
    content.append(Spacer(1,20))

def section(title_text, body):
    content.append(Paragraph(f"<b>{title_text}</b>", styles["Heading2"]))
    content.append(Spacer(1,10))
    content.append(Paragraph(body, styles["BodyText"]))
    content.append(Spacer(1,12))

def code_block(text):
    content.append(Preformatted(text, styles["Code"]))
    content.append(Spacer(1,12))

# Title
title("Bit Packing — Super Detailed Guide (Kid Friendly)")

section("1. What is the Goal?",
        "We want to store multiple numbers inside ONE number. "
        "We do this using binary (0 and 1). Think of it like packing things into a box.")

section("2. Binary Basics",
        "Every number in a computer is stored in binary.\n"
        "Example:\n"
        "1 = 1\n2 = 10\n3 = 11\n4 = 100\n5 = 101\n15 = 1111")

section("3. VERY IMPORTANT Example: 15 << 7",
        "We will break this step by step below.")

code_block("""Step 1: Convert to binary
15 = 1111

Step 2: Shift left by 7
Add 7 zeros:

1111 << 7 = 1111 0000000

Step 3: Final binary
11110000000

Step 4: Convert to decimal
= 1×2^10 + 1×2^9 + 1×2^8 + 1×2^7
= 1024 + 512 + 256 + 128
= 1920

FINAL:
15 << 7 = 1920""")

section("4. Right Shift Example: 15 >> 2",
        "Now we move bits to the right.")

code_block("""Step 1:
15 = 1111

Step 2:
1111 >> 2 = remove last 2 bits = 11

Step 3:
11 = 3

FINAL:
15 >> 2 = 3""")

section("5. Packing Two Numbers",
        "We combine two numbers into one.")

code_block("""region_id = 3
user_id = 25

Step 1:
3  = 00000011
25 = 00011001

Step 2:
3 << 8 = 00000011 00000000

Step 3: OR
00000011 00000000
|00000000 00011001
------------------
 00000011 00011001

Step 4:
= 793""")

section("6. Extract user_id",
        "Use AND with mask.")

code_block("""combined = 00000011 00011001
mask     = 00000000 11111111

AND:
= 00000000 00011001 = 25""")

section("7. Extract region_id",
        "Use right shift.")

code_block("""00000011 00011001 >> 8
= 00000011
= 3""")

section("8. Why (1 << n) - 1",
        "This creates n number of 1s.")

code_block("""Example: n = 5

1 << 5 = 100000
minus 1:
100000
-     1
------
011111

= 31""")

section("9. Character Example",
        "Characters are numbers inside computers.")

code_block("""'A' = 65 = 01000001

Step:
65 << 8 = 01000001 00000000
OR 5:
= 01000001 00000101

Decode:
>> 8 → 65 → 'A'""")

section("10. String Example",
        "Pack two characters.")

code_block("""'H' = 72 = 01001000
'i' = 105 = 01101001

Pack:
01001000 << 8 = 01001000 00000000
OR:
= 01001000 01101001

Decode:
last 8 bits → i
shift >> 8 → H""")

section("11. Golden Rule",
        "<< = make space, | = fill, >> = bring back, & = extract exact bits")

doc.build(content)

"./bit_packing_master_guide.pdf"