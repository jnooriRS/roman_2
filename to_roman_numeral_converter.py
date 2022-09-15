import click


def to_roman_numeral(arabic_number) -> str:
    # Extend key value pair to allow for speical case where smaller character can be minused.
    # In a list to loop thourgh in reversed order
    roman_table = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000],
    ]
    result = ""
    # Simple for loop that iterable from largest key to smallest
    # Divide user input with vlaue- if there is a remainder carry over and divese again
    for roman_symbol, value in reversed(roman_table):
        if arabic_number // value:
            count = arabic_number // value
            # create a string copy which is appended to string
            result += roman_symbol * count
            # Move onto next value in the roman_table
            arabic_number = arabic_number % value
    return result
    # print(result)


@click.command()
@click.option("--arabic_number", prompt="Integer you want to convert", type=int)
def to_roman_numeral_cli(arabic_number):
    return to_roman_numeral(arabic_number)


if __name__ == "__main__":
    print(to_roman_numeral(to_roman_numeral_cli))
    print(to_roman_numeral_cli())
