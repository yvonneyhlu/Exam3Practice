"""
PRACTICE Test 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS in 2D GRAPHICS problems.  ***

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Youhua Lu.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Test 2 question.
#     5 is a "typical" Test 2 question.
#     7 is a "hard" Test 2 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 2 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
########################################################################

import rosegraphics as rg
import math

def main():
    """ Calls the   TEST   functions in this module. """
    # run_test_hourglass()
    run_test_many_hourglasses()


def run_test_hourglass():
    """ Tests the    hourglass    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   hourglass   function:')
    print('--------------------------------------------------')

    test1 = '(n = 3, radius = 40, blue)'
    test2 = '(n = 8, radius = 15, green)'
    title1 = 'Hourglass, two tests: {} and {}'.format(test1, test2)
    window1 = rg.RoseWindow(600, 500, title1)

    hourglass(window1, 3, rg.Point(150, 200), 40, 'blue')
    hourglass(window1, 8, rg.Point(450, 250), 15, 'green')

    window1.close_on_mouse_click()

    test3 = '(n = 6, radius = 30, red)'
    title2 = 'Hourglass, one more test: {}'.format(test3)
    window2 = rg.RoseWindow(400, 700, title2)

    hourglass(window2, 6, rg.Point(200, 350), 30, 'red')

    window2.close_on_mouse_click()


def hourglass(window, n, point, radius, color):
    """
    See   hourglass_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Displays an "hourglass" shape of circles in the given window.
      -- Each circle has the given radius and given color.
      -- Each circle has a horizontal line drawn through it.
      -- The middlemost of the circles is centered at the given point.
      -- There is a single circle in that middlemost row.
      -- There are n rows (including the middlemost row)
            of circles going UP from the middlemost circle.
      -- There are n rows (including the middlemost row)
           of circles going DOWN from the middlemost circle.
      -- Each circle barely touches its neighbor circles.

    Preconditions:
      :type window: rg.RoseWindow
      :type n: int
      :type point: rg.Point
      :type radius: int
      :type color: str
    where n and radius are positive and color is a string that denotes
    a color that rosegraphics understands.
    """
    # ------------------------------------------------------------------
    # done: 2. Implement and test this function.
    #       We provided some tests for you (above).
    # ------------------------------------------------------------------
    ####################################################################
    # BONUS: Avoid replicated code if you can.  Hint: You are allowed
    #        to define an additional function(s) if you wish.
    ####################################################################
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      8
    #    TIME ESTIMATE:  25 minutes (warning: this problem is challenging)
    # ------------------------------------------------------------------
    center = rg.Circle(point, radius)
    center.attach_to(window)
    center.fill_color = color
    l = rg.Line(rg.Point(point.x-radius, point.y), rg.Point(point.x+radius, point.y))
    l.attach_to(window)
    for k in range(-n+1, n):
        for j in range(1, abs(k)+1):
            ps = rg.Point(point.x-radius*abs(k), point.y+math.sqrt(3)*k*radius)
            c1 = rg.Circle(ps,radius)
            c1.fill_color = color
            c1.attach_to(window)
            l = rg.Line(rg.Point(ps.x-radius,ps.y),rg.Point(ps.x+radius,ps.y))
            l.attach_to(window)
            c2 = rg.Circle(rg.Point(c1.center.x+2*radius*j, c1.center.y), radius)
            c2.fill_color = color
            c2.attach_to(window)
            l2 = rg.Line(rg.Point(c2.center.x-radius, c2.center.y), rg.Point(c2.center.x+radius, c2.center.y))
            l2.attach_to(window)
    window.render()


def run_test_many_hourglasses():
    """ Tests the    many_hourglasses    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   many_hourglasses   function:')
    print('--------------------------------------------------')

    test1 = '(n = 4, radius = 30, red-blue-black-green)'
    test2 = '(n = 3, radius = 70, brown-cyan-yellow-green)'
    title1 = 'Many hourglasses, two tests: {} and {}'.format(test1,
                                                             test2)
    window1 = rg.RoseWindow(800, 400, title1)

    square1 = rg.Square(rg.Point(50, 150), 30)
    square2 = rg.Square(rg.Point(400, 200), 70)

    many_hourglasses(window1, square1, 4,
                     ('red', 'blue', 'black', 'green'))
    many_hourglasses(window1, square2, 3,
                     ('brown', 'cyan', 'yellow', 'green'))
    window1.close_on_mouse_click()

    test3 = '(n = 7, radius = 40, red-black-blue)'
    title2 = 'Many hourglasses, one more test: {}'.format(test3)
    window2 = rg.RoseWindow(1200, 500, title2)

    square3 = rg.Square(rg.Point(50, 250), 40)

    many_hourglasses(window2, square3, 7, ('red', 'black', 'blue'))

    window2.close_on_mouse_click()


def many_hourglasses(window, square, m, colors):
    """
    See   many_hourglasses_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Displays  m  rectangles, where:
      -- Each rectangle has an hourglass of circles inside it,
           per the  hourglass  function above.
      -- The circles in the hourglasses are all the same size.
      -- The leftmost rectangle is the given square, and it contains
           an hourglass with a single circle that fills the square.
      -- Each successive rectangle is immediately to the right of the
           previous rectangle, and each contains an hourglass with
           the hourglass'  n   being one greater than the  n  used
           for the previous rectangle.
      -- The colors for the hourglass figures use the given sequence of
           colors, "wrapping" if m exceeds the length of the sequence.

    Preconditions:
      :type window: rg.RoseWindow
      :type square: rg.Square
      :type m: int
      :type colors: (list | tuple) of str
    where m is positive and colors is a sequence of strings,
    each of which denotes a color that rosegraphics understands.
    """
    # ------------------------------------------------------------------
    # done: 3. Implement and test this function.
    #       We provided some tests for you (above).
    # ------------------------------------------------------------------
    ####################################################################
    # IMPORTANT:
    #   1. Partial credit if you draw JUST the rectangles.
    #   2. No additional credit unless you CALL the  hourglass  function
    #        in the PREVIOUS problem appropriately
    #        to draw the hourglass figures.
    ####################################################################
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7  (assuming that you already have
    #                         a correct "hourglass" function above)
    #    TIME ESTIMATE:  20 minutes (warning: this problem is challenging)
    # ------------------------------------------------------------------
    radius = square.length_of_each_side/2
    center = square.center
    a = 0
    hourglass(window, 1, center, radius, colors[a])
    center2 = center
    rx = rg.Rectangle(rg.Point(center.x-radius,center.y-radius),rg.Point(center.x+radius,center.y+radius))
    rx.attach_to(window)
    for k in range(m-1):
        px = rg.Point(center2.x + (3+2*k)*radius,center.y)
        center2.x = px.x
        a = a + 1
        if a == len(colors):
            a = 0
        hourglass(window,k+2,px,radius,colors[a])
        p1 = rg.Point(center2.x-(k+2)*radius, center2.y-radius-(k+1)*radius*math.sqrt(3))
        p2 = rg.Point(center2.x+(k+2)*radius, center2.y+radius+(k+1)*radius*math.sqrt(3))
        r = rg.Rectangle(p1, p2)
        r.attach_to(window)
    window.render()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
