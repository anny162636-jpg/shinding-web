import re,html
Z=open('/home/claude/shinding-web/cases/zhong.html').read()
a=Z.index('<article');b=Z.index('</article>')+len('</article>')
art=Z[a:b]
script=''
V='?v=3'
def sp(i,t,x,y,s,color='#4A3A2E',w=500,f='f-sans',ls=0):
  return '<span class="%s" style="--i:%d;left:%.3f%%;top:%.3f%%;--s:%.1f;--ls:%s;color:%s;font-weight:%d">%s</span>'%(f,i,x/19.2,y/10.8,s,ls,color,w,html.escape(t))
def cen(t,cx,s,ascii=False):
  n=sum(0.6 if ord(c)<128 else 1 for c in t); return cx-n*s/2
def slide(n,spans,flow):
  tx=''.join(spans)
  fl=''.join('<p>%s</p>'%html.escape(p) for p in flow)
  return '<figure class="rl-ai cs-io" style="--W:1920"><div class="rl-st"><img class="rl-pg" src="./gemalan/s/%s.webp%s" alt="星之坊 %s" loading="lazy" decoding="async"><div class="rl-hv"></div><div class="rl-tx">%s</div></div>%s</figure>'%(n,V,n,tx,('<details class="rl-flow"><summary>展開本頁文字</summary><div class="rl-fb">%s</div></details>'%fl) if flow else '')
A='#B39A68';I='#4A3A2E';S='#9A8C78'
def lab(en,zh):
  return [sp(0,en,80,70,26,A,600,'f-sans',0.2),sp(1,'/',80,108,26,A,300),sp(2,zh,112,112,34,I,700,'f-serif')]
sl=[]
sl.append(slide('02',[sp(0,'CLIENT',cen('CLIENT',960,24),300,24,A,600),sp(1,'葛瑪蘭之星飯店｜星之坊',cen('葛瑪蘭之星飯店｜星之坊',960,30),720,30,I,500,'f-serif')],['葛瑪蘭之星飯店｜星之坊']))
boxes=[('4吋手提蛋糕盒','14×14×10.5 cm','絮語'),('6吋上下蓋蛋糕盒','21×21×16 cm','絮語'),('8吋上下蓋蛋糕盒','25.4×25.4×16 cm','蒲公英'),('花瓣盒（切片蛋糕盒）','15×10×13 cm','絮語')]
for k,(nm,sz,pat) in enumerate(boxes):
  s=[sp(0,'STOCK STRUCTURE %02d'%(k+1),80,70,24,A,600,'f-sans',0.2),sp(1,'/',80,106,24,A,300),sp(2,'公版盒型',108,110,34,I,700,'f-serif'),
     sp(3,'薪鼎公版盒型',cen('薪鼎公版盒型',410,26),930,26,'#6F6A64',700,'f-serif'),sp(4,'公版花色「%s」'%pat,cen('公版花色「%s」'%pat,410,20),975,20,'#8E8880',400),
     sp(5,'星之坊 套用設計',cen('星之坊 套用設計',1370,26),930,26,I,700,'f-serif'),sp(6,'%s・%s'%(nm,sz),cen('%s・%s'%(nm,sz),1370,20),975,20,S,400)]
  sl.append(slide('c%d'%(k+1),s,['公版盒型：%s %s'%(nm,sz),'左：薪鼎公版盒型（公版花色「%s」）'%pat,'右：星之坊 套用設計']))
s=lab('APPLIED DESIGN','套用的設計')+[sp(3,'設計來源',180,330,24,S,500),sp(4,'客戶自行設計',180,370,40,I,700,'f-serif'),sp(5,'品牌標誌',180,460,24,S,500),sp(6,'星之坊 STAR',180,500,32,I,600,'f-serif')]
for k,nm in enumerate(['奶油黃','檸檬黃','沙金','可可棕','白']):
  s.append(sp(7+k,nm,cen(nm,235+k*150,20),730,20,S,500))
sl.append(slide('04',s,['設計來源：客戶自行設計','品牌標誌：星之坊 STAR']))
sl.append(slide('09',[sp(0,'情境圖版位',cen('情境圖版位',960,48),440,48,A,700,'f-serif'),sp(1,'1920 × 1080・16:9・Codex 生成後替換',cen('1920 × 1080・16:9・Codex 生成後替換',960,26),530,26,S,500)],[]))
N=len(sl)+1
head='''<article class="cs" style="--cink:#4A3A2E;--caccent:#B39A68;--csub:#9A8C78;--cbg:#FBF6EA"><header class="rl-head2 cs-io"><p class="rl-eb">STOCK PACKAGING</p><h1><span class="rl-lw" style="--lg:url(./gemalan/logo.png);width:min(300px,62vw)"><img class="rl-logo" src="./gemalan/logo.png" alt="葛瑪蘭之星飯店 Logo"></span><span class="sr">葛瑪蘭之星飯店｜星之坊</span></h1><p class="rl-kind">公版盒型・客戶自行設計</p><p class="rl-en">Star Bakery — Cake Boxes on Stock Structures</p><div class="rl-meta2"><div><small>Client</small><b>葛瑪蘭之星飯店｜星之坊</b></div><div><small>Scope</small><b>公版盒型 4 款・印刷生產</b></div><div><small>Year</small><b>2023</b></div></div></header>'''
hero='<figure class="rl-hero"><img class="rl-pg" src="./gemalan/s/01-bg.webp%s" alt="星之坊 公版蛋糕盒" loading="eager"><img class="rl-float" src="./gemalan/s/01-float.png%s" alt="" aria-hidden="true" style="left:%.3f%%;top:%.3f%%;width:%.3f%%"></figure>'%(V,V,309/19.2,289/10.8,(1661-309)/19.2)
cnt='<div class="rl-prog" aria-hidden="true"><i></i></div><div class="rl-cnt" aria-hidden="true"><b>01</b><span>/ %02d</span></div>'%N
reel='<section class="rl-reel">'+''.join(sl)+'</section>'
cred='<section class="rl-cred"><div class="rl-cl"><p class="rl-ck">Credits</p><p class="rl-nt">（名單待確認）</p></div><ul><li><small>Client</small><b>葛瑪蘭之星飯店｜星之坊</b></li><li><small>Design</small><b>客戶自行設計</b></li><li><small>Stock Structures</small><b>薪鼎公版盒型</b></li><li><small>Production</small><b>Senior Deed</b></li><li><small>Year</small><b>2023</b></li></ul></section><div class="rl-end" style="padding-top:90px"><a href="../"><i>←</i>回到全部作品</a></div>'
newart=head+hero+cnt+reel+cred+script+'</article>'
P=Z[:a]+newart+Z[b:]
P=P.replace('<title>鍾師父｜薪鼎包裝 SENIOR DEED</title>','<title>【試作 v3】公版案例模板｜星之坊｜薪鼎包裝</title><meta name="robots" content="noindex">')
# fix relative paths for lab/ subfolder
for x in ['favicon.svg','favicon.png','case-engine.css','sd-shell.css','sd-logo-pack-horizontal.svg']:
  P=P.replace('"./'+x,'"../'+x)
P=P.replace('<a class="logo" href="./"','<a class="logo" href="../"').replace('<a class="cur" href="./"','<a class="cur" href="../"').replace('<a href="../">線上型錄','<a href="../../">線上型錄').replace('<a href="./" onclick','<a href="../" onclick')
open('/home/claude/shinding-web/cases/lab/gemalan-stock-v3.html','w').write(P)
print(N, len(P))
