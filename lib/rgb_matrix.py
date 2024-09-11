from machine import Pin
import weather as wd
import random
import utime as time
import array
import rp2
from math import cos, sin, radians, sqrt
from pico_system import get_files
import machine

# Defining functiones for showing numbers 0 to 9. (x,y = position most left bottom corner, color = color of number, size = x times original size)...

def set_8(matrix_obj: object, x, y, color, size,show:bool=True):

    # Fra nederst til øverst
    matrix_obj.set_horr_seg(x, y, color, 3+size, show) # Horisontal nede
    matrix_obj.set_horr_seg(x, y+2+size, color, 3+size, show) # Horisontal mitt
    matrix_obj.set_horr_seg(x, y+4+size*2, color, 3+size, show) # Horisontal oppe

    # Til høyre
    matrix_obj.set_vert_seg(x, y, color, 3+size, show) # vertikal, venstre, nede
    matrix_obj.set_vert_seg(x, y+2+size , color, 3+size, show) # vertikal, venstre, oppe
    # Til venstre
    matrix_obj.set_vert_seg(x+2+size, y, color, 3+size, show) # vertikal, høyre, nede
    matrix_obj.set_vert_seg(x+2+size, y+2+size, color, 3+size, show) # vertikal, høyre, oppe

def set_0(matrix_obj: object, x, y, color, size, show:bool=True):
    # Fra nederst til øverst
    matrix_obj.set_horr_seg(x, y, color, 3+size,show) # Horisontal nede
    matrix_obj.set_horr_seg(x, y+4+size*2, color, 3+size,show) # Horisontal oppe

    # Til høyre
    matrix_obj.set_vert_seg(x, y, color, 3+size,show) # vertikal, venstre, nede
    matrix_obj.set_vert_seg(x, y+2+size , color, 3+size,show) # vertikal, venstre, oppe
    # Til venstre
    matrix_obj.set_vert_seg(x+2+size, y, color, 3+size,show) # vertikal, høyre, nede
    matrix_obj.set_vert_seg(x+2+size, y+2+size, color, 3+size,show) # vertikal, høyre, oppe

def set_1(matrix_obj: object, x, y, color, size,show:bool=True):
    matrix_obj.set_vert_seg(x+2+size, y, color, 5+size, show) # vertikal, høyre, nede
    matrix_obj.set_pixel_color(x+1+size,y+3,color)

def set_2(matrix_obj: object, x, y, color, size,show:bool=True):
        # Fra nederst til øverst
    matrix_obj.set_horr_seg(x, y, color, 3+size, show) # Horisontal nede
    matrix_obj.set_horr_seg(x, y+2+size, color, 3+size, show) # Horisontal mitt
    matrix_obj.set_horr_seg(x, y+4+size*2, color, 3+size, show) # Horisontal oppe

    # Til høyre
    matrix_obj.set_vert_seg(x, y, color, 3+size, show) # vertikal, venstre, nede

    # Til venstre
    matrix_obj.set_vert_seg(x+2+size, y+2+size, color, 3+size, show) # vertikal, høyre, oppe

def set_3(matrix_obj: object, x, y, color, size,show:bool=True):
    # Fra nederst til øverst
    matrix_obj.set_horr_seg(x, y, color, 3+size, show) # Horisontal nede
    matrix_obj.set_horr_seg(x, y+2+size, color, 3+size, show) # Horisontal mitt
    matrix_obj.set_horr_seg(x, y+4+size*2, color, 3+size, show) # Horisontal oppe

    # Til venstre
    matrix_obj.set_vert_seg(x+2+size, y, color, 3+size, show) # vertikal, høyre, nede
    matrix_obj.set_vert_seg(x+2+size, y+2+size, color, 3+size, show) # vertikal, høyre, oppe

def set_4(matrix_obj: object, x, y, color, size,show:bool=True):
    # Fra nederst til øverst
    matrix_obj.set_horr_seg(x, y+2+size, color, 3+size, show) # Horisontal mitt

    # Til høyre
    matrix_obj.set_vert_seg(x, y+2+size , color, 3+size, show) # vertikal, venstre, oppe
    # Til venstre
    matrix_obj.set_vert_seg(x+2+size, y, color, 3+size, show) # vertikal, høyre, nede
    matrix_obj.set_vert_seg(x+2+size, y+2+size, color, 3+size, show) # vertikal, høyre, oppe

def set_5(matrix_obj: object, x, y, color, size,show:bool=True):
    # Fra nederst til øverst
    matrix_obj.set_horr_seg(x, y, color, 3+size, show) # Horisontal nede
    matrix_obj.set_horr_seg(x, y+2+size, color, 3+size, show) # Horisontal mitt
    matrix_obj.set_horr_seg(x, y+4+size*2, color, 3+size, show) # Horisontal oppe

    # Til høyre
    matrix_obj.set_vert_seg(x, y+2+size , color, 3+size, show) # vertikal, venstre, oppe
    # Til venstre
    matrix_obj.set_vert_seg(x+2+size, y, color, 3+size, show) # vertikal, høyre, nede

def set_6(matrix_obj: object, x, y, color, size,show:bool=True):
    # Fra nederst til øverst
    matrix_obj.set_horr_seg(x, y, color, 3+size, show) # Horisontal nede
    matrix_obj.set_horr_seg(x, y+2+size, color, 3+size, show) # Horisontal mitt
    matrix_obj.set_horr_seg(x, y+4+size*2, color, 3+size, show) # Horisontal oppe

    # Til høyre
    matrix_obj.set_vert_seg(x, y, color, 3+size, show) # vertikal, venstre, nede
    matrix_obj.set_vert_seg(x, y+2+size , color, 3+size, show) # vertikal, venstre, oppe
    # Til venstre
    matrix_obj.set_vert_seg(x+2+size, y, color, 3+size, show) # vertikal, høyre, nede

