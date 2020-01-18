import Image
import affichage
import os
from random import *
import argparse

randBinList = lambda n: [randint(0,1) for b in range(1,n+1)]

rayon=1

regle_taille = 2 ** (2 * rayon + 1)
Regle=list([0]*regle_taille)

def regle_ver_list_bin(numregle) :
  global rayon
  regle_taille=2**(2*rayon+1)
  r= list(str(bin(numregle)))# dis => bin(string)
  r.pop(0)
  r.pop(0)
  for i in range(len(r)):r[i]=int(r[i])     # bin(string)=>bin int
  for i in range(regle_taille-len(r)):
   r.insert(0,0)                            # ajouter les 0
  r.reverse()
  return r



def val_dans_reg(b):
    return Regle[int(b[::-1], 2)]


def nextConfig(g):
    newg=[0]*len(config)
    for i in range(len(g)):
      voisinage=""
      for v in range(-rayon,rayon+1):
        voisinage+=str(g[(i+v)%len(g)])
      newg[i]=val_dans_reg(voisinage)
    return newg


def diagramme_ET(nbit, config):
 matrice= [[0] * len(config)] * (nbit + 1)
 for i in range(nbit):
     matrice[i]=config
     config = nextConfig(config)
 matrice[nbit]=config
 return matrice



def afficheruneragle(nbit, config):
   matriceverimage(diagramme_ET(nbit, config)).show()
def animationragle(nbit, config):
    affichage.animation(diagramme_ET(nbit, config))



def generertout_regle(config, nbt, lien):
    global Regle
    if not os.path.exists("tt_reg/"):
        os.makedirs("tt_reg/")
    for i in range(2**(2**(2*rayon+1))):
        Regle= regle_ver_list_bin(i)
        img= matriceverimage(diagramme_ET(nbt, config))
        img.save(lien+'/regle'+str(i)+'.png')

def eq(a,b):
    for i in range(len(a)):
        if(a[i]!=b[i]):
            return False
    return True

def selection(DET):
    for i in DET:
        v=0
        for j in DET:
            if(eq(i,j)):
                v+=1
            if(v>1):
                return False
    return True

def generer_regles_selection(config, nbt, lien):
    global Regle
    if not os.path.exists("tt_reg/"):
        os.makedirs("tt_reg/")
    i=0
    while(i<2**(2**(2*rayon+1))):
        Regle= regle_ver_list_bin(i)
        det=diagramme_ET(nbt, config)
        if(selection(det)):
            img= matriceverimage(det)
            img.save(lien+'/regle'+str(i)+'.png')
        i+=1;

def matriceverimage(mat):
    img0 = Image.open('bloc0.jpg')
    img1 = Image.open('bloc1.jpg')
    M,N=img1.size

    imgf = Image.new('RGB',(M*len(mat[0]),N*(len(mat))))
    for k in range(len(mat[0])):
      for i in range(len(mat)):
        for j in range(len(mat[0])):
             if(mat[i][j]):
                imgf.paste(img1,(j*N,i*M))
             else:
                imgf.paste(img0, (j*N,i*M))

    return imgf









config= [0] * 30 + [1] + [0] * 30
#config= [0,0,0,1] *20

parser = argparse.ArgumentParser()

parser.add_argument('-c', default=randBinList(61),type=str,
                    dest='config',
                    help='Set the start config')

parser.add_argument('-size', default=61,type=int,
                    dest='size',
                    help='Set size of start config')

parser.add_argument('-time', default=100,type=int,
                    dest='time',
                    help='Set time')

parser.add_argument('-rule', default=30,type=int,
                    dest='rule',
                    help='Set rule')

parser.add_argument('-ray', default=1,type=int,
                    dest='ray',
                    help='Set Ray')

parser.add_argument('-act', dest='act', default=0,type=int,
help='0 animate pattern \n 1 show pattern \n 2 save pattern  \n 3 save all pattern  \n 4 save all best battern \n')

results = parser.parse_args()
a=results.config
config=[int(i) for i in a.split(" ")]
print config
rayon=results.ray
Regle=regle_ver_list_bin(results.rule)
time=results.time
confsize=results.size
act=results.act

if(confsize!=61):
    config=randBinList(confsize)

if(act==0):
 animationragle(time, config)
if(act==1):
 matriceverimage(diagramme_ET(time,config)).show()
if(act==2):
 matriceverimage(diagramme_ET(time,config)).save("res.png")
if(act==3):
 generertout_regle(config,60,"tt_reg/")
if(act==4):
 generer_regles_selection(config,100,"tt_reg/")