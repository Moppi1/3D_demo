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

        p_width = d.get_window_dimensions()[0]// 2 # half the window width

        def _project(point):
            vp = point.subvec(self.position)

            dis = (vp.skal(self.facing)) # distance from camera origin

            u = ((vp.skal(self.up)) /  dis ) * self.focal_length # calculating u screen coordinate (5.1.)
            u *= p_width

            v = ((vp.skal(self.side)) /  dis ) * self.focal_length
            v *= p_width

            return u,v,dis # u is up axis


        distance = np.zeros(len(triangles),float)
        screen_coords = np.zeros([len(triangles),3,2],ve.vec)
        show = np.ones(len(triangles),bool)


        i = 0
        for t in triangles:
            
            average_dis = 0
            j = 0
            for p in t: # every single point gets passed and projected

                u , v , dis = _project(p)

                if dis < 0.1 :
                    show[i] = False
                    break

                screen_coords[i][j][0] = v # corresponds the screen x
                screen_coords[i][j][1] = u # corresponds the screen y
                average_dis += dis/3       # averade distance of one triangle from camera

                j += 1
            distance[i] = average_dis
            i += 1
        
        #sorting by distance for nicer rendering
        order = distance.argsort()

        #finally drawing the triangles
        j=0
        end = show.size
        for i in screen_coords[order]: #final print of the surfaces
            
            if show[j]:
                d.fill_polygon_cords(i,(0,(240/end)*j+8,0), anti=True)
            j += 1


    def rotate(self,v:ve.vec): # rotating the camera
        self.facing=self.facing.rot(v.x,v.y,v.z).nor()
        self.side  =self.side.rot(v.x,v.y,v.z).nor()
        self.up    =self.up.rot(v.x,v.y,v.z).nor()
