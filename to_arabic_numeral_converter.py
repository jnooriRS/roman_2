import click


def to_arabic_number(roman):
    # largest to smallest- add them up
    # smallest to largest- minus them
    roman_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    # Does the numeral have a value after it, if so is it greatrer or less than?
    for numeral in range(len(roman)):
        if (
            numeral + 1 < len(roman)
            and roman_table[roman[numeral]] < roman_table[roman[numeral + 1]]
        ):
            result -= roman_table[roman[numeral]]
        else:
            result += roman_table[roman[numeral]]
    # Return the result with the value
    return result


@click.command()
# @click.argument("roman_numeral")
@click.option("--roman", prompt="Roman numeral to convert please", type=str)
def to_arabic_number_cli(roman):
    print("hello-world")
    result = to_arabic_number(roman)
    print(result)
    # return result


if __name__ == "__main__":
    to_arabic_number_cli()
