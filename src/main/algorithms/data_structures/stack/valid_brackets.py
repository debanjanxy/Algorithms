# Bracket Matching Problem

def is_valid_brackets(brackets):
    stack = []
    for bracket in brackets:
        if is_left_bracket(bracket):
            stack.append(bracket)
        elif stack:
            top = stack.pop()
            if reverse(top) != bracket:
                return False
    return True if not stack else False

def is_left_bracket(bracket):
    left = ['(', '{', '[']            
    return True if bracket in left else False

def reverse(bracket):
    if bracket == '(':
        return ')'
    elif bracket == ')':
        return '('
    if bracket == '{':
        return '}'
    elif bracket == '}':
        return '{'
    if bracket == '[':
        return ']'
    elif bracket == ']':
        return '['

if __name__ == "__main__":
    s = "[({})]"
    print(is_valid_brackets(s))