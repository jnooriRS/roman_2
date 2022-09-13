import click


@click.command()
@click.option("--arabic_number", prompt="Integer you want to convert", type=int)
def to_roman_numeral(arabic_number) -> str:
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
    for roman_symbol, value in reversed(roman_table):
        if arabic_number // value:
            count = arabic_number // value
            result += roman_symbol * count
            arabic_number = arabic_number % value
    print(result)


if __name__ == "__main__":
    print(to_roman_numeral())
