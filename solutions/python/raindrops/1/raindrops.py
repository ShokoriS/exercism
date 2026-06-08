def convert(number):

    responds = {3: "Pling",5: "Plang", 7:"Plong"}
    result = ""
    for num, response in responds.items():
        if number % num == 0:
            result = f"{result}{response}"

    return result if result else str(number)

