# Importieng the libraries
import vmath as ve
import draw as d
import numpy as np

# === Camara Object for rendering the objects (projection) ===
class camera():
    def __init__(self,focal_length:float) -> None:
        self.focal_length = focal_length
        self.position = ve.vec(0,0,0)
        self.facing = ve.vec(1,0,0)
        self.side = ve.vec(0,1,0)
        self.up = self.facing.cross(self.side)

        print("camera", str(self.up))
    
    def change_focal_length(self,nv): # replaces old focal length by new value
        self.focal_length = nv 
    
    def render(self,triangles) -> None:
        """triangles have to have the shape [[v1,v2,v3],...]"""

        p_width = d.get_window_dimensions()[1]// 2 # half the window width

        def _project(point): #projection of a single point (given as vector)

            vp = point.subvec(self.position)

            dis = vp.skal(self.facing) # distance from camera origin

            u = (vp.skal(self.up)  * self.focal_length) /  dis  # calculating u screen coordinate (5.1.)
            #u = u-1 if u >1 else u+1
            u *= p_width

            v = (vp.skal(self.side)* self.focal_length) /  dis  
            #v = v-1 if v >1 else v+1
            v *= p_width

            return u,v,dis
        
        def proj(point):
            vp = point.subvec(self.position)

            dis = vp.skal(self.facing)

            per = vp.perp(self.facing)

            v = (per.y/dis) * self.focal_length
            u = (per.z/dis) * self.focal_length
            return u*p_width,v*p_width,dis


        distance = np.zeros(len(triangles),float)
        screen_coords = np.zeros([len(triangles),3,2],ve.vec)
        show = np.ones(len(triangles),bool)


        i = 0
        for t in triangles:
            
            average_dis = 0
            j = 0
            for p in t: # every single point gets passed and projected

                u , v , dis = _project(p)

                if dis < 0.3 :
                    show[i] = False
                    break

                screen_coords[i][j][0] = v # corresponds the screen x
                screen_coords[i][j][1] = u # corresponds the screen y
                average_dis += dis/3       # averade distance of one triangle from camera

                j += 1
            distance[i] = average_dis
            i += 1
        
        
        def shade(): #shade with different colors by higher distance

            #sorting by distance for nicer rendering
            order = distance.argsort()[::-1]

            j=0
            end = show.size
            for i in screen_coords[order]: #final print of the surfaces
                
                if show[j]:
                    d.fill_polygon_cords(i,(0,(240/end)*j+8,0), anti=True)
                j += 1
            j=0

        def flat():  #shade in one single color (white)
            end = show.size
            j=0
            for i in screen_coords: #final print of the surfaces

                if show[j]:
                    d.fill_polygon_cords(i,(255,255,255))
                j += 1
        
        #finally drawing the triangles
        shade()



    def rotate(self,v:ve.vec): # rotating the camera
        self.facing=self.facing.rot(v.x,v.y,v.z).nor()
        self.side  =  self.side.rot(v.x,v.y,v.z).nor()
        self.up    =    self.up.rot(v.x,v.y,v.z).nor()
