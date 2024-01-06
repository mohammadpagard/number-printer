num = input("")

def number_printer(number: str) -> str:
    if len(number) <= 100:
        for n in number:
            yield '{}: {}'.format(n, n*int(n)) 

for i in number_printer(num):
    print(i)

