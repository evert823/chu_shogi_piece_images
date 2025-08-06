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
        self.dimension_data = None
        self.fullsquarewidth = 542
        self.fullsquareheight = 590
        self.piececolor = (214, 181, 105)
        self.boardcolor = (243, 226, 171)

    def load_kanji(self, filename):
        file1 = open(filename, encoding="utf-8")
        self.kanji_data = json.load(file1)
        file1.close()

    def load_dimensions(self, filename):
        file1 = open(filename, encoding="utf-8")
        self.dimension_data = json.load(file1)
        file1.close()
        self.fullsquarewidth = self.dimension_data['fullsquarewidth']
        self.fullsquareheight = self.dimension_data['fullsquareheight']
        assert self.dimension_data['tiletypes'][0]['tiletypename'] == "A_tokinstyle"
        assert self.dimension_data['tiletypes'][1]['tiletypename'] == "A"
        assert self.dimension_data['tiletypes'][2]['tiletypename'] == "B"
        assert self.dimension_data['tiletypes'][3]['tiletypename'] == "B_plus"
        assert self.dimension_data['tiletypes'][4]['tiletypename'] == "C"
        assert self.dimension_data['tiletypes'][5]['tiletypename'] == "D"

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
        mymarge = self.dimension_data['marge_to_2nd_kanji']
        draw = ImageDraw.Draw(pimage)
        font = ImageFont.truetype("C:\\Windows\\Fonts\\simsun.ttc", fontsize)
        if single_kanji == True:
            mytext = self.kanji_data[piecename]['single_kanji'][0]
            draw.text((x, y),mytext,fontcolor,font=font)
        else:
            mytext = self.kanji_data[piecename]['full_kanji'][0]
            draw.text((x, y),mytext,fontcolor,font=font)
            mytext = self.kanji_data[piecename]['full_kanji'][1]
            draw.text((x, y + fontsize + mymarge),mytext,fontcolor,font=font)

    def resize_image(self, pimage: Image, new_width: int, new_height: int):
        if pimage.width == new_width and pimage.height == new_height:
            return pimage.copy()
        resized_image = pimage.resize((new_width, new_height), resample=Image.LANCZOS)
        return resized_image

    def create_piece_size_fromjson(self, piecename: str, rotate: bool = False,
                                   ispromoted: bool = False, tiletypename : str = ""):
        tiletype_idx = 0
        while self.dimension_data['tiletypes'][tiletype_idx]['tiletypename'] != tiletypename:
            tiletype_idx += 1

        w = self.dimension_data['tiletypes'][tiletype_idx]['resized_template_width']
        h = self.dimension_data['tiletypes'][tiletype_idx]['resized_template_height']
        kx = self.dimension_data['tiletypes'][tiletype_idx]['put_kanji_x']
        ky = self.dimension_data['tiletypes'][tiletype_idx]['put_kanji_y']
        fs = self.dimension_data['tiletypes'][tiletype_idx]['font_size']
        single_kanji = self.dimension_data['tiletypes'][tiletype_idx]['single_kanji']

        #for tokin-style we always use single kanji
        if ispromoted:
            usefontcolor = (255, 0, 0)
        else:
            usefontcolor = (0, 0, 0)
        mypieceimage = self.resize_image(self.mycolouredtemplate, w, h)
        self.put_kanji(pimage=mypieceimage, x=kx, y=ky, piecename=piecename,
                                fontsize=fs, fontcolor=usefontcolor, single_kanji=single_kanji)
        mypieceimage = self.enlargesquare(mypieceimage)
        if rotate == True:
            mypieceimage = mypieceimage.rotate(180)
        return mypieceimage
