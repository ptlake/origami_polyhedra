import math

import streamlit as st
import matplotlib.pyplot as plt

x0 = 11.7 / 8.
y0 = 8.3 / 4.
ell0 = 1. - 0.5 * x0 / y0 * math.tan(0.5 * math.acos(1. / 3.))

def get_yscale():
    t=[(0,0,0,0)]
    for den in range(5):
        for num in range(-den+1,den):
            if math.gcd(num,den) == 1 and den - num < 5:
                if num < 0:
                    xmax = 5 + num
                else:
                    xmax = 5
                for x in range(1,xmax):
                    y = x/4 * math.tan(0.5 * math.acos(num/den))
                    t.append((num, den, x, y))
    t.sort(key=lambda x:x[3])
    return t
    

def draw_fold(yscale, angle, y1):
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

#def draw_fold(yscale, angle, y1, anglep, y1p):
#    y0p = y0 * yscale
#    
#    phi = 0.5 * math.pi - 0.5 * angle * math.pi / 180.
#    y2 = y1 + 0.5 * x0 * math.tan(phi)
#    x2 = 0.5 * x0 + y1 / math.tan(phi)
#    x3 = x2 * (1. - math.cos(2. * phi))
#    y3 = x2 * math.sin(2. * phi)
#
#    phip = 0.5 * math.pi - 0.5 * anglep * math.pi / 180.
#    y2p = y1p + 0.5 * x0 * math.tan(phip)
#    x2p = 0.5 * x0 + y1p / math.tan(phip)
#    x3p = x2p * (1. - math.cos(2. * phip))
#    y3p = x2p * math.sin(2. * phip)
#    
#    fig, ax = plt.subplots(figsize=(6, 4))
#    ax.axis('off')
#    ax.set_aspect(aspect='equal')
#    #frame bottom
#    ax.plot([x2, x0],[0,0], linewidth=1, color="black")
#    #frame right
#    ax.plot([x0, x0],[0, y0p - y2p], linewidth=1, color="black")
#    #frame top
#    ax.plot([x0 - x2p, 0],[y0p, y0p], linewidth=1, color="black")
#    #frame left
#    ax.plot([0, 0],[y0p, y2], linewidth=1, color="black")
#
#    #bottom corner
#    ax.plot([0, x3, x2, 0],[y2, y3, 0, y2], linewidth=1, color="black")
#    #top corner
#    ax.plot([x0, x0 - x3p, x0 - x2p, x0],[y0p - y2p, y0p - y3p, y0p, y0p - y2p], linewidth=1, color="black")
#
#    # horizontal bottom
#    ax.plot([x2 + y1 * (x3 - x2) / y3, x0],[y1, y1], linewidth=0.5, color="black")
#    ax.plot([0.5 * x0, x3* (y2 - y1) / y2],[y1, y2 + (y3 - y2) * (y2 - y1) / y2], linewidth=0.5, color="black")
#    # horizontal top
#    ax.plot([x0 - (x2p + y1p * (x3p - x2p) / y3p), 0],[y0p - y1p, y0p - y1p], linewidth=0.5, color="black")
#    ax.plot([x0 - 0.5 * x0, x0 - x3p * (y2p - y1p) / y2p],[y0p - y1p, y0p - (y2p + (y3p - y2p) * (y2p - y1p) / y2p)], linewidth=0.5, color="black")
#    
#    # 1/4 line diag bottom
#    ax.plot([0.25 * x0, x2 + (x3 - x2) * (x2 - 0.25 * x0) / x2],[y2 * (x2 - 0.25 * x0) / x2, y3 * (x2 - 0.25 * x0) / x2], linewidth=0.5, color="black")
#    # 1/4 line vertical
#    if x3 > 0.25 * x0:
#        ymin = y2 - 0.25 * x0 / x3 * (y2 - y3)
#    else:
#        ymin = y3 - (x3 - 0.25 * x0) / (x3 - x2) * y3
#    if x3p > 0.75 * x0:
#        ymax = y0p - (y2p - 0.75 * x0 / x3p * (y2p - y3p))
#    elif x2p > 0.75 * x0:
#        ymax = y0p - (y3p - (x3p - 0.75 * x0) / (x3p - x2p) * y3p)
#    else:
#        ymax = y0p
#
#    ax.plot([0.25 * x0, 0.25 * x0],[ymin, ymax], linewidth=0.5, color="black")
#    if x3p > 0.75 * x0 and x2p < 0.75 * x0:
#        ax.plot([0.25 * x0, 0.25 * x0], [y0p, y0p - (y3p - (x3p - 0.75 * x0) / (x3p - x2p) * y3p)], linewidth=0.5, color="black")
#        
#    # 1/2 line diag bottom
#    ax.plot([0.50 * x0, x2 + (x3 - x2) * (x2 - 0.50 * x0) / x2],[y2 * (x2 - 0.50 * x0) / x2, y3 * (x2 - 0.50 * x0) / x2], linewidth=0.5, color="black")
#    # 1/2 line diag top
#    ax.plot([0.50 * x0, x0 - (x2p + (x3p - x2p) * (x2p - 0.50 * x0) / x2p)],[y0p - (y2p * (x2p - 0.50 * x0) / x2p), y0p - (y3p * (x2p - 0.50 * x0) / x2p)], linewidth=0.5, color="black")
#    # 1/2 line
#    if x3 < 0.5 * x0:
#        ymin = y3 - (x3 - 0.5 * x0) / (x3 - x2) * y3
#    else:
#        ymin = y2 - 0.50 * x0 / x3 * (y2 - y3)
#    if x3p < 0.5 * x0:
#        ymax = y0p - (y3p - (x3p - 0.5 * x0) / (x3p - x2p) * y3p)
#    else:
#        ymax = y0p - (y2p - 0.50 * x0 / x3p * (y2p - y3p))
#    ax.plot([0.50 * x0, 0.50 * x0],[ymin, ymax], linewidth=0.5, color="black")
#    # 3/4 line diag top
#    ax.plot([x0 - 0.25 * x0, x0 - (x2p + (x3p - x2p) * (x2p - 0.25 * x0) / x2p)],[y0p - y2p * (x2p - 0.25 * x0) / x2p, y0p - y3p * (x2p - 0.25 * x0) / x2p], linewidth=0.5, color="black")
#    # 3/4 line vertical
#    if x3 > 0.75 * x0:
#        ymin = y2 - 0.75 * x0 / x3 * (y2 - y3)
#    elif x2 > 0.75 * x0:
#        ymin = y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3
#    else:
#        ymin = 0
#    if x3p > 0.25 * x0:
#        ymax = y0p - (y2p - 0.25 * x0 / x3p * (y2p - y3p))
#    else:
#        ymax = y0p - (y3p - (x3p - 0.25 * x0) / (x3p - x2p) * y3p)
#    ax.plot([0.75 * x0, 0.75 * x0], [ymin, ymax], linewidth=0.5, color="black")
#    if x3 > 0.75 * x0 and x2 < 0.75 * x0:
#        ax.plot([0.75 * x0, 0.75 * x0], [0, y3 - (x3 - 0.75 * x0) / (x3 - x2) * y3], linewidth=0.5, color="black")
#        
#    st.pyplot(fig)

