import object as o 
import camera as c
import draw   as d
import vmath  as v



def main():
    suzanne = o.object("objects/test_object.stl")
    suzanne.move(v.vec(20,0,0))

    sony = c.camera(5)

    d.window(1440,720,"3D Demo","graphics/Logotrans.png")

    frate = 70

    while True:
        d.clear((44, 44, 44))
        
        dt = d.delta_time(frate)

        speed = 300*(dt/1000)
        suzanne.rotate(v.vec(0,0,-1))

        suzanne.render(sony)
        print(1000/dt)

        d.update()

if __name__ == "__main__":
    main()