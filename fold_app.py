import math

import streamlit as st
import matplotlib.pyplot as plt

import st_plots

x0 = 11.7 / 8.
y0 = 8.3 / 4.
ell0 = 1. - 0.5 * x0 / y0 * math.tan(0.5 * math.acos(1. / 3.))

def get_yoffset():
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
    


def update_slider():
    st.session_state.slider = st.session_state["presets"][st.session_state.preset_choice][0] / 4.

    
yoffset_list = get_yoffset()
header = st.container()
row0 = st.container()
row1 = st.container()
rowa = st.container()
col0 = row0.columns(2, gap="medium")
col1 = row1.columns(3, gap="medium")
col1a, col2a, col3a = rowa.columns(3, gap="medium")

#if not "presets" in st.session_state:
st.session_state["presets"] = {}
st.session_state["presets"]["None"] = (4,90.,0,90.,0,-1)
st.session_state["presets"]["Tetrahedron"] = (4,60.,4,60.,4,6)
st.session_state["presets"]["Triakis Tetrahedron (a)"] = (6,33.5573,3,112.8854,1,12)
st.session_state["presets"]["Triakis Tetrahedron (b)"] = (10,33.5573,3,33.5573,3,6)
st.session_state["presets"]["Triakis Octahedron (a)"] = (7,31.3997,3,117.2006,6,24)
st.session_state["presets"]["Triakis Octahedron (b)"] = (11,31.3997,3,31.3997,3,12)
st.session_state["presets"]["Tetrakis Hexahedron (a)"] = (6,48.1897,2,83.6206,10,24)
st.session_state["presets"]["Tetrakis Hexahedron (b)"] = (7,48.1897,2,48.1897,2,12)

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
            "First Angle",
            format="%.4f",
            value = st.session_state["presets"][preset_choice][1],
            step=None
        )
        #y1 = st.number_input(
        #    "First y-offset",
        #    format="%.4f",
        #    step=None
        #)
        iy1 = st.select_slider(
            "First y-offset",
            options=range(len(yoffset_list)),
            value=st.session_state["presets"][preset_choice][2],
            format_func=lambda x: f'{yoffset_list[x][3]:6.4f}',
            key="box1"
        )
        anglep = st.number_input(
            "Second Angle",
            format="%.4f",
            value=st.session_state["presets"][preset_choice][3],
            step=None
        )
        #y1p = st.number_input(
        #    "Second y-offset",
        #    format="%.4f",
        #    step=None
        #)
        iy1p = st.select_slider(
            "Second y-offset",
            options=range(len(yoffset_list)),
            value=st.session_state["presets"][preset_choice][4],
            format_func=lambda x: f'{yoffset_list[x][3]:6.4f}',
            key="box2"
        )
        
        submitted = st.form_submit_button("Draw")

    if preset_choice == "None" and not submitted:
        st.write("Enter a query in the sidebar")
    else:
        y1 = yoffset_list[iy1][3] * x0
        y1p = yoffset_list[iy1p][3] * x0
        ell = (yscale - (y1 + y1p) / y0)/ ell0
        inum = 0
        with col0[0]:
            st_plots.draw_page(yscale, y0, x0)
            iy = int(yscale * 4)
            a = math.gcd(16, iy)
            frac = f"{iy // a}/{16 // a}"
            st.write(f"{inum}.  Fold a sheet of paper lengthwise by $1/8$ and heightwise by ${frac}$.  To achieve this height, make small creases on the side in successive halves in the order indicated to the left.")
            inum += 1
        with col1[0]:
            st_plots.draw_initial(yscale, y0, x0)
            st.write(f"{inum}.  Crease the paper in fourths lengthwise.")
            inum += 1
        with col1a:
            st.write(f"Angle: {angle:.3f}$^\circ$")
            st.write(f"Offset:  {yoffset_list[st.session_state.box1][0:3]}")
            st_plots.draw_fold(yscale, angle, y1, y0, x0)
        with col2a:
            st.write(f"Angle: {anglep:.3f}$^\circ$")
            st.write(f"Offset:  {yoffset_list[st.session_state.box2][0:3]}")
            st_plots.draw_fold(yscale, anglep, y1p, y0, x0)
        header.write(f"Side length: {ell:.3f}")
        header.write(f"Units needed: {st.session_state['presets'][preset_choice][5]}")

ell0 = 1. - 0.5 * x0 / y0 * math.tan(0.5 * math.acos(1. / 3.))
