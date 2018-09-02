"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Elijah Williams.
"""
###############################################################################
# DONE: 1.
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

larry = rg.SimpleTurtle('classic')
larry.pen = rg.Pen('violet', 3)
larry.speed = 20
terry = rg.SimpleTurtle('turtle')
terry.pen = rg.Pen('red', 3)
terry.speed = 20
for k in range(26):
    larry.draw_circle(13)
    larry.pen_up()
    larry.right(15)
    larry.forward(10)
    larry.pen_down()
    terry.draw_square(13)
    terry.pen_up()
    terry.left(15)
    terry.forward(10)
    terry.pen_down()