def set_7(matrix_obj: object, x, y, color, size,show:bool=True):
    # Fra nederst til øverst
    matrix_obj.set_horr_seg(x, y+4+size*2, color, 3+size, show) # Horisontal oppe

    # Til venstre
    matrix_obj.set_vert_seg(x+2+size, y, color, 3+size, show) # vertikal, høyre, nede
    matrix_obj.set_vert_seg(x+2+size, y+2+size, color, 3+size, show) # vertikal, høyre, oppe

def set_9(matrix_obj: object, x, y, color, size,show:bool=True):
        # Fra nederst til øverst
    matrix_obj.set_horr_seg(x, y+2+size, color, 3+size, show) # Horisontal mitt
    matrix_obj.set_horr_seg(x, y+4+size*2, color, 3+size, show) # Horisontal oppe

    # Til høyre
    matrix_obj.set_vert_seg(x, y+2+size , color, 3+size, show) # vertikal, venstre, oppe
    # Til venstre
    matrix_obj.set_vert_seg(x+2+size, y, color, 3+size, show) # vertikal, høyre, nede
    matrix_obj.set_vert_seg(x+2+size, y+2+size, color, 3+size, show) # vertikal, høyre, oppe

# For displaying numbers
def set_a(matrix_obj, x, y, color, size=0):
    # set_vert_seg(x, y, color, 4+size, False)
    # set_vert_seg(x+3+size, y, color, 4+size, False)

    # set_horr_seg(x+1, y+2+size, color, 2+size, False)
    # set_horr_seg(x+1, y+4+size, color, 2+size, False)

    matrix_obj.set_vert_seg(x, y, color, 4, False)
    matrix_obj.set_vert_seg(x+3, y, color, 4, False)

    matrix_obj.set_horr_seg(x+1, y+2, color, 2, False)
    matrix_obj.set_horr_seg(x+1, y+4, color, 2, False)

def set_b(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y,color,2,False)
    matrix_obj.set_horr_seg(x+1,y+2,color,2,False)
    matrix_obj.set_horr_seg(x+1,y+4,color,2,False)

    matrix_obj.set_vert_seg(x+3,y+1,color,1,False)
    matrix_obj.set_vert_seg(x+3,y+3,color,1,False)

    matrix_obj.set_vert_seg(x,y,color,5,False)
def set_c(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y,color,2,False)
    matrix_obj.set_horr_seg(x+1,y+4,color,2,False)

    matrix_obj.set_vert_seg(x,y+1,color,3,False)

    matrix_obj.set_vert_seg(x+3,y+1,color,1,False)
    matrix_obj.set_vert_seg(x+3,y+3,color,1,False)
def set_d(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y,color,2,False)
    matrix_obj.set_horr_seg(x+1,y+4,color,2,False)

    matrix_obj.set_vert_seg(x,y,color,5,False)
    matrix_obj.set_vert_seg(x+3,y+1,color,3,False)
def set_e(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y,color,3,False)
    matrix_obj.set_horr_seg(x+1,y+2,color,2,False)
    matrix_obj.set_horr_seg(x+1,y+4,color,3,False)

    matrix_obj.set_vert_seg(x,y,color,5,False)
def set_f(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y+2,color,2,False)
    matrix_obj.set_horr_seg(x+1,y+4,color,3,False)

    matrix_obj.set_vert_seg(x,y,color,5,False)
def set_g(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y,color,2,False)
    matrix_obj.set_horr_seg(x+1,y+4,color,2,False)

    matrix_obj.set_vert_seg(x,y+1,color,3,False)

    matrix_obj.set_vert_seg(x+3,y+1,color,1,False)
    matrix_obj.set_horr_seg(x+2,y+2,color,2,False)
def set_h(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y,color,5,False)
    matrix_obj.set_vert_seg(x+3,y,color,5,False)

    matrix_obj.set_horr_seg(x+1,y+2,color,2,False)
def set_i(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y,color,5,False)
def set_j(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y+1,color,1,False)
    matrix_obj.set_vert_seg(x+3,y+1,color,4,False)

    matrix_obj.set_horr_seg(x+1,y,color,2,False)
def set_k(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y,color,5,False)

    matrix_obj.set_vert_seg(x+3,y,color,1,False)
    matrix_obj.set_vert_seg(x+2,y+1,color,1,False)
    matrix_obj.set_vert_seg(x+1,y+2,color,1,False)
    matrix_obj.set_vert_seg(x+2,y+3,color,1,False)
    matrix_obj.set_vert_seg(x+3,y+4,color,1,False)
def set_l(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y,color,5,False)
    matrix_obj.set_horr_seg(x+1,y,color,3,False)
def set_m(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y,color,5,False)
    matrix_obj.set_vert_seg(x+3,y,color,5,False)

    matrix_obj.set_horr_seg(x+1,y+3,color,2,False)
def set_n(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y,color,5,False)
    matrix_obj.set_vert_seg(x+3,y,color,5,False)

    matrix_obj.set_horr_seg(x+1,y+3,color,1,False)
    matrix_obj.set_horr_seg(x+2,y+2,color,1,False)
def set_o(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y,color,2,False)
    matrix_obj.set_horr_seg(x+1,y+4,color,2,False)

    matrix_obj.set_vert_seg(x,y+1,color,3,False)
    matrix_obj.set_vert_seg(x+3,y+1,color,3,False)
def set_p(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y,color,5,False)

    matrix_obj.set_horr_seg(x+1,y+4,color,2,False)
    matrix_obj.set_horr_seg(x+1,y+2,color,2,False)
    matrix_obj.set_horr_seg(x+2,y+3,color,1,False)
def set_q(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y,color,2,False)
    matrix_obj.set_horr_seg(x+1,y+4,color,2,False)

    matrix_obj.set_vert_seg(x,y+1,color,3,False)
    matrix_obj.set_vert_seg(x+3,y+1,color,3,False)

    matrix_obj.set_vert_seg(x+3,y,color,1,False)
    matrix_obj.set_vert_seg(x+2,y+1,color,1,False)
