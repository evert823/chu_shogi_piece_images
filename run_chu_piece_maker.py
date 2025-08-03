from classes.chu_piece_maker import ChuPieceMaker

def create_piece_size_A_tokinstyle(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_A_tokinstyle(piecename=piecename, rotate=rotate, ispromoted=ispromoted)
    MyChuPieceMaker.save_image(mypieceimage, f".\\output\\{piecename}.png")

def create_piece_size_A(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_A(piecename=piecename, rotate=rotate, ispromoted=ispromoted)
    MyChuPieceMaker.save_image(mypieceimage, f".\\output\\{piecename}.png")

def create_piece_size_B(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_B(piecename=piecename, rotate=rotate, ispromoted=ispromoted)
    MyChuPieceMaker.save_image(mypieceimage, f".\\output\\{piecename}.png")

def create_piece_size_B_plus(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_B_plus(piecename=piecename, rotate=rotate, ispromoted=ispromoted)
    MyChuPieceMaker.save_image(mypieceimage, f".\\output\\{piecename}.png")

def create_piece_size_C(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_C(piecename=piecename, rotate=rotate, ispromoted=ispromoted)
    MyChuPieceMaker.save_image(mypieceimage, f".\\output\\{piecename}.png")

def create_piece_size_D(piecename: str, rotate: bool = False, ispromoted: bool = False):
    mypieceimage = MyChuPieceMaker.create_piece_size_D(piecename=piecename, rotate=rotate, ispromoted=ispromoted)
    MyChuPieceMaker.save_image(mypieceimage, f".\\output\\{piecename}.png")

MyChuPieceMaker = ChuPieceMaker()

MyChuPieceMaker.load_kanji(".\\kanji\\kanji.json")
print(f"Loaded kanji for {len(MyChuPieceMaker.kanji_data)} pieces")
myimage = MyChuPieceMaker.load_image(f".\\input\\shogipiecetemplate.png")
print(f"Loaded template image with width {myimage.width} height {myimage.height}")

myimage = MyChuPieceMaker.fill_from_point(myimage, 266, 248, MyChuPieceMaker.piececolor)
MyChuPieceMaker.mycolouredtemplate = MyChuPieceMaker.fill_from_point(myimage, 4, 4, MyChuPieceMaker.boardcolor)
print("We have created the coloured template")

create_piece_size_B(piecename="lance")
create_piece_size_B(piecename="reverse_chariot")
create_piece_size_B(piecename="side_mover")
create_piece_size_B_plus(piecename="ferocious_leopard")
create_piece_size_B(piecename="vertical_mover")
create_piece_size_C(piecename="copper_general")
create_piece_size_C(piecename="bishop")
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
create_piece_size_C(piecename="drunk_elephant")
create_piece_size_C(piecename="phoenix")
create_piece_size_D(piecename="queen")
create_piece_size_A(piecename="pawn")
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
