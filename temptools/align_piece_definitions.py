import json

def get_known_kanji():
    file1 = open(".\\new_kanji\\new_kanji.json", 'r', encoding="utf-8")
    new_kanji_data = json.load(file1)
    file1.close()
    return new_kanji_data

def load_piece_definitions(filename="..\\chess_variant_boardpainter\\piecedefinitions\\chushogipiecedefinitions.csv"):
    mypiecedefinitions = []
    File1 = open(filename, 'r')
    Lines = File1.readlines()
    for line in Lines:
        s = line.replace("\n", "")
        a = s.split(",")
        mypiecedefinitions.append((a[0], a[1]))
    File1.close()
    return mypiecedefinitions

def latin_abbreviation_set():
    LAS = set([pc[0].upper() for pc in mypiecedefinitions])
    return LAS

def enforce_uniqueness_latin_abbreviation():
    LAS = latin_abbreviation_set()
    if len(LAS) != len(mypiecedefinitions):
        raise Exception("Latin abbreviations no longer unique")

def write_piece_definitions(filename=".\\new_piecedefinitions\\chushogipiecedefinitions.csv"):
    File2 = open(filename, 'w')
    for pc in mypiecedefinitions:
        s = pc[0] + "," + pc[1] + "\n"
        File2.write(s)
    File2.close()

def hardcoded_definitions():
    global mypiecedefinitions
    hd = []
    #hd.append(('Dv', 'Deva'))
    mypiecedefinitions.extend(hd)


def try_meaningless(piecename):
    global seqnr
    piecename2 = piecename[0].upper() + piecename[1:]
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [a[i] for i in range(len(a))]
    c = ['8', '7', '6', '5', '4', '3', '2']
    d = []
    for x in c:
        for y in b:
            d.append(x + y)
    abbr = d[seqnr]
    seqnr += 1
    return (abbr, piecename2)

def try_automate_from_piecename(piecename):
    piecename2 = piecename[0].upper() + piecename[1:]
    a = piecename.split("_")
    abbr = "".join([x[0].upper() for x in a])
    if len(abbr) > 2:
        abbr = abbr[:2]
    return (abbr, piecename2)

def process_new_kanji_item(item):
    global mypiecedefinitions

    if item == "king_sente":
        return
    if item == "king_gote":
        return

    trymeaningful = True

    piecefound = False
    s = new_kanji_data[item]['full_kanji']
    for pc in mypiecedefinitions:
        if item == pc[1].lower():
            piecefound = True
            #print(f"{item} found in piece definitions")
    if piecefound == False:
        a = try_automate_from_piecename(item)
        LAS = latin_abbreviation_set()
        if a[0].upper() in LAS or trymeaningful == False:
            b = try_meaningless(item)
            mypiecedefinitions.append(b)
        else:
            mypiecedefinitions.append(a)
        enforce_uniqueness_latin_abbreviation()

def process_new_kanji():
    for item in new_kanji_data:
        process_new_kanji_item(item)


new_kanji_data = get_known_kanji()
print(f"Loaded kanji for {len(new_kanji_data)} pieces")
mypiecedefinitions = load_piece_definitions()
print(f"Loaded piece definitions for {len(mypiecedefinitions)} pieces")

hardcoded_definitions()
enforce_uniqueness_latin_abbreviation()

seqnr = 0

process_new_kanji()

write_piece_definitions()
print(f"Written piece definitions for {len(mypiecedefinitions)} pieces")

