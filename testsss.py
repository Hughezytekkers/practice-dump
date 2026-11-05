import random
from time import sleep

# Constants
SEPTEMBER2FEBURARY_ADDON = 50
REQUIRED_CHARACTERS = 7

INVALID_LETTERS = ["I", "Q", "Z"]
INVALID_FIRST_LETTERS = [
    "I",
    "J",
    "Q",
    "T",
    "U",
    "X",
    "Z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
INVALID_SECOND_LETTERS = [
    "Q",
    "I",
    "Z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
VALID_FIRST_LETTERS = "ABCDEFGHKLMNOPRSVWY"

OFFICES = [
    ["Anglia", "Peterborough", "ABCDEFGHJKLMN"],
    ["Anglia", "Norwich", "OPRSTU"],
    ["Anglia", "Ipswich", "VWXY"],
    ["Birmingham", "Birmingham", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["Cymru", "Cardiff", "ABCDEFGHJKLMNO"],
    ["Cymru", "Swansea", "PRSTUV"],
    ["Cymru", "Bangor", "WXY"],
    ["Deeside", "Chester", "ABCDEFGHJK"],
    ["Deeside", "Shrewsbury", "LMNOPRSTUVWXY"],
    ["Essex", "Chelmsford", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["Forest & Fens", "Nottingham", "ABCDEFGHJKLMNOP"],
    ["Forest & Fens", "Lincoln", "RSTUVWXY"],
    ["Garden of England", "Maidstone", "ABCDEFGHJKLMNO"],
    ["Garden of England", "Brighton", "PRSTUVWXY"],
    ["Hampshire & Dorset", "Bournemouth", "ABCDEFGHJ"],
    ["Hampshire & Dorset", "Portsmouth", "KLMNOPRSTUVXY"],
    ["Hampshire & Dorset", "Portsmouth (Isle of Wight)", "W"],
    ["(No official mnemonic)", "Luton", "ABCDEFGHJKL"],
    ["(No official mnemonic)", "Northampton", "MNOPRSTUVWXY"],
    ["London", "Wimbledon", "ABCDEFGHJ"],
    ["London", "Stanmore", "KLMNOPRST"],
    ["London", "Sidcup", "UVWXY"],
    ["Manchester", "Manchester", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["North", "Newcastle", "ABCDEFGHJKLMNO"],
    ["North", "Stockton", "PRSTUVWXY"],
    ["Oxford", "Oxford", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["Preston", "Preston", "ABCDEFGHJKLMNOPRST"],
    ["Preston", "Carlisle", "UVWXY"],
    ["Reading", "Reading", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["Scotland", "Glasgow", "ABCDEFGHJ"],
    ["Scotland", "Edinburgh", "KLMNO"],
    ["Scotland", "Dundee", "PRST"],
    ["Scotland", "Aberdeen", "UVW"],
    ["Scotland", "Inverness", "XY"],
    ["Severn Valley", "Worcester", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["West of England", "Exeter", "ABCDEFGHJ"],
    ["West of England", "Truro", "KL"],
    ["West of England", "Bristol", "MNOPRSTUVWXY"],
    ["Yorkshire", "Leeds", "ABCDEFGHJK"],
    ["Yorkshire", "Sheffield", "LMNOPRSTU"],
    ["Yorkshire", "Beverley", "VWXY"],
]

region_map = {
    "A": "Anglia",
    "B": "Birmingham",
    "C": "Cymru",
    "D": "Deeside",
    "E": "Essex",
    "F": "Forest & Fens",
    "G": "Garden of England",
    "H": "Hampshire & Dorset",
    "K": "(No official mnemonic)",
    "L": "London",
    "M": "Manchester",
    "N": "North",
    "O": "Oxford",
    "P": "Preston",
    "R": "Reading",
    "S": "Scotland",
    "V": "Severn Valley",
    "W": "West of England",
    "Y": "Yorkshire",
}

test_licence_plates = [
    # 1 - 41: Valid Regional Office Plates
    "AB 21 BTR",
    "AO 55 KLM",
    "AV 71 XYW",
    "BA 20 CDE",
    "CA 60 FGH",
    "CP 15 JKL",
    "CW 02 MNO",
    "DA 19 PRS",
    "DL 68 TUV",
    "EA 08 WXY",
    "FA 22 ABC",
    "FR 72 DEF",
    "GA 11 GHJ",
    "GP 61 KLM",
    "HA 05 NOP",
    "HK 55 RST",
    "HW 20 UVW",
    "KA 69 XYA",
    "KM 14 BCD",
    "LA 03 EFG",
    "LK 53 HJK",
    "LU 18 LMN",
    "MA 23 OPW",
    "NA 73 RST",
    "NP 12 UVW",
    "OA 62 EFG",
    "PA 07 HJK",
    "PU 57 LMN",
    "RA 21 OPR",
    "SA 09 STU",
    "SK 59 VWX",
    "SP 16 YAB",
    "SU 66 CDE",
    "SX 04 FGH",
    "VA 24 JKL",
    "WA 74 MNO",
    "WK 13 PRS",
    "WM 63 TUV",
    "YA 10 WXY",
    "YL 60 ABC",
    "YV 11 DEF",
    # 42 - 50: Age Identifiers & Cycles
    "AB 51 BTR",
    "AB 02 BTR",
    "AB 52 BTR",
    "AB 26 BTR",
    "AB 76 BTR",
    "AB 30 BTR",
    "AB 80 BTR",
    "AB 99 BTR",
    "AB 50 BTR",
    # 51 - 62: Length, Whitespace & Tag Boundaries
    "AB21BTR",
    "AB21BTR",
    "AB21BT",
    "AB21BTRS",
    "",
    "A",
    "  AB21BTR  ",
    "AB 00 BTR",
    "AB 01 BTR",
    "AM 21 BTR",
    "AY 21 BTR",
    "BI 21 BTR",
    # 63 - 80: Invalid Letters & Exclusions
    "IB 21 BTR",
    "JB 21 BTR",
    "QB 21 BTR",
    "TB 21 BTR",
    "UB 21 BTR",
    "XB 21 BTR",
    "ZB 21 BTR",
    "1B 21 BTR",
    "AI 21 BTR",
    "AQ 21 BTR",
    "AZ 21 BTR",
    "A2 21 BTR",
    "AB 21 ITR",
    "AB 21 BQR",
    "AB 21 BTZ",
    "AB 21 IQZ",
    "AZ 21 BTR",
    "JA 21 BTR",
    # 81 - 86: Custom & Non-Standard Format Rejections
    "A1",
    "VIP 1",
    "1 ABC",
    "ABC 123D",
    "A123 ABC",
    "IJZ 1234",
    # 87 - 100: Erroneous Inputs & Formatting
    "@B 21 BTR",
    "A# 21 BTR",
    "AB %$ BTR",
    "AB 21 BT!",
    "AB XX BTR",
    "1234567",
    "$%&*(@!",
    "FIFTEEN",
    "BTR 21 AB",
    "AB\t21\tBTR",
    "AB\n21\nBTR",
    "ÁB 21 BTR",
    "ab 21 bTr",
    "A B 2 1 B T R",
]


def strip_spaces(s):
    return s.replace(" ", "").replace("\t", "").replace("\n", "")


def check_plate_age(clean_plate):
    if len(clean_plate) < 4:
        return "Invalid length for age check"

    age = clean_plate[2:4]
    if not age.isdigit():
        return "Age identifier must be two digits"

    age_code = int(age)
    if 1 <= age_code <= 50:
        year = 2000 + age_code
        return f"Registered 1 March {year} - 31 August {year}"
    elif 51 <= age_code <= 76:
        start_year = 2000 + (age_code - SEPTEMBER2FEBURARY_ADDON)
        return f"Registered 1 Sept {start_year} - 28/29 Feb {start_year + 1}"
    else:
        return "Unrecognised age identifier"


def check_plate_location(clean_plate):
    if len(clean_plate) < 2:
        return "Invalid length for location check"

    first_letter = clean_plate[0]
    second_letter = clean_plate[1]
    target_region = region_map.get(first_letter)

    if not target_region:
        return f"Unknown region '{first_letter}'"

    for row in OFFICES:
        if row[0] == target_region and second_letter in row[2]:
            return f"Region: {row[0]}, Office: {row[1]}"

    return f"Unknown office for '{first_letter}{second_letter}'"


def validate_license_plate(raw_plate):
    clean_plate = strip_spaces(raw_plate).upper()

    if len(clean_plate) != REQUIRED_CHARACTERS:
        return False, f"Invalid length ({len(clean_plate)} chars)"

    first_letter = clean_plate[0]
    second_letter = clean_plate[1]
    last_three = clean_plate[4:]

    if (
        first_letter in INVALID_FIRST_LETTERS
        or first_letter not in VALID_FIRST_LETTERS
    ):
        return False, f"Invalid first letter '{first_letter}'"

    if second_letter in INVALID_SECOND_LETTERS:
        return False, f"Invalid second letter '{second_letter}'"

    for char in last_three:
        if not char.isalpha():
            return False, f"Non-alphabetic character '{char}'"
        if char in INVALID_LETTERS:
            return False, f"Forbidden letter '{char}'"

    age_res = check_plate_age(clean_plate)
    if "Registered" not in age_res:
        return False, age_res

    loc_res = check_plate_location(clean_plate)
    if "Region:" not in loc_res:
        return False, loc_res

    return True, f"Valid ({loc_res} | {age_res})"


def run_all_test_plates():
    print("\n" + "=" * 80)
    print(
        f"{'#':<4} | {'Input Plate':<18} | {'Status':<6} | Reason / Location & Age"
    )
    print("=" * 80)

    passed, failed = 0, 0
    for idx, plate in enumerate(test_licence_plates, 1):
        is_valid, reason = validate_license_plate(plate)
        status = "PASS" if is_valid else "FAIL"

        if is_valid:
            passed += 1
        else:
            failed += 1

        display = repr(plate) if ("\t" in plate or "\n" in plate) else f'"{plate}"'
        print(f"{idx:<4} | {display:<18} | {status:<6} | {reason}")

    print("=" * 80)
    print(
        f"TOTAL: {len(test_licence_plates)} | PASSED: {passed} | FAILED: {failed}"
    )
    print("=" * 80 + "\n")


def generate_license_plate():
    first_letter = random.choice(list(region_map.keys()))
    region = region_map[first_letter]

    possible_second_letters = "".join(
        row[2] for row in OFFICES if row[0] == region
    )
    second_letter = random.choice(possible_second_letters)

    age = random.randint(2, 26) + random.choice([0, SEPTEMBER2FEBURARY_ADDON])
    age_str = f"{age:02d}"

    alphabet = "".join(c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if c not in INVALID_LETTERS)
    last_three = "".join(random.choice(alphabet) for _ in range(3))

    return f"{first_letter}{second_letter} {age_str} {last_three}"


# Main Loop
quitChoice = False
user_plate = "AB 21 BTR"

while not quitChoice:
    sleep(0.5)
    print(f"\nCurrent active plate: {user_plate}")
    print("1. Run all 100 test plates")
    print("2. Check the active licence plate")
    print("3. Output car's age for active plate")
    print("4. Output location for active plate")
    print("5. Generate a new valid licence plate")
    print("6. Change active plate")
    print("7. Quit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        run_all_test_plates()
    elif choice == "2":
        is_valid, reason = validate_license_plate(user_plate)
        print(f"Plate: {user_plate} -> {'VALID' if is_valid else 'INVALID'}: {reason}")
    elif choice == "3":
        print(check_plate_age(strip_spaces(user_plate).upper()))
    elif choice == "4":
        print(check_plate_location(strip_spaces(user_plate).upper()))
    elif choice == "5":
        new_p = generate_license_plate()
        print(f"Generated: {new_p}")
        user_plate = new_p
    elif choice == "6":
        user_plate = input("Enter custom plate: ").strip()
    elif choice in ["7", "Q", "q"]:
        print("Quitting program...")
        quitChoice = True
    else:
        print("Invalid option, try again.")