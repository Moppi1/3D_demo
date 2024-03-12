import math

class vec:
    """"creates a 3 dimensinal vector with 3 given coords (all 0 at default)"""
    def __init__(self, x=0 , y=0 , z=0 ):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self): # hübsche Ausgabe : - )
        return f"{self.x},{self.y},{self.z}"

#3D Vector math

    def copy(self):
        return vec(self.x,self.y,self.z)

    def len(self): #returns length of vector
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def nor(self):#normalized vector
        """sets this vector to its normalized (len = 1)
        if ret== True : the normalized vector is only returned
        """
        len = self.len()
        if len != 0:
            x = self.x / len
            y = self.y / len
            z = self.z / len
            return vec(x,y,z)

    def addskal(self,s): #returns this vektor + skalar
        x = self.x + s
        y = self.y + s
        z = self.z + s
        return(vec(x,y,z))

    def addvec(self,v): #returns vector + vector2
        try:
            x = self.x + v.x
            y = self.y + v.y
            z = self.z + v.z
            return(vec(x,y,z))
        except:
            raise("v is not a vector")

    def subvec(self,v): #returns vector - vector2
        try:
            x = self.x - v.x
            y = self.y - v.y
            z = self.z - v.z
            return(vec(x,y,z))
        except:
            raise("v is not a vector")

    def mulvec(self,v): #retruns this vector multiplied with vector or scalar
        if type(v) == float or type(v) == int:
            x = self.x * v
            y = self.y * v
            z = self.z * v
        else:
            x = self.x * v.x
            y = self.y * v.y
            z = self.z * v.z
        return(vec(x,y,z))

    def skal(self,v): #returns dotproduct
        """returns skalarproduct of a this and a second vector"""
        return self.x * v.x + self.y * v.y + self.z * v.z

    def cross(self,v): #returns crossproduct
        """get the crossproduct of this vector and v2
        the crossproduct is normal to the surface created bei v and v2
        """
        x = self.y*v.z - self.z*v.y
        y = self.z*v.x - self.x*v.z
        z = self.x*v.y - self.y*v.x

        return vec(x , y , z)

    def on(self,v): #get vectorpart that is on v 
        """get the vectorpart of this vector which is on v"""

        skal = self.nor().skal(v)
        return v.mulvec(skal)

    def perp(self,v): #returns vectorpart that is perpendicular to v
        """get vectorpart that is perpendicular to v. """
        
        t = self.on(v)
        return self.subvec(t)

    def rot_axis(self,angle,axis="z"): #rotate vector around one globalaxes
        """rotates the vector around an axis(default:z) at a specific angle"""

        angle = math.radians(angle)

        if axis == "z": #rotation around z
            x = self.x * math.cos(angle) - self.y * math.sin(angle)
            y = self.x * math.sin(angle) + self.y * math.cos(angle)

            return vec(x,y,self.z)

        if axis == "x": #rotation around x
            y = self.y * math.cos(angle) - self.z * math.sin(angle)
            z = self.y * math.sin(angle) + self.z * math.cos(angle)

            return vec(self.x,y,z)
        
        if axis == "y": #rotation around y
            x = self.x * math.cos(angle) + self.z * math.sin(angle)
            z = -self.x * math.sin(angle) + self.z * math.cos(angle)

            return vec(x,self.y,z)

    def rot(self,rx=0,ry=0,rz=0): #rotate vector around multiple globalaxes
        """rotrates vector around all 3 global axis"""

        vt = self.rot_axis(rx,"x")
        vt = vt.rot_axis(ry,"y")
        vt = vt.rot_axis(rz,"z")


        return vt
