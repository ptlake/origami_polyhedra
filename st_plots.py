import math

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

style = "Simple, tail_width=0.5, head_width=6, head_length=8"
kw = dict(arrowstyle=style)

def intersect(x1,y1,x2,y2,x3,y3,x4,y4):
    """ Returns the intersect of the lines going through (x1, y1), (x2, y2) and (x3, y3), (x4, y4)
    """
    return ((x2 - x1) * (x3 * y4 - x4 * y3) - (x4 - x3) * (x1 * y2 - x2 * y1)) / ((x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1)), ((y2 - y1) * (x3 * y4 - x4 * y3) - (y4 - y3) * (x1 * y2 - x2 * y1)) / ((x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))

def draw_page(yscale, y0, x0, night_mode):
    if night_mode:
        plt.style.use('dark_background')
        lc = "white"
    else:
        plt.style.use('default')
        lc = "black"
    iy = int(4 * yscale)
    fig, ax = plt.subplots(figsize=(4 * x0, 2 * y0))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom page
    ax.plot([0, 7 * x0],[0, 0], linewidth=1, color=lc)
    if iy != 16:
        ax.plot([8 * x0, 7 * x0],[yscale * y0, yscale * y0], linewidth=1, color=lc)
    #frame right page
    ax.plot([8 * x0, 8 * x0],[4 * y0, yscale * y0], linewidth=1, color=lc)
    ax.plot([7 * x0, 7 * x0],[0, yscale * y0], linewidth=1, color=lc)
    #frame top page
    ax.plot([0, 7 * x0],[4 * y0, 4 * y0], linewidth=1, color=lc)
    if iy != 16:
        ax.plot([8 * x0, 7 * x0],[4 * y0, 4 * y0], linewidth=1, color=lc)
    #frame left page
    ax.plot([0, 0],[0, 4 * y0], linewidth=1, color=lc)
    #frame left unit
    ax.plot([7.15 * x0, 7.15 * x0],[-0.1 * y0, (yscale - 0.1) * y0], linewidth=1, color=lc)
    #frame top unit
    ax.plot([7.15 * x0, 8.15 * x0],[(yscale - 0.1) * y0, (yscale - 0.1) * y0], linewidth=1, color=lc)
    #frame right unit
    ax.plot([8.15 * x0, 8.15 * x0],[-0.1 * y0, (yscale - 0.1) * y0], linewidth=1, color=lc)
    #frame bottom unit
    ax.plot([7.15 * x0, 8.15 * x0],[-0.1 * y0, -0.1 * y0], linewidth=1, color=lc)
    #vertical divisions
    for i in range(1,8):
        ax.plot([i * x0, i * x0],[0, 4 * y0], linewidth=0.5, color=lc)
    #horizontal divisions:
    ax.plot([0, 7 * x0],[yscale * y0, yscale * y0], linewidth=0.5, color=lc)
    for i in range(2, 15 // iy + 1):
        ax.plot([0, 8 * x0],[i * yscale * y0, i * yscale * y0], linewidth=0.5, color=lc)
    #ref marks
    t = []
    jy = iy
    while jy <= 16:
        if jy != 16:
            t.append(jy)
        jy *= 2
    jy -= 16
    while jy != 16:
        t.append(jy)
        ax.plot([0, 0.15 * x0],[jy / 4 * y0, jy / 4 * y0], linewidth=0.5, color=lc)
        if jy > iy:
            ax.plot([8 * x0, 7.85 * x0],[jy / 4 * y0, jy / 4 * y0], linewidth=0.5, color=lc)
        else:
            ax.plot([8.15 * x0, 8 * x0],[(jy / 4 - 0.1) * y0, (jy / 4 - 0.1) * y0], linewidth=0.5, color=lc)
        jy *= 2
        if jy > 16:
            jy -=16
    for i,jy in enumerate(reversed(t)):
        ax.text(-0.25 * x0, (jy / 4 - 0.05) * y0, f'{i + 1}',{'size':6})
    st.pyplot(fig)
    
def draw_initial(yscale, y0, x0, night_mode):
    if night_mode:
        plt.style.use('dark_background')
        lc = "white"
    else:
        plt.style.use('default')
        lc = "black"

    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom page
    ax.plot([0, x0],[0, 0], linewidth=1, color=lc)
    #frame right page
    ax.plot([x0, x0],[0, yscale * y0], linewidth=1, color=lc)
    #frame top page
    ax.plot([0, x0],[yscale * y0, yscale * y0], linewidth=1, color=lc)
    #frame left page
    ax.plot([0, 0],[0, yscale * y0], linewidth=1, color=lc)
    #vertical divisions
    for i in range(1,4):
        ax.plot([i * x0 / 4, i * x0 / 4],[0, yscale * y0], linewidth=1.5, color=lc, linestyle="dashed")
    st.pyplot(fig)
    
def draw_guide1(yscale, y0, x0, yoffset, night_mode):
    if night_mode:
        plt.style.use('dark_background')
        lc = "white"
    else:
        plt.style.use('default')
        lc = "black"

    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom page
    ax.plot([0, x0],[0, 0], linewidth=1, color=lc)
    #frame right page
    ax.plot([x0, x0],[0, yscale * y0], linewidth=1, color=lc)
    #frame top page
    ax.plot([0, x0],[yscale * y0, yscale * y0], linewidth=1, color=lc)
    #frame left page
    ax.plot([0, 0],[0, yscale * y0], linewidth=1, color=lc)
    #vertical divisions
    for i in range(1,4):
        ax.plot([i * x0 / 4, i * x0 / 4],[0, yscale * y0], linewidth=0.5, color=lc)
    #crease line
    ix0 = yoffset[0]
    ix1 = yoffset[1]
    ix2 = yoffset[2]
    ix3 = max((min(((2 + ix2), 4)), ix1))
    if ix3 - ix0 > 4:
        ix3 = 4 + ix0
    phi = 0.5 * math.acos(ix0 / ix1)
    x1 = ix3 * 0.25 * x0
    y1 = x1 * math.tan(phi)
    #crease location
    dx = 0.1 * x0 * math.cos(phi)
    if ix3 - ix2 != 0:
        x1a = (ix3 - ix2) * 0.25 * x0 - dx
    else:
        x1a = 0
    y1a = y1 - y1 / x1 * x1a
    x1b = (ix3 - ix2) * 0.25 * x0 + dx
    y1b = y1 - y1 / x1 * x1b
    ax.plot([x1a, x1b],[y1a, y1b], linewidth=1.5, color=lc, linestyle="dashed")
    ax.plot([0,x1a],[y1, y1a], linewidth=0.5, color=lc)
    ax.plot([x1b,x1],[y1b, 0], linewidth=0.5, color=lc)
    if ix0:
        ixa = ix3 - ix1
        ixb = ix3 - ix0
        yb = ix1 * 0.25 * x0 * math.sin(2 * phi)
    else:
        ixa = 0
        ixb = ix3
        yb = ix3 * 0.25 * x0
    a = patches.FancyArrowPatch((ixa * 0.25 * x0, 0), (ixb * 0.25 * x0,  yb), shrinkA=10, shrinkB=10, connectionstyle="arc3,rad=-.3", color=lc, **kw)
    a1 = patches.FancyArrowPatch((ixb * 0.25 * x0,  yb), (ixa * 0.25 * x0, 0), shrinkA=10, shrinkB=10, connectionstyle="arc3,rad=.3", color=lc, **kw)
    plt.gca().add_patch(a)
    plt.gca().add_patch(a1)
    ax.scatter([ix3 * 0.25 * x0, ixa * 0.25 * x0, ixb * 0.25 * x0],[0, 0, yb], color=lc, s=30)        
    st.pyplot(fig)
    # where the crease is
    if (ix3 - ix2) == 0:
        s1 = "left side"
    elif (ix3 - ix2) == 1:
        s1 = "$1/4$ line"
    elif (ix3 - ix2) == 2:
        s1 = "centerline"
    elif (ix3 - ix2) == 3:
        s1 = "$3/4$ line"
    # the point being used
    if ixa == 0:
        s2 = "left corner"
    elif ixa == 1:
        s2 = "point on the $1/4$ line"
    elif ixa == 2:
        s2 = "point on the centerline"
    elif ixa == 3:
        s2 = "point on the $3/4$ line"
    # to be folded to the line
    s3 = "oops"
    if ixb == 1:
        s3 = "$1/4$ line"
    elif ixb == 2:
        s3 = "centerline"
    elif ixb == 3:
        s3 = "$3/4$ line"
    elif ixb == 4:
        s3 = "right side"
    # meeting at the bottom
    if ix3 == 0:
        s4 = "left corner"
    elif ix3 == 1:
        s4 = "point on the $1/4$ line"
    elif ix3 == 2:
        s4 = "point on the centerline"
    elif ix3 == 3:
        s4 = "point on the $3/4$ line"
    elif ix3 == 4:
        s4 = "right corner"
    direction = f"Make a small crease around the {s1} along the line formed by bringing the bottom {s2} to the {s3} and meeting at the bottom of {s4}."
    return ((x1a, x1b), (y1a, y1b)), direction
    
def draw_guide2(yscale, y0, x0, y1, crease, night_mode):
    if night_mode:
        plt.style.use('dark_background')
        lc = "white"
    else:
        plt.style.use('default')
        lc = "black"

    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom page
    ax.plot([0, x0],[0, 0], linewidth=1, color=lc)
    #frame right page
    ax.plot([x0, x0],[0, yscale * y0], linewidth=1, color=lc)
    #frame top page
    ax.plot([0, x0],[yscale * y0, yscale * y0], linewidth=1, color=lc)
    #frame left page
    ax.plot([0, 0],[0, yscale * y0], linewidth=1, color=lc)
    #vertical divisions
    for i in range(1,4):
        ax.plot([i * x0 / 4, i * x0 / 4],[0, yscale * y0], linewidth=0.5, color=lc)
    #crease line
    ax.plot(crease[0],crease[1], linewidth=0.5, color=lc)
    a = patches.FancyArrowPatch((x0 / 8, 0), (x0 / 8,  2 * y1), shrinkA=0, shrinkB=0, connectionstyle="arc3,rad=-.3", color=lc, **kw)
    a1 = patches.FancyArrowPatch((x0 / 8,  2 * y1), (x0 / 8, 0),shrinkA=0, shrinkB=0, connectionstyle="arc3,rad=.3", color=lc, **kw)
    plt.gca().add_patch(a)
    plt.gca().add_patch(a1)
        
    ax.plot([0, x0],[y1, y1], linewidth=1.5, color=lc, linestyle="dashed")
    st.pyplot(fig)    


def draw_angle1(yscale, angle, y1, y0, x0, crease, guide_bool, night_mode):
    if night_mode:
        plt.style.use('dark_background')
        lc = "white"
    else:
        plt.style.use('default')
        lc = "black"

    y0p = y0 * yscale
    
    phi = 0.5 * math.pi - 0.5 * angle * math.pi / 180.
    y2 = y1 + 0.5 * x0 * math.tan(phi)
    x2 = 0.5 * x0 + y1 / math.tan(phi)
    x3 = x2 * (1. - math.cos(2. * phi))
    y3 = x2 * math.sin(2. * phi)

    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom
    ax.plot([0, x0],[0,0], linewidth=1, color=lc)
    #frame right
    ax.plot([x0, x0],[0, y0p], linewidth=1, color=lc)
    #frame top
    ax.plot([x0, 0],[y0p, y0p], linewidth=1, color=lc)
    #frame left
    ax.plot([0, 0],[y0p, 0], linewidth=1, color=lc)

    #fold
    ax.plot([x2, 0],[0, y2], linewidth=1.5, color=lc, linestyle="dashed")

    if guide_bool:
        # horizontal
        ax.plot([0, x0],[y1, y1], linewidth=0.5, color=lc)
        # crease
        ax.plot(crease[0], crease[1], linewidth=0.5, color=lc)
    
    # 1/4 line vertical
    for i in range(1, 4):
        ax.plot([i * 0.25 * x0, i * 0.25 * x0],[0, y0p], linewidth=0.5, color=lc)
        

    st.pyplot(fig)

def draw_angle2(yscale, angle, y1, y0, x0, guide_bool, night_mode):
    if night_mode:
        plt.style.use('dark_background')
        lc = "white"
    else:
        plt.style.use('default')
        lc = "black"

    y0p = y0 * yscale
    
    phi = 0.5 * math.pi - 0.5 * angle * math.pi / 180.
    y2 = y1 + 0.5 * x0 * math.tan(phi)
    x2 = 0.5 * x0 + y1 / math.tan(phi)
    x3 = x2 * (1. - math.cos(2. * phi))
    y3 = x2 * math.sin(2. * phi)

    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom
    ax.plot([x2, x0],[0,0], linewidth=1, color=lc)
    #frame right
    ax.plot([x0, x0],[0, y0p], linewidth=1, color=lc)
    #frame top
    ax.plot([x0, 0],[y0p, y0p], linewidth=1, color=lc)
    #frame left
    ax.plot([0, 0],[y0p, y2], linewidth=1, color=lc)

    #bottom corner
    ax.plot([0, x3, x2, 0],[y2, y3, 0, y2], linewidth=1, color=lc)

    # horizontal bottom
    if guide_bool:
        ax.plot([x2 + y1 * (x3 - x2) / y3, x0],[y1, y1], linewidth=0.5, color=lc)
        ax.plot([0.5 * x0, x3* (y2 - y1) / y2],[y1, y2 + (y3 - y2) * (y2 - y1) / y2], linewidth=0.5, color=lc)

    # 1/4 line diag bottom
    ax.plot([0.25 * x0, x2 + (x3 - x2) * (x2 - 0.25 * x0) / x2],[y2 * (x2 - 0.25 * x0) / x2, y3 * (x2 - 0.25 * x0) / x2], linewidth=1.5, color=lc, linestyle="dashed")
    # 1/4 line vertical
    if x3 > 0.25 * x0:
        ymin = y2 - 0.25 * x0 / x3 * (y2 - y3)
    else:
        ymin = y3 - (x3 - 0.25 * x0) / (x3 - x2) * y3
    ax.plot([0.25 * x0, 0.25 * x0],[ymin, y0p], linewidth=1.5, color=lc, linestyle="dashed")
    ax.plot([0.25 * x0, x3* (y2 - y1) / y2],[y2 * (x2 - 0.25 * x0) / x2, y2 + (y3 - y2) * (y2 - y1) / y2], linewidth=1.5, color=lc, linestyle="dashdot")
        
    # 1/2 line diag bottom
    ax.plot([0.50 * x0, x2 + (x3 - x2) * (x2 - 0.50 * x0) / x2],[y2 * (x2 - 0.50 * x0) / x2, y3 * (x2 - 0.50 * x0) / x2], linewidth=0.5, color=lc)
    # 1/2 line
    if x3 < 0.5 * x0:
        ymin = y3 - (x3 - 0.5 * x0) / (x3 - x2) * y3
    else:
        ymin = y2 - 0.50 * x0 / x3 * (y2 - y3)
    ax.plot([0.50 * x0, 0.50 * x0],[ymin, y0p], linewidth=0.5, color=lc)
    # 3/4 line vertical
    if x3 > 0.75 * x0:
        ymin = y2 - 0.75 * x0 / x3 * (y2 - y3)
    elif x2 > 0.75 * x0:
        ymin = y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3
    else:
        ymin = 0
    ax.plot([0.75 * x0, 0.75 * x0], [ymin, y0p], linewidth=0.5, color=lc)
    if x3 > 0.75 * x0 and x2 < 0.75 * x0:
        ax.plot([0.75 * x0, 0.75 * x0], [0, y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3], linewidth=0.5, color=lc)

    a = patches.FancyArrowPatch((x3, y3), (x2 + (x3 - x2) * (x2 - 0.5 * x0) / x2, y3 * (x2 - 0.5 * x0) / x2), shrinkA=5, shrinkB=5, connectionstyle="arc3,rad=-.3", color=lc, **kw)
    plt.gca().add_patch(a)

    st.pyplot(fig)


def draw_angle3(yscale, angle, y1, y0, x0, guide_bool, night_mode, second_bool):
    if night_mode:
        plt.style.use('dark_background')
        lc = "white"
        lcp = "black"
    else:
        plt.style.use('default')
        lc = "black"
        lcp = "white"

    y0p = y0 * yscale
    
    phi = 0.5 * math.pi - 0.5 * angle * math.pi / 180.
    y2 = y1 + 0.5 * x0 * math.tan(phi)
    x2 = 0.5 * x0 + y1 / math.tan(phi)
    y2 *= (x2 - 0.25 * x0) / x2
    x3 = x2 - (x2 - 0.25 * x0) * math.cos(2 * phi)
    y3 = (x2 - 0.25 * x0) * math.sin(2 * phi)
    x4 = x2 + (x3 - x2) * (x2 - 0.5 * x0) / (x2 - 0.25 * x0)
    y4 = y3 * (x2 - 0.50 * x0) / (x2 - 0.25 * x0)

    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom
    ax.plot([x2, x0],[0,0], linewidth=1, color=lc)
    #frame right
    ax.plot([x0, x0],[0, y0p], linewidth=1, color=lc)
    #frame top
    ax.plot([x0, 0.25 * x0],[y0p, y0p], linewidth=1, color=lc)
    #frame left
    ax.plot([0.25 * x0, 0.25 * x0],[y0p, y2], linewidth=1, color=lc)

    if y1 > 0.001:
        dx = 0.03 * x0 * math.cos(1.75 * math.pi - 2 * phi)
        dy = 0.03 * x0 * math.sin(1.75 * math.pi - 2 * phi)
        dxp = -0.02 * x0
        xa, ya = intersect(
            0.5 * x0 + dxp,       0,
            0.5 * x0 + dxp,     y0p,
            x4 + dx, y4 + dy,
            0.5 * x0 + dx, y1 + dy)
        dyp = ya - y1
    else:
        dx = -0.02 * x0
        dy = 0
        dxp = -0.02 * x0
        dyp = 0
    #top layer
    ax.plot(
        [x0 / 4, x0 / 2 + dxp, x0 / 2 + dxp, 0.25 * x0],
        [   y0p,    y0p + dxp,     y1 + dyp,        y2],
        linewidth=1, color=lc)
    #second layer
    if x3 > 0.5 * x0 + dxp:
        ax.plot(
            [x0 / 2 + dxp, x4 + dx, x3],
            [    y1 + dyp, y4 + dy, y3],
            linewidth=1, color=lc)
    else:
        x3pp, y3pp = intersect(
            x3, y3,
            x4 + dx,  y4 + dy,
            0.5 * x0 + dxp, 0,
            0.5 * x0 + dxp, y0p)
        ax.plot(
            [x0 / 2 + dxp, x4 + dx, x3pp],
            [    y1 + dyp, y4 + dy, y3pp],
            linewidth=1, color=lc)
        
    #third layer
    if y1 > 0.001:
        x5, y5 = intersect(
            0.25 * x0,       y2,
            x2,        0,
            x0 / 2 + dxp, y1 + dyp,
            x4 + dx,  y4 + dy)
    else:
        x5, y5 = intersect(
                 0.25 * x0, y2,
                        x2,  0,
                        x3, y3,
            0.5 * x0 + dxp, y1)        
    if x3 > 0.5 * x0 + dxp:
        ax.plot(
            [                                       0.5 * x0 + dxp, x3, x2, x5],
            [y2 + (0.25 * x0 + dxp) / (x3 - 0.25 * x0) * (y3 - y2), y3,  0, y5],
            linewidth=1, color=lc)
    else:
        x3p, y3p = intersect(
            x3, y3,
            x2,  0,
            0.5 * x0 + dxp, 0,
            0.5 * x0 + dxp, y0p)
        ax.plot(
            [ x3p, x2, x5],
            [ y3p,  0, y5],
            linewidth=1, color=lc)
    
    # horizontal
    if guide_bool:
        if y3 > y1:
            xmax = x2 + y1 * (x3 - x2) / y3
        else:
            xmax = 0.25 * x0 + (x3 - 0.25 * x0) * (y2 - y1) / (y2 - y3)            
        ax.plot([xmax, x0],[y1, y1], linewidth=0.5, color=lc)
        if 0.25 * x0 + (x3 - 0.25 * x0) * (y2 - y1) / y2 > 0.5 * x0 + dxp:
            ax.plot([0.5 * x0 + dxp, 0.25 * x0 + (x3 - 0.25 * x0) * (y2 - y1) / y2],[y1 + dyp, y2 + (y3 - y2) * (y2 - y1) / y2], linewidth=0.5, color=lc)
    # 1/2 line diag
    if y1 > 0.001:
        x6, y6 = intersect(
            0.50 * x0,      y1,
            x4,      y4,
            x3,      y3,
            x4 + dx, y4 + dy)
        ax.plot([x6, x4],[y6, y4], linewidth=0.5, color=lc)
    # 1/2 line
    if x3 < 0.5 * x0:
        ymin = y3 - (x3 - 0.5 * x0) / (x3 - x2) * y3
    else:
        ymin = y2 + 0.25 * x0 / (x3 - 0.25 * x0) * (y3 - y2)
    ax.plot([0.50 * x0, 0.50 * x0],[ymin, y0p], linewidth=0.5, color=lc)
    # 3/4 line vertical
    if x3 > 0.75 * x0:
        ymin = y2 + 0.5 * x0 / (x3 - 0.25 * x0) * (y3 - y2)
    elif x2 > 0.75 * x0:
        ymin = y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3
    else:
        ymin = 0
    if second_bool:
        ax.plot(
            [0.75 * x0, 0.75 * x0],
            [        0,       y0p],
            linewidth=1.5, color=lc, linestyle="dashed")
    else:
        ax.plot([0.75 * x0, 0.75 * x0], [ymin, y0p], linewidth=0.5, color=lc)
        if x3 > 0.75 * x0 and x2 < 0.75 * x0:
            ax.plot([0.75 * x0, 0.75 * x0], [0, y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3], linewidth=0.5, color=lc)
    if second_bool:
        a = patches.FancyArrowPatch(
            (    x0, 0.75 * y0p),
            (x0 / 2, 0.75 * y0p),
            shrinkA=10, shrinkB=10, connectionstyle="arc3,rad=.3", color=lc, **kw)
        plt.gca().add_patch(a)
    else:
        a = patches.FancyArrowPatch(
            (x0 / 2, 0.75 * y0p),
            (     0, 0.75 * y0p),
            shrinkA=10, shrinkB=10, connectionstyle="arc3,rad=.3", color=lc, **kw)
        plt.gca().add_patch(a)
        b = patches.FancyArrowPatch(
            (x0 / 8   + 0.08 * x0 * math.sin(1099/1100 * 2 * math.pi), 0.9 * y0p + 0.08 * x0 * math.cos(1099/1100 * 2 * math.pi)),
            (x0 / 8   + 0.08 * x0 * math.sin(1100/1100 * 2 * math.pi), 0.9 * y0p + 0.08 * x0 * math.cos(1100/1100 * 2 * math.pi)),
            shrinkA=10, shrinkB=10, connectionstyle="arc3,rad=.3", color=lc, **kw)
        plt.gca().add_patch(b)
        ax.plot(
            [ x0 / 8   + 0.08 * x0 * math.sin(i/1100 * 2 * math.pi) for i in range(100,1000)],
            [0.9 * y0p + 0.08 * x0 * math.cos(i/1100 * 2 * math.pi) for i in range(100,1000)],
            color=lc
        )
    ax.scatter([0],[0], color=lcp)

    st.pyplot(fig)

def draw_final(yscale, angle, y1, anglep, y1p, y0, x0, guide_bool, guide_boolp, night_mode):
    if night_mode:
        plt.style.use('dark_background')
        lc = "white"
        lcp = "black"
    else:
        plt.style.use('default')
        lc = "black"
        lcp = "white"

    y0p = y0 * yscale
    
    phi = 0.5 * math.pi - 0.5 * angle * math.pi / 180.
    y2 = y1 + 0.5 * x0 * math.tan(phi)
    x2 = 0.5 * x0 + y1 / math.tan(phi)
    y2 *= (x2 - 0.25 * x0) / x2
    x3 = x2 - (x2 - 0.25 * x0) * math.cos(2 * phi)
    y3 = (x2 - 0.25 * x0) * math.sin(2 * phi)
    x4 = x2 + (x3 - x2) * (x2 - 0.5 * x0) / (x2 - 0.25 * x0)
    y4 = y3 * (x2 - 0.50 * x0) / (x2 - 0.25 * x0)

    phip = 0.5 * math.pi - 0.5 * anglep * math.pi / 180.
    y2p = y1p + 0.5 * x0 * math.tan(phip)
    x2p = 0.5 * x0 + y1p / math.tan(phip)
    y2p *= (x2p - 0.25 * x0) / x2p
    x3p = x2p - (x2p - 0.25 * x0) * math.cos(2 * phip)
    y3p = (x2p - 0.25 * x0) * math.sin(2 * phip)
    x4p = x2p + (x3p - x2p) * (x2p - 0.5 * x0) / (x2p - 0.25 * x0)
    y4p = y3p * (x2p - 0.50 * x0) / (x2p - 0.25 * x0)

    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #pins figure size
    ax.scatter([0],[0], color=lcp)
    ax.scatter([x0],[y0p], color=lcp)
    # bottom layer
    x_poly = []
    y_poly = []
    x_poly.append(0.25 * x0)
    y_poly.append(y2p)
    if x2p > 0.75 * x0:
        x_poly.append(0.75 * x0)
        y_poly.append(y2p * (x2p - 0.75 * x0) / (x2p - 0.25 * x0))
    else:
        x_poly.extend([x2p, 0.75 * x0])
        y_poly.extend([0,0])
    x_poly.append(0.75 * x0)
    y_poly.append(y0p - y2)
    if x2 > 0.75 * x0:
        x_poly.append(0.25 * x0)
        y_poly.append(y0p - y2 * (x2 - 0.75 * x0) / (x2 - 0.25 * x0))
    else:
        x_poly.extend([x0 - x2, 0.25 * x0])
        y_poly.extend([y0p,y0p])
    ax.fill(x_poly, y_poly, facecolor=lcp, edgecolor=lc, zorder=0)
    ax.plot(
        [0.5 * x0, 0.5 * x0],
        [y1p, y0p - y1],
        linewidth=0.5, color=lc, zorder=1)
    if guide_boolp:
        ax.plot(
            [0.5 * x0, 0.75 * x0],
            [y1p, y1p],
            linewidth=0.5, color=lc, zorder=1)
    if guide_bool:
        ax.plot(
            [0.5 * x0, 0.25 * x0],
            [y0p - y1, y0p - y1],
            linewidth=0.5, color=lc, zorder=1)
    # second layer bottom
    x_poly = [0.25 * x0]
    y_poly = [y2p]
    if x3p > 0.75 * x0 and x2p > 0.75 * x0:
        x_poly.extend([0.75 * x0, 0.75 * x0])
        y_poly.extend([y2p - y2p * 0.5 * x0 / (x2p - 0.25 * x0), y2p - 0.5 * x0 * (y2p - y3p) / (x3p - 0.25 * x0)])
    elif x3p > 0.75 * x0:
        x_poly.extend([0.75 * x0, 0.75 * x0 , x2p])
        y_poly.extend([y2p + (y2p - y3p) * 0.5 * x0 / (0.25 * x0 - x3p), y3p * (x2p - 0.75 * x0) / (x2p - x3p), 0])
    elif x2p > 0.75 * x0:
        x_poly.extend([0.75 * x0, 0.75 * x0, x3p])
        y_poly.extend([y2p - 0.5 * x0 * y2p / (x2p - 0.25 * x0), y3p - y3p * (x3p - 0.75 * x0) / (x3p - x2p), y3p])
    else:
        x_poly.extend([x3p, x2p])
        y_poly.extend([y3p, 0])
    ax.fill(x_poly, y_poly, facecolor=lcp, edgecolor=lc, zorder=2)
    if x4p < 0.75 * x0:
        ax.plot([0.5 * x0, x4p],
                [y1p, y4p],
                linewidth=0.5, color=lc, zorder=3)
    else:
        ax.plot([0.5 * x0, 0.75 * x0],
                [y1p, y1p + (y4p - y1p) * (0.25 * x0) / (x4p - 0.5 * x0)],
                linewidth=0.5, color=lc, zorder=3)
    #second layer top
    x_poly = [0.75 * x0]
    y_poly = [y0p - y2]
    if x3 > 0.75 * x0 and x2 > 0.75 * x0:
        x_poly.extend([0.25 * x0, 0.25 * x0])
        y_poly.extend([y0p - y2 + y2 * 0.5 * x0 / (x2 - 0.25 * x0), y0p - y2 + 0.5 * x0 * (y2 - y3) / (x3 - 0.25 * x0)])
    elif x3 > 0.75 * x0:
        x_poly.extend([0.25 * x0, 0.25 * x0 , x0 - x2])
        y_poly.extend([y0p - y2 - (y2 - y3) * 0.5 * x0 / (0.25 * x0 - x3), y0p - y3 * (x2 - 0.75 * x0) / (x2 - x3), y0p])
    elif x2 > 0.75 * x0:
        x_poly.extend([0.25 * x0, 0.25 * x0, x0 - x3])
        y_poly.extend([y0p - y2 + 0.5 * x0 * y2 / (x2 - 0.25 * x0), y0p - y3 + y3 * (x3 - 0.75 * x0) / (x3 - x2), y0p - y3])
    else:
        x_poly.extend([x0 - x3, x0 - x2])
        y_poly.extend([y0p - y3, y0p])
    ax.fill(x_poly, y_poly, facecolor=lcp, edgecolor=lc, zorder=2)
    if x4 < 0.75 * x0:
        ax.plot([0.5 * x0, x0 - x4],
                [y0p - y1, y0p - y4],
                linewidth=0.5, color=lc, zorder=3)
    else:
        ax.plot([0.5 * x0, 0.25 * x0],
                [y0p - y1, y0p - y1 - (y4 - y1) * (0.25 * x0) / (x4 - 0.5 * x0)],
                linewidth=0.5, color=lc, zorder=3)
        
    """
    x_poly = [0.75 * x0, x0 - x2]
    y_poly = [y0p - y2, y0p]
    if x3 > 0.75 * x0 and x2 > 0.75 * x0:
        print()
    elif x3 > 0.75 * x0:
        x_poly.extend([0.25 * x0, 0.25 * x0])
        y_poly.extend([y0p - y3 * (x2 - 0.75 * x0) / (x2 - x3), y0p - y2 - (y2 - y3) * 0.5 * x0 / (0.25 * x0 - x3)])
    elif x2 > 0.75 * x0:
        pass
    else:
        x_poly.append(x0 - x3)
        y_poly.append(y0p - y3)
    ax.fill(x_poly, y_poly, facecolor=lcp, edgecolor=lc, zorder=2)
    """
    """
    #frame bottom
    if y1 < 0.001:
        ax.plot([x2, 0.5 * x0 + 0.02 * x0],[0,0], linewidth=1, color=lc)
    #frame right
    ax.plot([0.75 * x0, 0.75 * x0],[y0p - y2, 0], linewidth=1, color=lc)
    #frame top
    ax.plot([x0 - x2, 0.25 * x0],[y0p, y0p], linewidth=1, color=lc)
    #frame left
    ax.plot([0.25 * x0, 0.25 * x0],[y0p, y2], linewidth=1, color=lc)

    if y1 > 0.001:
        dx = 0.03 * x0 * math.cos(1.75 * math.pi - 2 * phi)
        dy = 0.03 * x0 * math.sin(1.75 * math.pi - 2 * phi)
        dxp = -0.02 * x0
        xa, ya = intersect(
            0.5 * x0 + dxp,       0,
            0.5 * x0 + dxp,     y0p,
            x4 + dx, y4 + dy,
            0.5 * x0 + dx, y1 + dy)
        dyp = ya - y1
    else:
        dx = -0.02 * x0
        dy = 0
        dxp = -0.02 * x0
        dyp = 0
    #top layer
    ax.plot(
        [x0 / 4, x0 / 2 + dxp, x0 / 2 + dxp, 0.25 * x0],
        [   y0p,    y0p + dxp,     y1 + dyp,        y2],
        linewidth=1, color=lc)
    ax.plot(
        [x0 - x0 / 4, x0 - x0 / 2 - dxp, x0 - x0 / 2 - dxp, x0 - 0.25 * x0],
        [   0,   dxp,   y0p - y1 + dyp,      y0p - y2],
        linewidth=1, color=lc)
    #second layer
    if x3 > 0.5 * x0 + dxp:
        ax.plot(
            [x0 / 2 + dxp, x4 + dx, x3],
            [    y1 + dyp, y4 + dy, y3],
            linewidth=1, color=lc)
    else:
        x3pp, y3pp = intersect(
            x3, y3,
            x4 + dx,  y4 + dy,
            0.5 * x0 + dxp, 0,
            0.5 * x0 + dxp, y0p)
        ax.plot(
            [x0 / 2 + dxp, x4 + dx, x3pp],
            [    y1 + dyp, y4 + dy, y3pp],
            linewidth=1, color=lc)
        
    #third layer
    if y1 > 0.001:
        x5, y5 = intersect(
            0.25 * x0,       y2,
            x2,        0,
            x0 / 2 + dxp, y1 + dyp,
            x4 + dx,  y4 + dy)
    else:
        x5, y5 = intersect(
                 0.25 * x0, y2,
                        x2,  0,
                        x3, y3,
            0.5 * x0 + dxp, y1)        
    if x3 > 0.5 * x0 + dxp:
        ax.plot(
            [                                       0.5 * x0 + dxp, x3, x2, x5],
            [y2 + (0.25 * x0 + dxp) / (x3 - 0.25 * x0) * (y3 - y2), y3,  0, y5],
            linewidth=1, color=lc)
    else:
        x3p, y3p = intersect(
            x3, y3,
            x2,  0,
            0.5 * x0 + dxp, 0,
            0.5 * x0 + dxp, y0p)
        ax.plot(
            [ x3p, x2, x5],
            [ y3p,  0, y5],
            linewidth=1, color=lc)
    
    # horizontal
    if guide_bool:
        if 0.25 * x0 + (x3 - 0.25 * x0) * (y2 - y1) / y2 > 0.5 * x0 + dxp:
            ax.plot([0.5 * x0 + dxp, 0.25 * x0 + (x3 - 0.25 * x0) * (y2 - y1) / y2],[y1 + dyp, y2 + (y3 - y2) * (y2 - y1) / y2], linewidth=0.5, color=lc)
    # 1/2 line diag
    if y1 > 0.001:
        x6, y6 = intersect(
            0.50 * x0,      y1,
            x4,      y4,
            x3,      y3,
            x4 + dx, y4 + dy)
        ax.plot([x6, x4],[y6, y4], linewidth=0.5, color=lc)
    # 1/2 line
    if x3 < 0.5 * x0:
        ymin = y3 - (x3 - 0.5 * x0) / (x3 - x2) * y3
    else:
        ymin = y2 + 0.25 * x0 / (x3 - 0.25 * x0) * (y3 - y2)
    ax.plot([0.50 * x0, 0.50 * x0],[ymin, y0p], linewidth=0.5, color=lc)
    ax.scatter([0],[0], color=lcp)
    ax.scatter([x0],[y0p], color=lcp)
    """
    st.pyplot(fig)

def draw_fold(yscale, angle, y1, y0, x0, night_mode):
    y0p = y0 * yscale
    
    phi = 0.5 * math.pi - 0.5 * angle * math.pi / 180.
    y2 = y1 + 0.5 * x0 * math.tan(phi)
    x2 = 0.5 * x0 + y1 / math.tan(phi)
    x3 = x2 * (1. - math.cos(2. * phi))
    y3 = x2 * math.sin(2. * phi)

    if night_mode:
        plt.style.use('dark_background')
        lc = "white"
    else:
        plt.style.use('default')
        lc = "black"
    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    
    #frame bottom
    ax.plot([x2, x0],[0,0], linewidth=1, color=lc)
    #frame right
    ax.plot([x0, x0],[0, y0p], linewidth=1, color=lc)
    #frame top
    ax.plot([x0, 0],[y0p, y0p], linewidth=1, color=lc)
    #frame left
    ax.plot([0, 0],[y0p, y2], linewidth=1, color=lc)

    #bottom corner
    ax.plot([0, x3, x2, 0],[y2, y3, 0, y2], linewidth=1, color=lc)

    # horizontal
    ax.plot([x2 + y1 * (x3 - x2) / y3, x0],[y1, y1], linewidth=0.5, color=lc)
    ax.plot([0.5 * x0, x3* (y2 - y1) / y2],[y1, y2 + (y3 - y2) * (y2 - y1) / y2], linewidth=0.5, color=lc)
    
    # 1/4 line diag bottom
    ax.plot([0.25 * x0, x2 + (x3 - x2) * (x2 - 0.25 * x0) / x2],[y2 * (x2 - 0.25 * x0) / x2, y3 * (x2 - 0.25 * x0) / x2], linewidth=0.5, color=lc)
    # 1/4 line vertical
    if x3 > 0.25 * x0:
        ymin = y2 - 0.25 * x0 / x3 * (y2 - y3)
    else:
        ymin = y3 - (x3 - 0.25 * x0) / (x3 - x2) * y3

    ax.plot([0.25 * x0, 0.25 * x0],[ymin, y0p], linewidth=0.5, color=lc)
        
    # 1/2 line diag bottom
    ax.plot([0.50 * x0, x2 + (x3 - x2) * (x2 - 0.50 * x0) / x2],[y2 * (x2 - 0.50 * x0) / x2, y3 * (x2 - 0.50 * x0) / x2], linewidth=0.5, color=lc)
    # 1/2 line
    if x3 < 0.5 * x0:
        ymin = y3 - (x3 - 0.5 * x0) / (x3 - x2) * y3
    else:
        ymin = y2 - 0.50 * x0 / x3 * (y2 - y3)
    ax.plot([0.50 * x0, 0.50 * x0],[ymin, y0p], linewidth=0.5, color=lc)
    # 3/4 line vertical
    if x3 > 0.75 * x0:
        ymin = y2 - 0.75 * x0 / x3 * (y2 - y3)
    elif x2 > 0.75 * x0:
        ymin = y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3
    else:
        ymin = 0
    ax.plot([0.75 * x0, 0.75 * x0], [ymin, y0p], linewidth=0.5, color=lc)
    if x3 > 0.75 * x0 and x2 < 0.75 * x0:
        ax.plot([0.75 * x0, 0.75 * x0], [0, y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3], linewidth=0.5, color=lc)
        
    st.pyplot(fig)
