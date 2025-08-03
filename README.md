This project is for creating individual image files for Chu Shogi pieces

Or more in general: Shogi variant pieces

The steps in this proces are:
- Load the template image (basically the pentagonal shape of the tile)
- Load the json containing the kanji definitions
- Fill board and piece color
- Reshape piece
- Reshape square
- Put the kanji (red for promotion)
- Revert the image if it is for Gote
- Save the result
