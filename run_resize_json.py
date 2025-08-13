from classes.chu_piece_maker import ChuPieceMaker

MyChuPieceMaker = ChuPieceMaker()

MyChuPieceMaker.load_dimensions(".\\input\\dimensions_542_590.json")
MyChuPieceMaker.resize_and_save_dimensions(".\\input\\dimensions_180_196.json", scalefactor=3)
MyChuPieceMaker.load_dimensions(".\\input\\dimensions_542_590_single_kanji.json")
MyChuPieceMaker.resize_and_save_dimensions(".\\input\\dimensions_180_196_single_kanji.json", scalefactor=3)
