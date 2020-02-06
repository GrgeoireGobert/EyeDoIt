##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Maths : module d'outils mathématiques 3D.
#
#  Le module Maths contient les classes : \n
#  -> Vector : représentation d'un vecteur 3D \n
#  -> Matrix : représentation d'une matrice 3x3

import numpy

##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Vector : classe de vecteur 3D
#
#  Hérite de np.ndarray avec restriction sur la taille.
#  Comporte donc les méthodes et opérateurs de np.ndarray
class Vector(numpy.ndarray):
   
    ##
    #
    #  @param self Le pointeur vers l'objet Vector
    #  @param x coordonnée x
    #  @param y coordonnée y
    #  @param z coordonnée z
    #
    #  @brief Constructeur de classe
    def __new__(self, x,y,z , dtype = 'float', copy = True):
        data=[[x],[y],[z]]
        new = numpy.array(data, dtype, copy = copy).view(self)
        return new
   
    ##
    #
    #  @param self Le pointeur vers l'objet Vector
    #
    #  @brief Renvoie la coordonnée x du vecteur
    def x(self):
        return self[0][0]
     
    ##
    #
    #  @param self Le pointeur vers l'objet Vector
    #
    #  @brief Renvoie la coordonnée y du vecteur
    def y(self):
        return self[1][0]
     
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Renvoie la coordonnée z du vecteur
    def z(self):
        return self[2][0]
   
    ##
    #
    #  @param self Le pointeur vers l'objet Vector
    #
    #  @brief Renvoie la norme du vecteur
    def norm(self):
        return numpy.sqrt(self.x()**2+self.y()**2+self.z()**2)
   
    ##
    #
    #  @param self Le pointeur vers l'objet Vector
    #
    #  @brief Normalise le vecteur pour le rendre unitaire
    def normalize(self):
        norme=self.norm()
        assert norme > 0, 'La norme est nulle, normalisation impossible'
        self[0][0]=self[0][0]/norme
        self[1][0]=self[1][0]/norme
        self[2][0]=self[2][0]/norme
            
   
    ##
    #
    #  @param self Le pointeur vers l'objet Vector
    #
    #  @brief Affichage du vecteur
    def showVector(self):
        print("Vector (x={},y={},z={})".format("%.4f" % self.x(),"%.4f" % self.y(),"%.4f" % self.z()))
        
    
    ##
    #
    #  @param self Le pointeur vers l'objet Vector
    #  @param other Un autre vector
    #
    #  @return Bool : égalité entre les deux Vector
    #
    #  @brief Test d'égalité entre deux Vector
    def __eq__(self,other):
        return self.x()==other.x() and self.y()==other.y() and self.z()==other.z()




##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Vector : classe de matrice 3x3
#
#  Hérite de np.ndarray avec restriction sur la taille.
#  Comporte donc les méthodes et opérateurs de np.ndarray
class Matrix(numpy.ndarray):
   
    ##
    #
    #  @param self Le pointeur vers l'objet Matrix
    #  @param data Les cofficients sous forme [[Line1],[Line2],[Line3]]
    #  @param transpose Booléen indiquant s'il faut transposer la matrice
    #
    #  @brief Constructeur de classe
    def __new__(self, data , transpose=False, dtype = 'float', copy = True):
        #Vérification taille OK
        assert len(data)==3, 'Classe pour matrice 3x3'
        for i in range(3):
            assert len(data)==3, 'Classe pour matrice 3x3'
        
        new = numpy.array(data, dtype, copy = copy).view(self)
        
        if transpose:
            new=new.transpose()
            
        return new
        
    ##
    #
    #  @param self Le pointeur vers l'objet Matrix
    #
    #  @brief Affichage de la matrice
    def showMatrix(self):
        print("Matrix")
        print(self)
