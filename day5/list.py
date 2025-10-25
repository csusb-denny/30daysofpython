lst = list()
question2 = [5, 10, 15, 20, 25]
print(len(question2))
print(question2[0], question2[len(question2)//2], question2[len(question2) - 1])

mixed_data_types = ['Denny', 27, 5.8, 'Married', '9388 Field Stone Ave']
for x in mixed_data_types:
  print(x)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
for companies in it_companies:
  print(companies)
print(len(it_companies))
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[len(it_companies) - 1])
it_companies[0] = it_companies[0].upper()
print(it_companies[0])
it_companies.insert(int(input("Enter Index of Insertion: ")), (input("Enter Company to Insert: ")))

company_exist = (input("enter company to check for: "))

for place in it_companies:
  if place == company_exist:
    print(True)


it_companies.sort()
it_companies.sort(reverse=True)

it_companies[:3]
it_companies[:-3]

it_companies.pop(0)
it_companies.pop(len(it_companies) // 2)