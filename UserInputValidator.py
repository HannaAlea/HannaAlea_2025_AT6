class UserInputValidator:
    def validate_positive_integers(self, items):
        """
        Accepts a list of strings.
        Returns a list of valid positive integers.
        """
        valid_numbers = []

        for s in items:
            if s.isdigit():
                num = int(s)
                if num > 0:
                    valid_numbers.append(num)

        # show a message when a list is validated
        self.display_message("List validation complete.")

        return valid_numbers

    def display_message(self, message):
        print(message)