"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and MeghnaAllamudi.
"""
###############################################################################
# TODO: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

stephen = rg.SimpleTurtle('turtle')
stephen.pen = rg.Pen('blue', 3)
stephen.speed = 20

meghna = rg.SimpleTurtle('turtle')
meghna.pen = rg.Pen('red',5)
meghna.speed = 20

size = 300

for k in range(13):


    stephen.draw_square(size)


    stephen.pen_up()
    stephen.right(25)
    stephen.forward(10)
    stephen.left(25)


    stephen.pen_down()
    size = size - 9

for i in range(13):
    meghna.draw_square(size)

    meghna.pen_up()
    meghna.right(50)
    meghna.forward(20)
    meghna.left(50)

    meghna.pen_down()
    size=size-9

window.close_on_mouse_click()