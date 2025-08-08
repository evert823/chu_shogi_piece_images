from classes.chu_piece_maker import ChuPieceMaker

def imagefilename(piecename: str, rotate: bool = False, ispromoted: bool = False):
    result = f"{outputpath}{piecename}"

    if piecename.endswith("_sente"):
        pass
    elif piecename.endswith("_gote"):
        pass
    else:
        if rotate:
            result += "_gote"
        else:
            result += "_sente"
    
    if ispromoted:
        result += "_promoted"

    result += ".png"
    return result

def create_piece_size_A_tokinstyle(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_fromjson(piecename=piecename, rotate=rotate, ispromoted=ispromoted, tiletypename="A_tokinstyle")
    MyChuPieceMaker.save_image(mypieceimage, imagefilename(piecename=piecename, rotate=rotate, ispromoted=ispromoted))

def create_piece_size_A(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_fromjson(piecename=piecename, rotate=rotate, ispromoted=ispromoted, tiletypename="A")
    MyChuPieceMaker.save_image(mypieceimage, imagefilename(piecename=piecename, rotate=rotate, ispromoted=ispromoted))

def create_piece_size_B(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_fromjson(piecename=piecename, rotate=rotate, ispromoted=ispromoted, tiletypename="B")
    MyChuPieceMaker.save_image(mypieceimage, imagefilename(piecename=piecename, rotate=rotate, ispromoted=ispromoted))

def create_piece_size_B_plus(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_fromjson(piecename=piecename, rotate=rotate, ispromoted=ispromoted, tiletypename="B_plus")
    MyChuPieceMaker.save_image(mypieceimage, imagefilename(piecename=piecename, rotate=rotate, ispromoted=ispromoted))

def create_piece_size_C(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_fromjson(piecename=piecename, rotate=rotate, ispromoted=ispromoted, tiletypename="C")
    MyChuPieceMaker.save_image(mypieceimage, imagefilename(piecename=piecename, rotate=rotate, ispromoted=ispromoted))

def create_piece_size_D(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_fromjson(piecename=piecename, rotate=rotate, ispromoted=ispromoted, tiletypename="D")
    MyChuPieceMaker.save_image(mypieceimage, imagefilename(piecename=piecename, rotate=rotate, ispromoted=ispromoted))

def add_for_tenjiku():
    create_piece_size_A_tokinstyle(piecename="dog")
    create_piece_size_A_tokinstyle(piecename="dog", rotate=True)
    create_piece_size_B_plus(piecename="side_soldier")
    create_piece_size_B_plus(piecename="side_soldier", rotate=True)
    create_piece_size_B_plus(piecename="vertical_soldier")
    create_piece_size_B_plus(piecename="vertical_soldier", rotate=True)
    create_piece_size_C(piecename="chariot_soldier")
    create_piece_size_C(piecename="chariot_soldier", rotate=True)
    create_piece_size_C(piecename="knight")
    create_piece_size_C(piecename="knight", rotate=True)
    create_piece_size_C(piecename="iron_general")
    create_piece_size_C(piecename="iron_general", rotate=True)
    create_piece_size_C(piecename="horned_falcon")
    create_piece_size_C(piecename="horned_falcon", rotate=True)
    create_piece_size_C(piecename="soaring_eagle")
    create_piece_size_C(piecename="soaring_eagle", rotate=True)
    create_piece_size_C(piecename="water_buffalo")
    create_piece_size_C(piecename="water_buffalo", rotate=True)
    create_piece_size_C(piecename="bishop_general")
    create_piece_size_C(piecename="bishop_general", rotate=True)
    create_piece_size_C(piecename="rook_general")
    create_piece_size_C(piecename="rook_general", rotate=True)
    create_piece_size_C(piecename="vice_general")
    create_piece_size_C(piecename="vice_general", rotate=True)
    create_piece_size_C(piecename="great_general")
    create_piece_size_C(piecename="great_general", rotate=True)
    create_piece_size_C(piecename="fire_demon")
    create_piece_size_C(piecename="fire_demon", rotate=True)
    create_piece_size_C(piecename="lion_hawk")
    create_piece_size_C(piecename="lion_hawk", rotate=True)
    create_piece_size_C(piecename="free_eagle")
    create_piece_size_C(piecename="free_eagle", rotate=True)

    create_piece_size_A(piecename="multi_general", ispromoted=True)
    create_piece_size_A(piecename="multi_general", ispromoted=True, rotate=True)
    create_piece_size_B_plus(piecename="chariot_soldier", ispromoted=True)
    create_piece_size_B_plus(piecename="chariot_soldier", ispromoted=True, rotate=True)
    create_piece_size_B_plus(piecename="water_buffalo", ispromoted=True)
    create_piece_size_B_plus(piecename="water_buffalo", ispromoted=True, rotate=True)
    create_piece_size_C(piecename="bishop_general", ispromoted=True)
    create_piece_size_C(piecename="bishop_general", ispromoted=True, rotate=True)
    create_piece_size_C(piecename="fire_demon", ispromoted=True)
    create_piece_size_C(piecename="fire_demon", ispromoted=True, rotate=True)
    create_piece_size_C(piecename="great_general", ispromoted=True)
    create_piece_size_C(piecename="great_general", ispromoted=True, rotate=True)
    create_piece_size_C(piecename="heavenly_tetrarch", ispromoted=True)
    create_piece_size_C(piecename="heavenly_tetrarch", ispromoted=True, rotate=True)
    create_piece_size_C(piecename="lion_hawk", ispromoted=True)
    create_piece_size_C(piecename="lion_hawk", ispromoted=True, rotate=True)
    create_piece_size_C(piecename="rook_general", ispromoted=True)
    create_piece_size_C(piecename="rook_general", ispromoted=True, rotate=True)
    create_piece_size_C(piecename="side_soldier", ispromoted=True)
    create_piece_size_C(piecename="side_soldier", ispromoted=True, rotate=True)
    create_piece_size_C(piecename="vertical_soldier", ispromoted=True)
    create_piece_size_C(piecename="vertical_soldier", ispromoted=True, rotate=True)
    create_piece_size_C(piecename="vice_general", ispromoted=True)
    create_piece_size_C(piecename="vice_general", ispromoted=True, rotate=True)
    create_piece_size_D(piecename="free_eagle", ispromoted=True)
    create_piece_size_D(piecename="free_eagle", ispromoted=True, rotate=True)

def create_complete_chu_set():
    create_piece_size_B(piecename="lance")
    create_piece_size_B(piecename="lance", rotate=True)
    create_piece_size_B(piecename="reverse_chariot")
    create_piece_size_B(piecename="reverse_chariot", rotate=True)
    create_piece_size_B(piecename="side_mover")
    create_piece_size_C(piecename="side_mover", ispromoted=True)
    create_piece_size_B(piecename="side_mover", rotate=True)
    create_piece_size_C(piecename="side_mover", rotate=True, ispromoted=True)
    create_piece_size_B_plus(piecename="ferocious_leopard")
    create_piece_size_B_plus(piecename="ferocious_leopard", rotate=True)
    create_piece_size_B(piecename="vertical_mover")
    create_piece_size_C(piecename="vertical_mover", ispromoted=True)
    create_piece_size_B(piecename="vertical_mover", rotate=True)
    create_piece_size_C(piecename="vertical_mover", rotate=True, ispromoted=True)
    create_piece_size_C(piecename="copper_general")
    create_piece_size_C(piecename="copper_general", rotate=True)
    create_piece_size_C(piecename="bishop")
    create_piece_size_B_plus(piecename="bishop", ispromoted=True)
    create_piece_size_C(piecename="bishop", rotate=True)
    create_piece_size_B_plus(piecename="bishop", rotate=True, ispromoted=True)
    create_piece_size_C(piecename="rook")
    create_piece_size_C(piecename="rook", ispromoted=True)
    create_piece_size_C(piecename="rook", rotate=True)
    create_piece_size_C(piecename="rook", rotate=True, ispromoted=True)
    create_piece_size_C(piecename="silver_general")
    create_piece_size_C(piecename="silver_general", rotate=True)
    create_piece_size_C(piecename="dragon_horse")
    create_piece_size_C(piecename="dragon_horse", ispromoted=True)
    create_piece_size_C(piecename="dragon_horse", rotate=True)
    create_piece_size_C(piecename="dragon_horse", rotate=True, ispromoted=True)
    create_piece_size_C(piecename="gold_general")
    create_piece_size_A(piecename="gold_general", ispromoted=True)
    create_piece_size_C(piecename="gold_general", rotate=True)
    create_piece_size_A(piecename="gold_general", rotate=True, ispromoted=True)
    create_piece_size_B_plus(piecename="blind_tiger")
    create_piece_size_B_plus(piecename="blind_tiger", rotate=True)
    create_piece_size_C(piecename="dragon_king")
    create_piece_size_C(piecename="dragon_king", ispromoted=True)
    create_piece_size_C(piecename="dragon_king", rotate=True)
    create_piece_size_C(piecename="dragon_king", rotate=True, ispromoted=True)
    create_piece_size_D(piecename="king_sente")
    create_piece_size_D(piecename="king_gote", rotate=True)
    create_piece_size_C(piecename="kirin")
    create_piece_size_C(piecename="kirin", rotate=True)
    create_piece_size_C(piecename="lion")
    create_piece_size_C(piecename="lion", ispromoted=True)
    create_piece_size_C(piecename="lion", rotate=True)
    create_piece_size_C(piecename="lion", rotate=True, ispromoted=True)
    create_piece_size_C(piecename="drunk_elephant")
    create_piece_size_A(piecename="drunk_elephant", ispromoted=True)
    create_piece_size_C(piecename="drunk_elephant", rotate=True)
    create_piece_size_A(piecename="drunk_elephant", rotate=True, ispromoted=True)
    create_piece_size_C(piecename="phoenix")
    create_piece_size_C(piecename="phoenix", rotate=True)
    create_piece_size_D(piecename="queen")
    create_piece_size_C(piecename="queen", ispromoted=True)
    create_piece_size_D(piecename="queen", rotate=True)
    create_piece_size_C(piecename="queen", rotate=True, ispromoted=True)
    create_piece_size_A(piecename="pawn")
    create_piece_size_A(piecename="pawn", rotate=True)
    create_piece_size_A(piecename="go_between")
    create_piece_size_A(piecename="go_between", rotate=True)
    create_piece_size_A_tokinstyle(piecename="tokin", ispromoted=True)
    create_piece_size_A_tokinstyle(piecename="tokin", rotate=True, ispromoted=True)
    create_piece_size_B(piecename="flying_ox", ispromoted=True)
    create_piece_size_B_plus(piecename="flying_stag", ispromoted=True)
    create_piece_size_B(piecename="free_boar", ispromoted=True)
    create_piece_size_C(piecename="horned_falcon", ispromoted=True)
    create_piece_size_C(piecename="prince", ispromoted=True)
    create_piece_size_C(piecename="soaring_eagle", ispromoted=True)
    create_piece_size_B(piecename="whale", ispromoted=True)
    create_piece_size_B(piecename="white_horse", ispromoted=True)

    create_piece_size_B(piecename="flying_ox", rotate=True, ispromoted=True)
    create_piece_size_B_plus(piecename="flying_stag", rotate=True, ispromoted=True)
    create_piece_size_B(piecename="free_boar", rotate=True, ispromoted=True)
    create_piece_size_C(piecename="horned_falcon", rotate=True, ispromoted=True)
    create_piece_size_C(piecename="prince", rotate=True, ispromoted=True)
    create_piece_size_C(piecename="soaring_eagle", rotate=True, ispromoted=True)
    create_piece_size_B(piecename="whale", rotate=True, ispromoted=True)
    create_piece_size_B(piecename="white_horse", rotate=True, ispromoted=True)

MyChuPieceMaker = ChuPieceMaker()

#MyChuPieceMaker.load_dimensions(".\\input\\dimensions_542_590.json")
#MyChuPieceMaker.load_dimensions(".\\input\\dimensions_542_590_single_kanji.json")

outputpath = ".\\output_set1\\"
MyChuPieceMaker.load_dimensions(".\\input\\dimensions_73_79_single_kanji.json")
print(f"Loaded dimension data for tiletypes {[item['tiletypename'] for item in MyChuPieceMaker.dimension_data['tiletypes']]}")
MyChuPieceMaker.load_kanji(".\\kanji\\kanji.json")
print(f"Loaded kanji for {len(MyChuPieceMaker.kanji_data)} pieces")
myimage = MyChuPieceMaker.load_image(f".\\input\\shogipiecetemplate.png")
print(f"Loaded template image with width {myimage.width} height {myimage.height}")
myimage = MyChuPieceMaker.fill_from_point(myimage, 266, 248, MyChuPieceMaker.piececolor)
MyChuPieceMaker.mycolouredtemplate = MyChuPieceMaker.fill_from_point(myimage, 4, 4, MyChuPieceMaker.boardcolor)
print("We have created the coloured template")
create_complete_chu_set()
add_for_tenjiku()
print("We have created the image files")


outputpath = ".\\output_set2\\"
MyChuPieceMaker.load_dimensions(".\\input\\dimensions_73_79.json")
print(f"Loaded dimension data for tiletypes {[item['tiletypename'] for item in MyChuPieceMaker.dimension_data['tiletypes']]}")
MyChuPieceMaker.load_kanji(".\\kanji\\kanji.json")
print(f"Loaded kanji for {len(MyChuPieceMaker.kanji_data)} pieces")
myimage = MyChuPieceMaker.load_image(f".\\input\\shogipiecetemplate.png")
print(f"Loaded template image with width {myimage.width} height {myimage.height}")
myimage = MyChuPieceMaker.fill_from_point(myimage, 266, 248, MyChuPieceMaker.piececolor)
MyChuPieceMaker.mycolouredtemplate = MyChuPieceMaker.fill_from_point(myimage, 4, 4, MyChuPieceMaker.boardcolor)
print("We have created the coloured template")
create_complete_chu_set()
add_for_tenjiku()
print("We have created the image files")
