all_hints = ["1 . Is it divisble by 6?",
             "2 . Is it divisble by 2?",
             "3 . Is it multiple by 15?",
             "4 . Is it multiple by 21?",
             "5 . Is it multiple by 8?"]


def hint(number, n_hint):
    if n_hint != 0:
        need = input(
            f"\nDo you want a hint ? Hints remaining {n_hint}\n Type 'yes' or 'no' : ").lower()
        if need == 'yes':
            n_hint -= 1
            print("\n".join(all_hints))
            hint_number = int(input(
                "Give The index of the hint you want to take \nType '1' '2' '3' '4' or '5' : "))
            if (hint_number == 1 and number % 6 == 0) or (hint_number == 2 and number % 2 == 0) or (hint_number == 3 and number % 3 == 0 and number % 5 == 0) or (hint_number == 4 and number % 3 == 0 and number % 7 == 0) or (hint_number == 5 and number % 4 == 0 and number % 8 == 0):
                return ("Yes\n\n", "yes")
            return ("no\n", "yes")
        elif need == "no":
            return (f"Hints remaining {n_hint}\n", "no")
        else:
            return ("Invalid Choice.")
    else:
        need = input(
            f"\nDo you want a hint ? Hints remaining {n_hint}\n Type 'yes' or 'no' : ").lower()
        return (f"Sorry .... Hints remaining {n_hint}\n\n", "no")
