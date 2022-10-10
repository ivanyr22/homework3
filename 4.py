years = float(input("Введите количество лет: "))
exhibits = int(input("Введите количество экспонатов "))
exhibits_per_year = 365 * 24 * 12 #5 минут на экспонат
print("За ", years, ' лет будет просмотрено ', years * exhibits_per_year, ' экпонатов')
years_to_see =  exhibits / exhibits_per_year
days_to_see = years_to_see * 365
print(exhibits, ' экспонатов будет просмотрено за', years_to_see, ' лет, что равняется ', days_to_see, ' дням или ', days_to_see * 24, 'часам')