def set_r(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y,color,5,False)

    matrix_obj.set_vert_seg(x+2,y,color,1,False)
    matrix_obj.set_vert_seg(x+1,y+1,color,1,False)
    matrix_obj.set_horr_seg(x+1,y+2,color,2,False)
    matrix_obj.set_vert_seg(x+3,y+2,color,3,False)
    matrix_obj.set_horr_seg(x+1,y+4,color,2,False)
def set_s(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x,y,color,3,False)
    matrix_obj.set_horr_seg(x+3,y+1,color,1,False)
    matrix_obj.set_horr_seg(x+1,y+2,color,2,False)
    matrix_obj.set_horr_seg(x,y+3,color,1,False)
    matrix_obj.set_horr_seg(x+1,y+4,color,3,False)
def set_t(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x+1,y,color,4,False)
    matrix_obj.set_horr_seg(x,y+4,color,3,False)
def set_u(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y,color,2,False)

    matrix_obj.set_vert_seg(x,y+1,color,4,False)
    matrix_obj.set_vert_seg(x+3,y+1,color,4,False)
def set_v(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y,color,1,False)

    matrix_obj.set_vert_seg(x,y+1,color,4,False)
    matrix_obj.set_vert_seg(x+2,y+1,color,4,False)
def set_w(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y,color,5,False)
    matrix_obj.set_vert_seg(x+3,y,color,5,False)

    matrix_obj.set_horr_seg(x+1,y+1,color,2,False)
def set_x(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x,y,color,2,False)
    matrix_obj.set_vert_seg(x+3,y,color,2,False)

    matrix_obj.set_horr_seg(x+1,y+2,color,2,False)

    matrix_obj.set_vert_seg(x,y+3,color,2,False)
    matrix_obj.set_vert_seg(x+3,y+3,color,2,False)
def set_y(matrix_obj, x, y, color):
    matrix_obj.set_vert_seg(x+1,y,color,3,False)
    matrix_obj.set_vert_seg(x,y+3,color,2,False)
    matrix_obj.set_vert_seg(x+2,y+3,color,2,False)
def set_z(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x,y,color,4,False)
    matrix_obj.set_horr_seg(x,y+1,color,1,False)
    matrix_obj.set_horr_seg(x+1,y+2,color,2,False)
    matrix_obj.set_horr_seg(x+3,y+3,color,1,False)
    matrix_obj.set_horr_seg(x,y+4,color,4,False)
def set_dot(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x,y,color,1,False)
def set_colon(matrix_obj, x, y, color):
    matrix_obj.set_pixel_color(x,y,color)
    matrix_obj.set_pixel_color(x,y+4,color)
def set_exclamation_mark(matrix_obj, x, y, color):
    matrix_obj.set_pixel_color(x+1,y,color)
    matrix_obj.set_vert_seg(x+1,y+2,color,3,False)
def set_question_mark(matrix_obj, x, y, color):
    matrix_obj.set_pixel_color(x+1,y,color)
    matrix_obj.set_pixel_color(x+1,y+2,color)
    matrix_obj.set_pixel_color(x+2,y+3,color)
    matrix_obj.set_horr_seg(x,y+4,color,3,False)
def set_hyphen(matrix_obj, x, y, color):
    matrix_obj.set_horr_seg(x+1,y+2,color,2,False)


#
# Some rainbow effects
#
def wheel(pos):
    """Generate rainbow colors across 0-255 positions"""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

def rainbow_spiral(matrix_obj: object, max_runs: int):
        center_x = 8
        center_y = 8
        max_radius = 11

        angle_offset = 0
        runs = 0

        cos_table = [int(1000 * cos(radians(angle))) for angle in range(360)]
        sin_table = [int(1000 * sin(radians(angle))) for angle in range(360)]

        while matrix_obj.run and runs <= max_runs:
            for angle in range(360):
                for radius in range(max_radius):
                    x = center_x + (radius * cos_table[(angle + angle_offset) % 360]) // 1000
                    y = center_y + (radius * sin_table[(angle + angle_offset) % 360]) // 1000
                    color = wheel((angle + radius * 10) % 256)
                    matrix_obj.set_pixel_color(x, y, color)

                    # Break out if necessary
                    if not matrix_obj.run:
                        return
                    # self.strip.set_pixel(self.coordinates_to_number(x, y), color)
                matrix_obj.show()
                # time.sleep(wait)
            angle_offset += 10  # Increase the angle offset to make the spiral rotate
            runs += 1

def rainbow_wave(matrix_obj: object, times:int = -1):
    phase = 0
    while True:
        for x in range(16):
            for y in range(16):
                color = wheel((x + phase) % 256)
                #matrix_obj.strip.set_pixel(matrix_obj.coordinates_to_number(x, y), color)
                matrix_obj.set_pixel_color(x,y,color)

                # Break out if necesary
                if matrix_obj.run == False:
                    return

        matrix_obj.show()
        #time.sleep(duration)
        phase += 1  # Increment phase for horizontal movement
        if times > 0:
            times -= 1
        if times == 0:
            break

def randomRGB(matrix_obj: object, runtime:float):
    delay = 0.4
    dot_count = 50
    start_time = time.time()

    while matrix_obj.run == True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        for _ in range(dot_count):
            matrix_obj.set_np(random.randint(0, matrix_obj.numpix-1), Matrix_fun.colors_rgb[random.randint(0, len(Matrix_fun.colors_rgb)-1)])
            #matrix_obj.np[random.randint(0, matrix_obj.numpix-1)] = Matrix_fun.colors_rgb[random.randint(0, len(Matrix_fun.colors_rgb)-1)]
        matrix_obj.show()
        time.sleep(delay)
        matrix_obj.wait(delay)
        matrix_obj.clear()

        if elapsed_time > runtime:
            return

