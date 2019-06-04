def gs(pix):
    return pix[0]*30+pix[1]*59+pix[2]*11
red,teal,navy,offwhite,green,driedblood,communeyellow,deepblue,white = (218,20,21),(112,150,160),(0,48,80),(250,227,173),(176,183,167),(69,0,0),(69+69+69,169,69),(0,34,69),(255,255,255)
presets = {"og":[red,teal,navy,offwhite,green],"commie":[red,offwhite,driedblood,communeyellow],"emo":[teal,green,offwhite,deepblue,white],"pride":[communeyellow,red,green,teal,(129,39,169),(9,59,39),(15,69,69),(30,69,90)]}
colors = presets["pride"]
colors = sorted(colors,key=gs)
threshholds = [(gs(colors[i])+gs(colors[i+1])+1)//2 for i in range(len(colors)-1)] + [25600]

themes = [["emo","pride"],["og","commie"]]
def closest(pix):
    g = gs(pix)
    for i in range(len(colors)):
        if g < threshholds[i]:return colors[i]
    return colors[-1]
import os
from PIL import Image
for i in os.listdir("./in"):
    if not "Store" in i:
        try:
            b = Image.open("./in/"+i)
        except:
            print(i + " is mega gay")
        p = b.load()
        b2 = Image.new("RGB", (b.width * 2, b.height * 2))
        w = b.width
        h = b.height
        for i_ in (0,1):
            for j_ in (0,1):
                print("working...")
                colors = sorted(presets[themes[i_][j_]],key=gs)
                threshholds = [(gs(colors[i])+gs(colors[i+1])+1)//2 for i in range(len(colors)-1)] + [25600]
                p2 = b2.load()
                for x in range(b.width):
                    for y in range(b.height):
                        p2[x+i_*w,y+j_*h] = closest(p[x,y])
        b2.save(i[:-4]+"_composit"+".png","png")
        for x in range(b.width):
            for y in range(b.height):
                p[x,y] = closest(p[x,y])
        b.save(i[:-4]+"_"+".png","png")
                        
