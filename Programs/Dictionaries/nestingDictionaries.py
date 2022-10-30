capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'India': 'Delhi',
}

# Nesting list in dictionary
travel_log = {
    'France': ['Paris', 'Lyon', 'Lille', 'Nancy'],
    'Germany': ['Berlin', 'Munich', 'Frankfurt', 'Hamburg'],
    'India': ['Delhi', 'Haryana', 'Bangalore', 'Mumbai'],
}

# Nesting dictionary in dictionary
travel_log = {
    'France': {
        'cities_visited': ['Paris', 'Lyon', 'Lille', 'Nancy'],
        'total_visits': 12,
    },
    'Germany': {
        'cities_visited': ['Berlin', 'Munich', 'Frankfurt', 'Hamburg'],
        'total_visits': 8,
    },
    'India': {
        'cities_visited': ['Delhi', 'Haryana', 'Bangalore', 'Mumbai'],
        'total_visits': 20,
    },
}

# Nesting dictionary in list
travel_log = [
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Lyon', 'Lille', 'Nancy'],
        'total_visits': 12,

    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin', 'Munich', 'Frankfurt', 'Hamburg'],
        'total_visits': 8,

    },
    {
        country: 'India',
        'cities_visited': ['Delhi', 'Haryana', 'Bangalore', 'Mumbai'],
        'total_visits': 20,

    },
]
