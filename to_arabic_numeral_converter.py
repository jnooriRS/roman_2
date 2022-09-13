import click


def to_arabic_number(roman) -> int:
    roman_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for numeral in range(len(roman)):
        if (
            numeral + 1 < len(roman)
            and roman_table[roman[numeral]] < roman_table[roman[numeral + 1]]
        ):
            result -= roman_table[roman[numeral]]
        else:
            result += roman_table[roman[numeral]]

    return result


@click.command()
@click.argument("roman_numeral")
@click.option("--roman", prompt="Roman numeral to convert please", type=str)
def to_arabic_number_cli(roman):
    return to_arabic_number(roman)


if __name__ == "__main__":
    print(to_arabic_number())
