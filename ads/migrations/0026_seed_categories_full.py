from django.db import migrations

DATA = {
    "Авто": {
        # Немецкие
        "BMW": [
            "1 Series","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series",
            "X1","X2","X3","X4","X5","X6","X7","XM",
            "M2","M3","M4","M5","M8","Z4","i3","i4","i5","iX",
        ],
        "Mercedes-Benz": [
            "A-Class","B-Class","C-Class","E-Class","S-Class","CLA","CLS",
            "GLA","GLB","GLC","GLE","GLS","G-Class","AMG GT","EQC","EQS","EQA",
            "Sprinter","Vito","V-Class",
        ],
        "Audi": [
            "A1","A3","A4","A5","A6","A7","A8",
            "Q2","Q3","Q5","Q7","Q8","TT","R8","e-tron","e-tron GT",
            "RS3","RS4","RS5","RS6","RS7",
        ],
        "Volkswagen": [
            "Polo","Golf","Jetta","Passat","Arteon","Phaeton",
            "Tiguan","Touareg","T-Roc","ID.3","ID.4","ID.6",
            "Touran","Caravelle","Multivan","Amarok","Transporter",
        ],
        "Opel": [
            "Corsa","Astra","Insignia","Mokka","Zafira","Vectra",
            "Omega","Antara","Crossland","Grandland",
        ],
        "Porsche": [
            "911","918","Boxster","Cayman","718","718 Cayman",
            "Cayenne","Macan","Panamera","Taycan",
        ],
        # Японские
        "Toyota": [
            "Yaris","Corolla","Camry","Avalon","Prius","C-HR",
            "RAV4","Venza","Highlander","Land Cruiser","Land Cruiser Prado","Fortuner",
            "Hilux","Alphard","Supra","86","Sequoia","4Runner",
        ],
        "Honda": [
            "Fit","Jazz","City","Civic","Accord","Legend",
            "HR-V","Vezel","CR-V","Pilot","Passport","Ridgeline",
            "FR-V","Element","Freed","Odyssey","Stream","CR-Z",
        ],
        "Nissan": [
            "Micra","Note","Juke","Almera","Sentra","Tiida",
            "Qashqai","X-Trail","Murano","Patrol","Pathfinder","Armada",
            "Teana","Maxima","GT-R","Leaf","Ariya","Navara","Frontier",
        ],
        "Mazda": [
            "Mazda 2","Mazda 3","Mazda 6","MX-5","CX-3","CX-30",
            "CX-5","CX-8","CX-9","CX-60","CX-90","RX-8",
        ],
        "Mitsubishi": [
            "Colt","Lancer","Galant","Eclipse","Eclipse Cross",
            "ASX","Outlander","Outlander Sport","Pajero","Pajero Sport",
            "L200","Delica","Grandis",
        ],
        "Subaru": [
            "Impreza","WRX","WRX STI","Legacy","Outback",
            "Forester","XV","Crosstrek","Ascent","BRZ","Levorg",
        ],
        "Lexus": [
            "IS","ES","GS","LS","LC","RC",
            "UX","NX","RX","GX","LX","RZ",
        ],
        "Suzuki": [
            "Alto","Celerio","Swift","Baleno","Ciaz",
            "Jimny","Vitara","Grand Vitara","SX4","S-Cross","Ignis","Across",
        ],
        "Infiniti": [
            "Q30","Q50","Q60","Q70","QX30","QX50",
            "QX55","QX60","QX70","QX80","FX35","FX37",
        ],
        # Корейские
        "Hyundai": [
            "i10","i20","i30","Elantra","Sonata","Azera",
            "Solaris","Accent","Veloster","Kona","Tucson",
            "Santa Fe","Santa Cruz","Palisade","Creta","ix35",
            "IONIQ","IONIQ 5","IONIQ 6","Staria",
        ],
        "Kia": [
            "Picanto","Rio","Ceed","ProCeed","Stinger",
            "Cerato","K5","K8","Soul","Seltos","Sportage",
            "Sorento","Carnival","Telluride","Stonic","EV6","EV9",
        ],
        "Genesis": [
            "G70","G80","G90","GV70","GV80","GV60",
        ],
        # Французские
        "Peugeot": [
            "107","108","206","207","208","301","308","408","508",
            "2008","3008","4008","5008","Partner","Expert","Rifter",
        ],
        "Renault": [
            "Twingo","Clio","Megane","Laguna","Talisman",
            "Logan","Sandero","Duster","Captur","Kadjar","Koleos",
            "Arkana","Kaptur","Fluence","Zoe","Kangoo","Trafic",
        ],
        "Citroen": [
            "C1","C2","C3","C4","C5","C6","C8",
            "DS3","DS4","DS5","Berlingo","Jumpy","Jumper","C3 Aircross","C5 Aircross",
        ],
        # Итальянские
        "Fiat": [
            "500","500X","500L","Punto","Grande Punto","Bravo",
            "Tipo","Panda","Doblo","Ducato","Scudo",
        ],
        "Alfa Romeo": [
            "147","156","159","Giulia","Giulietta","Mito",
            "Stelvio","Tonale","Brera","Spider",
        ],
        "Ferrari": [
            "488 GTB","488 Spider","F8 Tributo","F8 Spider",
            "SF90","Roma","Portofino","812 Superfast","GTC4Lusso","LaFerrari",
        ],
        "Lamborghini": [
            "Huracan","Huracan Evo","Urus","Aventador","Aventador SVJ","Gallardo",
        ],
        "Maserati": [
            "Ghibli","Quattroporte","Levante","GranTurismo","GranCabrio","Grecale",
        ],
        # Британские
        "Land Rover": [
            "Defender","Discovery","Discovery Sport",
            "Range Rover","Range Rover Sport","Range Rover Velar","Range Rover Evoque",
            "Freelander",
        ],
        "Jaguar": [
            "XE","XF","XJ","F-Type","E-Pace","F-Pace","I-Pace",
        ],
        "Aston Martin": [
            "DB9","DB11","DB12","Vantage","DBS","Rapide","DBX",
        ],
        "Bentley": [
            "Continental GT","Continental GTC","Flying Spur","Bentayga","Mulsanne",
        ],
        "Rolls-Royce": [
            "Phantom","Ghost","Wraith","Dawn","Cullinan","Silver Shadow",
        ],
        "Mini": [
            "Cooper","Cooper S","Cooper SE","Cabrio","Clubman",
            "Countryman","Paceman","Coupe","Roadster",
        ],
        # Американские
        "Ford": [
            "Fiesta","Focus","Mondeo","Fusion","Taurus",
            "Mustang","Explorer","Expedition","Escape","Kuga","Edge",
            "F-150","F-250","F-350","Bronco","EcoSport","Maverick",
        ],
        "Chevrolet": [
            "Aveo","Cruze","Malibu","Impala","Camaro","Corvette",
            "Captiva","Equinox","Blazer","Traverse","Tahoe","Suburban","Trailblazer",
            "Colorado","Silverado","Spark","Trax",
        ],
        "Cadillac": [
            "ATS","CT4","CT5","CT6","XTS","Escalade","XT4","XT5","XT6","Lyriq",
        ],
        "Dodge": [
            "Challenger","Charger","Durango","Journey","RAM 1500",
        ],
        "Jeep": [
            "Renegade","Compass","Cherokee","Grand Cherokee","Grand Cherokee 4xe",
            "Wrangler","Gladiator","Commander",
        ],
        "Tesla": [
            "Model 3","Model 3 Performance","Model Y","Model S","Model S Plaid",
            "Model X","Cybertruck","Roadster",
        ],
        # Шведские
        "Volvo": [
            "S40","S60","S90","V40","V60","V90",
            "XC40","XC60","XC90","C30","C40","EX90",
        ],
        # Чешские
        "Skoda": [
            "Fabia","Rapid","Scala","Octavia","Superb",
            "Kamiq","Karoq","Kodiaq","Enyaq","Yeti",
        ],
        # Испанские
        "Seat": [
            "Ibiza","Arona","Leon","Toledo","Ateca","Tarraco","Alhambra",
        ],
        # Китайские
        "Geely": [
            "Emgrand","Coolray","Atlas","Tugella","Atlas Pro","Monjaro","Okavango",
        ],
        "Chery": [
            "Tiggo 3","Tiggo 4","Tiggo 4 Pro","Tiggo 7","Tiggo 7 Pro",
            "Tiggo 8","Tiggo 8 Pro","Arrizo 5","Arrizo 8",
        ],
        "Haval": [
            "H6","H9","H2","F7","F7x","Jolion","Dargo","Poer",
        ],
        "BYD": [
            "Han","Tang","Song","Atto 3","Seal","Dolphin","Seagull","Destroyer 05",
        ],
        "Changan": [
            "CS35 Plus","CS55 Plus","CS75 Plus","UNI-T","UNI-K","UNI-V","Lamore",
        ],
        "Exeed": [
            "TXL","LX","VX","RX","TX",
        ],
        "Great Wall": [
            "Hover H3","Hover H5","Hover H6","Wingle 7",
        ],
        # Российские / СНГ
        "Lada": [
            "Granta","Granta Cross","Vesta","Vesta Sport","Vesta SW",
            "Largus","XRAY","XRAY Cross","Niva","Niva Travel","Kalina","Priora",
        ],
        "UAZ": [
            "Patriot","Hunter","Буханка (452)","Pickup","3909",
        ],
        "GAZ": [
            "Gazelle Next","Gazelle NN","Sobol","Sobol NN","Volga",
        ],
        # Другое авто
        "Daewoo": [
            "Matiz","Nexia","Lanos","Nubira","Kalos","Lacetti","Gentra",
        ],
        "Peugeot (доп.)": [
            "Partner Tepee","Traveller",
        ],
        "Acura": [
            "ILX","TLX","RDX","MDX","NSX",
        ],
        "Smart": [
            "fortwo","fortwo cabrio","forfour","EQ fortwo",
        ],
    },

    "Телефоны": {
        "Apple": [
            "iPhone 6","iPhone 6 Plus","iPhone 6s","iPhone 6s Plus",
            "iPhone 7","iPhone 7 Plus","iPhone 8","iPhone 8 Plus",
            "iPhone X","iPhone XR","iPhone XS","iPhone XS Max",
            "iPhone 11","iPhone 11 Pro","iPhone 11 Pro Max",
            "iPhone 12 mini","iPhone 12","iPhone 12 Pro","iPhone 12 Pro Max",
            "iPhone 13 mini","iPhone 13","iPhone 13 Pro","iPhone 13 Pro Max",
            "iPhone 14","iPhone 14 Plus","iPhone 14 Pro","iPhone 14 Pro Max",
            "iPhone 15","iPhone 15 Plus","iPhone 15 Pro","iPhone 15 Pro Max",
            "iPhone 16","iPhone 16 Plus","iPhone 16 Pro","iPhone 16 Pro Max",
            "iPhone SE (2020)","iPhone SE (2022)","iPhone SE (2024)",
        ],
        "Samsung": [
            "Galaxy S8","Galaxy S9","Galaxy S10","Galaxy S10+","Galaxy S10e",
            "Galaxy S20","Galaxy S20+","Galaxy S20 Ultra",
            "Galaxy S21","Galaxy S21+","Galaxy S21 Ultra","Galaxy S21 FE",
            "Galaxy S22","Galaxy S22+","Galaxy S22 Ultra",
            "Galaxy S23","Galaxy S23+","Galaxy S23 Ultra","Galaxy S23 FE",
            "Galaxy S24","Galaxy S24+","Galaxy S24 Ultra","Galaxy S24 FE",
            "Galaxy Note 10","Galaxy Note 10+","Galaxy Note 20","Galaxy Note 20 Ultra",
            "Galaxy A12","Galaxy A13","Galaxy A14","Galaxy A22","Galaxy A23","Galaxy A24",
            "Galaxy A32","Galaxy A33","Galaxy A34","Galaxy A52","Galaxy A53","Galaxy A54",
            "Galaxy A72","Galaxy A73","Galaxy A04","Galaxy A05","Galaxy A15","Galaxy A35","Galaxy A55",
            "Galaxy Z Fold 3","Galaxy Z Fold 4","Galaxy Z Fold 5","Galaxy Z Fold 6",
            "Galaxy Z Flip 3","Galaxy Z Flip 4","Galaxy Z Flip 5","Galaxy Z Flip 6",
            "Galaxy M52","Galaxy M53","Galaxy M54",
        ],
        "Xiaomi": [
            "Mi 9","Mi 10","Mi 10 Pro","Mi 11","Mi 11 Ultra","Mi 12","Mi 12 Pro","Mi 13","Mi 13 Pro","Mi 14","Mi 14 Pro",
            "13T","13T Pro","14T","14T Pro",
            "Redmi 9","Redmi 10","Redmi 12","Redmi 13","Redmi 13C",
            "Redmi Note 9","Redmi Note 9 Pro","Redmi Note 10","Redmi Note 10 Pro",
            "Redmi Note 11","Redmi Note 11 Pro","Redmi Note 12","Redmi Note 12 Pro",
            "Redmi Note 13","Redmi Note 13 Pro","Redmi Note 13 Pro+",
            "POCO X3","POCO X3 Pro","POCO X4","POCO X5","POCO X5 Pro","POCO X6","POCO X6 Pro",
            "POCO F3","POCO F4","POCO F4 GT","POCO F5","POCO F5 Pro",
            "POCO M3","POCO M4","POCO M5","POCO C40","POCO C55",
        ],
        "Huawei": [
            "P20","P20 Pro","P30","P30 Pro","P40","P40 Pro","P40 Pro+",
            "P50","P50 Pro","P60","P60 Pro",
            "Mate 20","Mate 20 Pro","Mate 30","Mate 30 Pro",
            "Mate 40","Mate 40 Pro","Mate 50","Mate 50 Pro","Mate 60","Mate 60 Pro",
            "Nova 5T","Nova 7","Nova 8","Nova 9","Nova 10","Nova 11","Nova 12",
            "Y9","Y7","Y6","Y5",
        ],
        "Honor": [
            "8X","9X","10 Lite","20","20 Pro","30","30 Pro",
            "50","50 Pro","70","70 Pro","80","80 Pro","90","90 Pro",
            "Magic 4","Magic 4 Pro","Magic 5","Magic 5 Pro","Magic 6","Magic 6 Pro",
            "X8","X9","X9b","200","200 Pro",
        ],
        "OnePlus": [
            "7 Pro","8","8 Pro","8T","9","9 Pro","9RT",
            "10 Pro","10T","11","11R","12","12R",
            "Nord","Nord 2","Nord 2T","Nord 3","Nord CE 3","Nord CE 4",
            "Ace 2","Ace 2V","Ace 3",
        ],
        "Google": [
            "Pixel 4","Pixel 4 XL","Pixel 4a","Pixel 5","Pixel 5a",
            "Pixel 6","Pixel 6 Pro","Pixel 6a",
            "Pixel 7","Pixel 7 Pro","Pixel 7a",
            "Pixel 8","Pixel 8 Pro","Pixel 8a",
            "Pixel 9","Pixel 9 Pro","Pixel 9 Pro XL","Pixel 9 Pro Fold",
        ],
        "Sony": [
            "Xperia 5","Xperia 10","Xperia 10 II","Xperia 10 III","Xperia 10 IV","Xperia 10 V",
            "Xperia 1","Xperia 1 II","Xperia 1 III","Xperia 1 IV","Xperia 1 V","Xperia 1 VI",
            "Xperia 5 II","Xperia 5 III","Xperia 5 IV","Xperia 5 V",
        ],
        "Motorola": [
            "Moto G9","Moto G10","Moto G20","Moto G30","Moto G32","Moto G42","Moto G52","Moto G62","Moto G72","Moto G82",
            "Moto G100","Moto G200","Moto G54","Moto G84",
            "Edge 20","Edge 30","Edge 40","Edge 40 Pro","Edge 40 Neo",
            "Razr 40","Razr 40 Ultra","ThinkPhone",
        ],
        "Realme": [
            "5","6","7","8","9","9 Pro","9 Pro+","10","10 Pro","10 Pro+",
            "11","11 Pro","11 Pro+","12","12 Pro","12 Pro+",
            "GT","GT Neo","GT 2","GT 2 Pro","GT 3","GT 5","GT 6",
            "C11","C21","C25","C30","C33","C35","C51","C53","C55","C67",
            "Narzo 50","Narzo 60","Narzo 70",
        ],
        "Nokia": [
            "5.4","6.2","7.2","8.3","G10","G11","G20","G21","G22","G42","G60",
            "C01 Plus","C21 Plus","C32","X10","X20","X30","XR20","3310 (2017)",
        ],
        "OPPO": [
            "A15","A16","A17","A18","A38","A54","A57","A74","A76","A78","A96","A98",
            "Reno 5","Reno 6","Reno 7","Reno 8","Reno 8 Pro","Reno 9","Reno 10","Reno 11","Reno 12",
            "Find X3","Find X3 Pro","Find X5","Find X5 Pro","Find X6","Find X6 Pro","Find X7","Find X7 Ultra",
            "Find N2","Find N2 Flip","Find N3","Find N3 Flip",
        ],
        "Vivo": [
            "Y11","Y20","Y21","Y22","Y27","Y33","Y35","Y36","Y56","Y76","Y100",
            "V21","V23","V25","V27","V29","V30","V30 Pro",
            "X60","X70","X80","X80 Pro","X90","X90 Pro","X100","X100 Pro",
            "iQOO 9","iQOO 10","iQOO 11","iQOO 12","iQOO Neo 7","iQOO Neo 8","iQOO Z7","iQOO Z9",
        ],
        "ZTE": [
            "Blade A52","Blade A53","Blade A72","Blade A73","Blade V40","Blade V50",
            "Nubia Red Magic 6","Nubia Red Magic 7","Nubia Red Magic 8","Nubia Red Magic 9",
            "Axon 40 Ultra","Axon 50 Ultra",
        ],
        "Infinix": [
            "Hot 12","Hot 20","Hot 30","Hot 40","Hot 40i",
            "Note 12","Note 30","Note 40","Zero 20","Zero 30","Zero 40",
            "Smart 7","Smart 8",
        ],
        "Tecno": [
            "Spark 9","Spark 10","Spark 20","Spark 20 Pro",
            "Camon 19","Camon 20","Camon 30",
            "Pova 4","Pova 5","Phantom X2",
        ],
        "Asus": [
            "ROG Phone 5","ROG Phone 6","ROG Phone 7","ROG Phone 8",
            "Zenfone 8","Zenfone 9","Zenfone 10","Zenfone 11 Ultra",
        ],
    },

    "Планшеты": {
        "Apple": [
            "iPad 7 (2019)","iPad 8 (2020)","iPad 9 (2021)","iPad 10 (2022)",
            "iPad mini 5","iPad mini 6","iPad mini 7",
            "iPad Air 3","iPad Air 4","iPad Air 5","iPad Air M2",
            "iPad Pro 11 (2018)","iPad Pro 11 (2020)","iPad Pro 11 M1","iPad Pro 11 M2","iPad Pro 11 M4",
            "iPad Pro 12.9 (2018)","iPad Pro 12.9 (2020)","iPad Pro 12.9 M1","iPad Pro 12.9 M2",
            "iPad Pro 13 M4",
        ],
        "Samsung": [
            "Galaxy Tab A7","Galaxy Tab A7 Lite","Galaxy Tab A8","Galaxy Tab A9","Galaxy Tab A9+",
            "Galaxy Tab S6","Galaxy Tab S6 Lite","Galaxy Tab S7","Galaxy Tab S7+","Galaxy Tab S7 FE",
            "Galaxy Tab S8","Galaxy Tab S8+","Galaxy Tab S8 Ultra",
            "Galaxy Tab S9","Galaxy Tab S9+","Galaxy Tab S9 Ultra","Galaxy Tab S9 FE",
        ],
        "Huawei": [
            "MatePad T8","MatePad T10","MatePad T10s",
            "MatePad 11","MatePad 11.5","MatePad Air",
            "MatePad Pro 11","MatePad Pro 12.6","MatePad Pro 13.2",
            "MediaPad M5","MediaPad M6",
        ],
        "Xiaomi": [
            "Pad 5","Pad 5 Pro","Pad 6","Pad 6 Pro","Pad 6 Max","Pad 6S Pro",
            "Redmi Pad","Redmi Pad SE","Redmi Pad Pro",
        ],
        "Lenovo": [
            "Tab M7","Tab M8","Tab M9","Tab M10","Tab M10 Plus","Tab M10 FHD Plus",
            "Tab P11","Tab P11 Pro","Tab P11 Gen 2","Tab P12","Tab P12 Pro",
            "Tab Extreme","IdeaPad Duet 3","IdeaPad Duet 5","Legion Y700",
        ],
        "Microsoft": [
            "Surface Pro 7","Surface Pro 8","Surface Pro 9","Surface Pro 10",
            "Surface Go 2","Surface Go 3","Surface Duo 2",
        ],
        "Amazon": [
            "Fire 7","Fire HD 8","Fire HD 10","Fire HD 10 Plus","Fire Max 11",
        ],
        "Realme": [
            "Pad","Pad Mini","Pad X","Pad 2",
        ],
        "Honor": [
            "Pad 8","Pad X8","Pad X9","MagicPad 13",
        ],
    },

    "Ноутбуки": {
        "Apple": [
            "MacBook Air 13 M1","MacBook Air 13 M2","MacBook Air 13 M3",
            "MacBook Air 15 M2","MacBook Air 15 M3",
            "MacBook Pro 13 M1","MacBook Pro 13 M2",
            "MacBook Pro 14 M1 Pro","MacBook Pro 14 M1 Max",
            "MacBook Pro 14 M2 Pro","MacBook Pro 14 M2 Max",
            "MacBook Pro 14 M3","MacBook Pro 14 M3 Pro","MacBook Pro 14 M3 Max",
            "MacBook Pro 16 M1 Pro","MacBook Pro 16 M1 Max",
            "MacBook Pro 16 M2 Pro","MacBook Pro 16 M2 Max",
            "MacBook Pro 16 M3 Pro","MacBook Pro 16 M3 Max",
        ],
        "Dell": [
            "XPS 13","XPS 13 Plus","XPS 15","XPS 17","XPS 14",
            "Inspiron 14","Inspiron 15","Inspiron 16",
            "Latitude 5420","Latitude 5520","Latitude 7420","Latitude 9520",
            "Vostro 3510","Vostro 5510","Vostro 5620",
            "Alienware M15","Alienware M16","Alienware M17","Alienware x14","Alienware x15","Alienware x17",
            "G15","G16",
        ],
        "HP": [
            "Pavilion 14","Pavilion 15","Pavilion 16","Pavilion x360",
            "Envy 13","Envy 14","Envy 15","Envy x360",
            "Spectre x360 13","Spectre x360 14","Spectre x360 16",
            "EliteBook 840","EliteBook 850","EliteBook 1040",
            "ProBook 440","ProBook 450","ProBook 650",
            "Omen 15","Omen 16","Omen 17",
            "Victus 15","Victus 16","ZBook Studio","ZBook Fury",
        ],
        "Lenovo": [
            "ThinkPad X1 Carbon","ThinkPad X1 Extreme","ThinkPad X1 Yoga",
            "ThinkPad T14","ThinkPad T14s","ThinkPad T15","ThinkPad T16",
            "ThinkPad E14","ThinkPad E15","ThinkPad E16",
            "IdeaPad 3","IdeaPad 5","IdeaPad 5 Pro","IdeaPad Flex 5",
            "IdeaPad Slim 5","IdeaPad Slim 3","IdeaPad Gaming 3",
            "Legion 5","Legion 5 Pro","Legion 5i","Legion 7","Legion 7i","Legion Pro 5","Legion Pro 7",
            "Yoga 6","Yoga 7","Yoga 9","Yoga Slim 7","Yoga Slim 9",
        ],
        "Asus": [
            "ZenBook 13","ZenBook 14","ZenBook 14X","ZenBook 15","ZenBook Pro 14","ZenBook Pro 16",
            "VivoBook 14","VivoBook 15","VivoBook 16","VivoBook S14","VivoBook S15",
            "ExpertBook B9","ProArt Studiobook 16",
            "ROG Strix G15","ROG Strix G16","ROG Strix Scar 15","ROG Strix Scar 16","ROG Strix Scar 17",
            "ROG Zephyrus G14","ROG Zephyrus G15","ROG Zephyrus M16","ROG Zephyrus Duo 16",
            "TUF Gaming A15","TUF Gaming A17","TUF Gaming F15","TUF Gaming F17",
            "Chromebook CX9",
        ],
        "Acer": [
            "Aspire 3","Aspire 5","Aspire 7","Aspire Vero",
            "Swift 1","Swift 3","Swift 5","Swift X","Swift Go",
            "Spin 3","Spin 5","Spin 7",
            "Nitro 5","Nitro 16","Nitro 17",
            "Predator Helios 300","Predator Helios 16","Predator Helios 18",
            "Predator Triton 300","Predator Triton 500","ConceptD 7",
        ],
        "MSI": [
            "Modern 14","Modern 15","Creator 15","Creator 17",
            "GF63 Thin","GF75 Thin","GS66 Stealth","GS76 Stealth",
            "GP66 Leopard","GP76 Leopard","GL66","GL76",
            "GE66 Raider","GE76 Raider","GT76 Titan",
            "Katana GF66","Katana GF76","Vector GP66","Vector GP76",
            "Crosshair 15","Crosshair 17","Sword 15","Sword 17",
            "Prestige 13","Prestige 14","Prestige 15",
            "Stealth 15M","Stealth 16","Stealth 17",
        ],
        "Samsung": [
            "Galaxy Book 2","Galaxy Book 2 Pro","Galaxy Book 2 Pro 360",
            "Galaxy Book 3","Galaxy Book 3 Pro","Galaxy Book 3 Pro 360","Galaxy Book 3 Ultra",
            "Galaxy Book 4","Galaxy Book 4 Pro","Galaxy Book 4 Ultra","Galaxy Book 4 Edge",
        ],
        "Huawei": [
            "MateBook D14","MateBook D15","MateBook D16",
            "MateBook 14","MateBook 14s","MateBook 16","MateBook 16s",
            "MateBook X Pro","MateBook E",
        ],
        "LG": [
            "Gram 13","Gram 14","Gram 15","Gram 16","Gram 17",
            "Gram 2-in-1","Gram Style","UltraPC 14","UltraPC 15","UltraPC 16",
        ],
        "Xiaomi": [
            "Mi Notebook Pro 14","Mi Notebook Pro 15","Mi Notebook Air",
            "RedmiBook 14","RedmiBook 15","RedmiBook 16",
            "Book Pro 14","Book Pro 15","Book S 12","Book Air 13",
        ],
        "Razer": [
            "Blade 14","Blade 15","Blade 17","Blade 18","Blade Stealth",
        ],
        "Microsoft": [
            "Surface Laptop 4","Surface Laptop 5","Surface Laptop 6",
            "Surface Laptop Studio","Surface Laptop Studio 2",
            "Surface Book 3","Surface Pro 9 (ноутбук)",
        ],
    },

    "Игровые консоли": {
        "Sony": [
            "PlayStation 3","PlayStation 4","PlayStation 4 Slim","PlayStation 4 Pro",
            "PlayStation 5","PlayStation 5 Slim","PlayStation 5 Pro",
            "PSP 1000","PSP 2000","PSP 3000","PS Vita","PS Vita Slim",
        ],
        "Microsoft": [
            "Xbox 360","Xbox 360 S","Xbox 360 E",
            "Xbox One","Xbox One S","Xbox One X",
            "Xbox Series S","Xbox Series X",
        ],
        "Nintendo": [
            "Nintendo 3DS","Nintendo 3DS XL","Nintendo 2DS","Nintendo New 2DS XL",
            "Wii","Wii U","Nintendo Switch","Nintendo Switch Lite","Nintendo Switch OLED",
            "Game Boy Advance","Game Boy Advance SP",
        ],
        "Valve": [
            "Steam Deck 256GB","Steam Deck 512GB","Steam Deck OLED 512GB","Steam Deck OLED 1TB",
        ],
        "Atari": [
            "Atari VCS",
        ],
        "Аксессуары": [
            "Геймпад PS5 DualSense","Геймпад Xbox Series","Геймпад Nintendo Pro",
            "VR PlayStation VR","VR PlayStation VR2",
            "Гарнитура игровая","Руль игровой","Аркадный стик",
        ],
    },

    "Фото и видео": {
        "Canon": [
            "EOS R3","EOS R5","EOS R5 C","EOS R6","EOS R6 Mark II","EOS R7","EOS R8","EOS R10","EOS R50","EOS R100",
            "EOS 5D Mark IV","EOS 6D Mark II","EOS 90D","EOS 850D","EOS 250D",
            "EOS M50","EOS M50 Mark II","EOS M200",
            "PowerShot G7X","PowerShot G7X Mark II","PowerShot G7X Mark III",
            "PowerShot G1X","PowerShot SX740","Legria HF",
        ],
        "Nikon": [
            "Z9","Z8","Z7 II","Z6 III","Z6 II","Z5 II","Z5","Z50","Zfc","Z30",
            "D6","D850","D780","D750","D500","D7500","D5600","D5500","D3500",
            "Coolpix P950","Coolpix P1000","Coolpix B600",
        ],
        "Sony": [
            "Alpha 1","Alpha 7 IV","Alpha 7 III","Alpha 7C","Alpha 7C II","Alpha 7R V","Alpha 7R IV",
            "Alpha 7S III","Alpha 9 III","Alpha 6700","Alpha 6400","Alpha 6600","Alpha 6100","ZV-E10","ZV-E1",
            "RX100 VII","RX100 VI","RX10 IV","RX1R II","FX3","FX30","FX6 II",
        ],
        "Fujifilm": [
            "X-T5","X-T4","X-T3","X-T30 II","X-S20","X-S10",
            "X-H2","X-H2S","X100VI","X100V","X-E4","X-Pro3",
            "GFX 100S","GFX 50S II","GFX 100 II","Instax Mini 12","Instax Wide 300",
        ],
        "Panasonic": [
            "Lumix S5 II","Lumix S5 IIX","Lumix S5","Lumix S1","Lumix S1R","Lumix S1H",
            "Lumix GH6","Lumix GH5 II","Lumix G9 II","Lumix G100",
        ],
        "DJI": [
            "Mini 2","Mini 2 SE","Mini 3","Mini 3 Pro","Mini 4 Pro",
            "Air 2S","Air 3","Mavic 3","Mavic 3 Cine","Mavic 3 Classic","Mavic 3 Pro",
            "Inspire 3","Matrice 30","Avata","Avata 2","FPV",
            "Osmo Pocket 3","Osmo Mobile 6","Osmo Action 4","Osmo Action 5 Pro",
            "Ronin RS3","Ronin RS3 Pro","Ronin RS4","Ronin RS4 Pro",
        ],
        "GoPro": [
            "HERO8 Black","HERO9 Black","HERO10 Black","HERO11 Black","HERO11 Black Mini",
            "HERO12 Black","HERO13 Black","GoPro MAX",
        ],
        "Insta360": [
            "ONE X2","ONE X3","ONE RS","ONE RS 1-inch","X3","X4","GO 2","GO 3",
        ],
        "Объективы": [
            "Canon EF 50mm 1.8","Canon RF 24-70mm","Nikon AF-S 50mm",
            "Sony FE 85mm","Sigma 35mm Art","Tamron 28-75mm",
            "Viltrox 85mm","Samyang 14mm",
        ],
        "Штативы и стабилизаторы": [
            "Joby GorillaPod","Manfrotto 190","Benro Travel Angel",
            "Zhiyun Crane 3S","Zhiyun Weebill 3","DJI RS 3 Mini",
        ],
    },

    "Аудиотехника": {
        "Apple": [
            "AirPods (2-го поколения)","AirPods (3-го поколения)",
            "AirPods Pro (1-го поколения)","AirPods Pro (2-го поколения)",
            "AirPods Max",
        ],
        "Sony": [
            "WH-1000XM3","WH-1000XM4","WH-1000XM5",
            "WF-1000XM3","WF-1000XM4","WF-1000XM5",
            "WH-CH710N","WH-CH720N","WF-C700N","WF-C500",
            "LinkBuds S","LinkBuds Open","Inzone H9","Inzone H7","Inzone H5",
        ],
        "Samsung": [
            "Galaxy Buds Live","Galaxy Buds Pro","Galaxy Buds 2","Galaxy Buds 2 Pro",
            "Galaxy Buds FE","Galaxy Buds 3","Galaxy Buds 3 Pro",
        ],
        "Bose": [
            "QuietComfort 35 II","QuietComfort 45","QuietComfort Ultra",
            "700","SoundLink II","SoundLink Flex","SoundLink Max",
            "Sport Earbuds","QuietComfort Earbuds","QuietComfort Earbuds II",
        ],
        "Sennheiser": [
            "HD 560S","HD 600","HD 650","HD 800 S",
            "Momentum 3","Momentum 4","Momentum True Wireless 3","Momentum True Wireless 4",
            "CX True Wireless","ACCENTUM Plus",
        ],
        "JBL": [
            "Charge 5","Charge 5 Wi-Fi","Flip 6","Flip 7","Xtreme 3","Xtreme 4","Pulse 5",
            "Tune 710BT","Tune 760NC","Live 660NC","Live Pro 2","Tour One M2",
            "Vibe 300TWS","Wave 300TWS","Free NC TWS",
        ],
        "Marshall": [
            "Emberton","Emberton II","Emberton III","Tufton","Woburn III",
            "Stanmore III","Acton III","Major IV","Major V",
            "Monitor II ANC","Motif II ANC","Minor IV",
        ],
        "Harman Kardon": [
            "Onyx Studio 6","Onyx Studio 7","Onyx Studio 8",
            "Aura Studio 3","Citation 500","Citation 300","Citation 200",
        ],
        "Bang & Olufsen": [
            "Beoplay H95","Beoplay HX","Beoplay EX","Beoplay EQ",
            "Beosound A1","Beosound A5","Beosound Stage",
        ],
        "Xiaomi": [
            "Redmi Buds 3 Pro","Redmi Buds 4 Pro","Redmi Buds 5 Pro",
            "Buds 4 Pro","Buds 5 Pro","Sound Portable","Sound Outdoor",
        ],
        "Huawei": [
            "FreeBuds 3","FreeBuds 4","FreeBuds 5","FreeBuds Pro 2","FreeBuds Pro 3",
            "Sound Joy","Sound X",
        ],
    },

    "Телевизоры": {
        "Samsung": [
            "QLED Q60C","QLED Q70C","QLED Q80C","QLED Q90C",
            "Neo QLED QN85C","Neo QLED QN90C","Neo QLED QN95C",
            "OLED S90C","OLED S95C",
            "The Frame 2022","The Frame 2023","The Frame 2024",
            "Crystal UHD 7 Series","Crystal UHD 8 Series",
            "The Serif","The Sero","The Terrace",
        ],
        "LG": [
            "OLED A3","OLED B3","OLED C3","OLED G3","OLED Z3",
            "OLED A4","OLED B4","OLED C4","OLED G4","OLED M4",
            "NanoCell 75","NanoCell 86","NanoCell 90",
            "QNED 80","QNED 85","QNED 90","QNED 99",
            "UHD UP77","UHD UP80",
        ],
        "Sony": [
            "Bravia XR A80L","Bravia XR A90L","Bravia XR A95L",
            "Bravia XR X90L","Bravia XR X93L","Bravia XR X95L",
            "Bravia 7","Bravia 8","Bravia 9",
        ],
        "Philips": [
            "OLED+908","OLED+937","OLED+957","OLED+937",
            "Ambilight 7608","Ambilight 8808","Ambilight PUS8108",
        ],
        "Hisense": [
            "U8K","U9K","U7K","U6K",
            "ULED Mini-LED 75U8K","ULED Plus 65U7K",
            "A6K","A7K",
        ],
        "TCL": [
            "C935","C845","C745","C645",
            "QLED 55C735","QLED 65C835",
            "Mini LED 65C935",
        ],
        "Mi/Xiaomi": [
            "TV A2 32","TV A2 43","TV A2 50","TV A2 55","TV A2 65",
            "TV 5X 55","TV 5X 65","TV Max 86","TV A Pro 55","TV A Pro 65",
        ],
        "Panasonic": [
            "OLED MZ1500","OLED MZ1000","OLED LZ1000",
            "LED MX800","LED LX650","LED LX600",
        ],
    },

    "Бытовая техника": {
        "Холодильники Samsung": [
            "RB34A7B5D","RS68A8840","RF65A967","Side by Side RL34","French Door RF23",
        ],
        "Холодильники LG": [
            "GC-B459SMUM","GN-H702HMHZ","GSJ760PZXV","Door-in-Door GSXV91",
        ],
        "Холодильники Bosch": [
            "KGN39XIEP","KGN39VXBT","KGV36VWEAS","KSV36BIEP","KAN92LB35",
        ],
        "Холодильники Indesit": [
            "DF 4180 W","ITS 4180 W","ITR 4180 W","DS 4200 SB",
        ],
        "Стиральные машины Samsung": [
            "WW90T4541AE","WW11BGA046AE","WD80T554CBX","WD10T654DBH",
        ],
        "Стиральные машины LG": [
            "F2V5GS0W","F4WV509S1","FH4G1BCS2","F4WV710S2T",
        ],
        "Стиральные машины Bosch": [
            "WGG14400OE","WGB256A40","WGB25400ME","WAXH2E40ME",
        ],
        "Пылесосы Dyson": [
            "V8 Animal","V10 Absolute","V11 Torque Drive","V12 Detect Slim","V15 Detect",
            "Gen5detect","360 Heurist","360 Vis Nav","Omni-Glide",
        ],
        "Пылесосы Xiaomi": [
            "G9 Plus","G10 Plus","G11","G20 Lite","H10 Flex","B101CN","STYTJ06ZHM",
        ],
        "Пылесосы Philips": [
            "XC3154","XC7055","FC9552","FC9748","SpeedPro Max XC7742",
        ],
        "Роботы-пылесосы": [
            "Roomba i7+","Roomba j7+","Roomba Combo j9+",
            "Roborock S8 Pro Ultra","Roborock S7 MaxV","Roborock Q8 Max",
            "Xiaomi Mi Robot Vacuum Mop 2 Ultra","Dreame L10s Ultra","Ecovacs Deebot T20",
        ],
        "Микроволновки": [
            "Samsung MG23K3575AW","LG MS2044DB","Panasonic NN-ST342W",
        ],
        "Посудомоечные машины": [
            "Bosch SMS45DI10Q","Electrolux EEM43200L","Beko DFN29330W",
        ],
    },

    "Одежда": {
        "Nike": [
            "Air Max 90","Air Max 95","Air Max 97","Air Max 270","Air Max 2090",
            "Air Force 1 Low","Air Force 1 Mid","Air Force 1 High",
            "Dunk Low","Dunk Mid","Dunk High",
            "Air Jordan 1 Low","Air Jordan 1 Mid","Air Jordan 1 Retro High",
            "Air Jordan 4","Air Jordan 11","Jordan 3 Retro",
            "Tech Fleece Hoodie","Tech Fleece Jogger","Sportswear Club Fleece",
            "Blazer Low","Blazer Mid","React Infinity","Pegasus 40","Vaporfly",
        ],
        "Adidas": [
            "Ultraboost 22","Ultraboost 23","Ultraboost Light",
            "NMD R1","NMD R2","NMD V3",
            "Superstar","Gazelle","Samba","Campus",
            "Stan Smith","Forum Low","Forum Mid",
            "Yeezy 350 V2","Yeezy 500","Yeezy 700","Yeezy Slide",
            "Originals Trefoil Hoodie","Tiro 23","Condivo 22","Squadra 21",
        ],
        "Puma": [
            "RS-X","Suede Classic","Future Rider","Cali","Clyde","Slipstream",
            "Palermo","Speedcat","Mirage Mox","Tsugi Netfit",
        ],
        "New Balance": [
            "990v5","990v6","574","550","2002R","327","530","9060","1080v12","Fresh Foam X",
        ],
        "Converse": [
            "Chuck Taylor All Star Low","Chuck Taylor All Star High",
            "Chuck 70 Low","Chuck 70 High","One Star","Run Star Hike",
        ],
        "Vans": [
            "Old Skool","Sk8-Hi","Era","Authentic","Slip-On","Half Cab","Waffle One",
        ],
        "Zara": [
            "Куртки","Пальто","Парки","Кардиганы","Свитеры","Толстовки",
            "Футболки","Поло","Рубашки",
            "Джинсы","Брюки","Шорты","Юбки","Платья","Костюмы",
        ],
        "H&M": [
            "Футболки","Худи","Толстовки","Джинсы","Брюки","Шорты",
            "Куртки","Пальто","Платья","Юбки",
        ],
        "Uniqlo": [
            "Ultra Light Down Jacket","Ultra Light Down Vest","Ultra Light Down Parka",
            "AIRism T-Shirt","Heattech Extra Warm","Heattech Cotton",
            "Flannel Shirt","Oxford Shirt","KAWS","Lemaire Collection",
        ],
        "Stone Island": [
            "Осенняя коллекция","Зимняя коллекция","Shadow Project","Junior",
        ],
        "The North Face": [
            "Nuptse Jacket","Thermoball","Gotham","McMurdo","1996 Retro Nuptse",
            "Venture 2","Resolve","Hedgehog Fastpack","VECTIV",
        ],
        "Supreme": [
            "Box Logo Hoodie","Box Logo Tee","Camp Cap","5-Panel","Backpack",
        ],
        "Off-White": [
            "Industrial Belt","Arrows Hoodie","Diag Tee","Nike Collab",
        ],
        "Balenciaga": [
            "Triple S","Track","Speed Trainer","Defender","Runner",
            "Hoodie","Tee","Cargo Pants",
        ],
        "Gucci": [
            "Ace Sneakers","Rhyton","Flashtrek",
            "GG Supreme Bag","Dionysus Bag","Marmont Bag",
            "Bomber Jacket","Polo Shirt",
        ],
        "Louis Vuitton": [
            "Speedy","Neverfull","Keepall","Dauphine","Twist",
            "Archlight Sneaker","Run Away Sneaker","Trainer",
        ],
    },

    "Недвижимость": {
        "Квартиры": [
            "Студия","Апартаменты","1-комнатная","2-комнатная","3-комнатная",
            "4-комнатная","5-комнатная","Многокомнатная","Пентхаус","Мансарда",
        ],
        "Дома": [
            "Частный дом","Коттедж","Таунхаус","Дуплекс","Дача","Садовый дом","Ферма",
        ],
        "Коммерческая": [
            "Офис","Торговое помещение","Магазин","Склад","Производство",
            "Ресторан / Кафе","Гараж","Автосервис","Гостиница","Медцентр",
        ],
        "Земля": [
            "ИЖС","СНТ","ЛПХ","Сельхозназначение","Промназначение","Лесной участок",
        ],
        "Зарубежная": [
            "Турция","ОАЭ","Таиланд","Испания","Черногория","Грузия","Кипр",
        ],
        "Гаражи и машиноместа": [
            "Гараж","Машиноместо в паркинге","Бокс","Ракушка",
        ],
    },

    "Запчасти": {
        "Двигатель": [
            "Контрактный двигатель","Новый двигатель","Б/у двигатель",
            "Турбина","Компрессор","Головка блока","Блок цилиндров",
            "Коленвал","Распредвал","Шатун","Поршень","Масляный насос",
        ],
        "КПП и трансмиссия": [
            "АКПП контрактная","МКПП контрактная","Вариатор","Роботизированная КПП",
            "Карданный вал","Дифференциал","Раздаточная коробка","Сцепление",
        ],
        "Подвеска": [
            "Амортизаторы","Пружины","Рычаги","Стойки","Ступицы","Подшипники",
            "Шаровые опоры","Наконечники рулевые","Стабилизатор",
        ],
        "Кузов": [
            "Капот","Крылья","Бампер передний","Бампер задний","Двери",
            "Лонжероны","Пороги","Крыша","Крышка багажника","Зеркала",
        ],
        "Электрика": [
            "Фары","Фонари задние","Генератор","Стартер","Аккумулятор",
            "ЭБУ двигателя","Блок управления АКПП","Датчики","Проводка",
        ],
        "Тормозная система": [
            "Тормозные диски","Тормозные колодки","Суппорты","Тормозной цилиндр","Тормозной шланг",
        ],
        "Шины и диски": [
            "Летние шины","Зимние шины","Всесезонные шины",
            "Штампованные диски","Литые диски","Кованые диски",
            "Колёса в сборе",
        ],
        "Стёкла и оптика": [
            "Лобовое стекло","Боковые стёкла","Заднее стекло","Фара LED","Фара ксенон",
        ],
        "Интерьер": [
            "Сиденья","Торпеда","Руль","Накладки","Ковры",
        ],
        "Аксессуары": [
            "Накидки на сиденья","Автохимия","Регистратор","Навигатор","Антирадар",
            "Парктроник","Камера заднего вида","Коврики в салон","Багажник на крышу",
        ],
    },

    "Услуги": {
        "Ремонт техники": [
            "Ремонт телефонов","Замена экрана","Замена аккумулятора",
            "Ремонт ноутбуков","Чистка ноутбука","Замена матрицы",
            "Ремонт телевизоров","Ремонт планшетов","Ремонт наушников",
        ],
        "Ремонт авто": [
            "Кузовной ремонт","Покраска","Рихтовка","Полировка",
            "Ремонт двигателя","Замена масла","Диагностика",
            "Шиномонтаж","Развал-схождение","Тонировка",
        ],
        "Ремонт квартир": [
            "Косметический ремонт","Капитальный ремонт","Дизайн интерьера",
            "Поклейка обоев","Укладка плитки","Натяжные потолки",
            "Установка окон","Сантехника","Электрика",
        ],
        "Строительство": [
            "Строительство домов","Фундамент","Кровля","Фасад","Теплоизоляция",
        ],
        "Красота и здоровье": [
            "Маникюр","Педикюр","Ламинирование ресниц","Брови","Татуаж",
            "Парикмахер","Стрижка","Окрашивание","Кератин",
            "Массаж","Косметолог","Солярий","Визаж",
        ],
        "IT услуги": [
            "Создание сайтов","Разработка приложений","Дизайн логотипа",
            "SEO продвижение","Настройка рекламы","SMM","Фотосъёмка","Видеосъёмка",
            "Восстановление данных","Настройка компьютеров","Программирование",
        ],
        "Обучение": [
            "Репетитор по математике","Репетитор по физике","Репетитор по английскому",
            "Подготовка к ЕГЭ","Курсы программирования","Курсы дизайна","Курсы вождения",
            "Онлайн-обучение","Бизнес-коучинг",
        ],
        "Грузоперевозки": [
            "Газель","Переезд квартирный","Межгородские перевозки","Грузчики",
        ],
    },

    "Товары для дома": {
        "Мебель": [
            "Диван","Кресло","Кровать","Матрас","Шкаф","Комод",
            "Стол обеденный","Стул","Табурет","Тумба","Стеллаж","Полка",
            "Детская кровать","Двухъярусная кровать","Письменный стол",
        ],
        "Освещение": [
            "Люстра","Торшер","Настольная лампа","Бра","Светодиодная лента",
            "Умная лампа Яндекс","Умная лампа Xiaomi","Трековый светильник",
        ],
        "Текстиль": [
            "Постельное бельё","Подушка","Одеяло","Плед","Покрывало",
            "Полотенца","Шторы","Ковёр","Ковровая дорожка",
        ],
        "Посуда и кухня": [
            "Кастрюля","Сковорода","Нож кухонный","Разделочная доска",
            "Тарелки","Кружки","Термос","Блендер","Миксер","Мультиварка",
        ],
        "Инструменты": [
            "Дрель","Шуруповёрт","Перфоратор","Болгарка","Сварочный аппарат",
            "Набор инструментов","Лобзик","Рулетка","Уровень",
        ],
        "Сантехника": [
            "Ванна","Душевая кабина","Унитаз","Умывальник","Смеситель",
            "Полотенцесушитель","Водонагреватель","Фильтр воды",
        ],
    },

    "Детские товары": {
        "Коляски": [
            "Прогулочная коляска","Люлька","Трансформер 2в1","Трансформер 3в1",
            "Joie Litetrax","Bugaboo Fox","Cybex Mios","Stokke Xplory",
        ],
        "Автокресла": [
            "Группа 0+","Группа 1","Группа 2-3","Изофикс",
            "Cybex Cloud","Maxi-Cosi","Britax Römer",
        ],
        "Игрушки": [
            "Конструктор LEGO","Кубики","Пазлы","Куклы","Машинки",
            "Мягкие игрушки","Настольные игры","Развивающие игры",
            "Радиоуправляемые","Nerf","Hot Wheels",
        ],
        "Одежда детская": [
            "Для новорождённых","0-3 года","3-7 лет","7-12 лет","Подростковая",
        ],
        "Школьные товары": [
            "Рюкзак школьный","Пенал","Тетради","Карандаши","Краски","Пластилин",
        ],
        "Питание": [
            "Детское питание","Смеси","Пюре","Бутылочки","Стерилизаторы",
        ],
    },

    "Спорт и отдых": {
        "Велосипеды": [
            "Горный велосипед","Шоссейный","Городской","BMX","Электровелосипед",
            "Trek","Specialized","Giant","Cube","Cannondale","Scott",
        ],
        "Самокаты": [
            "Xiaomi Electric Scooter","Ninebot Max","Kugoo M2 Pro","Dualtron","Электросамокат детский",
        ],
        "Тренажёры": [
            "Беговая дорожка","Велотренажёр","Эллипсоид","Гребной тренажёр",
            "Штанга","Гантели","Гири","Турник","Шведская стенка",
        ],
        "Туризм": [
            "Палатка","Спальный мешок","Рюкзак туристический","Коврик","Горелка",
            "Треккинговые палки","Фонарь налобный","Котелок",
        ],
        "Лыжи и сноуборд": [
            "Горные лыжи","Лыжные ботинки","Сноуборд","Крепления","Шлем горнолыжный",
            "Очки горнолыжные","Лыжные палки","Беговые лыжи",
        ],
        "Фитнес": [
            "Коврик для йоги","Фитнес-резинки","Скакалка","Хула-хуп",
            "Гантели разборные","Утяжелители","Пояс для похудения",
        ],
        "Командные виды": [
            "Мяч футбольный","Мяч баскетбольный","Мяч волейбольный",
            "Бутсы","Кроссовки для зала","Форма спортивная",
        ],
        "Водный спорт": [
            "SUP-доска","Каяк","Каноэ","Гидрокостюм","Маска для дайвинга",
        ],
    },

    "Другое": {
        "Антиквариат и коллекции": [
            "Монеты","Банкноты","Марки","Картины","Статуэтки","Старинная мебель",
            "Пластинки виниловые","Старые книги","Фотоаппараты плёночные",
        ],
        "Животные": [
            "Щенки","Котята","Попугаи","Аквариумные рыбки","Черепахи",
            "Хомяки","Кролики","Морские свинки","Улитки","Экзотические животные",
        ],
        "Корм для животных": [
            "Корм для кошек","Корм для собак","Корм для птиц",
            "Royal Canin","Hill's","Purina Pro Plan","Whiskas","Pedigree",
        ],
        "Книги и журналы": [
            "Художественная литература","Учебники","Детские книги",
            "Бизнес и саморазвитие","Техническая литература","Комиксы и манга",
        ],
        "Музыкальные инструменты": [
            "Гитара акустическая","Гитара электрическая","Бас-гитара","Укулеле",
            "Пианино","Синтезатор","Барабанная установка","Скрипка","Труба","Саксофон",
            "DJ-контроллер","Midi-клавиатура","Педали эффектов",
        ],
        "Растения": [
            "Комнатные цветы","Рассада","Семена","Кашпо","Грунт",
        ],
        "Разное": [
            "Б/у","Новое","Подарочные сертификаты","Обмен",
        ],
    },
}


def add_data(apps, schema_editor):
    Category = apps.get_model("ads", "Category")
    Brand = apps.get_model("ads", "Brand")
    Model = apps.get_model("ads", "Model")

    for category_name, brands in DATA.items():
        category, _ = Category.objects.get_or_create(name=category_name)
        for brand_name, models in brands.items():
            brand, _ = Brand.objects.get_or_create(name=brand_name, category=category)
            for model_name in models:
                Model.objects.get_or_create(name=model_name, brand=brand)


def remove_data(apps, schema_editor):
    Category = apps.get_model("ads", "Category")
    Category.objects.filter(name__in=DATA.keys()).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0025_seed_categories"),
    ]

    operations = [
        migrations.RunPython(add_data, remove_data),
    ]
