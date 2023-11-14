import math

import streamlit as st
import matplotlib.pyplot as plt

def draw_page(yscale, y0, x0):
    iy = int(4 * yscale)
    fig, ax = plt.subplots(figsize=(6, 4))
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
    iy = int(4 * yscale)
    fig, ax = plt.subplots(figsize=(6, 4))
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
    ##vertical divisions
    for i in range(1,4):
        ax.plot([i * x0 / 4, i * x0 / 4],[0, yscale * y0], linewidth=1, color="black", linestyle="dashed")
    st.pyplot(fig)
    

def draw_fold(yscale, angle, y1, y0, x0):
    y0p = y0 * yscale
    
    phi = 0.5 * math.pi - 0.5 * angle * math.pi / 180.
    y2 = y1 + 0.5 * x0 * math.tan(phi)
    x2 = 0.5 * x0 + y1 / math.tan(phi)
    x3 = x2 * (1. - math.cos(2. * phi))
    y3 = x2 * math.sin(2. * phi)

    fig, ax = plt.subplots(figsize=(6, 4))
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
