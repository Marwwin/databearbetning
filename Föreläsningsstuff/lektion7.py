###
# LEKTION 7
# 

# Bilder som data

# Visa bild med matpoltlib
#%%
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

# Läs in bild
lena = img.imread("lenasmall.png")
#plt.imshow(lena)
print("datatyp", lena.dtype)
print("dimensioner", lena.shape)

type(lena)
intLena = np.int_(lena*255)
## att välja kolumner på numpy arrays är lätt med

rL = intLena[:,:,0]
gL =  intLena[:,:,1]
bL =  intLena[:,:,2]
imageA = img.imread("poke.png")
dena = img.imread("dennis_small.png")
fabio = img.imread("fabio64.png")
rgbaLena = np.int_(imageA*255)

denaInt = np.int_(dena*255)
fabioInt = np.int_(fabio*255)
alphaDena = denaInt[:,:,0]
alphaDenaNorm  = np.interp(alphaDena, (alphaDena.min(),alphaDena.max()), (245,255))
alphaDenaNorm = np.int_(np.round_(alphaDenaNorm,0))

#intLena
#[y for y in x for x in lenaRed]
#print(lenaRed)

#plt.imshow(rgbaLena[:,:,0], clim=(250,255))

#fig = plt.figure()
#a = fig.add_subplot(1,3,1)
#a.set_title("Red")
#plt.imshow(rgbaLena[:,:,0], cmap="Greys", clim=(0,255))
#a = fig.add_subplot(1,3,2)
#a.set_title("Green")
#plt.imshow(rgbaLena[:,:,1], cmap="Greys", clim=(0,255))
#a = fig.add_subplot(1,3,3)
#a.set_title("Blue")
#plt.imshow(rgbaLena[:,:,2], cmap="Greys", clim=(0,255))
#plt.imshow(denaInt[:,:,1])
denaFabio = np.dstack((fabioInt[:,:,0],fabioInt[:,:,1],fabioInt[:,:,2],alphaDenaNorm))
fig = plt.figure()
a = fig.add_subplot(1,2,1)
a.set_title("Fabio")
plt.imshow(denaFabio)
a = fig.add_subplot(1,2,2)
a.set_title("Dena")
plt.imshow(denaFabio[:,:,3],cmap="Greys",clim=(245,255))


# %%
