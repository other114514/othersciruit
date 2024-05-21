import cv2
i = cv2.imread("1.bmp")
out=0
count=0
def convert(i):
    out  =0
    h,l = i.shape[0],i.shape[1]
    for x in range(l):
        for y in range(h):
            out=(out<<1)+(sum(i[y,x])<20)
            if (y+1)%8==0:
              id8 = bin(out)[2:]
              id4 = id8[::-1]+'0'*(8-len(id8))
              yield int(id4,2)
              out=0
with open("test.bin","wb") as f:
  f.write(bytearray(convert(i)))
