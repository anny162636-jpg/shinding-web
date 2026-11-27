from PIL import Image, ImageDraw, ImageFilter
import os
S='/home/claude/shinding-web/cases/lab/gemalan/'
O='/home/claude/shinding-web/cases/lab/gemalan/s/'; os.makedirs(O,exist_ok=True)
W,H=1920,1080
BG=(251,246,234); TINT=(244,234,208); DEEP=(233,217,178); INK=(74,58,46)
def stage(top=BG,bot=DEEP):
  im=Image.new('RGB',(W,H),top); d=ImageDraw.Draw(im)
  for y in range(H):
    t=max(0,(y-H*0.55)/(H*0.45)); c=tuple(int(top[i]*(1-t)+bot[i]*t) for i in range(3)); d.line([(0,y),(W,y)],fill=c)
  return im
def load(n,h=None,w=None):
  im=Image.open(S+n+'.webp').convert('RGBA'); im=im.crop(im.getbbox())
  if h: im=im.resize((int(im.width*h/im.height),h),Image.LANCZOS)
  if w: im=im.resize((w,int(im.height*w/im.width)),Image.LANCZOS)
  return im
def shadow(base,im,x,y,blur=28,op=70,dy=18):
  a=im.split()[3].point(lambda v:v*op//255); sh=Image.new('RGBA',im.size,(74,58,46,0)); sh.putalpha(a)
  pad=blur*3; L=Image.new('RGBA',(im.width+pad*2,im.height+pad*2),(0,0,0,0)); L.paste(sh,(pad,pad)); L=L.filter(ImageFilter.GaussianBlur(blur))
  base.alpha_composite(L,(x-pad,y-pad+dy)); base.alpha_composite(im,(x,y))
def save(im,n): im.convert('RGB').save(O+n+'.webp',quality=88); print(n)

# 01 hero: group
b=stage().convert('RGBA'); g=Image.new('RGBA',(W,H),(0,0,0,0))
items=[('c8_1',430,700,250),('c6_1',360,250,330),('c4_2',380,1300,300),('petal_1',300,930,560)]
for n,h,x,y in items:
  im=load(n,h=h); shadow(g,im,x-im.width//2+ (0), y+ (h- im.height)) if False else shadow(g,im,x-im.width//2,y)
bb=g.getbbox(); 
b2=b.copy(); b2.alpha_composite(g); save(b2,'01')
fl=g.crop(bb); fl.save(O+'01-float.png'); print('float bbox',bb)
# clean bg for hero (without products) = b
save(b,'01-bg')
# 02 logo slide
b=Image.new('RGBA',(W,H),BG+(255,)); lg=Image.open(S+'logo.png').convert('RGBA'); lg=lg.resize((900,int(lg.height*900/lg.width)),Image.LANCZOS)
b.alpha_composite(lg,((W-900)//2,380)); save(b,'02')
# 03 stock lineup on tint
b=stage(TINT,DEEP).convert('RGBA')
xs=[(c,x) for c,x in zip(['c4_1','c6_1','c8_1','petal_1'],[300,760,1220,1640])]
for n,x in xs:
  im=load(n,w=330 if n!='petal_1' else 260); shadow(b,im,x-im.width//2,640-im.height)
save(b,'03')
# 04 applied design: badge closeup from c6_1 + swatches area left blank
b=Image.new('RGBA',(W,H),BG+(255,))
im=Image.open(S+'c6_1.webp').convert('RGBA'); w,h=im.size; cr=im.crop((int(w*.30),int(h*.38),int(w*.70),int(h*.80))); cr=cr.resize((760,int(cr.height*760/cr.width)),Image.LANCZOS)
d=ImageDraw.Draw(b); d.rectangle([980,0,W,H],fill=TINT); b.alpha_composite(cr,(1070,(H-cr.height)//2))
sw=[(247,231,176),(246,212,81),(191,174,134),(107,84,64),(255,255,255)]
for i,c in enumerate(sw):
  x=180+i*150; d.ellipse([x,600,x+110,710],fill=c,outline=(220,208,180),width=2)
save(b,'04')
# 05-08 angles
for k,(n,nm) in enumerate([('c4','4吋'),('c6','6吋'),('c8','8吋'),('petal','花瓣')]):
  b=stage(BG,TINT).convert('RGBA')
  for j,x in enumerate([360,960,1560]):
    im=load('%s_%d'%(n,j+1),w=480); 
    if im.height>560: im=load('%s_%d'%(n,j+1),h=560)
    shadow(b,im,x-im.width//2,880-im.height)
  save(b,'%02d'%(5+k))
