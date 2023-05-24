import cv2
import numpy as np
class Cadena:
  def __init__(self):
    pk = 9
    dimg = "hexa.png"
    #jfif
    img = cv2.imread("./"+dimg)
    pb = img[:,:,0]
    pg = img[:,:,1]
    pr = img[:,:,2]

    imagen2 = img.copy()

    #-----Encontramos los bordes de la imagen-----
    # Proceso de Segmentacion con Canny
    cv2.imshow("Img original gris", pg)
    # Filtro gaussiano
    blur = cv2.GaussianBlur(pg, (pk,pk), 0)
    cv2.imshow("Eliminacion de Ruido Gauss", blur)
    # Deteccion de bordes
    canny = cv2.Canny(blur,20, 250)
    cv2.imshow("Bordes", canny)
    #print(canny.shape)
    pixl = self.objPixels(canny)
    #print(pixl)
    rev = self.revPixels(pixl, canny)

    cv2.waitKey()
    cv2.destroyAllWindows()

  def objPixels(self, img):
    height = img.shape[0]
    width = img.shape[1]
    pixbord  = []
    for i in range(height):
      for j in range(width):
        pixel = img[i, j]
        if pixel == 255:
          #print(pixel)
          pixbord.append([i, j])
        else:
          img[i, j] = 0
    return pixbord

  def revPixels(self, contorno, imagen):
    filas = imagen.shape[0]
    columnas = imagen.shape[1]
    
    x = []
    y = []
    for i in range(len(contorno)):
      x.append(contorno[i][0])
      y.append(contorno[i][1])

    m = x[0]
    n = y[0]

    bord = []
    bord.append([m, n])

    nline = []
    lineavar = 0
    lineavab = 0
    lineahd = 0
    lineahi = 0
    #for dat in range(len(contorno)):
    nimg = np.zeros((filas, columnas), np.uint8)
    refimg = nimg.copy()

    salida = 0
    dat = 0
    nl = 30
    while salida != 1:
      nimg[bord[dat][0], bord[dat][1]] = 255
      cv2.imshow("", nimg)
      cv2.waitKey(50)

      #print(bord)
      #print("pixel ", dat, bord[dat][0],bord[dat][1])

      m = bord[dat][0] 
      n = bord[dat][1]
      #print("\n")

      band = 0
      kernel = []
      kernelpix = []

      p1 = 0
      p2 = 0
      p3 = 0
      p4 = 0
      p5 = 0
      p6 = 0
      p7 = 0
      p8 = 0

      p1 = imagen[m-1, n-1]
      p2 = imagen[m-1, n]
      p3 = imagen[m-1, n+1]
      p4 = imagen[m, n-1]
      p5 = imagen[m, n+1]
      p6 = imagen[m+1, n-1]
      p7 = imagen[m+1, n]
      p8 = imagen[m+1, n+1]

      kernelpix = [[m-1, n-1], [m-1, n], [m-1, n+1], [m, n-1], [m, n+1], [m+1, n-1], [m+1, n]
, [m+1, n+1]]

      kernel = [p1, p2,p3, p4, p5, p6, p7, p8]

      if p1 == 255 and band == 0 and kernelpix[0] not in bord:
        i = 3
        j = 3
        #print("p1")
        band = 1
        bord.append(kernelpix[0])
        lineavar = 0
        lineavab = 0
        lineahd = 0
        lineahi = 0

      if p2 == 255 and band == 0 and kernelpix[1] not in bord:
        i = 3
        j = 3
        #print("p2")
        band = 1
        bord.append(kernelpix[1])
        lineavar += 1
        if lineavar > nl:
          print("Hay una linea vertical de ", lineavar, " pixeles.")
        lineavab = 0
        lineahd = 0
        lineahi = 0

      if p3 == 255 and band == 0 and kernelpix[2] not in bord:
        i = 3
        j = 3
        #print("p3")
        band = 1
        bord.append(kernelpix[2])
        lineavar = 0
        lineavab = 0
        lineahd = 0
        lineahi = 0

      if p5 == 255 and band == 0 and kernelpix[4] not in bord:
        i = 3
        j = 3
        #print("p5")
        band = 1
        bord.append(kernelpix[4])
        lineahd += 1
        if lineahd > nl:
          print("Hay una linea horizontal de ", lineahd, " pixeles.")
        lineavar = 0
        lineavab = 0
        lineahi = 0

      if p8 == 255 and band == 0 and kernelpix[7] not in bord:
        i = 3
        j = 3
        #print("p8")
        band = 1
        bord.append(kernelpix[7])
        lineavar = 0
        lineavab = 0
        lineahd = 0
        lineahi = 0

      if p7 == 255 and band == 0 and kernelpix[6] not in bord:
        i = 3
        j = 3
        #print("p7")
        band = 1
        bord.append(kernelpix[6])
        lineavab += 1
        if lineavab > nl:
          print("Hay una linea vertical de ", lineavab, " pixeles.")
        lineavar = 0
        lineahd = 0
        lineahi = 0

      if p6 == 255 and band == 0 and kernelpix[5] not in bord:
        i = 3
        j = 3
        #print("p6")
        band = 1
        bord.append(kernelpix[5])
        lineavar = 0
        lineavab = 0
        lineahd = 0
        lineahi = 0

      if p4 == 255 and band == 0 and kernelpix[3] not in bord:
        i = 3
        j = 3
        #print("p4")
        band = 1
        bord.append(kernelpix[3])
        lineahi += 1
        if lineahi > nl:
          print("Hay una linea horizontal de ", lineahi, " pixeles.")
        lineavar = 0
        lineavab = 0
        lineahd = 0

      if band == 0:
        bord.append([bord[dat-1][0],bord[dat-1][1]])


      #print(kernel) #Imprimimos los vecinos del pixel
      #print(kernelpix)
      #print(bord) #Imprimimos los pixeles agregados a bordes

      imas = np.hstack((nimg, refimg))
      cv2.imshow ("Imagenes ", imas)
      diferencia = cv2.subtract(nimg, refimg)
      if not np.any(diferencia):
        salida = 1
        print("Son iguales las imagenes. Termino")
      dat += 1
      refimg = nimg.copy()

    return filas

cart = Cadena()