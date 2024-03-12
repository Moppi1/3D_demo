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


        distance = np.zeros([len(triangles),3],float)
        screen_coords = np.zeros([len(triangles),3,2],ve.vec)
        show = np.ones(len(triangles),bool)


        i = 0
        for t in triangles:
            
            #t_data[]
            j = 0
            for p in t: # every single point gets passed and projected

                u , v , dis = _project(p)

                if dis < 0.1 :
                    show[i][j]=False
                    break

                screen_coords[i][j][0] = v # corresponds the screen x
                screen_coords[i][j][1] = u # corresponds the screen y
                distance[i][j] = dis

                j += 1
            i += 1

            #finally drawing the triangles
        for i in screen_coords: #final print of the surfaces
            #color += 1
            d.fill_polygon_cords(i,(255,255,255), anti=True)#,anti=True
