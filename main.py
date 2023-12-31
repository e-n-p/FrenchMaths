import random

DATA = {
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
    10: "dix",
    11: "onze",
    12: "douze",
    13: "treize",
    14: "quatorze",
    15: "quinze ",
    16: "seize",
    17: "dix-sept",
    18: "dix-huit",
    19: "dix-neuf",
    20: "vingt",
    21: "vingt et un",
    22: "vingt-deux",
    23: "vingt-trois",
    24: "vingt-quatre",
    25: "vingt-cinq",
    26: "vingt-six",
    27: "vingt-sept",
    28: "vingt-huit",
    29: "vingt-neuf",
    30: "trente",
    31: "trente et un",
    32: "trente-deux",
    33: "trente-trois",
    34: "trente-quatre",
    35: "trente-cinq",
    36: "trente-six",
    37: "trente-sept",
    38: "trente-huit",
    39: "trente-neuf",
    40: "quarante",
    41: "quarante et un",
    42: "quarante-deux",
    43: "quarante-trois",
    44: "quarante-quatre",
    45: "quarante-cinq",
    46: "quarante-six",
    47: "quarante-sept",
    48: "quarante-huit",
    49: "quarante-neuf",
    50: "cinquante",
    51: "cinquante et un",
    52: "cinquante-deux",
    53: "cinquante-trois",
    54: "cinquante-quatre",
    55: "cinquante-cinq",
    56: "cinquante-six",
    57: "cinquante-sept",
    58: "cinquante-huit",
    59: "cinquante-neuf",
    60: "soixante",
    61: "soixante et un",
    62: "soixante-deux",
    63: "soixante-trois",
    64: "soixante-quatre",
    65: "soixante-cinq",
    66: "soixante-six",
    67: "soixante-sept",
    68: "soixante-huit",
    69: "soixante-neuf",
    70: "soixante-dix",
    71: "soixante et onze",
    72: "soixante-douze",
    73: "soixante-treize",
    74: "soixante-quatorze",
    75: "soixante-quinze",
    76: "soixante-seize",
    77: "soixante-dix-sept",
    78: "soixante-dix-huit",
    79: "soixante-dix-neuf",
    80: "quatre-vingts",
    81: "quatre-vingt-un",
    82: "quatre-vingt-deux",
    83: "quatre-vingt-trois",
    84: "quatre-vingt-quatre",
    85: "quatre-vingt-cinq",
    86: "quatre-vingt-six",
    87: "quatre-vingt-sept",
    88: "quatre-vingt-huit",
    89: "quatre-vingt-neuf",
    90: "quatre-vingt-dix",
    91: "quatre-vingt-onze",
    92: "quatre-vingt-douze",
    93: "quatre-vingt-treize",
    94: "quatre-vingt-quatorze",
    95: "quatre-vingt-quinze",
    96: "quatre-vingt-seize",
    97: "quatre-vingt-dix-sept",
    98: "quatre-vingt-dix-huit",
    99: "quatre-vingt-dix-neuf",
    100: "cent",
    101: "cent un",
    102: "cent deux",
    103: "cent trois",
    104: "cent quatre",
    105: "cent cinq",
    106: "cent six",
    107: "cent sept",
    108: "cent huit",
    109: "cent neuf",
    110: "cent dix",
    111: "cent onze",
    112: "cent douze",
    113: "cent treize",
    114: "cent quatorze",
    115: "cent quinze ",
    116: "cent seize",
    117: "cent dix-sept",
    118: "cent dix-huit",
    119: "cent dix-neuf",
    120: "cent vingt",
    121: "cent vingt et un",
    122: "cent vingt-deux",
    123: "cent vingt-trois",
    124: "cent vingt-quatre",
    125: "cent vingt-cinq",
    126: "cent vingt-six",
    127: "cent vingt-sept",
    128: "cent vingt-huit",
    129: "cent vingt-neuf",
    130: "cent trente",
    131: "cent trente et un",
    132: "cent trente-deux",
    133: "cent trente-trois",
    134: "cent trente-quatre",
    135: "cent trente-cinq",
    136: "cent trente-six",
    137: "cent trente-sept",
    138: "cent trente-huit",
    139: "cent trente-neuf",
    140: "cent quarante",
    141: "cent quarante et un",
    142: "cent quarante-deux",
    143: "cent quarante-trois",
    144: "cent quarante-quatre",
    145: "cent quarante-cinq",
    146: "cent quarante-six",
    147: "cent quarante-sept",
    148: "cent quarante-huit",
    149: "cent quarante-neuf",
    150: "cent cinquante",
    151: "cent cinquante et un",
    152: "cent cinquante-deux",
    153: "cent cinquante-trois",
    154: "cent cinquante-quatre",
    155: "cent cinquante-cinq",
    156: "cent cinquante-six",
    157: "cent cinquante-sept",
    158: "cent cinquante-huit",
    159: "cent cinquante-neuf",
    160: "cent soixante",
    161: "cent soixante et un",
    162: "cent soixante-deux",
    163: "cent soixante-trois",
    164: "cent soixante-quatre",
    165: "cent soixante-cinq",
    166: "cent soixante-six",
    167: "cent soixante-sept",
    168: "cent soixante-huit",
    169: "cent soixante-neuf",
    170: "cent soixante-dix",
    171: "cent soixante et onze",
    172: "cent soixante-douze",
    173: "cent soixante-treize",
    174: "cent soixante-quatorze",
    175: "cent soixante-quinze",
    176: "cent soixante-seize",
    177: "cent soixante-dix-sept",
    178: "cent soixante-dix-huit",
    179: "cent soixante-dix-neuf",
    180: "cent quatre-vingts",
    181: "cent quatre-vingt-un",
    182: "cent quatre-vingt-deux",
    183: "cent quatre-vingt-trois",
    184: "cent quatre-vingt-quatre",
    185: "cent quatre-vingt-cinq",
    186: "cent quatre-vingt-six",
    187: "cent quatre-vingt-sept",
    188: "cent quatre-vingt-huit",
    189: "cent quatre-vingt-neuf",
    190: "cent quatre-vingt-dix",
    191: "cent quatre-vingt-onze",
    192: "cent quatre-vingt-douze",
    193: "cent quatre-vingt-treize",
    194: "cent quatre-vingt-quatorze",
    195: "cent quatre-vingt-quinze",
    196: "cent quatre-vingt-seize",
    197: "cent quatre-vingt-dix-sept",
    198: "cent quatre-vingt-dix-huit",
    199: "cent quatre-vingt-dix-neuf",
    200: "deux cent",
}


def write_a_number():
    goal = random.randint(2, 200)
    response = input(f"\nWhat is {goal} in french?\n")
    if response == DATA[goal]:
        print("Correct!")
    else:
        print("Wrong")
        print(f"The answer was {DATA[goal]}")


def simple_math():
    goal = random.randint(2, 200)
    delta = random.randint(1, goal)
    answer = goal - delta
    response = input(f"\nWhat is (?) + {DATA[delta]} = {DATA[goal]}\n")
    if response == DATA[answer]:
        print("Correct!")
    else:
        print("Wrong")
        print(f"The answer was {DATA[answer]}")


def ask_for_number():
    response = int(input("\nWhich french number would you like to see? Between 1 and 200\n"))
    print(DATA[response])


def main():
    game = 0
    try:
        game = int(input(
            """What game would you like to play? 
                1= Write out the given number in French,
                2= Solve a simple math question in French,
                3= Ask how to write a number in French
           """))
    except ValueError:
        print("Not a valid choice")

    match game:
        case 1:
            for n in range(5):
                write_a_number()
        case 2:
            for n in range(5):
                simple_math()
        case 3:
            for n in range(5):
                ask_for_number()
        case _:
            print("Pick a valid number next time")


if __name__ == "__main__":
    main()
