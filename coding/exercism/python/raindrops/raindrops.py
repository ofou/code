def convert(number):

    factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }

    sounds = [v for (k, v) in factors.items() if number % k == 0]

    return str(number) if not sounds else "".join(sounds)
