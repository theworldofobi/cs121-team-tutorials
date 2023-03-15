def f(x):
    '''
    Real valued square function  f(x) == x^2
    '''

    return x*x


def integrate():
    ''' Integrate the function f using the rectangle method '''

    ### YOUR CODE GOES HERE
    #
    # Replace the following line with your code.
    # Your code should compute the integral of
    # function f from 0 to 1 using N rectangles.
    # You should store the value of the integral in
    # variable total_area
    #
    total_area = 0
    a = 0
    b = 1
    n = 10

    dx = (b - a) / n

    for i in range(0, n):
        area = f(i * dx) * dx
        total_area += area

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return total_area
