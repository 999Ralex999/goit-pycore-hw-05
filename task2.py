import re

def generator_numbers(text: str):
    regex = re.compile(r'\b\d+\.\d+\b')  
    for match in re.finditer(regex, text):
        yield float(match.group()) 


def sum_profit(text: str, func):
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

print(list(generator_numbers(text))) 
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") 