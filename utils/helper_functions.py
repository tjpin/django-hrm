import string, random

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octomer", "November", "December"]

def parse_months(n):
    return [m[1] for m in enumerate(MONTHS) if m[0] == n-1]

def generate_id(length):
   numbers = string.digits 
   return int(''.join(random.choice(numbers) for i in range(length))
)