def firework_animation(matrix):
    def shoot_firework(start_x, start_y, end_y, color):
        for y in range(start_y, end_y + 1):
            matrix.set_pixel_color(start_x, y, color)
            if y != start_y:
                matrix.set_pixel_color(start_x, y - 1, (0, 0, 0))
            matrix.show()
            time.sleep(0.05)

            if matrix.run != True:
                return

    def explode_firework(center_x, center_y, colors):
        for radius in range(1, 5):  # Expanding radius
            color = random.choice(colors)
            for angle in range(0, 360, 30):  # Firework spread
                rad = radians(angle)  # Convert to radians
                x = int(center_x + radius * random.uniform(0.8, 1.2) * cos(rad))
                y = int(center_y + radius * random.uniform(0.8, 1.2) * sin(rad))
                if 0 <= x < matrix.MATRIX_WIDTH and 0 <= y < matrix.MATRIX_HEIGHT:
                    matrix.set_pixel_color(x, y, color)

                if matrix.run != True:
                    return

            matrix.show()
            time.sleep(0.1)

    matrix.clear()
    colors = matrix.colors_rgb  # Various colors

    for _ in range(5):  # 5 fireworks
        #start_x = center_x
        start_x =  random.randint(0, matrix.MATRIX_WIDTH - 1)
        start_y = 0
        end_y = random.randint(matrix.MATRIX_HEIGHT // 2, matrix.MATRIX_HEIGHT - 1)  # Random height for explosion
        shoot_color = (255, 255, 255)  # White for shooting effect

        shoot_firework(start_x, start_y, end_y, shoot_color)
        explode_firework(start_x, end_y, colors)
        matrix.clear()
        matrix.wait(0.1)

        if matrix.run != True:
            return

def balls_bouncing_animation(matrix, num_balls, runtime):
    def distance(ball1, ball2):
        # Calculate Euclidean distance between two balls
        return sqrt((ball1[0] - ball2[0]) ** 2 + (ball1[1] - ball2[1]) ** 2)

    balls = []
    for _ in range(num_balls):
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        ball_x, ball_y = random.randint(0, 15), random.randint(0, 15)
        velocity_x, velocity_y = random.choice([-1, 1]), random.choice([-1, 1])
        balls.append((ball_x, ball_y, velocity_x, velocity_y, ball_color))

        # Break out if necessary
        if not matrix.run:
            return

    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time < runtime:
            for i in range(len(balls)):
                ball_x, ball_y, velocity_x, velocity_y, ball_color = balls[i]

                # Update ball position
                ball_x += velocity_x
                ball_y += velocity_y

                # Check for collisions with the boundaries
                if ball_x >= matrix.MATRIX_WIDTH:
                    ball_x = matrix.MATRIX_WIDTH - 1
                    velocity_x *= -1  # Reverse x velocity
                elif ball_x < 0:
                    ball_x = 0
                    velocity_x *= -1  # Reverse x velocity

                if ball_y >= matrix.MATRIX_HEIGHT:
                    ball_y = matrix.MATRIX_HEIGHT - 1
                    velocity_y *= -1  # Reverse y velocity
                elif ball_y < 0:
                    ball_y = 0
                    velocity_y *= -1  # Reverse y velocity

                # Check for collisions between balls
                for j in range(len(balls)):
                    if i != j:
                        other_ball_x, other_ball_y, _, _, _ = balls[j]
                        if distance((ball_x, ball_y), (other_ball_x, other_ball_y)) <= 1:
                            # Balls collide, reverse velocities
                            velocity_x *= -1
                            velocity_y *= -1
                            break

                    # Break out if necessary
                    if not matrix.run:
                        return

                balls[i] = (ball_x, ball_y, velocity_x, velocity_y, ball_color)

            matrix.clear()
            for ball_x, ball_y, _, _, ball_color in balls:
                matrix.set_pixel_color(ball_x, ball_y, ball_color)
            matrix.show()
            time.sleep(0.1)

            # Break out if necessary
            if not matrix.run:
                return
        else:
            return


@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
   # Define timing constants for the WS2812 protocol
    T1 = 2  # Number of cycles for a logic 1
    T2 = 5  # Number of cycles for the total bit duration
    T3 = 3  # Number of cycles for a logic 0

    # Define the start of the program
    wrap_target()

    # Loop over each bit to send out the data
    label("bitloop")

    # Output a bit from the shift register (x) and set the side-set pin low
    out(x, 1)               .side(0)    [T3 - 1]

    # If the bit is 0, jump to the "do_zero" label, otherwise continue
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]

    # Loop back to process the next bit
    jmp("bitloop")          .side(1)    [T2 - 1]

    # Handle the case for sending a logic 0
    label("do_zero")
    nop().side(0)                       [T2 - 1]

    # Define the end of the program
    wrap()

