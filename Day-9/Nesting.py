#Nesting:

capitals = {
    "france": "paris",
    "Germany": "Berlin"
}

#nesting Dictionary in a Dictornary
travel_log = {
    "france": {"cities_visited": ["paris", "lillie", "Dijon"], "total_visitors":12} ,#three places in one value
    "germany": {"cities_visited": ["berlin","Hamburg","Stuttgart"], "total_visitors":5}
}

#nesting Dictionary in a list
travel_log = [
    {"country": "France",
     "cities_visited": ["paris", "lillie", "Dijon"],
      "total_visitors": 12
      },#three places in one value}

        {"country": "Germany",
         "cities_visited": ["berlin","Hamburg","Stuttgart"],
          "total_visitors":5
          },
]

