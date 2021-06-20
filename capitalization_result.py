# Capitalization result
V0=int(input('Enter initial capital deposit: '))
r=int(input('Entar annual rate of return in %: '))
n=int(input('Enter number of years: '))
i=int(input('Enter inflation rate in %: '))
print("Capitalization result: ",V0*(1+(((r/100)-(i/100))/(1+(i/100))))**n)