class Matrix:
    """
    A class for controlling a WS2812B LED matrix connected to a Raspberry Pi Pico.

    Atributes:
    - width: Number of pixels in the x-direction.
    - height: Number of pixels in the y-direction.
    - gpio_pin: GPIO pin to which the matrix is connected.
    """

    def __init__(self, width:int, height:int, gpio_pin:int) -> None:
        self.numpix = width * height # Total number of pixels
        self.MATRIX_WIDTH = width
        self.MATRIX_HEIGHT = height
        self.brightness = 100 # Brightness percentage (0-100)

        # Create the state machine
        self.sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(gpio_pin))
        #self.sm = rp2.StateMachine(0, ws2812, freq=4_000_000, sideset_base=Pin(gpio_pin))
        self.sm.active(1)

        # Initialize the pixel array
        self.np = array.array("I", [0 for _ in range(self.numpix)])

    def get_buffer_data(self) -> list:
        """
        Returns the buffer data as a list of RGB values.
        """

        #return [pixel for pixel in self.np]
        return [[(self.np[i] >> 8) & 0xff, (self.np[i] >> 16) & 0xff, self.np[i] & 0xff] for i in range(self.numpix)]

    def set_brightness(self, brightness_percent:int):
        """
        Sets the brightness of the LEDs, brightness_percent must be between 0-100.
        """

        # Makes shure the percent is in the allowed range
        if brightness_percent > 100:
            brightness_percent = 100
        elif brightness_percent < 0:
            brightness_percent = 0
        self.brightness = brightness_percent

    def adjust_brightness(self, color, brightness) -> tuple:
        """
         Adjusts the brightness of an RGB color.

        Parameters:
        - color: Tuple (R, G, B)
        - brightness: Float from 0.0 to 1.0

        Returns:
        - Adjusted color tuple
        """
        r, g, b = color
        r = int(r * brightness)
        g = int(g * brightness)
        b = int(b * brightness)
        return (r, g, b)

    def clear(self):
        """ Clearing buffer """
        for i in range(self.numpix):
            self.np[i] = 0

    def show(self):
        """ Display data stored in buffer """
        irq_state = machine.disable_irq()  # Disable interrupts
        self.sm.put(self.np, 8)
        machine.enable_irq(irq_state)  # Enable interrupts

    def coordinates_to_number(self, x, y):
        """ Translate coordinates to the correct LED number """
        if y % 2 == 0:
            # Even row (0-based), numbered from left to right
            return y * self.MATRIX_WIDTH + x
        else:
            # Odd row (0-based), numbered from right to left
            return y * self.MATRIX_WIDTH + (self.MATRIX_WIDTH-1 - x)

    def set_np(self, num, color):
        """
        Set color of selected neopixel
        """
        if self.brightness == 100:
            r, g, b = color
            r, g, b = int(r), int(g), int(b)
        else:
            r, g, b = self.adjust_brightness(color, self.brightness / 100)


        self.np[num] = (r << 8) | (g << 16) | b

    def set_pixel_color(self, x:int, y:int, color) -> None:
        """
        Sets the selected pixel to the selected color. Bottom left corner is (0,0).

        Parameters:
        - x: x-coordinate
        - y: y-coordinate
        - color: color to set the pixel to, should be tuple (R, G, B)
        """
        # check that the pixel is not out of range
        if x < self.MATRIX_WIDTH and x >= 0 and y < self.MATRIX_HEIGHT and y >= 0:
            self.set_np(self.coordinates_to_number(x, y), color)

    # x and y are the leftmost starting point
    def set_horr_seg(self, x, y, color, length, show_on_matrix=True):
        """
        Lights up a horizontal segment of the LED matrix.

        Parameters:
        - x: Starting x-coordinate of the segment.
        - y: y-coordinate of the segment.
        - color: RGB tuple (R, G, B) to set the segment.
        - length: Length of the segment.
        - show_on_matrix: Whether to display immediately or just update buffer.
        """

        # Set pixels in buffer
        for i in range(length):
            x_coordinate = x + i
            if x_coordinate < self.MATRIX_WIDTH and y < self.MATRIX_HEIGHT and x_coordinate >= 0 and y >= 0:
                #self.strip.set_pixel(self.coordinates_to_number(x+i, y),color)
                self.set_pixel_color(x+i,y,color)

        # Display the image
        if show_on_matrix == True:
            self.show()

    def set_vert_seg(self, x, y, color, length, show_on_matrix=True):
        """
        Lights up a vertical segment of the LED matrix.

        Parameters:
        - x: x-coordinate of the segment.
        - y: Starting y-coordinate of the segment.
        - color: RGB tuple (R, G, B) to set the segment.
        - length: Length of the segment.
        - show_on_matrix: Whether to display immediately or just update buffer.
        """

        # Set pixels in buffer
        for i in range(length):
            y_coordinate = y + 1
            if y_coordinate < self.MATRIX_HEIGHT and x < self.MATRIX_WIDTH and y_coordinate >= 0 and x >= 0:
                #self.strip.set_pixel(self.coordinates_to_number(x, y+i),color)
                self.set_pixel_color(x,y+i,color)

        # Display the image
        if show_on_matrix == True:
            self.show()

    def rotate_left(self, num_of_pixels=1):
        """
        Rotate the pixels to the left
        """
        self.np = self.np[num_of_pixels:] + self.np[:num_of_pixels]
        self.show()

    def rotate_right(self, num_of_pixels=1):
        """
        Rotate the pixels to the right
        """
        num_of_pixels = -num_of_pixels
        self.np = self.np[num_of_pixels:] + self.np[:num_of_pixels]
        self.show()

