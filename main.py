from utils import to_twos_comp, to_str, value
from subtractor import four_bit_subtractor, test

def main():
    print("Eric Reed - HW 12 (Subtraction is Addition) Demo Code")
    while True:
        menu_option = input("a(utomatic) test, m(anual) test, q(uit): ")
        menu_option = menu_option.strip().lower()
        if menu_option not in "amq":
            print("Invalid option")
            continue
        if menu_option == "q": break

        if menu_option == "a":
            test()
            print("Automatic tests passed")
            continue

        # menu_option == "m"
        print("Format: A - B")
        print("Both numbers must be in [-8, 8) range")
        while True:
            try:
                a = int(input("Enter number for A: "))
                assert a in range(-8, 8)
                break
            except ValueError:
                print("Not a number")
            except AssertionError:
                print("Out of range")
        while True:
            try:
                b = int(input("Enter number for B: "))
                assert b in range(-8, 8)
                break
            except ValueError:
                print("Not a number")
            except AssertionError:
                print("Out of range")
        print(f"Calculating {a} - {b}")
        a_twos_comp = to_twos_comp(a)
        b_twos_comp = to_twos_comp(b)
        print(f"In two's complement, calculating {to_str(a_twos_comp)} - {to_str(b_twos_comp)}")

        result = four_bit_subtractor(*a_twos_comp, *b_twos_comp)
        result_num = result[0:4]
        result_overflow = result[4]
        if (a - b) not in range(-8, 8):
            assert result_overflow
            print("Overflow detected successfully")
        else:
            assert not result_overflow
            assert value(result_num) == (a - b)
            result_val = value(result_num)
            print(f"Result is {to_str(result_num)} in two's complement, or {result_val}")
            print(f"{a} - {b} = {result_val}")

        print("Test passed")

if __name__ == "__main__":
    main()
