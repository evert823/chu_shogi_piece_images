import pandas as pd
import json

def get_known_kanji():
    file1 = open("..\\chu_shogi_piece_images\\kanji\\kanji.json", 'r', encoding="utf-8")
    known_kanji_data = json.load(file1)
    file1.close()
    return known_kanji_data

def write_kanji(kanji_data, shortfilename):
    file2 = open(f".\\new_kanji\\{shortfilename}.json", 'w', encoding="utf-8")
    json.dump(kanji_data, file2, ensure_ascii=False, indent=4)
    file2.close()

def clean_piecename(piecename):
    s = piecename.lower().replace(" ", "_")
    s = s.replace("-", "_")
    s = s.replace("*", "")
    s = s.replace("'", "")
    s = s.replace("flyer", "flier")
    if s == "gobetween":
        return "go_between"
    if s == "yaksha":
        return "she_devil"
    if s[:14] == "great_elephant":
        return "great_elephant"
    if s == "drunken_elephant":
        return "drunk_elephant"
    if s == "running_chariot":
        return "racing_chariot"
    if s == "front_standard":
        return "standard_bearer"
    if s == "dove":
        return "wooden_dove"
    if s.find("king") > -1 and s.find("challen") > -1:
        return "king_sente"
    if s.find("king") > -1 and s.find("rei") > -1:
        return "king_gote"
    if s == "king":
        return "king_sente"
    if s == "jeweled_general":
        return "king_sente"
    if s == "king_general":
        return "king_gote"
    if s.find("_(") > -1:
        s = s[:s.find("_(")]
    if s.find("[") > -1:
        s = s[:s.find("[")]
    if s == "silver_hare":
        return "silver_rabbit"
    return s

def clean_kanji_row(row):
    global known_kanji_data
    foundname = row[col_piecename]
    if isinstance(foundname, str) == False:
        return
    cleanname = clean_piecename(foundname)
    item = None
    remark = ""
    if col_single_kanji == "":
        k1_in = "."
    else:
        k1_in = row[col_single_kanji]

    k2_in = row[col_full_kanji]
    if isinstance(k2_in, str) == False:
        return

    k2_in = k2_in.replace('†', '')
    k2_in = k2_in.replace(' ', '')
    k2_in = k2_in.replace('(自在)天王', '自在')
    try:
        item = known_kanji_data[cleanname]
        if k1_in != item['single_kanji']:
            remark += " mismatch single kanji"
        if k2_in != item['full_kanji']:
            remark += " mismatch full kanji"
    except:
        remark = " NOT FOUND IN KNOWN KANJI - NOW ADDING"
        known_kanji_data[cleanname] = {"full_kanji": k2_in, "single_kanji": k1_in}
        print(f"{cleanname},{remark}")

def clean_kanji(df):
    for _, row in df.iterrows():
        clean_kanji_row(row)

def get_tenjiku():
    global col_piecename
    global col_full_kanji
    global col_single_kanji
    col_piecename = "Piece"
    col_full_kanji = "Kanji"
    col_single_kanji = "Abbrev..1"
    list_of_df = pd.read_html("https://en.wikipedia.org/wiki/Tenjiku_shogi")
    df = list_of_df[0]
    return df

def get_dai():
    global col_piecename
    global col_full_kanji
    global col_single_kanji
    col_piecename = "Piece name"
    col_full_kanji = "Kanji"
    col_single_kanji = "Abbrev."
    list_of_df = pd.read_html("https://en.wikipedia.org/wiki/Dai_shogi")
    df = list_of_df[0]
    return df

def get_dai_dai():
    global col_piecename
    global col_full_kanji
    global col_single_kanji
    col_piecename = "Piece"
    col_full_kanji = "Kanji"
    col_single_kanji = "Abbrev..1"
    list_of_df = pd.read_html("https://en.wikipedia.org/wiki/Dai_dai_shogi")
    df = list_of_df[0]
    return df

def get_maka_dai_dai():
    global col_piecename
    global col_full_kanji
    global col_single_kanji
    col_piecename = "Piece"
    col_full_kanji = "Kanji"
    col_single_kanji = ""
    list_of_df = pd.read_html("https://en.wikipedia.org/wiki/Maka_dai_dai_shogi")
    df = list_of_df[1]
    return df

def get_tai():
    global col_piecename
    global col_full_kanji
    global col_single_kanji
    col_piecename = "Piece (*promoted piece only)"
    col_full_kanji = "Kanji"
    col_single_kanji = ""
    list_of_df = pd.read_html("https://en.wikipedia.org/wiki/Tai_shogi")
    df = list_of_df[0]
    return df

def get_taikyoku():
    global col_piecename
    global col_full_kanji
    global col_single_kanji
    print("Tenjiku")
    col_piecename = "Piece"
    col_full_kanji = "Kanji"
    col_single_kanji = ""
    df = pd.read_csv(".\\taikyoku.csv", sep='\t')
    #list_of_df = pd.read_html("https://en.wikipedia.org/wiki/Taikyoku_shogi")
    #df = list_of_df[1][1:]
    print(df)
    return df

def get_taikyoku2():
    global col_piecename
    global col_full_kanji
    global col_single_kanji
    print("Tenjiku")
    col_piecename = "Promotes to"
    col_full_kanji = "Kanji.1"
    col_single_kanji = ""
    df = pd.read_csv(".\\taikyoku.csv", sep='\t')
    #list_of_df = pd.read_html("https://en.wikipedia.org/wiki/Taikyoku_shogi")
    #df = list_of_df[1][1:]
    print(df)
    return df


def validate_kanji():
    for item1 in known_kanji_data:
        for item2 in known_kanji_data:
            if item1 < item2:
                if known_kanji_data[item1]['full_kanji'] == known_kanji_data[item2]['full_kanji']:
                    print(f"{item1},{known_kanji_data[item1]},{item2},{known_kanji_data[item2]}")
    for item in known_kanji_data:
        s = known_kanji_data[item]['full_kanji']
        if len(s) != 2:
            print(f"{item},{known_kanji_data[item]}")

col_piecename = ""
col_full_kanji = ""
col_single_kanji = ""

known_kanji_data = get_known_kanji()
print(f"Loaded kanji for {len(known_kanji_data)} pieces")
write_kanji(known_kanji_data, "kanji")
df = get_tenjiku()
clean_kanji(df)
df = get_dai()
clean_kanji(df)
df = get_dai_dai()
clean_kanji(df)
df = get_maka_dai_dai()
clean_kanji(df)
df = get_tai()
clean_kanji(df)

df = get_taikyoku()
clean_kanji(df)
df = get_taikyoku2()
clean_kanji(df)



print(f"Writing new kanji for {len(known_kanji_data)} pieces")
write_kanji(known_kanji_data, "new_kanji")

validate_kanji()
