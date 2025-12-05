def prompt_and_validate(prompt, expected_type):
    """
    Prompt user to enter correctly formatted data for
    the expected type until it's correct. Uses exception handling.
    """
    while True:  # keep looping until they do it right
        value = input(prompt)

        try:
            if expected_type == "String":
                result = value.strip()
                if not result:
                    raise ValueError("String input cannot be empty.")
                return result

            elif expected_type == "Integer":
                try:
                    result = int(str(value).strip())
                except (TypeError, ValueError):
                    raise ValueError("Integer input must be a whole number.")
                if result <= 0:
                    raise ValueError("Integer input must be > 0.")
                return result

            elif expected_type == "URL":
                result = value.strip()
                if not result:
                    raise ValueError("URL input cannot be empty.")
                if not result.startswith(("http://", "https://")):
                    raise ValueError("URL must start with http:// or https://")
                if "." not in result or result.endswith("."):
                    raise ValueError("URL must contain a valid domain ending (.com).")
                return result

        except ValueError as e:
            print(e)