def update_slider():
    st.session_state.slider = st.session_state["presets"][st.session_state.preset_choice][0] / 4.
    
yscale_list = get_yscale()
col1, col2, col3 = st.columns([1,1,1])

#if not "presets" in st.session_state:
st.session_state["presets"] = {}
st.session_state["presets"]["None"] = (4,90.,0,90.,0)
st.session_state["presets"]["Tetrahedron"] = (4,60.,4,60.,4)
st.session_state["presets"]["Triakis Tetrahedron (a)"] = (6,33.5573,3,112.8854,1)
st.session_state["presets"]["Triakis Tetrahedron (b)"] = (10,33.5573,3,33.5573,3)
st.session_state["presets"]["Triakis Octahedron (a)"] = (7,31.3997,3,117.2006,6)
st.session_state["presets"]["Triakis Octahedron (b)"] = (11,31.3997,3,31.3997,3)
st.session_state["presets"]["Tetrakis Hexahedron (a)"] = (6,48.1897,2,83.6206,10)
st.session_state["presets"]["Tetrakis Hexahedron (b)"] = (7,48.1897,2,48.1897,2)

with st.sidebar:
    preset_choice = st.selectbox(
        "Presets",
        options=st.session_state["presets"].keys(),
        on_change=update_slider,
        key="preset_choice"
    )
    
with st.form("selections"):
    with st.sidebar:
        yscale = st.slider(
            "y-scale",
            min_value=0.25,
            max_value=4.00,
            value = st.session_state["presets"][preset_choice][0] / 4.,
            step=0.25,
            key='slider'
        )
        angle = st.number_input(
            "Bottom Angle",
            format="%.4f",
            value = st.session_state["presets"][preset_choice][1],
            step=None
        )
        #y1 = st.number_input(
        #    "Bottom y-offset",
        #    format="%.4f",
        #    step=None
        #)
        y1 = st.selectbox(
            "Bottom y-offset",
            options=yscale_list,
            index=st.session_state["presets"][preset_choice][2],
            key="box1"
        )
        anglep = st.number_input(
            "Top Angle",
            format="%.4f",
            value=st.session_state["presets"][preset_choice][3],
            step=None
        )
        #y1p = st.number_input(
        #    "Top y-offset",
        #    format="%.4f",
        #    step=None
        #)
        y1p = st.selectbox(
            "Top y-offset",
            options=yscale_list,
            index=st.session_state["presets"][preset_choice][4],
            key="box2"
        )
        
        submitted = st.form_submit_button("Draw")

    if preset_choice == "None" and not submitted:
        st.write("Enter a query in the sidebar")
    else:
        if preset_choice == "None":
            st.session_state["presets"]["None"] = (int(yscale * 4.), angle, yscale_list.index(st.session_state.box1), anglep, yscale_list.index(st.session_state.box2))
        y1 = y1[3] * x0
        y1p = y1p[3] * x0
        ell = (yscale - (y1 + y1p) / y0)/ ell0
        st.write(f"Side length: {ell:.3f}")
        with col1:
            draw_fold(yscale, angle, y1)
        with col2:
            draw_fold(yscale, anglep, y1p)

ell0 = 1. - 0.5 * x0 / y0 * math.tan(0.5 * math.acos(1. / 3.))
