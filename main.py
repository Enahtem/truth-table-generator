


##########################################################
# TRUTH TABLE THINGS (SEPERATE)
##########################################################

def to_binary(output_size, number):
    return [number] if output_size == 1 else to_binary(output_size - 1, number // 2) + [number % 2]

def format_statement(variables, values, statement):
    allowed_characters = variables + ["(", ")", "¬", "∧", "∨"]
    statement = "".join(char for char in statement if char in allowed_characters)
    for i in range(len(variables)):
        statement = statement.replace(variables[i], str(values[i]))
    return statement

def evaluate_not(value):
    return "1" if value == "0" else "0"

def evaluate_and(value1, value2):
    return "1" if value1 == value2 == "1" else "0"

def evaluate_or(value1, value2):
    return "1" if value1 == "1" or value2 == "1" else "0"

def evaluate(formatted_statement):
    if "(" in formatted_statement:
        start = formatted_statement.find("(")
        open_bracket_count, end = 1, start + 1
        while end < len(formatted_statement):
            if formatted_statement[end] == '(':
                open_bracket_count += 1
            elif formatted_statement[end] == ')':
                open_bracket_count -= 1
            if open_bracket_count == 0:
                break
            end += 1
        return evaluate(formatted_statement[:start] + evaluate(formatted_statement[start + 1:end]) + formatted_statement[end + 1:])
    if "¬" in formatted_statement:
        not_index = formatted_statement.find("¬")
        return evaluate(formatted_statement[:not_index] + evaluate_not(formatted_statement[not_index + 1:not_index + 2]) + formatted_statement[not_index + 2:])
    if "∧" in formatted_statement or "∨" in formatted_statement:
        operator_index = formatted_statement.find("∧") if "∧" in formatted_statement and (not "∨" in formatted_statement or formatted_statement.find("∧") < formatted_statement.find("∨")) else formatted_statement.find("∨")
        return evaluate(formatted_statement[:operator_index - 1]+(evaluate_and if formatted_statement[operator_index] == "∧" else evaluate_or)(formatted_statement[operator_index - 1:operator_index],formatted_statement[operator_index + 1:operator_index + 2])+formatted_statement[operator_index + 2:])
    return formatted_statement

def truth_table(variables, statement):
    header = "| " + " | ".join(variables) + " | S |"
    print(header)

    for i in range(2**len(variables)):
        values = to_binary(len(variables), i)
        row = "| " + " | ".join(map(str, values)) + f" | {evaluate(format_statement(variables, values, statement))} |"
        print(row)
    print()

truth_table(["a", "b", "c"], "((¬a∧b)∨c)")
truth_table(["p", "q"], "p∨q")
truth_table(["x", "y", "z"], "(x∧y)∨(z∧¬x)")
