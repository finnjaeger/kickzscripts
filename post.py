from enum import Enum

class PostType(Enum):
    PHOTO = 1
    VIDEO = 2
    ALBUM = 8


class Post:

    pk = 0
    shortcode = "shortcode"
    thumbnail = "thumbnail"
    likes = 0
    comments = 0
    caption = "caption"
    post_type = PostType.PHOTO
    photoLocation = "String"
    notDownloadable = False
    hashtags = []
    brand = "Misc"
    category = "None"

    def __init__(self, sc, tn, l, com, cap, dt, p, typ, ht):
        self.pk = p
        self.shortcode = sc
        self.thumbnail = tn
        self.likes = l
        self.comments = com
        self.caption = cap
        self.datetime = dt
        self.post_type = typ
        self.hashtags = ht 


    def findCategory(self, tags: list):
        c = "None"
        categories = {
            "basketballobsessed": "Basketball",
            "streetwear": "Streetwear",
            "fortheculture": "Culture"
        }
        for hashtag in tags:
            hashtag = hashtag.lower()
            try:
                c = categories[hashtag]
                break
            except:
                print()
        return c


    def findBrand(self, tags: list):
        b = "Misc"
        brands = {
            "47": "47",
            "adidasoriginals": "adidas",
            "adidasperformance": "adidas",
            "adidas": "adidas",
            "alphaindustries": "alphaindustries",
            "arys": "arys",
            "asics": "asics",
            "bauerfeind": "bauerfeind",
            "bayernhustlesharder": "bayernhustlesharder",
            "betoncire": "betoncire",
            "birkenstock": "birkenstock",
            "calvinkleinjeans": "calvinklein",
            "calvinklein": "calvinklein",
            "ck": "calvinklein",
            "carhartt wip": "carhartt",
            "carhartt": "carhartt",
            "champion": "champion",
            "championreverseweave": "champion",
            "chimodu": "chimodu",
            "chinatownmarket": "chinatownmarket",
            "clarksoriginals": "clarks",
            "clarks": "clarks",
            "columbia": "columbia",
            "converse": "converse",
            "devastates": "devastates",
            "dfns": "dfns",
            "diaperbookclub": "diaperbookclub",
            "dickies": "dickies",
            "drmartens": "dr. martens",
            "docmartens": "dr. martens",
            "eastpak": "eastpak",
            "ellesse": "ellesse",
            "euroleague": "euroleague",
            "ewingathletics": "ewingathletics",
            "fillingpieces": "fillingpieces",
            "five": "five",
            "flexfit": "flexfit",
            "folk": "folk",
            "funko": "funko",
            "greatamerican": "great american",
            "guess": "guess",
            "guessjeans": "guess",
            "hankjobenhavn": "han kjobenhavn",
            "harmony": "harmony",
            "helmutlang": "helmut lang",
            "heresy": "heresy",
            "herschel": "herschel",
            "honorthegift": "honor the gift",
            "htg": "honor the gift",
            "huf": "huf",
            "hyperice": "hyperice",
            "jasonmarkk": "jasonmarkk",
            "jordan": "jordan",
            "jordankids": "jordankids",
            "junglesjungles": "jungles jungles",
            "jungles": "jungles jungles",
            "k1x": "k1x",
            "k1xwmns": "k1x",
            "kappa": "kappa",
            "karlkani": "karl kani",
            "kreem": "kreem",
            "kreemo": "kreemo",
            "lacoste": "lacoste",
            "market": "market",
            "mcdavid": "mcdavid",
            "mistertee": "mister tee",
            "mitchellandness": "mitchell and ness",
            "mizuno": "mizuno",
            "molten": "molten",
            "newbalance": "new balance",
            "nb": "new balance",
            "newera": "new era",
            "nike": "nike",
            "nikekids": "nike",
            "norseprojects": "norse projects",
            "northwest": "northwest",
            "on": "on",
            "ourlegacy": "our legacy",
            "ovadiaandsons": "ovadia and sons",
            "panini": "panini",
            "peak": "peak",
            "penfield": "penfield",
            "playdude": "playdude",
            "pleasures": "pleasures",
            "poloralphlauren": "polo ralph lauren",
            "polo": "polo ralph lauren",
            "porteryoshida&co": "porter yoshida & co",
            "porteryoshida": "porter yoshida & co",
            "puma": "puma",
            "raisedbywolves": "raised by wolves",
            "reebok": "reebok",
            "reell": "reell",
            "rokit": "rokit",
            "seanjohn": "sean john",
            "sergiotacchini": "sergio tacchini",
            "socksss": "socksss",
            "soleyama": "soleyama",
            "soulland": "soulland",
            "spalding": "spalding",
            "stance": "stance",
            "starter": "starter",
            "stepneyworkersclub": "stepneyworkersclub",
            "sunspel": "sunspel",
            "taschen": "taschen",
            "thenorthface": "the north face",
            "tnf": "the north face",
            "timberland": "timberland",
            "tommyjeans": "tommy hilfiger",
            "tommyhilfiger": "tommy hilfiger",
            "tommysport": "tommysport",
            "ultrapro": "ultra pro",
            "underarmour": "under armor",
            "ua": "under armor",
            "unfairathletics": "unfair athletics",
            "urbanclassics": "urban classics",
            "vans": "vans",
            "vondutch": "vondutch",
            "vor": "vor",
            "vorshoes": "vor",
            "wilson": "wilson",
            "wincraft": "wincraft",
            "woodwood": "wood wood",
            "woolrich": "woolrich",
            "ymc": "ymc",
            "youmustcreate": "ymc",
        }
        for hashtag in tags:
            hashtag = hashtag.lower()
            try:
                b = brands[hashtag]
                break
            except:
                print()
        return b  
                

