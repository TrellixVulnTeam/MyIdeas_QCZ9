class City():
    def __init__(self, name, country, age):
        self.name = name
        self.country = country
        self.age = age
        self.population = 2870000
        self.polution = 23
    def describe_city_obsh(self):
        print('This is '+self.name.title()+". It is located in "+self.country.title()+' and it is more than '
                                                                                      +str(self.age)+' years old!')
    def growth_of_population(self):
        self.population += 34000
        return self.population
    def polution_of_air(self):
        self.polution += 2
        return self.polution
rome = City('Rome', 'Italy', 5000)
rome.describe_city_obsh()
print('Now there live approximately 2870000 people.')
print('This is how it`s population is going to grow for the next 10 years: ')
for i in range(5):
    print(rome.growth_of_population())
print('Rome is not hte biggest city in the world, but air pollution is one of the problems there.'
      'That`s every year the concentration of carbon dioxide is growing this fast : ')
for i in range(7):
    print(str(rome.polution_of_air()) + '%')
print('...')