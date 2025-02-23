from django.shortcuts import render

def calculator(request):
    result = None
    if request.method == "POST":
        try:

            num1 = float(request.POST["num1"])
            num2 = float(request.POST["num2"])
            operator = request.POST["operator"]

            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    result = "Error: Division by Zero is not allowed."
                else:
                    result = num1 / num2

            elif operator == "%":
                if num2 == 0:
                    result = "Error: Modulo by zero is not allowed."
                else:
                    result = num1 % num2

            else:
                result = f"Error: '{operator}' is not a valid operator."

        except ValueError:
            result = "Error: Invalid input"

    return render(request, "index.html", {"result": result})
        