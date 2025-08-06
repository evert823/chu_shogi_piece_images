from classes.chu_piece_maker import ChuPieceMaker

MyChuPieceMaker = ChuPieceMaker()

MyChuPieceMaker.load_dimensions(".\\input\\dimensions_542_590_single_kanji.json")

MyChuPieceMaker.resize_and_save_dimensions(".\\input\\dimensions_73_79_single_kanji.json")
