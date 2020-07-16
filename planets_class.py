# To find radius of the planet, number of days in planet, largest planet:-

class Planet:

    one_earth_year=365.25
    
    def __init__(self,planet_name,diameter,no_of_moons,length_year):
        self.planet_name=planet_name
        self.diameter=diameter
        self.no_of_moons=no_of_moons
        self.length_year=length_year
        if "earth year" in self.length_year:
            self.length_year=str(float(self.length_year.split()[0])*Planet.one_earth_year)
        else:
            self.length_year=self.length_year.split()[0]
            
    def planet_radius(self):
        print("The Radius of planet Neptune is:",self.diameter/2,"km\n")
        
    def days_in_planet(self):
        print("Number of days in Jupiter is:",round(float(self.length_year)),"days\n")


def largest_planet():
    list=[]
    obj_list=[mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
    for planet_obj in range(len(obj_list)):
        list.append(obj_list[planet_obj].diameter)
    print("The largest planet is:",obj_list[list.index(max(list))].planet_name)
        
mercury = Planet("Mercury",4879,0,"88 days")
venus = Planet("Venus",12100,0,"225 days")
earth = Planet("Earth",12755,1,"365 days")
mars = Planet("Mars",6786,2,"687 days")
jupiter = Planet("Jupiter",142800,79,"12 earth year")
saturn = Planet("Saturn",120537,82,"29.5 earth year")
uranus = Planet("Uranus",51819,27,"84 earth year")
neptune = Planet("Neptune",49529,14,"165 earth year")


neptune.planet_radius()
jupiter.days_in_planet()
largest_planet()
