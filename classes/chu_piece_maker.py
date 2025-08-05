from PIL import Image
import json
from PIL import ImageFont
from PIL import ImageDraw

class ChuPieceMaker():
    """
    This class supports creation of individual image files for Chu Shogi pieces
    (or more in general: pieces from Shogi variants)
    The hardcoded numbers are the result of tuning dimensions and colors
    Input:
    - template image
    - json that contains the kanji as unicode string
    Output:
    - individual piece image
    """
    def __init__(self):
        self.tolerance = 4
        self.kanji_data = None
        self.mycolouredtemplate = None
        self.fullsquarewidth = 542
        self.fullsquareheight = 590
        self.piececolor = (214, 181, 105)
        self.boardcolor = (243, 226, 171)

    def load_kanji(self, filename):
        file1 = open(filename, encoding="utf-8")
        self.kanji_data = json.load(file1)
        file1.close()

    def load_image(self, filename):
        #Under the hat, pillow handles formats like jpg, bmp, png
        myimage = Image.open(filename, mode='r')
        return myimage
    
    def save_image(self, pimage: Image, pfilename):
        #Under the hat, pillow handles formats like jpg, bmp, png
        pimage.save(pfilename)

    def colors_equal(self, pixA, pixB):
        if abs(pixA[0] - pixB[0]) > self.tolerance:
            return False
        if abs(pixA[1] - pixB[1]) > self.tolerance:
            return False
        if abs(pixA[2] - pixB[2]) > self.tolerance:
            return False
        return True

    def get_rgb(self, pimage: Image, x, y):
        try:
            r, g, b = pimage.getpixel((x, y))
        except:
            r, g, b, a = pimage.getpixel((x, y))
        return r, g, b

    def pixelidx(self, pwidth, x, y):
        #Maps coordinates (x, y) to the 1D index of array pixels
        return (y * pwidth) + x

    def fill_from_point(self, pimage: Image, x, y, usecolor: tuple):
        w, h = pimage.size
        infinitely_far = (w + h) ** 2
        pixels = list(pimage.getdata())

        trigger_color = self.get_rgb(pimage, x, y)

        target_color = usecolor

        #Each cell 2D array area_tracker is tuple (distance, checked_neighbours)
        area_tracker = [[(infinitely_far, False) for i in range(w)] for j in range(h)]
        area_tracker[y][x] = (0, False)

        progress_made = True
        aerea_size = 0
        while progress_made == True:
            progress_made = False
            if aerea_size % 100 == 0:
                print(f"aerea_size {aerea_size}")
            for i in range(w):
                for j in range(h):
                    if area_tracker[j][i][0] < infinitely_far and area_tracker[j][i][1] == False:
                        for (i2, j2) in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
                            if i2 >= 0 and j2 >= 0 and i2 < w and j2 < h:
                                if area_tracker[j2][i2][0] >= infinitely_far:
                                    if self.colors_equal(trigger_color, self.get_rgb(pimage, i2, j2)):
                                        area_tracker[j2][i2] = (area_tracker[j][i][0] + 1, False)
                                        progress_made = True
                                        aerea_size += 1
                        area_tracker[j][i] = (area_tracker[j][i][0], True)


        for i in range(w):
            for j in range(h):
                if area_tracker[j][i][0] < infinitely_far:
                    n = self.pixelidx(w, i, j)
                    pixels[n] = target_color

        modified_image = Image.new("RGB", pimage.size)
        modified_image.putdata(pixels)
        return modified_image

    def enlargesquare(self, pimage: Image):
        new_img = Image.new("RGB", (self.fullsquarewidth, self.fullsquareheight), self.boardcolor)
        x = (self.fullsquarewidth - pimage.width) // 2
        y = (self.fullsquareheight - pimage.height) - 27
        y2 = ((self.fullsquareheight - pimage.height) * 2) // 3
        #print(f"y {y} y2 {y2} y - y2 {y - y2}")
        new_img.paste(pimage, (x, y2))
        return new_img

    def put_kanji(self, pimage: Image, x: int, y: int, piecename: str,
                  fontsize: int, fontcolor: tuple, single_kanji=False):
        draw = ImageDraw.Draw(pimage)
        font = ImageFont.truetype("C:\\Windows\\Fonts\\simsun.ttc", fontsize)
        mytext = self.kanji_data[piecename][0]
        draw.text((x, y),mytext,fontcolor,font=font)
        if single_kanji == False:
            mytext = self.kanji_data[piecename][1]
            draw.text((x, y + fontsize + 15),mytext,fontcolor,font=font)

    def resize_image(self, pimage: Image, new_width: int, new_height: int):
        if pimage.width == new_width and pimage.height == new_height:
            return pimage.copy()
        resized_image = pimage.resize((new_width, new_height), resample=Image.LANCZOS)
        return resized_image

    def create_piece_size_A_tokinstyle(self, piecename: str, rotate: bool = False, ispromoted: bool = False):
        #for tokin-style we always use single kanji
        if ispromoted:
            usefontcolor = (255, 0, 0)
        else:
            usefontcolor = (0, 0, 0)
        mypieceimage = self.resize_image(self.mycolouredtemplate, 387, 387)
        self.put_kanji(pimage=mypieceimage, x=93, y=130, piecename=piecename,
                                fontsize=187, fontcolor=usefontcolor, single_kanji=True)
        mypieceimage = self.enlargesquare(mypieceimage)
        if rotate == True:
            mypieceimage = mypieceimage.rotate(180)
        return mypieceimage

    def create_piece_size_A(self, piecename: str, rotate: bool = False, ispromoted: bool = False):
        #size A is smallest, for pawn and go-between
        if ispromoted:
            usefontcolor = (255, 0, 0)
        else:
            usefontcolor = (0, 0, 0)
        mypieceimage = self.resize_image(self.mycolouredtemplate, 387, 387)
        self.put_kanji(pimage=mypieceimage, x=112, y=35, piecename=piecename,
                                fontsize=166, fontcolor=usefontcolor)
        mypieceimage = self.enlargesquare(mypieceimage)
        if rotate == True:
            mypieceimage = mypieceimage.rotate(180)
        return mypieceimage

    def create_piece_size_B(self, piecename: str, rotate: bool = False, ispromoted: bool = False):
        #size B is for Lance, VM, SM and similar size
        if ispromoted:
            usefontcolor = (255, 0, 0)
        else:
            usefontcolor = (0, 0, 0)
        mypieceimage = self.resize_image(self.mycolouredtemplate, 389, 429)
        self.put_kanji(pimage=mypieceimage, x=112, y=56, piecename=piecename,
                                fontsize=170, fontcolor=usefontcolor)
        mypieceimage = self.enlargesquare(mypieceimage)
        if rotate == True:
            mypieceimage = mypieceimage.rotate(180)
        return mypieceimage

    def create_piece_size_B_plus(self, piecename: str, rotate: bool = False, ispromoted: bool = False):
        #size B-plus is for Ferocious Leopard, Blind Tiger
        if ispromoted:
            usefontcolor = (255, 0, 0)
        else:
            usefontcolor = (0, 0, 0)
        mypieceimage = self.resize_image(self.mycolouredtemplate, 429, 429)
        self.put_kanji(pimage=mypieceimage, x=132, y=56, piecename=piecename,
                                fontsize=170, fontcolor=usefontcolor)
        mypieceimage = self.enlargesquare(mypieceimage)
        if rotate == True:
            mypieceimage = mypieceimage.rotate(180)
        return mypieceimage

    def create_piece_size_C(self, piecename: str, rotate: bool = False, ispromoted: bool = False):
        #size C is for Rook, Bishop and similar size
        if ispromoted:
            usefontcolor = (255, 0, 0)
        else:
            usefontcolor = (0, 0, 0)
        mypieceimage = self.resize_image(self.mycolouredtemplate, 476, 476)
        self.put_kanji(pimage=mypieceimage, x=138, y=65, piecename=piecename,
                                fontsize=187, fontcolor=usefontcolor)
        mypieceimage = self.enlargesquare(mypieceimage)
        if rotate == True:
            mypieceimage = mypieceimage.rotate(180)
        return mypieceimage

    def create_piece_size_D(self, piecename: str, rotate: bool = False, ispromoted: bool = False):
        #size D is for largest - Queen, King
        if ispromoted:
            usefontcolor = (255, 0, 0)
        else:
            usefontcolor = (0, 0, 0)
        mypieceimage = self.resize_image(self.mycolouredtemplate, 542, 542)
        self.put_kanji(pimage=mypieceimage, x=166, y=87, piecename=piecename,
                                fontsize=210, fontcolor=usefontcolor)
        mypieceimage = self.enlargesquare(mypieceimage)
        if rotate == True:
            mypieceimage = mypieceimage.rotate(180)
        return mypieceimage
