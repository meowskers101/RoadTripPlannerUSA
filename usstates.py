# ----- Graph of US States -----
usa_map = {
    "Alabama": ["Florida", "Georgia", "Tennessee", "Mississippi"],
    "Alaska": ["Hawaii","Washington"],
    "Arizona": ["California", "Nevada", "Utah", "Colorado", "New Mexico"],
    "Arkansas": ["Louisiana", "Mississippi", "Tennessee", "Missouri", "Oklahoma", "Texas"],
    "California": ["Oregon", "Nevada", "Arizona"],
    "Colorado": ["Wyoming", "Nebraska", "Kansas", "Oklahoma", "New Mexico", "Arizona", "Utah"],
    "Connecticut": ["New York", "Massachusetts", "Rhode Island"],
    "Delaware": ["Maryland", "Pennsylvania", "New Jersey"],
    "Florida": ["Alabama", "Georgia"],
    "Georgia": ["Florida", "Alabama", "Tennessee", "North Carolina", "South Carolina"],
    "Hawaii": ["California"],
    "Idaho": ["Washington", "Oregon", "Nevada", "Utah", "Wyoming", "Montana"],
    "Illinois": ["Wisconsin", "Iowa", "Missouri", "Kentucky", "Indiana"],
    "Indiana": ["Illinois", "Kentucky", "Ohio", "Michigan"],
    "Iowa": ["Minnesota", "Wisconsin", "Illinois", "Missouri", "Nebraska", "South Dakota"],
    "Kansas": ["Nebraska", "Missouri", "Oklahoma", "Colorado"],
    "Kentucky": ["Illinois", "Indiana", "Ohio", "West Virginia", "Virginia", "Tennessee", "Missouri"],
    "Louisiana": ["Arkansas", "Mississippi", "Texas"],
    "Maine": ["New Hampshire"],
    "Maryland": ["Delaware", "Pennsylvania", "Virginia", "West Virginia"],
    "Massachusetts": ["Connecticut", "New York", "New Hampshire", "Rhode Island", "Vermont"],
    "Michigan": ["Indiana", "Ohio", "Wisconsin", "Minnesota"],
    "Minnesota": ["North Dakota", "South Dakota", "Iowa", "Wisconsin", "Michigan"],
    "Mississippi": ["Alabama", "Arkansas", "Tennessee", "Louisiana"],
    "Missouri": ["Iowa", "Illinois", "Kentucky", "Tennessee", "Arkansas", "Oklahoma", "Kansas", "Nebraska"],
    "Montana": ["Idaho", "Wyoming", "South Dakota", "North Dakota"],
    "Nebraska": ["Colorado", "Iowa", "Kansas", "Missouri", "South Dakota", "Wyoming"],
    "Nevada": ["Idaho", "Utah", "Arizona", "California", "Oregon"],
    "New Hampshire": ["Maine", "Massachusetts", "Vermont"],
    "New Jersey": ["Delaware", "Pennsylvania", "New York"],
    "New Mexico": ["Arizona", "Utah", "Colorado", "Oklahoma", "Texas"],
    "New York": ["Connecticut", "Massachusetts", "Vermont", "New Jersey", "Pennsylvania", "Rhode Island"],
    "North Carolina": ["Virginia", "Tennessee", "Georgia", "South Carolina"],
    "North Dakota": ["Minnesota", "South Dakota", "Montana"],
    "Ohio": ["Pennsylvania", "West Virginia", "Kentucky", "Indiana", "Michigan"],
    "Oklahoma": ["Kansas", "Missouri", "Arkansas", "Texas", "New Mexico", "Colorado"],
    "Oregon": ["California", "Nevada", "Idaho", "Washington"],
    "Pennsylvania": ["New York", "New Jersey", "Delaware", "Maryland", "West Virginia", "Ohio"],
    "Rhode Island": ["Connecticut", "Massachusetts"],
    "South Carolina": ["Georgia", "North Carolina"],
    "South Dakota": ["North Dakota", "Minnesota", "Iowa", "Nebraska", "Wyoming", "Montana"],
    "Tennessee": ["Kentucky", "Virginia", "North Carolina", "Georgia", "Alabama", "Mississippi", "Arkansas", "Missouri"],
    "Texas": ["New Mexico", "Oklahoma", "Arkansas", "Louisiana"],
    "Utah": ["Idaho", "Wyoming", "Colorado", "New Mexico", "Arizona", "Nevada"],
    "Vermont": ["New York", "New Hampshire", "Massachusetts"],
    "Virginia": ["Kentucky", "West Virginia", "Maryland", "North Carolina", "Tennessee"],
    "Washington": ["Idaho", "Oregon"],
    "West Virginia": ["Ohio", "Pennsylvania", "Maryland", "Virginia", "Kentucky"],
    "Wisconsin": ["Minnesota", "Iowa", "Illinois", "Michigan"],
    "Wyoming": ["Montana", "South Dakota", "Nebraska", "Colorado", "Utah", "Idaho"]
}

