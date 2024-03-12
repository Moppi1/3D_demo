import vmath as v
import camera
#this class is used to create and transform an object with a 
#given shape (csv file) . The object can be rendered with a given camera object

class object:
    """load an object from text file by name of this file
    can also get an transform along the axis (by default x= y= z= 0)
    """
    def __init__(self,path:str,name:str="new object"):
        self.name = name
        
        # here was the replaced csv importer
        def load_stl(txt): # imports the stl object file
            """returns a list of triangles"""
            triangle = []

            file = open(txt,'r') # opening and importing
            content = file.readlines()
            file.close()

            for i in range(len(content)): #  processing of the stl object

                cl = content[i] # current line

                if cl.find("outer loop") != -1 :
                    tri = []
                    for j in range(3):
                        cl = content[i+j+1]
                        cl = cl.replace("vertex ","")
                        cl = cl.split(" ")
                        tri.append(v.vec(float(cl[0]),float(cl[1]),float(cl[2])))
                    triangle.append(tri)
                    i += 5
            return triangle


        self.tri = load_stl(path)

        self.position = v.vec(0,0,0) #Translation along the axes
        self.scale = v.vec(1,1,1) # scale along the axes
        self.rotation = v.vec(0,0,0) #Rotation around the glaobal axes

        #print([str(j) for j in self.tri])
        

    def __str__(self): #just for debugging purposes
        l1 = "---- " + self.name + " ----\n"
        l2 = "pos : "+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+"\n"
        l3 = "rot : "+str(self.rx)+" , "+str(self.ry)+" , "+str(self.rz)+"\n"
        l4 = "siz : "+str(self.sx)+" , "+str(self.sy)+" , "+str(self.sz)+"\n"
        t = [l1,l2,l3,l4]
        return "".join([i for i in t])
    

    def render(self,camera:camera,shading=1):
        """renders this object with a given camera object"""
        camera.render(self.apply(),shading)


    # ===== Transformation (just defining the Transformations)=====
    def setposition(self,v:v.vec): #Translatation
        """moves the object to given values"""
        self.position.x = v.x
        self.position.y = v.y
        self.position.z = v.z
    def move(self,v:v.vec):
        """moves the object by given values"""
        self.position.x += v.x
        self.position.y += v.y
        self.position.z += v.z


    def setrotation(self,v,over:bool=True): # Rotation
        """sets rotation to given values along global axis
        ---
        if over is False, only the rotation-values != 0 will overwrite an axis rotation
        """
        
        self.rotation.x = self.rotation.x if v.x == 0 and over == False else v.x
        self.rotation.y = self.rotation.y if v.y == 0 and over == False else v.y
        self.rotation.z = self.rotation.z if v.z == 0 and over == False else v.z
    def rotate(self,v:v.vec):
        """rotates the object by given values along global axis"""
        self.rotation.x += v.x
        self.rotation.y += v.y
        self.rotation.z += v.z


    def setsize(self,v:v.vec): #Scaling
        """sets the size to given values"""
        self.sx = v.x
        self.sy = v.y
        self.sz = v.z
    def size(self,v:v.vec):
        """changes the size by given values"""
        self.scale.x += v.x
        self.scale.y += v.y
        self.scale.z += v.z

    # ===== applying the Transformation before rendering the Object =====
    def apply(self):
        """applies the transformation to the triangles"""

        t_coords = []
        for i in self.tri: #applies transform on 
            tri = []
            for j in i:

                t = j.mulvec(self.scale)                                            #scaling
                t = t.rot(self.rotation.x,self.rotation.y,self.rotation.z)          #rotating
                t = t.addvec(self.position)                                         #translating
                tri.append(t)

            t_coords.append(tri)

        return t_coords