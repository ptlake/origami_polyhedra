import math

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

style = "Simple, tail_width=0.5, head_width=6, head_length=8"
kw = dict(arrowstyle=style, color="k")

def draw_page(yscale, y0, x0):
    iy = int(4 * yscale)
    fig, ax = plt.subplots(figsize=(4 * x0, 2 * y0))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom page
    ax.plot([0, 7 * x0],[0, 0], linewidth=1, color="black")
    if iy != 16:
        ax.plot([8 * x0, 7 * x0],[yscale * y0, yscale * y0], linewidth=1, color="black")
    #frame right page
    ax.plot([8 * x0, 8 * x0],[4 * y0, yscale * y0], linewidth=1, color="black")
    ax.plot([7 * x0, 7 * x0],[0, yscale * y0], linewidth=1, color="black")
    #frame top page
    ax.plot([0, 7 * x0],[4 * y0, 4 * y0], linewidth=1, color="black")
    if iy != 16:
        ax.plot([8 * x0, 7 * x0],[4 * y0, 4 * y0], linewidth=1, color="black")
    #frame left page
    ax.plot([0, 0],[0, 4 * y0], linewidth=1, color="black")
    #frame left unit
    ax.plot([7.15 * x0, 7.15 * x0],[-0.1 * y0, (yscale - 0.1) * y0], linewidth=1, color="black")
    #frame top unit
    ax.plot([7.15 * x0, 8.15 * x0],[(yscale - 0.1) * y0, (yscale - 0.1) * y0], linewidth=1, color="black")
    #frame right unit
    ax.plot([8.15 * x0, 8.15 * x0],[-0.1 * y0, (yscale - 0.1) * y0], linewidth=1, color="black")
    #frame bottom unit
    ax.plot([7.15 * x0, 8.15 * x0],[-0.1 * y0, -0.1 * y0], linewidth=1, color="black")
    #vertical divisions
    for i in range(1,8):
        ax.plot([i * x0, i * x0],[0, 4 * y0], linewidth=0.5, color="black")
    #horizontal divisions:
    ax.plot([0, 7 * x0],[yscale * y0, yscale * y0], linewidth=0.5, color="black")
    for i in range(2, 15 // iy + 1):
        ax.plot([0, 8 * x0],[i * yscale * y0, i * yscale * y0], linewidth=0.5, color="black")
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
        ax.plot([0, 0.15 * x0],[jy / 4 * y0, jy / 4 * y0], linewidth=0.5, color="black")
        if jy > iy:
            ax.plot([8 * x0, 7.85 * x0],[jy / 4 * y0, jy / 4 * y0], linewidth=0.5, color="black")
        else:
            ax.plot([8.15 * x0, 8 * x0],[(jy / 4 - 0.1) * y0, (jy / 4 - 0.1) * y0], linewidth=0.5, color="black")
        jy *= 2
        if jy > 16:
            jy -=16
    for i,jy in enumerate(reversed(t)):
        ax.text(-0.25 * x0, (jy / 4 - 0.05) * y0, f'{i + 1}',{'size':6})
    st.pyplot(fig)
    
def draw_initial(yscale, y0, x0):
    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom page
    ax.plot([0, x0],[0, 0], linewidth=1, color="black")
    #frame right page
    ax.plot([x0, x0],[0, yscale * y0], linewidth=1, color="black")
    #frame top page
    ax.plot([0, x0],[yscale * y0, yscale * y0], linewidth=1, color="black")
    #frame left page
    ax.plot([0, 0],[0, yscale * y0], linewidth=1, color="black")
    #vertical divisions
    for i in range(1,4):
        ax.plot([i * x0 / 4, i * x0 / 4],[0, yscale * y0], linewidth=1.5, color="black", linestyle="dashed")
    st.pyplot(fig)
    
def draw_guide1(yscale, y0, x0, yoffset):
    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom page
    ax.plot([0, x0],[0, 0], linewidth=1, color="black")
    #frame right page
    ax.plot([x0, x0],[0, yscale * y0], linewidth=1, color="black")
    #frame top page
    ax.plot([0, x0],[yscale * y0, yscale * y0], linewidth=1, color="black")
    #frame left page
    ax.plot([0, 0],[0, yscale * y0], linewidth=1, color="black")
    #vertical divisions
    for i in range(1,4):
        ax.plot([i * x0 / 4, i * x0 / 4],[0, yscale * y0], linewidth=0.5, color="black")
    #crease line
    ix0 = yoffset[0]
    ix1 = yoffset[1]
    ix2 = yoffset[2]
    ix3 = max((min(((2 + ix2), 4)), ix1))
    if ix3 - ix0 > 4:
        st.write("here")
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
    ax.plot([x1a, x1b],[y1a, y1b], linewidth=1.5, color="black", linestyle="dashed")
    ax.plot([0,x1a],[y1, y1a], linewidth=0.5, color="black")
    ax.plot([x1b,x1],[y1b, 0], linewidth=0.5, color="black")
    if ix0:
        ixa = ix3 - ix1
        ixb = ix3 - ix0
        yb = ix1 * 0.25 * x0 * math.sin(2 * phi)
    else:
        ixa = 0
        ixb = ix3
        yb = ix3 * 0.25 * x0
    a = patches.FancyArrowPatch((ixa * 0.25 * x0, 0), (ixb * 0.25 * x0,  yb), shrinkA=10, shrinkB=10, connectionstyle="arc3,rad=-.3", **kw)
    a1 = patches.FancyArrowPatch((ixb * 0.25 * x0,  yb), (ixa * 0.25 * x0, 0), shrinkA=10, shrinkB=10, connectionstyle="arc3,rad=.3", **kw)
    plt.gca().add_patch(a)
    plt.gca().add_patch(a1)
    ax.scatter([ix3 * 0.25 * x0, ixa * 0.25 * x0, ixb * 0.25 * x0],[0, 0, yb], color="black", s=30)        
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
    
def draw_guide2(yscale, y0, x0, y1, crease):
    fig, ax = plt.subplots(figsize=(2 * x0, 2 * y0 * yscale))
    ax.axis('off')
    ax.set_aspect(aspect='equal')
    #frame bottom page
    ax.plot([0, x0],[0, 0], linewidth=1, color="black")
    #frame right page
    ax.plot([x0, x0],[0, yscale * y0], linewidth=1, color="black")
    #frame top page
    ax.plot([0, x0],[yscale * y0, yscale * y0], linewidth=1, color="black")
    #frame left page
    ax.plot([0, 0],[0, yscale * y0], linewidth=1, color="black")
    #vertical divisions
    for i in range(1,4):
        ax.plot([i * x0 / 4, i * x0 / 4],[0, yscale * y0], linewidth=0.5, color="black")
    #crease line
    ax.plot(crease[0],crease[1], linewidth=0.5, color="black")
    a = patches.FancyArrowPatch((x0 / 8, 0), (x0 / 8,  2 * y1), shrinkA=0, shrinkB=0, connectionstyle="arc3,rad=-.3", **kw)
    a1 = patches.FancyArrowPatch((x0 / 8,  2 * y1), (x0 / 8, 0),shrinkA=0, shrinkB=0, connectionstyle="arc3,rad=.3", **kw)
    plt.gca().add_patch(a)
    plt.gca().add_patch(a1)
        
    ax.plot([0, x0],[y1, y1], linewidth=1.5, color="black", linestyle="dashed")
    st.pyplot(fig)    


def draw_angle1(yscale, angle, y1, y0, x0, crease, guide_bool):
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
    ax.plot([0, x0],[0,0], linewidth=1, color="black")
    #frame right
    ax.plot([x0, x0],[0, y0p], linewidth=1, color="black")
    #frame top
    ax.plot([x0, 0],[y0p, y0p], linewidth=1, color="black")
    #frame left
    ax.plot([0, 0],[y0p, 0], linewidth=1, color="black")

    #fold
    ax.plot([x2, 0],[0, y2], linewidth=1.5, color="black", linestyle="dashed")

    if guide_bool:
        # horizontal
        ax.plot([0, x0],[y1, y1], linewidth=0.5, color="black")
        # crease
        ax.plot(crease[0], crease[1], linewidth=0.5, color="black")
    
    # 1/4 line vertical
    for i in range(1, 4):
        ax.plot([i * 0.25 * x0, i * 0.25 * x0],[0, y0p], linewidth=0.5, color="black")
        

    st.pyplot(fig)

def draw_angle2(yscale, angle, y1, y0, x0, guide_bool):
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
    ax.plot([x2, x0],[0,0], linewidth=1, color="black")
    #frame right
    ax.plot([x0, x0],[0, y0p], linewidth=1, color="black")
    #frame top
    ax.plot([x0, 0],[y0p, y0p], linewidth=1, color="black")
    #frame left
    ax.plot([0, 0],[y0p, y2], linewidth=1, color="black")

    #bottom corner
    ax.plot([0, x3, x2, 0],[y2, y3, 0, y2], linewidth=1, color="black")

    # horizontal bottom
    if guide_bool:
        ax.plot([x2 + y1 * (x3 - x2) / y3, x0],[y1, y1], linewidth=0.5, color="black")
        ax.plot([0.5 * x0, x3* (y2 - y1) / y2],[y1, y2 + (y3 - y2) * (y2 - y1) / y2], linewidth=0.5, color="black")

    # 1/4 line diag bottom
    ax.plot([0.25 * x0, x2 + (x3 - x2) * (x2 - 0.25 * x0) / x2],[y2 * (x2 - 0.25 * x0) / x2, y3 * (x2 - 0.25 * x0) / x2], linewidth=1.5, color="black", linestyle="dashed")
    # 1/4 line vertical
    if x3 > 0.25 * x0:
        ymin = y2 - 0.25 * x0 / x3 * (y2 - y3)
    else:
        ymin = y3 - (x3 - 0.25 * x0) / (x3 - x2) * y3
    ax.plot([0.25 * x0, 0.25 * x0],[ymin, y0p], linewidth=1.5, color="black", linestyle="dashed")
    ax.plot([0.25 * x0, x3* (y2 - y1) / y2],[y2 * (x2 - 0.25 * x0) / x2, y2 + (y3 - y2) * (y2 - y1) / y2], linewidth=1.5, color="black", linestyle="dashdot")
        
    # 1/2 line diag bottom
    ax.plot([0.50 * x0, x2 + (x3 - x2) * (x2 - 0.50 * x0) / x2],[y2 * (x2 - 0.50 * x0) / x2, y3 * (x2 - 0.50 * x0) / x2], linewidth=0.5, color="black")
    # 1/2 line
    if x3 < 0.5 * x0:
        ymin = y3 - (x3 - 0.5 * x0) / (x3 - x2) * y3
    else:
        ymin = y2 - 0.50 * x0 / x3 * (y2 - y3)
    ax.plot([0.50 * x0, 0.50 * x0],[ymin, y0p], linewidth=0.5, color="black")
    # 3/4 line vertical
    if x3 > 0.75 * x0:
        ymin = y2 - 0.75 * x0 / x3 * (y2 - y3)
    elif x2 > 0.75 * x0:
        ymin = y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3
    else:
        ymin = 0
    ax.plot([0.75 * x0, 0.75 * x0], [ymin, y0p], linewidth=0.5, color="black")
    if x3 > 0.75 * x0 and x2 < 0.75 * x0:
        ax.plot([0.75 * x0, 0.75 * x0], [0, y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3], linewidth=0.5, color="black")

    a = patches.FancyArrowPatch((x3, y3), (x2 + (x3 - x2) * (x2 - 0.5 * x0) / x2, y3 * (x2 - 0.5 * x0) / x2), shrinkA=5, shrinkB=5, connectionstyle="arc3,rad=-.3", **kw)
    plt.gca().add_patch(a)

    st.pyplot(fig)

def draw_fold(yscale, angle, y1, y0, x0):
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
    ax.plot([x2, x0],[0,0], linewidth=1, color="black")
    #frame right
    ax.plot([x0, x0],[0, y0p], linewidth=1, color="black")
    #frame top
    ax.plot([x0, 0],[y0p, y0p], linewidth=1, color="black")
    #frame left
    ax.plot([0, 0],[y0p, y2], linewidth=1, color="black")

    #bottom corner
    ax.plot([0, x3, x2, 0],[y2, y3, 0, y2], linewidth=1, color="black")

    # horizontal bottom
    ax.plot([x2 + y1 * (x3 - x2) / y3, x0],[y1, y1], linewidth=0.5, color="black")
    ax.plot([0.5 * x0, x3* (y2 - y1) / y2],[y1, y2 + (y3 - y2) * (y2 - y1) / y2], linewidth=0.5, color="black")
    
    # 1/4 line diag bottom
    ax.plot([0.25 * x0, x2 + (x3 - x2) * (x2 - 0.25 * x0) / x2],[y2 * (x2 - 0.25 * x0) / x2, y3 * (x2 - 0.25 * x0) / x2], linewidth=0.5, color="black")
    # 1/4 line vertical
    if x3 > 0.25 * x0:
        ymin = y2 - 0.25 * x0 / x3 * (y2 - y3)
    else:
        ymin = y3 - (x3 - 0.25 * x0) / (x3 - x2) * y3

    ax.plot([0.25 * x0, 0.25 * x0],[ymin, y0p], linewidth=0.5, color="black")
        
    # 1/2 line diag bottom
    ax.plot([0.50 * x0, x2 + (x3 - x2) * (x2 - 0.50 * x0) / x2],[y2 * (x2 - 0.50 * x0) / x2, y3 * (x2 - 0.50 * x0) / x2], linewidth=0.5, color="black")
    # 1/2 line
    if x3 < 0.5 * x0:
        ymin = y3 - (x3 - 0.5 * x0) / (x3 - x2) * y3
    else:
        ymin = y2 - 0.50 * x0 / x3 * (y2 - y3)
    ax.plot([0.50 * x0, 0.50 * x0],[ymin, y0p], linewidth=0.5, color="black")
    # 3/4 line vertical
    if x3 > 0.75 * x0:
        ymin = y2 - 0.75 * x0 / x3 * (y2 - y3)
    elif x2 > 0.75 * x0:
        ymin = y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3
    else:
        ymin = 0
    ax.plot([0.75 * x0, 0.75 * x0], [ymin, y0p], linewidth=0.5, color="black")
    if x3 > 0.75 * x0 and x2 < 0.75 * x0:
        ax.plot([0.75 * x0, 0.75 * x0], [0, y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3], linewidth=0.5, color="black")
        
    st.pyplot(fig)
