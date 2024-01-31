import random

DATA = {
    "1": "un",
    "2": "deux",
    "3": "trois",
    "4": "quatre",
    "5": "cinq",
    "6": "six",
    "7": "sept",
    "8": "huit",
    "9": "neuf",
    "10": "dix",
    "11": "onze",
    "12": "douze",
    "13": "treize",
    "14": "quatorze",
    "15": "quinze ",
    "16": "seize",
    "17": "dix-sept",
    "18": "dix-huit",
    "19": "dix-neuf",
    "20": "vingt",
    "21": "vingt et un",
    "22": "vingt-deux",
    "23": "vingt-trois",
    "24": "vingt-quatre",
    "25": "vingt-cinq",
    "26": "vingt-six",
    "27": "vingt-sept",
    "28": "vingt-huit",
    "29": "vingt-neuf",
    "30": "trente",
    "31": "trente et un",
    "32": "trente-deux",
    "33": "trente-trois",
    "34": "trente-quatre",
    "35": "trente-cinq",
    "36": "trente-six",
    "37": "trente-sept",
    "38": "trente-huit",
    "39": "trente-neuf",
    "40": "quarante",
    "41": "quarante et un",
    "42": "quarante-deux",
    "43": "quarante-trois",
    "44": "quarante-quatre",
    "45": "quarante-cinq",
    "46": "quarante-six",
    "47": "quarante-sept",
    "48": "quarante-huit",
    "49": "quarante-neuf",
    "50": "cinquante",
    "51": "cinquante et un",
    "52": "cinquante-deux",
    "53": "cinquante-trois",
    "54": "cinquante-quatre",
    "55": "cinquante-cinq",
    "56": "cinquante-six",
    "57": "cinquante-sept",
    "58": "cinquante-huit",
    "59": "cinquante-neuf",
    "60": "soixante",
    "61": "soixante et un",
    "62": "soixante-deux",
    "63": "soixante-trois",
    "64": "soixante-quatre",
    "65": "soixante-cinq",
    "66": "soixante-six",
    "67": "soixante-sept",
    "68": "soixante-huit",
    "69": "soixante-neuf",
    "70": "soixante-dix",
    "71": "soixante et onze",
    "72": "soixante-douze",
    "73": "soixante-treize",
    "74": "soixante-quatorze",
    "75": "soixante-quinze",
    "76": "soixante-seize",
    "77": "soixante-dix-sept",
    "78": "soixante-dix-huit",
    "79": "soixante-dix-neuf",
    "80": "quatre-vingts",
    "81": "quatre-vingt-un",
    "82": "quatre-vingt-deux",
    "83": "quatre-vingt-trois",
    "84": "quatre-vingt-quatre",
    "85": "quatre-vingt-cinq",
    "86": "quatre-vingt-six",
    "87": "quatre-vingt-sept",
    "88": "quatre-vingt-huit",
    "89": "quatre-vingt-neuf",
    "90": "quatre-vingt-dix",
    "91": "quatre-vingt-onze",
    "92": "quatre-vingt-douze",
    "93": "quatre-vingt-treize",
    "94": "quatre-vingt-quatorze",
    "95": "quatre-vingt-quinze",
    "96": "quatre-vingt-seize",
    "97": "quatre-vingt-dix-sept",
    "98": "quatre-vingt-dix-huit",
    "99": "quatre-vingt-dix-neuf",
    "100": "cent",
    "1000": "mille",
}


def number_builder(number, start=1, end=1000):
    lexical_number = ""
    if not number:
        number = random.randint(start, end)

    str_num = str(number)
    index = len(str_num)
    for n in str_num:
        if index == 4:
            lexical_number += DATA["1000"] + " "
        if index == 3:
            if n != "0" and n != "1":
                lexical_number += DATA[n] + " " + DATA["100"] + " "
            elif n == "1":
                lexical_number += DATA["100"] + " "
        if index == 2:
            if n != "0":
                n += str_num[-1]
                lexical_number += DATA[n]
                break
        if index == 1 and n != "0":
            lexical_number += DATA[n]
        index -= 1
    return lexical_number


def write_a_number():
    goal = random.randint(1, 1000)
    response = input(f"\nWhat is {goal} in french?\n")
    correct_answer = number_builder(goal)
    if response == correct_answer:
        print("Correct!")
    else:
        print("Wrong")
        print(f"The answer was {correct_answer}")


def simple_math():
    goal = random.randint(2, 1000)
    delta = random.randint(1, goal)
    answer = goal - delta
    response = input(f"\nWhat is (?) + {number_builder(delta)} = {number_builder(goal)}\n")
    correct_answer = number_builder(answer)
    if response == correct_answer:
        print("Correct!")
    else:
        print("Wrong")
        print(f"The answer was {correct_answer}")


def ask_for_number():
    response = int(input("\nWhich french number would you like to see? Between 1 and 1000\n"))
    print(number_builder(response))


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