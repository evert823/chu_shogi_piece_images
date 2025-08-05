from classes.chu_piece_maker import ChuPieceMaker

def imagefilename(piecename: str, rotate: bool = False, ispromoted: bool = False):
    path = ".\\output\\"
    result = f"{path}{piecename}"

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

MyChuPieceMaker = ChuPieceMaker()

#MyChuPieceMaker.load_dimensions(".\\input\\dimensions_542_590.json")
MyChuPieceMaker.load_dimensions(".\\input\\dimensions_73_79.json")
print(f"Loaded dimension data for tiletypes {[item['tiletypename'] for item in MyChuPieceMaker.dimension_data['tiletypes']]}")
MyChuPieceMaker.load_kanji(".\\kanji\\kanji.json")
print(f"Loaded kanji for {len(MyChuPieceMaker.kanji_data)} pieces")
myimage = MyChuPieceMaker.load_image(f".\\input\\shogipiecetemplate.png")
print(f"Loaded template image with width {myimage.width} height {myimage.height}")

myimage = MyChuPieceMaker.fill_from_point(myimage, 266, 248, MyChuPieceMaker.piececolor)
MyChuPieceMaker.mycolouredtemplate = MyChuPieceMaker.fill_from_point(myimage, 4, 4, MyChuPieceMaker.boardcolor)
print("We have created the coloured template")

#TODO we need to add lines for ALL promoted pieces and also for all Gote's pieces
create_piece_size_B(piecename="lance")
create_piece_size_B(piecename="lance", rotate=True)
create_piece_size_B(piecename="reverse_chariot")
create_piece_size_B(piecename="side_mover")
create_piece_size_B_plus(piecename="ferocious_leopard")
create_piece_size_B(piecename="vertical_mover")
create_piece_size_C(piecename="copper_general")
create_piece_size_C(piecename="bishop")
create_piece_size_B_plus(piecename="bishop", ispromoted=True)
create_piece_size_C(piecename="bishop", rotate=True)
create_piece_size_B_plus(piecename="bishop", rotate=True, ispromoted=True)
create_piece_size_C(piecename="rook")
create_piece_size_C(piecename="silver_general")
create_piece_size_C(piecename="dragon_horse")
create_piece_size_C(piecename="gold_general")
create_piece_size_B_plus(piecename="blind_tiger")
create_piece_size_C(piecename="dragon_king")
create_piece_size_D(piecename="king_sente")
create_piece_size_D(piecename="king_gote", rotate=True)
create_piece_size_C(piecename="kirin")
create_piece_size_C(piecename="lion")
create_piece_size_C(piecename="lion", rotate=True)
create_piece_size_C(piecename="drunk_elephant")
create_piece_size_C(piecename="phoenix")
create_piece_size_D(piecename="queen")
create_piece_size_A(piecename="pawn")
create_piece_size_A(piecename="pawn", rotate=True)
create_piece_size_A(piecename="go_between")
create_piece_size_A_tokinstyle(piecename="tokin", ispromoted=True)
create_piece_size_B(piecename="flying_ox", ispromoted=True)
create_piece_size_B_plus(piecename="flying_stag", ispromoted=True)
create_piece_size_B(piecename="free_boar", ispromoted=True)
create_piece_size_C(piecename="horned_falcon", ispromoted=True)
create_piece_size_C(piecename="prince", ispromoted=True)
create_piece_size_C(piecename="soaring_eagle", ispromoted=True)
create_piece_size_B(piecename="whale", ispromoted=True)
create_piece_size_B(piecename="white_horse", ispromoted=True)

print("We have created the image files")
