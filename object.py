import vmath as v
import camera
#this class is used to create and transform an object with a 
#given shape (csv file) . The object can be rendered with a given camera object

class object:
    """load an object from text file by name of this file
    can also get an transform along the axis (by default x= y= z= 0)
    """
    def __init__(self,text:str,name:str="new object"):
        self.name = name
        
        # here was the replaced csv importer
        def loadstl(txt):
            """returns a list of triangles , and a list of normals"""
            normal = []
            triangle = []

            file = open(txt,'r')
            content = file.readlines()
            file.close()
            for i in range(len(content)):
                cl = content[i]
                if cl.find("facet normal") != -1 :
                    cl =cl.replace("facet normal ","")
                    #cl.replace("\n","")
                    cl = cl.split(" ")
                    normal.append(vmath.vec(float(cl[0]),float(cl[1]),float(cl[2])))

                elif cl.find("outer loop") != -1 :
                    tri = []
                    for j in range(3):
                        cl = content[i+j+1]
                        cl = cl.replace("vertex ","")
                        #cl.replace("\n","")
                        cl = cl.split(" ")
                        tri.append(vmath.vec(float(cl[0]),float(cl[1]),float(cl[2])))
                    triangle.append(tri)
                    i += 5
            return triangle , normal


        self.form , self.normal = loadstl(text)

        self.position = v.vec(0,0,0) #Translation along the axes
        self.scale = v.vec(1,1,1) # scale alon the axes
        self.rotation = v.vec(0,0,0) #Rotation around the glaobal axes

        self.tri = self.form
        #print([str(j) for j in self.tri])
        

    def __str__(self): #just for debugging purposes
        l1 = "---- " + self.name + " ----\n"
        l2 = "pos : "+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+"\n"
        l3 = "rot : "+str(self.rx)+" , "+str(self.ry)+" , "+str(self.rz)+"\n"
        l4 = "siz : "+str(self.sx)+" , "+str(self.sy)+" , "+str(self.sz)+"\n"
        t = [l1,l2,l3,l4]
        return "".join([i for i in t])
    

    def render(self,camera:camera):
        """renders this object with a given camera object"""
        self.apply()
        camera.render(self.tri,self.normal)

    def setposition(self,v:v.vec):
        """moves the object to given values"""
        self.position.x = v.x
        self.position.y = v.y
        self.position.z = v.z
    def move(self,v:v.vec):
        """moves the object by given values"""
        self.position.x += v.x
        self.position.y += v.y
        self.position.z += v.z
        self.x = round(self.x,4)
        self.y = round(self.y,4)
        self.z = round(self.z,4)


    def setrotation(self,v,over:bool=True):
        """sets rotation to given values along global axis
        ---
        if over is False, only the rotation-values != 0 will overwrite an axis rotation
        """
        
        self.rotation.x = self.rotation.x if v.x == 0 and over == False else v.x
        self.rotation.y = self.rotation.y if v.y == 0 and over == False else v.y
        self.rotation.z = self.rotation.z if v.z == 0 and over == False else v.z
    def rotate(self,v):
        """rotates the object by given values along global axis"""
        self.rotation.x += v.x
        self.rotation.ry += v.y
        self.rotation.z += v.z

    def setsize(self,x,y,z):
        """sets the size to given values"""
        self.sx = x
        self.sy = y
        self.sz = z
    def size(self,x,y,z):
        """changes the size by given values"""
        self.sx = x
        self.sy = y
        self.sz = z

    def apply(self):
        """adds the transformation to the triangles"""
        self.tri = [] #resets the triangles
        
        for i in self.form: #applies transform on 
            tri = []
            for j in i:
                t = v.vec(j.x,j.y,j.z)
                t.mulvec(v.vec(self.sx,self.sy,self.sz)) #size
                t.rot(self.rx,self.ry,self.rz) #rotation
                t.addvec(v.vec(self.x,self.y,self.z)) #pos
                tri.append(t)
            self.tri.append(tri)