state_info = {
    "California": {
        "things_to_do": ["Drive the Pacific Coast Highway", "Visit Disneyland", "Explore Yosemite National Park"],
        "fun_fact": "California produces over 80% of U.S. wine.",
        "drive_time": 6
    },
    "Florida": {
        "things_to_do": ["Visit Disney World", "Relax on Miami Beach", "Explore the Everglades"],
        "fun_fact": "Florida has the longest coastline in the contiguous U.S.",
        "drive_time": 5
    },
    "New York": {
        "things_to_do": ["See the Statue of Liberty", "Walk Central Park", "Visit Niagara Falls"],
        "fun_fact": "New York City was the first capital of the U.S.",
        "drive_time": 4
    },
    "Texas": {
        "things_to_do": ["Visit The Alamo", "Explore Austin’s music scene", "Tour NASA in Houston"],
        "fun_fact": "Texas is larger than any European country.",
        "drive_time": 7
    },
    "Washington": {
        "things_to_do": ["Visit Mount Rainier", "Explore Pike Place Market", "See the Space Needle"],
        "fun_fact": "Washington is the only state named after a president.",
        "drive_time": 4
    },
    "Nevada": {
        "things_to_do": ["Visit Las Vegas", "Explore Lake Tahoe", "Drive scenic Highway 50"],
        "fun_fact": "Over 85% of Nevada is owned by the federal government.",
        "drive_time": 3
    },
    "Arizona": {
        "things_to_do": ["See the Grand Canyon", "Explore Sedona", "Drive Route 66 segments"],
        "fun_fact": "Arizona is home to the largest ponderosa pine forest in the world.",
        "drive_time": 4
    },
    "Illinois": {
        "things_to_do": ["Visit Millennium Park", "See Willis Tower", "Explore Chicago’s museums"],
        "fun_fact": "The first skyscraper in the world was built in Chicago.",
        "drive_time": 3
    },
    "Massachusetts": {
        "things_to_do": ["Walk the Freedom Trail", "Visit Boston Common", "Tour Harvard University"],
        "fun_fact": "Massachusetts was the first U.S. state to legalize same-sex marriage.",
        "drive_time": 2
    },
    "Georgia": {
        "things_to_do": ["Explore Atlanta museums", "Visit Savannah historic district", "Drive the Blue Ridge Scenic Route"],
        "fun_fact": "Georgia was the last of the original 13 colonies to be established.",
        "drive_time": 3
    },
    "Colorado": {
        "things_to_do": ["Ski in the Rockies", "Hike 14ers", "Visit Denver attractions"],
        "fun_fact": "Colorado is the only state where every part is above 1,000 meters in elevation.",
        "drive_time": 4
    },
    "Hawaii": {
        "things_to_do": ["Relax on Waikiki Beach", "Hike Diamond Head", "Visit Volcanoes National Park"],
        "fun_fact": "Hawaii is the only U.S. state made entirely of islands.",
        "drive_time": 2
    },
    "Alaska": {
        "things_to_do": ["See the Northern Lights", "Cruise Kenai Fjords", "Hike Denali National Park"],
        "fun_fact": "Alaska has the longest coastline of any U.S. state.",
        "drive_time": 5
    },
    "Pennsylvania": {
        "things_to_do": ["Visit Liberty Bell", "Explore Hersheypark", "Walk historic Philadelphia"],
        "fun_fact": "The first U.S. library was established in Philadelphia.",
        "drive_time": 3
    },
    "Michigan": {
        "things_to_do": ["Drive the Upper Peninsula", "Visit Mackinac Island", "Tour Detroit museums"],
        "fun_fact": "Michigan has the longest freshwater coastline of any state.",
        "drive_time": 4
    }
    ,
    "Alabama": {
        "things_to_do": ["Drive the Gulf Coast", "Visit Birmingham Civil Rights sites", "Explore Gulf Shores"],
        "fun_fact": "Alabama is home to the U.S. Space & Rocket Center in Huntsville.",
        "drive_time": 3
    },
    "Arkansas": {
        "things_to_do": ["Visit Hot Springs National Park", "Hike the Ozarks", "Explore Crystal Bridges Museum"],
        "fun_fact": "Arkansas has more than 600,000 acres of national forest land.",
        "drive_time": 3
    },
    "Connecticut": {
        "things_to_do": ["Walk Mystic Seaport", "Visit Yale University", "See Gillette Castle"],
        "fun_fact": "Connecticut hosted the first nuclear-powered submarine launch in the U.S.",
        "drive_time": 2
    },
    "Delaware": {
        "things_to_do": ["Walk the beaches at Rehoboth", "Visit historic New Castle", "Explore Wilmington museums"],
        "fun_fact": "Delaware was the first state to ratify the U.S. Constitution.",
        "drive_time": 1
    },
    "Idaho": {
        "things_to_do": ["Hike Sawtooth Mountains", "Visit Sun Valley", "Explore Coeur d'Alene"],
        "fun_fact": "Idaho produces about one-third of the potatoes grown in the U.S.",
        "drive_time": 4
    },
    "Indiana": {
        "things_to_do": ["Attend the Indy 500", "Explore Indianapolis museums", "Visit Brown County"],
        "fun_fact": "The Indianapolis Motor Speedway is one of the largest sporting venues in the world.",
        "drive_time": 3
    },
    "Iowa": {
        "things_to_do": ["Drive the Loess Hills", "Visit the Iowa State Fair", "Explore Des Moines' art scene"],
        "fun_fact": "Iowa was the first state to implement a presidential nominating caucus.",
        "drive_time": 3
    },
    "Kansas": {
        "things_to_do": ["Visit Dodge City historic sites", "See the Tallgrass Prairie", "Explore Wichita museums"],
        "fun_fact": "Kansas is roughly at the geographic center of the contiguous United States.",
        "drive_time": 3
    },
    "Kentucky": {
        "things_to_do": ["Tour the Kentucky Bourbon Trail", "Visit Mammoth Cave National Park", "Attend the Kentucky Derby"],
        "fun_fact": "More bourbon is produced in Kentucky than in any other state.",
        "drive_time": 3
    },
    "Louisiana": {
        "things_to_do": ["Visit New Orleans' French Quarter", "Explore Cajun country", "Take a swamp tour"],
        "fun_fact": "Louisiana's culture blends French, African, American, and French-Canadian influences.",
        "drive_time": 3
    },
    "Maine": {
        "things_to_do": ["Visit Acadia National Park", "Eat lobster in coastal towns", "Lighthouse sightseeing"],
        "fun_fact": "Maine is the easternmost state in the U.S. mainland.",
        "drive_time": 2
    },
    "Maryland": {
        "things_to_do": ["Visit the Inner Harbor in Baltimore", "Explore Annapolis", "Try Maryland crab cakes"],
        "fun_fact": "Maryland is known for its blue crabs and seafood.",
        "drive_time": 2
    },
    "Minnesota": {
        "things_to_do": ["Visit the Mall of America", "Explore the Boundary Waters", "See the Twin Cities' parks"],
        "fun_fact": "Minnesota is called the Land of 10,000 Lakes.",
        "drive_time": 3
    },
    "Mississippi": {
        "things_to_do": ["Explore the Delta blues scene", "Visit historic Natchez", "Tour antebellum homes"],
        "fun_fact": "The Mississippi River runs along the state's western border.",
        "drive_time": 3
    },
    "Missouri": {
        "things_to_do": ["Visit the Gateway Arch in St. Louis", "Explore Kansas City jazz and BBQ", "Hike Ozark trails"],
        "fun_fact": "Missouri is home to the starting point of the Lewis and Clark Expedition.",
        "drive_time": 3
    },
    "Montana": {
        "things_to_do": ["Visit Glacier National Park", "Drive scenic mountain roads", "Explore Yellowstone's northern edge"],
        "fun_fact": "Montana has some of the largest tracts of undeveloped land in the U.S.",
        "drive_time": 4
    },
    "Nebraska": {
        "things_to_do": ["Visit Chimney Rock", "Explore Omaha's Old Market", "See Sandhills scenery"],
        "fun_fact": "Nebraska's Sandhills are one of the largest sand dune formations in the Western Hemisphere.",
        "drive_time": 3
    },
    "New Hampshire": {
        "things_to_do": ["Drive the Kancamagus Highway", "Visit the White Mountains", "Explore Portsmouth"],
        "fun_fact": "New Hampshire holds the first primary in the U.S. presidential nominating calendar.",
        "drive_time": 2
    },
    "New Jersey": {
        "things_to_do": ["Walk the Jersey Shore", "Visit Liberty State Park", "Explore Princeton"],
        "fun_fact": "New Jersey has a diverse mix of urban and rural areas in a small state.",
        "drive_time": 2
    },
    "New Mexico": {
        "things_to_do": ["Visit Santa Fe arts and architecture", "Explore Carlsbad Caverns", "Drive the Turquoise Trail"],
        "fun_fact": "New Mexico has one of the highest percentages of Hispanic and Latino populations in the U.S.",
        "drive_time": 4
    },
    "North Carolina": {
        "things_to_do": ["Drive the Blue Ridge Parkway", "Visit the Outer Banks", "Explore Asheville breweries"],
        "fun_fact": "North Carolina has both Atlantic beaches and Appalachian mountains.",
        "drive_time": 3
    },
    "North Dakota": {
        "things_to_do": ["Visit Theodore Roosevelt National Park", "Explore Fargo's cultural scene", "See the Badlands"],
        "fun_fact": "North Dakota is one of the least densely populated U.S. states.",
        "drive_time": 3
    },
    "Ohio": {
        "things_to_do": ["Visit the Rock and Roll Hall of Fame", "Explore Hocking Hills", "See Pro Football Hall of Fame"],
        "fun_fact": "Ohio played a major role in early aviation history and industry.",
        "drive_time": 3
    },
    "Oklahoma": {
        "things_to_do": ["Explore the National Cowboy & Western Heritage Museum", "Visit Tulsa's art deco sites", "See the Wichita Mountains"],
        "fun_fact": "Oklahoma has a rich Native American history and many tribal nations.",
        "drive_time": 3
    },
    "Oregon": {
        "things_to_do": ["Drive the Oregon Coast", "Visit Crater Lake National Park", "Explore Portland's food scene"],
        "fun_fact": "Oregon is known for its diverse landscapes, from coast to mountains to desert.",
        "drive_time": 4
    },
    "Rhode Island": {
        "things_to_do": ["Walk Newport mansions", "Visit Providence's WaterFire (seasonal)", "Relax on small coastal beaches"],
        "fun_fact": "Rhode Island is the smallest U.S. state by area.",
        "drive_time": 1
    },
    "South Carolina": {
        "things_to_do": ["Visit Charleston historic district", "Relax on Hilton Head or Myrtle Beach", "Explore Congaree National Park"],
        "fun_fact": "South Carolina was the first state to secede from the Union in 1860.",
        "drive_time": 3
    },
    "South Dakota": {
        "things_to_do": ["See Mount Rushmore", "Explore Badlands National Park", "Visit Custer State Park"],
        "fun_fact": "South Dakota is home to some of the country's most iconic memorials and natural landscapes.",
        "drive_time": 3
    },
    "Tennessee": {
        "things_to_do": ["Visit Nashville's music scene", "Explore Graceland in Memphis", "Drive scenic routes in the Smokies"],
        "fun_fact": "Tennessee is a center of American music, especially country and blues.",
        "drive_time": 3
    },
    "Utah": {
        "things_to_do": ["Visit Zion and Bryce Canyon National Parks", "Ski in Park City", "Explore Salt Lake City"],
        "fun_fact": "Utah has five national parks with spectacular red-rock landscapes.",
        "drive_time": 4
    },
    "Vermont": {
        "things_to_do": ["Drive scenic fall foliage routes", "Visit small towns and maple farms", "Hike Green Mountain trails"],
        "fun_fact": "Vermont is known for its maple syrup production.",
        "drive_time": 2
    },
    "Virginia": {
        "things_to_do": ["Visit Colonial Williamsburg", "Explore Shenandoah National Park", "See historic Richmond"],
        "fun_fact": "Virginia has many important early U.S. historic sites and was the birthplace of several presidents.",
        "drive_time": 3
    },
    "West Virginia": {
        "things_to_do": ["Hike the Appalachian Trails", "Explore New River Gorge", "See historic coal country sites"],
        "fun_fact": "West Virginia separated from Virginia during the Civil War to form a new state.",
        "drive_time": 3
    },
    "Wisconsin": {
        "things_to_do": ["Visit Milwaukee breweries", "Explore Door County", "See the Wisconsin Dells"],
        "fun_fact": "Wisconsin is famous for its cheese production.",
        "drive_time": 3
    },
    "Wyoming": {
        "things_to_do": ["Visit Yellowstone National Park", "See Grand Teton", "Explore wide open western landscapes"],
        "fun_fact": "Wyoming has the smallest population of any U.S. state.",
        "drive_time": 4
    }
}