class Matrix_fun(Matrix):
    """
    Subclass of Matrix, includes functiones for displaying images, text, lightshows... etc.
    """
    red = (255, 0, 0)
    orange = (255, 50, 0)
    yellow = (255, 100, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    indigo = (100, 0, 90)
    violet = (200, 0, 100)
    pink = (255,20,147)
    colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

    def __init__(self, width: int, height: int, gpio_pin: int) -> None:
        super().__init__(width, height, gpio_pin)
        # Required in some methodes
        self.run = False
        # Required in the setClock method
        self.minute = 0

    def wait(self, wait_time: float) -> None:
        """ Stops the program for x-amount of time """
        last_display_time = time.time()

        while self.run:
            current_time = time.time()
            elapsed_time = current_time - last_display_time

            if elapsed_time > wait_time:
                return

    def set_num(self, num:int, x:int, y:int, color, size:int=0, show:bool=True):
        """ Shows selected number on LED matrix (only one digit 0-9) """
        if num == 0:
            set_0(self,x, y, color, size, show)
        elif num == 1:
            set_1(self,x, y, color, size, show)
        elif num == 2:
            set_2(self,x, y, color, size, show)
        elif num == 3:
            set_3(self,x, y, color, size, show)
        elif num == 4:
            set_4(self,x, y, color, size, show)
        elif num == 5:
            set_5(self,x, y, color, size, show)
        elif num == 6:
            set_6(self,x, y, color, size, show)
        elif num == 7:
            set_7(self,x, y, color, size, show)
        elif num == 8:
            set_8(self,x, y, color, size, show)
        elif num == 9:
            set_9(self,x, y, color, size, show)
        else:
            print("ERR, first parameter (num) must be between 0-9")
            return "err"

    def set_symbol(self, symbol:str, x:int, y:int, color):
        """ Pushes the selected symbol to the fram buffer, requiers "self.show()" """
        symbol = symbol.lower()

        # If it is a digit
        try:
            number = int(symbol)
            self.set_num(number,x,y,color,show=False)
        except ValueError:
            pass

        if symbol == "a": set_a(self, x,y,color)
        elif symbol == "b": set_b(self,x,y,color)
        elif symbol == "c": set_c(self,x,y,color)
        elif symbol == "d": set_d(self,x,y,color)
        elif symbol == "e": set_e(self,x,y,color)
        elif symbol == "f": set_f(self,x,y,color)
        elif symbol == "g": set_g(self,x,y,color)
        elif symbol == "h": set_h(self,x,y,color)
        elif symbol == "i": set_i(self,x,y,color)
        elif symbol == "j": set_j(self,x,y,color)
        elif symbol == "k": set_k(self,x,y,color)
        elif symbol == "l": set_l(self,x,y,color)
        elif symbol == "m": set_m(self,x,y,color)
        elif symbol == "n": set_n(self,x,y,color)
        elif symbol == "o": set_o(self,x,y,color)
        elif symbol == "p": set_p(self,x,y,color)
        elif symbol == "q": set_q(self,x,y,color)
        elif symbol == "r": set_r(self,x,y,color)
        elif symbol == "s": set_s(self,x,y,color)
        elif symbol == "t": set_t(self,x,y,color)
        elif symbol == "u": set_u(self,x,y,color)
        elif symbol == "v": set_v(self,x,y,color)
        elif symbol == "w": set_w(self,x,y,color)
        elif symbol == "x": set_x(self,x,y,color)
        elif symbol == "y": set_y(self,x,y,color)
        elif symbol == "z": set_z(self,x,y,color)
        elif symbol == ".": set_dot(self,x,y,color)
        elif symbol == ":": set_colon(self,x,y,color)
        elif symbol == "!": set_exclamation_mark(self, x, y, color)
        elif symbol == "?": set_question_mark(self, x, y, color)
        elif symbol == "-": set_hyphen(self,x,y,color)
        else:
            #print("ERR. Does not exist")
            return "ERR, symbol does not exist"

    def show_text(self, text:str, color, y:int, delay:float=0.075, run_times:int=-1):
        """ Shows a scrolling text, run_time = -1 -> infinite """

        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        text = text.lower()
        x = self.MATRIX_WIDTH - 1

        try:
            while self.run == True or run_times > 0:
                x_sep = 0
                self.clear()
                i = 1
                for letter in text:
                    x_sep += 5
                    # Avoid error, if not space
                    if letter != " ":
                        # If it is a number
                        if letter in numbers:
                            self.set_num(int(letter), x+x_sep, y, color, show=False)
                        # If it is not a number
                        else:
                            self.set_symbol(letter, x+x_sep, y, color)
                    # If we have reatched the end
                    if i == len(text) and (x+x_sep == 0):
                        x = 15
                        # If run times is selected
                        if run_times != -1:
                            run_times -= 1
                    i += 1
                self.show()
                time.sleep(delay)
                x -= 1

        except Exception as e:
            print("Thread Exception:", e)

    def setClock_hour(self, color, x:int=0, y:int=5):
        """ Function push hour to frame buffer """
        size = 0
        hour = time.localtime()[3]
        if hour < 10: # If only one digit
            self.set_num(hour, x+3, y, color, size, show=False)
        else:
            hour_1 = hour // 10
            hour_2 = hour % 10
            self.set_num(hour_1, x, y, color, size, show=False)
            self.set_num(hour_2, x+4, y, color, size, show=False)

    def setClock_min(self, color, x:int=0, y:int=5):
        """ Function push minutes to frame buffer """
        size = 0
        minute = time.localtime()[4]
        min_1 = minute // 10
        min_2 = minute % 10

        self.set_num(min_1, x+9, y, color, size, show=False) # The possition might need to change depending on the size of the matrix
        self.set_num(min_2, x+13, y, color, size, show=False)

    def show_clock(self, color, x:int=0, y:int=5): #setClock
        """
        This function displays the current time on the matrix
        It use setClock_hour and setClock_min in adition to adding a dot as seperator
        """

        # First time initialization
        self.minute = time.localtime()[4]
        #self.strip.set_pixel(self.coordinates_to_number(x+7, y),color) # dot
        self.set_pixel_color(x+7,y,(color[0]*0.5,color[0]*0.5,color[0]*0.5)) # dot
        self.setClock_hour(color, x, y)
        self.setClock_min(color, x, y)

        self.show()

        while self.run == True:
            # Make dot blink every second
            if time.localtime()[5] % 2 == 0:
                #self.strip.set_pixel(self.coordinates_to_number(x+7, y),(color[0]*0.5,color[0]*0.5,color[0]*0.5)) # dot
                self.set_pixel_color(x+7,y,(color[0]*0.5,color[0]*0.5,color[0]*0.5)) # dot
                self.show()
            else:
                #self.strip.set_pixel(self.coordinates_to_number(x+7, y),(0,0,0)) # dot
                self.set_pixel_color(x+7,y,(0,0,0)) # dot
                self.show()

            # Checks if the minutes have changed
            if self.minute != time.localtime()[4]:
                self.clear() # Clear display
                self.minute = time.localtime()[4]

                self.setClock_hour(color, x, y)
                self.setClock_min(color, x, y)

                self.show()

    def show_rainbow_effects(self, time_between:float) -> None:
        """ Show different rainbow effects """

        number = 2
        last_display_time = time.time()

        # So we do not need to wait
        rainbow_spiral(self,time_between//2)

        while self.run:

            # Calculate time passed
            current_time = time.time()
            elapsed_time = current_time - last_display_time

            # Display different effects
            if number == 1:
                rainbow_spiral(self,time_between//2)
            elif number == 2:
                rainbow_wave(self,25*time_between)
            elif number == 3:
                randomRGB(self,time_between)
            elif number == 4:
                firework_animation(self)
            elif number == 5:
                balls_bouncing_animation(self,4,time_between)

            # If enoughf time has passed
            if elapsed_time > time_between:

                if number > 5:
                    number = 1
                else:
                    number += 1

                self.clear()
                last_display_time = current_time

    # Internet symbol
    def setFig_wifi(self, color, numer_show:int=4, show=True):
        """" Shows a wifi sybol by the selected color and number of lines """
        # Seperated by the dots
        if numer_show >= 1:
            self.set_horr_seg(7, 0, color, 2, show)
            self.set_horr_seg(7, 1, color, 2, show)

        if numer_show >= 2:
            self.set_horr_seg(5, 2, color, 1, show)
            self.set_horr_seg(10, 2, color, 1, show)
            self.set_horr_seg(5, 3, color, 6, show)
            self.set_horr_seg(6, 4, color, 4, show)

        if numer_show >= 3:
            self.set_vert_seg(4, 5, color, 2, show)
            self.set_vert_seg(5, 6, color, 2, show)
            self.set_horr_seg(5, 7, color, 5, show)
            self.set_horr_seg(6, 8, color, 4, show)
            self.set_vert_seg(11, 5, color, 2, show)
            self.set_vert_seg(10, 6, color, 2, show)

        if numer_show >= 4:
            self.set_vert_seg(0, 8, color, 2, show)
            self.set_vert_seg(1, 9, color, 2, show)
            self.set_vert_seg(2, 10, color, 2, show)

            self.set_horr_seg(3, 11, color, 10, show)
            self.set_horr_seg(3, 12, color, 10, show)

            self.set_vert_seg(15, 8, color, 2, show)
            self.set_vert_seg(14, 9, color, 2, show)
            self.set_vert_seg(13, 10, color, 2, show)

    def show_smileys(self, time_between: float) -> None:
        """
        Display the emojis stored in emoji folder in random order
        """
        self.cycle_images("figures/emojis", time_between, True)

    def get_bitmap_data(self, bitmap_file: str) -> list:
        """ Get PPM P3 file data and return it as a list """

        # Epty list to store the image data
        filedata_list = []

        # Open selected file
        try:
            with open(bitmap_file, "r") as file:
                # Stores file data in a list with lists
                for row in file:
                    row = row.strip().split(" ", 3) # Remove trayling tags and split into sublist
                    filedata_list.append(row)
        except OSError as e:
            print(f"ERR, could not find file: {e}")
            return "ERR, could not find file"

        # Check for correct file format
        if filedata_list[0][0] != "P3":
            print("File format is not suported")
            return None
        else:
            return filedata_list

    def push_image(self, width: int, hight: int, data: list, x: int=0, y: int=0) -> None:
        """
        Push image data to the buffer
        Parametert:
        - x: x-coordiante to bottom leftmost corner
        - y: y-coordinate to bottom leftmost corner
        - width: image width
        - hight: image hight
        - data: list with tuples (r,g,b)
        """

        for i in range(hight): # Columns
            for j in range(width): # Rows
                color = tuple(int(c) for c in data[i * width + j])
                self.set_pixel_color(x + j, y + hight - i -1, color) # Set pixel

    def push_image_reverse_lines(self, width: int, hight: int, data: list, x: int=0, y: int=0) -> None:
        """
        Setting image when pixel data folows the physical layout of the matrix
        Parametert:
        - x: x-coordiante to bottom leftmost corner
        - y: y-coordinate to bottom leftmost corner
        - width: image width
        - hight: image hight
        - data: list with tuples (r,g,b)
        """

        index = 0
        for i in range(self.MATRIX_HEIGHT):
            for j in range(self.MATRIX_WIDTH):

                if i % 2 == 0:
                    self.set_pixel_color(j + x, i + y, data[index])
                # Reverse
                else:
                    self.set_pixel_color(self.MATRIX_WIDTH - j - 1 - x, i + y, data[index])


                index += 1

    def show_bitmap(self, bitmap_file: str, x:int = 0, y:int = 0, filedata:list=[], show:bool = True) -> None:
        """
        Displays a PPM P3 image on the matrix.
        Parameters:
        - bitmap_file: filepath to image
        - x: bottom leftmost corner
        - y: bottom leftmost corner
        - show: show the image immediately, or just add to buffer
        """

        # If data was not given, get data
        if not filedata:
            filedata_list = self.get_bitmap_data(bitmap_file)

            # If there was a problem getting the data
            if filedata_list is None:
                raise ValueError("Error: Unable to load bitmap data.")
        else:
            filedata_list = filedata

        # Get file with and hight
        image_width = int(filedata_list[1][0])
        image_hight = int(filedata_list[1][1])

        # Push data to frame buffer
        self.push_image(image_width, image_hight, filedata_list[3:], x, y)

        # Show image if set to True
        if show:
            self.show() # Show on LED-matrix

    def show_images_ppm(self, folder_path, time_between):
        """ Display images in selected folder, display message on matrix if there are no images """
        images = self.cycle_images(folder_path, time_between)

        # Display text on matrix
        if images is None:
            self.show_text("No images",(255,255,255),5)

    def image_tansition_current_up(self, start_y: int=0) -> None:
        """ Moves the current image up and out """

        # Get image data from buffer
        filedata = self.get_buffer_data()

        # Animation
        for i in range(self.MATRIX_HEIGHT+1):
            self.clear()
            self.push_image_reverse_lines(self.MATRIX_WIDTH, self.MATRIX_HEIGHT, filedata, y = i + start_y)
            self.show()

            # Quicken escape
            if self.run != True:
                break

    def image_transition_up(self, filepath, start_y: int=0) -> None:
        """ Moves the image up"""

        # Get image data
        filedata = self.get_bitmap_data(filepath)

        # Animation
        for i in range(self.MATRIX_HEIGHT+1):
            self.clear()
            self.show_bitmap("", filedata=filedata, y=i + start_y)

            # Quicken escape
            if self.run != True:
                break

    def cycle_images(self, folder_path: str, time_between: float, random_index: bool=False) -> None:
        """ Cycle through images in selected folder """

        # Get filenames
        files = get_files(folder_path, "ppm")

        # If no files where found
        if not files:
            return None

        # Display first image
        index = 0
        show = f"{folder_path}/{files[index]}"
        self.show_bitmap(show)

        last_display_time = time.time()

        # Cycle through the images
        while self.run:
            current_time = time.time()
            elapsed_time = current_time - last_display_time

            # Avoid error
            if elapsed_time < 0:
                last_display_time = current_time - time_between

            # If the spessified time has passed
            if elapsed_time > time_between:
                # Random index
                if random_index:
                    index =  random.randint(0, len(files)-1)
                # Sequential index
                else:
                    if index < len(files)-1:
                        index += 1
                    else:
                        index = 0

                # Move image out
                self.image_transition_up(show)

                # Move new image in
                show = f"{folder_path}/{files[index]}"
                self.image_transition_up(show, start_y=-self.MATRIX_HEIGHT)

                # Clear buffer to save memory
                self.clear()

                last_display_time = current_time

    def show_date(self, show:bool=False):
        self.show_bitmap("figures/calendar_template.ppm", show=False)
        day = time.localtime()[2]

        if day < 10:
            self.set_num(day,6,2,(0,0,0),size=1,show=False)
        else:
            num1 = day // 10
            num2 = day % 10
            self.set_num(num1,4,3,(0,0,0),show=False)
            self.set_num(num2,9,3,(0,0,0),show=False)
        if show:
            self.show()

    def show_weather_icon(self, show:bool=False):
        """ Displays a weather icon, corresponding to the weather data stored in "weather.py" """

        symbol_code = wd.weather_data["symbol_code_id"]

        # Define icon code and corresponding icon
        # Icons: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
        icons = {
            "01d": "sun.ppm",
            "02d": "sun_and_cloudy.ppm",
            "03d": "cloud.ppm",
            "04d": "broken_clouds.ppm",
            "09d": "rain.ppm",
            "10d": "sun_and_rain.ppm",
            "11d": "thunder.ppm",
            "13d": "snow.ppm",
            "50d": "foggy.ppm",
            "-00": "sun_red.ppm",

            "01n": "sun.ppm",
            "02n": "sun_and_cloudy.ppm",
            "03n": "cloud.ppm",
            "04n": "broken_clouds.ppm",
            "09n": "rain.ppm",
            "10n": "sun_and_rain.ppm",
            "11n": "thunder.ppm",
            "13n": "snow.ppm",
            "50n": "foggy.ppm"
        }

        # Display image
        if symbol_code in icons.keys():
            self.show_bitmap(f"/figures/weather_icons/{icons[symbol_code]}", show=show)
        else:
            self.show_bitmap(f"/figures/exclamation_mark.ppm", show=show)
            print("Error, icon does not exist!")

    def show_temp(self, show:bool=False):
        """
        Display the temperature on matrix

        Not good for numbers with more than 2 digits
        """

        # Extract temperature
        temp = wd.weather_data["temp"]
        temp_str = str(int(round(temp,0)))

        # Display thermostat image
        if int(temp) > 0:
            self.show_bitmap(f"/figures/thermostat.ppm", show=False)
        else:
            self.show_bitmap(f"/figures/thermostat_cold.ppm", show=False)

        start_x = 8-len(temp_str) # Calculate offset

        iteration = 0
        # Set the numbers
        for digit in temp_str:
            x_pos = start_x+4*iteration
            self.set_symbol(digit,x_pos,5,(255,255,255))
            iteration += 1

        # Degree icon
        self.set_pixel_color(x_pos+4, 11, (255,255,255))

        # Display image
        if show:
            self.show()

    def show_info(self, time_between:float=10):
        """ Circles through different information on the Matrix """
        last_display_time = time.time()

        # So we do not need to wait
        self.show_weather_icon(True)

        number = 2
        while self.run:
            current_time = time.time()
            elapsed_time = current_time - last_display_time

            # Reset counter
            if number > 4:
                number = 1

            # Avoid error
            if elapsed_time < 0:
                last_display_time = current_time - time_between

            # If the spessified time has gone
            if elapsed_time > time_between:
                self.image_tansition_current_up()
                self.clear()
                if number == 1:
                    self.show_weather_icon()
                elif number == 2:
                    self.show_temp()
                elif number == 3:
                    self.show_date()
                else:
                    #self.strip.set_pixel(self.coordinates_to_number(7, 5),(100,100,100)) # dot
                    self.set_pixel_color(7,5,(100,100,100)) # dot
                    self.setClock_hour((255,255,255))
                    self.setClock_min((255,255,255))

                self.image_tansition_current_up(start_y=-self.MATRIX_HEIGHT) # Move image in

                number += 1
                last_display_time = current_time
            time.sleep_ms(1) # Avoid error

    def show_loading_bar(self, number:int,color,speed:float=0.3,animation:bool=False):
        """ Shows a loading bar. Number must be between 0 and 16 """
        if number > self.MATRIX_WIDTH:
            number = self.MATRIX_WIDTH
        y = self.MATRIX_HEIGHT//2
        if animation:
            for i in range(number):
                #self.strip.set_pixel(self.coordinates_to_number(i, y),color)
                #self.strip.set_pixel(self.coordinates_to_number(i, y-1),color)
                self.set_pixel_color(i,y,color)
                self.set_pixel_color(i,y-1,color)
                self.show()
                time.sleep(speed)
        else:
            self.set_horr_seg(0,y,color,number,show_on_matrix=False)
            self.set_horr_seg(0,y-1,color,number,show_on_matrix=False)
            self.show()