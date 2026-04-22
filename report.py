class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = Stack()
    postfix = ""
    
    for char in expression:
        
        if char.isalnum():
            postfix += char
        
       
        elif char == '(':
            stack.push(char)
        
       
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()  # remove '('
        
        
        else:
            while (not stack.is_empty() and 
                   precedence(char) <= precedence(stack.peek())):
                postfix += stack.pop()
            stack.push(char)

    
    while not stack.is_empty():
        postfix += stack.pop()

    return postfix



def evaluate_postfix(expression):
    stack = Stack()

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            val2 = stack.pop()
            val1 = stack.pop()

            if char == '+':
                stack.push(val1 + val2)
            elif char == '-':
                stack.push(val1 - val2)
            elif char == '*':
                stack.push(val1 * val2)
            elif char == '/':
                stack.push(val1 / val2)
            elif char == '^':
                stack.push(val1 ** val2)

    return stack.pop()



def main():
    while True:
        print("\n===== Expression Conversion & Evaluation Tool =====")
        print("1. Infix to Postfix")
        print("2. Evaluate Postfix")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            infix = input("Enter Infix Expression: ")
            postfix = infix_to_postfix(infix)
            print("Postfix Expression:", postfix)

        elif choice == '2':
            postfix = input("Enter Postfix Expression: ")
            result = evaluate_postfix(postfix)
            print("Result:", result)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")



if __name__ == "__main__":
    main()