akamap = {
    ###########################################################################################################SPECIAL
    # acronym expansions
    "INTL FCStone Inc": ["International Assets Holding Corp", "FCStone Group"],
    "NFP Corp": "National Financial Partners",
    "NXXI Inc": "Nutrition 21 Inc",
    "CNX Gas Corp": "Consol Energy Inc",
    "WEX Inc": "Wright Express Corp",
    "LRAD Corp": "American Technology Corp",
    'RS Legacy Corp': 'RadioShack Corp',
    'L Brands Inc': 'Limited Brands Inc',
    'HP Inc': 'Hewlett-Packard Co', #DASH
    'Acas LLC': 'American Capital Ltd',
    'SLM Corp': 'Sallie Mae Corp',
    'Flex Ltd': 'Flextronics International Ltd',

    # straight up different name
    'Twenty-First Century Fox Inc': 'News Corporation',
    'Perrigo Corporation Ltd': 'Elan Corporation',
    'BlackBerry Ltd': ['Research In Motion Ltd', 'RIM'],
    'Mondelez International Inc': 'Kraft Foods Inc',
    'Chubb Ltd': 'Ace Ltd',
    'Anthem Inc': 'WellPoint Inc',
    'VEON Ltd': 'VimpelCom Ltd',
    'Blue Ridge Mountain Resources Inc': ['Magnum Hunter Resources Corp', 'Petro Resources Corp'],
    'Repsol Oil & Gas Canada Inc': 'Talisman Energy Inc',
    'Tegna Inc': 'Gannett Co Inc',
    'Hillshire Brands Co': 'Sara Lee Corp',
    'S&P Global Inc': ['McGraw-Hill Cos Inc', 'McGraw-Hill Companies Inc', 'McGraw-Hill Financial Inc'], #DASH
    'Leidos Holdings Inc': ['Science Applications International Corporation', 'SAIC'],
    'Keurig Green Mountain Inc': 'Green Mountain Coffee Roasters Inc',
    'Orbital ATK Inc': ['Alliant Techsystems Inc', 'Orbital Sciences Corp', 'ATK'],
    'Komatsu Mining Corp': 'Joy Global Inc',
    'Ionis Pharmaceuticals Inc': 'Isis Pharmaceuticals Inc',
    'Lanxess Solutions Us Inc': 'Chemtura',
    'United Continental Holdings Inc': 'UAL Corp',
    'American Outdoor Brands Corp': 'Smith & Wesson Holding Corp',
    'Energy Transfer Partners LP': 'Sunoco Logistics Partners LP',
    'Kate Spade & Co': 'Liz Claiborne Inc',
    'American Airlines Group Inc': 'AMR Corp',
    'Wendys Co': ["Wendy's", 'Triarc Cos Inc'],
    'Alpha Appalachia Holdings Inc': 'Massey Energy Co',
    'Westrock MWV LLC': 'MeadWestvaco Corp',
    'Targa Pipeline Partners LP': ['Atlas Pipeline Partners, L.P.', 'Atlas Energy Resources, LLC'],

    # straight up different, but it's just a nickname
    'Federal Home Loan Mortgage Corp': 'Freddie Mac',
    "Federal National Mortgage Association": "Fannie Mae",
    'China Petroleum & Chemical Corp': 'Sinopec',
    'Aluminum Corp of China Ltd': 'Chalco',
    'Laboratory Corporation of America Holdings': 'LabCorp',

    # foreign non-obvious acronyms / mergers / the likes
    "Mobil\'nye Telesistemy PAO": "MTS",
    'Petroleo Brasileiro SA Petrobras': 'Petrobras',
    'Arconic Inc': 'Alcoa',
    'Toronto-Dominion Bank': ['TD Bank', 'TD Canada Trust'],
    'Herc Holdings Inc': 'Hertz Global Holdings Inc',
    'Bank of Nova Scotia': 'Scotiabank',
    'ConocoPhillips': ['Conoco Inc', 'Phillips Petroleum Co'],
    'Kraft Heinz Foods Co': ['H. J. Heinz Co', 'HJ Heinz Co', 'Heinz'],

    # partial matches
    'Citigroup Inc': 'Citi',
    'GlaxoSmithKline PLC': 'Glaxo',
    'Walgreen Co': 'Walgreens',

    # special cases that almost fit a pattern but don't
    'Amazon.com Inc': 'Amazon Inc',
    'Bank of America Corp': ['BofA', 'B of A'],
    'E I du Pont de Nemours and Co': 'DuPont',
    'Bank of Montreal': 'BMO',
    'JPMorgan Chase & Co': ['JP Morgan Chase', 'JPMorganChase', 'JPM'],
    'Exxon Mobil Corp': 'ExxonMobil',
    'J C Penney Company Inc': 'J.C. Penney Co Inc',
    'Kohls Corp': "Kohl's Corp",
    "Dr.Reddy's Laboratories Ltd": 'Dr Reddys Laboratories',
    'Lions Gate Entertainment Corp': 'Lionsgate',
    'Canadian National Railway Co': 'CN Rail',
    'Canadian Pacific Railway Ltd': 'CP Rail',
    'Intercontinental Exchange Inc': ['IntercontinentalExchange Inc', 'ICE'],
    "Childrens Place Inc": ["The Children's Place Retail Stores, Inc.", "Children's Place Retail Stores, Inc."],

    #####################################################################################################SPECIAL
    # almost acronyms were it not for stopwords
    'Royal Bank of Scotland Group PLC': 'RBS',
    "Royal Bank of Canada": "RBC",
    'Canadian Imperial Bank of Commerce': 'CIBC',

    # acronyms
    "O I Corp": "OI Corp",
    "Semiconductor Manufacturing International Corp": "SMIC",
    "General Electric Co": "GE",
    'International Business Machines Corp': 'IBM',
    'American International Group Inc': 'AIG Inc',
    'General Motors Co': 'GM',
    'United Parcel Service Inc': 'UPS',
    'Advanced Micro Devices Inc': 'AMD',
    'Johnson & Johnson': ['JNJ', 'J&J'],
    'Procter & Gamble Co': 'P&G',
    'Banco Bilbao Vizcaya Argentaria S.A.': 'BBVA',
    'Automatic Data Processing Inc': 'ADP',
    'Taiwan Semiconductor Manufacturing Co Ltd': 'TSMC',
    'Electronic Arts Inc': 'EA',
    'American Electric Power Company Inc': 'AEP',
    'Archer Daniels Midland Co': 'ADM',
    'Texas Instruments Inc': 'TI',
    'United Microelectronics Corp': 'UMC',
    'Illinois Tool Works Inc': 'ITW',
    'Chicago Bridge & Iron Company NV': 'CB&I',

    ###################################################################################################SPECIAL
    # combo case
    'Bank of New York Mellon Corp': ['BNY Mellon', 'Mellon'],
    'Fiat Chrysler Automobiles NV': ['FCA', 'Chrysler Automobiles'],

    # name starts in middle of official name
    "Telefonaktiebolaget LM Ericsson": "Ericsson",
    'Royal Dutch Shell PLC': 'Shell',
    'BHP Billiton PLC': 'Billiton',
    'Banco Santander SA': 'Santander',
    'Walt Disney Co': 'Disney',
    'Koninklijke Philips NV': 'Philips',
    'Eli Lilly and Co': 'Lilly',
    'Charles Schwab Corp': 'Schwab',
    'ZF TRW Automotive Holdings Corp': 'TRW Automotive Holdings Corp',

}