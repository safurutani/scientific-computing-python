def arithmetic_arranger(problems, solution = None):
    #setting up the bones of the format
    line1 = ""
    line2 = "\n"
    line3 = "\n"
    line4 = "\n"

    #formatting the spaces
    between_probs = "    "
    buffer = " "

    #check for initial problem number error
    if len(problems) > 5:
      #raise Exception('Error: Too many problems.')
      return "Error: Too many problems."
    nonDigit = "abcdefghijklmnopqrstuvwxyz"
    arranged_problems = ""

    #goes through each math problem provided and separates it into 4 components
    for prob in problems:
        #check if numbers are 4 digits or less
        num1 = prob[0:prob.index(" ")]
        num2 = prob[prob.index(" ") + 3:]

      #check for correct digits
        for char in nonDigit:
           for i in prob:
              if i == char:
                return "Error: Numbers must only contain digits."
        if int(num1) > 9999 or int(num1) < -9999: 
          return "Error: Numbers cannot be more than four digits."
        if int(num2) > 9999 or int(num2) < -9999: 
          return "Error: Numbers cannot be more than four digits."

        #check what the operator is and if it's valid
        operation = prob[prob.index(" ") + 1]
        if operation == "+":
            answer = int(num1) + int(num2)
        elif operation == "-":
            answer = int(num1) - int(num2)
        else:
          return "Error: Operator must be '+' or '-'."

        #find the bigger number for formatting purposes
        bigger = num1
        if int(num2) > int(num1): bigger = num2

        #final formatting
        line1 += buffer * (len(bigger) + 2 - len(num1)) + num1
        line2 += operation + buffer * (len(bigger) + 1 - len(num2)) + num2
        line3 += "-" * (len(bigger) + 2)
        line4 += buffer * (len(bigger) + 2 - len(str(answer))) + str(answer)

        if prob != problems[-1]:
            line1 += between_probs
            line2 += between_probs
            line3 += between_probs
            line4 += between_probs

        if solution: arranged_problems = line1 + line2 + line3 + line4
        else: arranged_problems = line1 + line2 + line3
    print(arranged_problems)

    return arranged_problems
