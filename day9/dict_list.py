travel=[
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuggart"]
    }
]
def add_new_country(country_vis,times_vis,cities_vis):
    new_country={}
    new_country["country"]=country_vis
    new_country["visits"]=times_vis
    new_country["cities"]=cities_vis
    travel.append(new_country)




add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel)