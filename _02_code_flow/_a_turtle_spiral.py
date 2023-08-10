import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    bob = turtle.Turtle()
    # This code sets our shape to a turtle
    bob.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    bob.speed(5)
    # Set your turtle's color using .color('green')
    bob.color('green')
    # Use a loop to repeat a the code below 50 times
    for i in range(50):
        bob.color(get_random_color())
        bob.forward(5*i)
        bob.right(360/7)
        bob.width(i)
        # Set the turtle color to a random color

        # Move the turtle (5*i) pixels. 'i' is the loop variable
        
        # Turn the turtle (360/7) degrees to the right
         
        # Change the turtle width to 'i' (the loop variable)
        
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
