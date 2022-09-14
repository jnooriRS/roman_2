from pickle import APPEND
from flask import Flask
from flask import render_template, request

app = Flask(__name__)


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
        arabic_number_int = int(arabic_number)
        if arabic_number_int // value:
            count = arabic_number_int // value
            result += roman_symbol * count
            arabic_number = arabic_number_int % value
    return result


@app.route("/roman/", methods=["POST", "GET"])
def roman_converter():
    if request.method == "POST":
        arabic_user_input = request.form["number"]
        return render_template(
            "result.html",
            number_decimal=arabic_user_input,
            number_roman=to_roman_numeral(arabic_user_input),
        )
    else:
        return render_template("roman.html", not_valid=False)


def to_arabic_number(roman):
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


@app.route("/arabic/", methods=["POST", "GET"])
def arabic_converter():
    if request.method == "POST":
        user_input = request.form["number"]
        return render_template(
            "result.html",
            number_decimal=user_input,
            number_roman=to_arabic_number(user_input),
        )
    else:
        return render_template("arabic.html", not_valid=False)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
