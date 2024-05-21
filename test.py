import cv2
v="ap.mp4"
t=0
count=0
fps = 6
h,l=63,113
video = cv2.VideoCapture(v)
clip_l = 60
id_ = 0
f = open("0.bin","wb")
def convert(i):
    for x in range(h):
        for y in range(l):
            out=(out<<1)+(sum(i[y,x])<20)
            if (y+1)%8==0:
              yield out
              out=0
def get_t(t,fps):
    return 30//fps*t
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
print("少女祈祷中...")
while t<get_t(3*60,fps):
    if count==fps:
        count=0
        _,i = video.read()
        i = cv2.resize(i,(113,64),cv2.INTER_LINEAR)
        f.write(bytearray(convert(i)))
        #cv2.imwrite(f"output\\{t}.bmp",i)
        t+=1
    else:
        count+=1
        video.read()
f.close()
