from PIL import ImageTk, Image


def imageItem(infoPic, infoWidth, infoHeight):
    imgTemp = Image.open(infoPic)
    imgTemp = imgTemp.resize((infoWidth, infoHeight))
    imgFin = ImageTk.PhotoImage(imgTemp)

    return imgFin
