import object as o 
import camera as c
from   draw   import*
import vmath  as v
#import time   as t

# main variabels
frate = 40 # variable Framerate (Program tries to match the framerate)


def main():
    suzanne = o.object("objects/suzanne.stl")#"objects/test_object.stl"
    suzanne.setrotation(v.vec(0,0,90),True)
    suzanne.move(v.vec(20,0,0))

    sony = c.camera(5)

    window(1440,720,"3D Demo","graphics/Logotrans.png")#720

    def keybindings(spd):

        
        # Kamerarotation
        if key("Right"):sony.rotate(v.vec(0,0,spd))
        if key("Left"): sony.rotate(v.vec(0,0,-spd))

        # Objekt Steuerung
        if key("w"): suzanne.move(v.vec(spd,0,0))
        if key("s"): suzanne.move(v.vec(-spd,0,0))
        if key("a"): suzanne.move(v.vec(0,-spd*0.5,0))
        if key("d"): suzanne.move(v.vec(0,spd*0.5,0))
        if key("e"): suzanne.move(v.vec(0,0,-spd))
        if key("q"): suzanne.move(v.vec(0,0,spd))

        if key("y"): suzanne.size(v.vec(spd*0.1,spd*0.1,spd*0.1))
        if key("x"): suzanne.size(v.vec(spd*-0.1,spd*-0.1,spd*-0.1))

        if key("r"): suzanne.rotate(v.vec(0,0,1))


    # ===== Main-Loop =====
    while True:
        clear((44, 44, 44))
        
        dt = delta_time(frate) # calculating deltatime
        speed = (dt/100)

        keybindings(speed)

        suzanne.render(sony) #calling the render function of the object (suzanne)

        update()


if __name__ == "__main__":
    main()