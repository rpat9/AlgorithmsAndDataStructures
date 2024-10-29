from stack_list import Stack, Empty

def eval_expr(expression):
    """
    This function evaluates an arithmetic expression using a stack. The expression can contain digits and the operators '+' and '-'.
    The '+' and '-' operators have the same precedence and the expression is evaluated from left to right.
 
    Parameters:
    expression (str): The arithmetic expression to evaluate. The expression can contain digits (0-9) and the operators '+' and '-'.
 
    Returns:
    int: The result of the arithmetic expression.
    """
    
    # Initialize the stacks
    
    stackNumbers = Stack()
    stackOperators = Stack()
    
    # Parse the expression.
    # If the character is a digit, accumulate it in a string for multi-digit numbers.
    # If the character is an operator, push the accumulated number to the number stack, and push the operator to the operator stack.
    
    number = ''
    for char in expression:
        if char.isdigit():
            number+=char
        if char in ['+', '-']:
            stackNumbers.push(int(number))
            stackOperators.push(char)
            number = ''    
    
    # Push the last accumulated number onto the number stack.
    stackNumbers.push(int(number))
 
    # Reverse the stacks
    tempStackNumbers = Stack()
    tempStackOperators = Stack()
    
    while not stackNumbers.is_empty():
        tempStackNumbers.push(stackNumbers.pop())
        
    while not stackOperators.is_empty():
        tempStackOperators.push(stackOperators.pop())
    
    # Initialize the result with the first number from the reversed number stack.
    result = tempStackNumbers.pop()
    
    # Perform the operations.
    
    while not tempStackOperators.is_empty():
        op = tempStackOperators.pop()
        num = tempStackNumbers.pop()
        
        if op == '+':
            result += num
        elif op == '-':
            result -= num
    
    return result  



if __name__ == '__main__':
    expression = "1+2"
    print(eval_expr(expression))  # 3
    expression = "1+2-3"
    print(eval_expr(expression))  # 0
    expression = "1+2-3+4-5"
    print(eval_expr(expression))  # -1