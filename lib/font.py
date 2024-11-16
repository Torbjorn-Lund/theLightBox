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


### For displaying numbers
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