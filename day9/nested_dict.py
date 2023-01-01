#nested dictionary

travel={
    "France":{"cities":["paris","lille","dijon"],"total_vsited":12},#dict in a dict
    "Germany" :["berlin","hamburg"],# list in a dict
}

#nesting dict in a list
travel=[
    {"country":"France", #string
    "cities":["paris","lille","dijon"], #list
    "total_vsited":12 #value
    },
    {"country": "Germany" ,"cities":["berlin","hamburg"]}
]

