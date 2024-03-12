import object as o 
import camera as c
import draw   as d
import vmath  as v
import time   as t

# main variabels
frate = 70 # variable Framerate (Program tries to match the framerate)


def main():
    suzanne = o.object("objects/test_object.stl")
    suzanne.move(v.vec(20,0,0))

    sony = c.camera(5)

    d.window(1440,720,"3D Demo","graphics/Logotrans.png")

    def keybindings(spd):

        
        # Kamerarotation
        if d.key("Right"):sony.rotate(v.vec(0,0,1))
        if d.key("Left"):sony.rotate(v.vec(0,0,-1))

        # Objekt Steuerung
        if d.key("w"): suzanne.move(v.vec(0.1,0,0))
        if d.key("s"): suzanne.move(v.vec(-0.1,0,0))
        if d.key("a"): suzanne.move(v.vec(0,-0.1,0))
        if d.key("d"): suzanne.move(v.vec(0,0.1,0))
        if d.key("e"): suzanne.move(v.vec(0,0,-0.1))
        if d.key("q"): suzanne.move(v.vec(0,0,0.1))

        if d.key("y"): suzanne.size(v.vec(0.1,0.1,0.1))
        if d.key("x"): suzanne.size(v.vec(-0.1,-0.1,-0.1))

        if d.key("r"): suzanne.rotate(v.vec(0,0,1))


    # ===== Main-Loop =====
    while True:
        d.clear((44, 44, 44))

        
        dt = d.delta_time(frate) # calculating deltatime
        speed = 300*(dt/1000)

        keybindings(speed)

        suzanne.render(sony) #calling the redner function of the object (suzanne)
        print(1000/dt)


if __name__ == "__main__":
    main()