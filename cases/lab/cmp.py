exec(open('compose.py').read().split('# 01 hero')[0])
CAT='/tmp/cat/'
NEU=(243,241,238)
def cutfit(im,maxw,maxh):
  r=min(maxw/im.width,maxh/im.height); return im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
pairs=[('c4','c4_1'),('c6','c6_1'),('c8','c8_1'),('petal','petal_1')]
for k,(cat,rd) in enumerate(pairs):
  b=Image.new('RGBA',(W,H),BG+(255,)); d=ImageDraw.Draw(b)
  # left panel neutral, right panel VI gradient
  L=820
  d.rectangle([0,0,L,H],fill=NEU)
  for y in range(H):
    t=max(0,(y-H*0.5)/(H*0.5)); c=tuple(int(TINT[i]*(1-t)+DEEP[i]*t) for i in range(3)); d.line([(L,y),(W,y)],fill=c)
  # floor lines
  d.line([(80,860),(L-80,860)],fill=(222,217,210),width=2); d.line([(L+80,860),(W-80,860)],fill=(214,196,156),width=2)
  a=cutfit(Image.open(CAT+cat+'_cut2.png').convert('RGBA'),520,470); shadow(b,a,L//2-a.width//2,850-a.height,blur=22,op=60,dy=12)
  r=cutfit(load(rd),640,560); shadow(b,r,L+(W-L)//2-r.width//2,850-r.height)
  # arrow at seam
  y=640; d.line([(L-40,y),(L+40,y)],fill=(179,154,104),width=3); d.polygon([(L+40,y-10),(L+58,y),(L+40,y+10)],fill=(179,154,104))
  save(b,'c%d'%(k+1))
