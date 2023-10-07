
import re
strings = ["12abc123", "45XYZ789", "123abc789", "ABc123456"]
pattern = r"\d{2}[a-zA-Z]{3}\d{3}"

for string in strings:
    if re.match(pattern, string):
        print(f"String '{string}' matches the pattern.")
    else:
        print(f"String '{string}' does not match the pattern.")


"""select e1.name as emp1 , e2.name as emp2
from employee e1
left join empoyeee e2
on e1.id=e2.id
where e1.id<e2.id"""