default_kwargs = [{}, {"locale": "en_US"}]

loc_lat_long = [
    ({}, True),
    ({"latitude": 37.7670169511878}, True),
    ({"longitude": -122.42184275}, True),
    ({"location": "San Francisco"}, False),
    ({"latitude": 37.7670169511878, "longitude": -122.42184275}, False),
    (
        {
            "location": "San Francisco",
            "latitude": 37.7670169511878,
            "longitude": -122.42184275,
        },
        False,
    ),
]
