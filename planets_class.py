# To find radius of the planet, number of days in planet, largest planet:-

class Galaxy:

    one_earth_year=365.25
    
    def __init__(self,planet_name,diameter,no_of_moons,length_year):
        self.planet_name=planet_name
        self.diameter=diameter
        self.no_of_moons=no_of_moons
        self.length_year=length_year
        if "earth year" in self.length_year:
            self.length_year=str(float(self.length_year.split()[0])*Galaxy.one_earth_year)
        else:
            self.length_year=self.length_year.split()[0]


def rad_of_neptune():
    print("The Radius of planet Neptune is:",neptune.diameter/2,"km\n")

def days_in_jupiter():
    print("Number of days in Jupiter is:",round(float(jupiter.length_year)),"days\n")

def largest_planet():
    l=[]
    x=[mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
    for i in range(len(x)):
        l.append(x[i].diameter)
    print("The largest planet is:",x[l.index(max(l))].planet_name)
        
mercury = Galaxy("Mercury",4879,0,"88 days")
venus = Galaxy("Venus",12100,0,"225 days")
earth = Galaxy("Earth",12755,1,"365 days")
mars = Galaxy("Mars",6786,2,"687 days")
jupiter = Galaxy("Jupiter",142800,79,"12 earth year")
saturn = Galaxy("Saturn",120537,82,"29.5 earth year")
uranus = Galaxy("Uranus",51819,27,"84 earth year")
neptune = Galaxy("Neptune",49529,14,"165 earth year")


rad_of_neptune()
days_in_jupiter()
largest_planet()
