def gs(pix):
    return pix[0]*30+pix[1]*59+pix[2]*11
red,teal,navy,offwhite,green,driedblood,communeyellow,deepblue,white = (218,20,21),(112,150,160),(0,48,80),(250,227,173),(176,183,167),(69,0,0),(69+69+69,169,69),(0,34,69),(255,255,255)
presets = {"og":[red,teal,navy,offwhite,green],"commie":[red,offwhite,driedblood,communeyellow],"emo":[teal,green,offwhite,deepblue,white]}
colors = presets["emo"]
colors = sorted(colors,key=gs)
threshholds = [(gs(colors[i])+gs(colors[i+1])+1)//2 for i in range(len(colors)-1)] + [25600]
def closest(pix):
    g = gs(pix)
    for i in range(len(colors)):
        if g < threshholds[i]:return colors[i]
    return colors[-1]
import os
from PIM import Image
for i in os.listdir("./in"):
    if not "Store" in i:
        try:
            b = Image.open("./in/"+i)
        except:
            print(i + " is mega gay")
        p = b.load()
        for x in range(b.width):
            for y in range(b.height):
                p[x,y] = closest(p[x,y])
        b.save(i[:-4]+"_"+".png","png")
