from PIL import Image
import sys

def image_print(fpath, txt_path):
    #try to open image
    try:
        im = Image.open(fpath)
    except:
        print("failed to open image file")
        raise Exception("image open failure")
    print("Img Mode: " + im.mode)
    print("Img Size: " + str(im.size))
    
    #change image to single band (B & W) and scale it
    im = im.convert("L")
    x = 55
    y = 55
    size = (x, y)
    im.thumbnail(size, Image.NEAREST)
    
    #assign values for characters
    xtrema = im.getextrema()
    mnv = xtrema[0]
    mxv = xtrema[1]
    print(mnv)
    print(mxv)
    diff = (mxv - mnv)/8
    p1 = mnv + diff #%
    p2 = mnv + 2 * diff ##
    p3 = mnv + 3 * diff #(
    p4 = mnv + 4 * diff #*
    p5 = mnv + 5 * diff #/
    p6 = mnv + 6 * diff #'
    p7 = mnv + 7 * diff #.
    p8 = 255 #
    
    print("Custom character cutoffs: " + str((p1, p2, p3, p4, p5, p6, p7, p8)))
    
    #initialize 2d list for characters
    lst = [[' ' for i in range(x)] for i in range(y)]

    try:
       f = open(txt_path, "w")
    except:
        raise Exception("couldn't open text file")
    
    #print pixels      
    for j in range(im.size[1]):
        for i in range(im.size[0]):
            try:
                px = im.getpixel((i, j))
            except:
                print((i, j))
                raise Exception()
            if (px < p1):
                #sys.stdout.write(2*'%')
                f.write(2*'%')
            elif (px < p2):
                #sys.stdout.write(2*'#')
                f.write(2*'#')
            elif (px < p3):
                #sys.stdout.write(2*'(')
                f.write(2*'(')
            elif (px < p4):
                #sys.stdout.write(2*'*')
                f.write(2*'*')
            elif (px < p5):
                #sys.stdout.write('//')
                f.write(2*'/')
            elif (px < p6):
                #sys.stdout.write('\'\'')
                f.write(2*'\'')
            elif (px < p7):
                #sys.stdout.write('..')
                f.write(2*'.')
            elif (px <= p8):
                #sys.stdout.write('  ')
                f.write(2*' ')
            else:
                print("pixel value: " + str(px))
                raise Exception("pixel assignment error")
        f.write('\n')
    
    #print ascii image

    #for i in range(x):
        #for i in range(j):
            #sys.stdout.write(lst[i][j])
        #print('')
                  
    print("success")

# def main():
#     fnm = ""
#     if (not(len(sys.argv) == 3)):
#         print("wrong no. of arguments")
#     else:
#         fnm = sys.argv[1]
#         txt_file = sys.argv[2]
#         image_print(fnm, txt_file)
# main()