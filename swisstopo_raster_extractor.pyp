import c4d, os, sys

sys.path.append(os.path.dirname(__file__))

import od_swisstopo_image_extractor as img_extractor

ID_SWISSTOPO_RASTER_EXTRACTOR = 1059288

class ImageExtractor(c4d.plugins.CommandData):
    def Execute(self, doc) :
        img_extractor.main()
        return True

def icone(nom) :
    bmp = c4d.bitmaps.BaseBitmap()
    dir, file = os.path.split(__file__)
    fn = os.path.join(dir, "res", nom)
    bmp.InitWith(fn)
    return bmp
    
if __name__=='__main__':
    c4d.plugins.RegisterCommandPlugin(id=ID_SWISSTOPO_RASTER_EXTRACTOR, str="swisstopo extracteur d'images",
                                      info=0, help="", dat=ImageExtractor(),
                                      icon=icone("esri_import_image.png"))