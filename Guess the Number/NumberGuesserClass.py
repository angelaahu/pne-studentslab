class NumberGuesser:
    def __init__(self, secret_number = None, attempts = None):
        self.secret_number = secret_number
        self.attempts = attempts

    def guess(self, number):
        count = 0
        if number != secret_numer:
            count += 1
        if number == secret_number:
            result = f"You won after {count} attempts"
        elif number > secret_number:
            result = "Lower"
        elif number < secret_number:
            result = "Higher"

        return result

    def __str__(self):
        return self.attempts



