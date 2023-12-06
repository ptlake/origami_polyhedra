import math

import streamlit as st
import matplotlib.pyplot as plt

import st_plots
import st_funcs

# Paper size
x0 = 11.7 / 8.
y0 = 8.3 / 4.
ell0 = 1. - 0.5 * x0 / y0 * math.tan(0.5 * math.acos(1. / 3.))    
    
yoffset_list = st_funcs.get_yoffset()
header = st.container()
# premake containers - making too many...
rows = [st.container() for i in range(10)]
cells = [rows[i].columns(3, gap="medium") if i !=0 else rows[i].columns(2, gap="medium") for i in range(len(rows))]

#st.session_state["presets"] = {}
#st.session_state["presets"]["None"] = (4,90.,0,90.,0,-1)
#st.session_state["presets"]["Tetrahedron"] = (4,60.,4,60.,4,6)
#st.session_state["presets"]["Triakis Tetrahedron (a)"] = (6,33.5573,3,112.8854,1,12)
#st.session_state["presets"]["Triakis Tetrahedron (b)"] = (10,33.5573,3,33.5573,3,6)
#st.session_state["presets"]["Triakis Octahedron (a)"] = (7,31.3997,3,117.2006,6,24)
#st.session_state["presets"]["Triakis Octahedron (b)"] = (11,31.3997,3,31.3997,3,12)
#st.session_state["presets"]["Tetrakis Hexahedron (a)"] = (6,48.1897,2,83.6206,10,24)
#st.session_state["presets"]["Tetrakis Hexahedron (b)"] = (7,48.1897,2,48.1897,2,12)
#st.session_state["presets"]["Rhombic Dodecahedron"] = (4,109.471,4,70.5288,8,24)
#st.session_state["presets"]["Disdyakis Dodecahedron (a)"] = (6,55.025,8,87.202,10,24)
#st.session_state["presets"]["Disdyakis Dodecahedron (b)"] = (7,87.202,10,37.773,1,24)
#st.session_state["presets"]["Disdyakis Dodecahedron (c)"] = (8,55.025,8,37.773,1,24)

# read presets
if "presets" not in st.session_state:
    st.session_state["presets"] = st_funcs.read_presets()
if "default_preset" not in st.session_state:
    st.session_state["default_preset"] = 0
if "prev_preset" not in st.session_state:
    st.session_state["prev_preset"] = 0



with st.sidebar:
    preset_bool = st.toggle("Use Presets")
    full_bool = st.toggle("Full instructions")
    night_mode = st.toggle("Night mode")

    if not preset_bool:
        if st.session_state["default_preset"] is not None:
            st.session_state["prev_preset"] = st.session_state["default_preset"]
        st.session_state["default_preset"] = None
    elif st.session_state["default_preset"] is None:
        st.session_state["default_preset"] = st.session_state["prev_preset"]
    preset_choice = st.selectbox(
        "Presets",
        options=st.session_state["presets"].keys(),
        index=st.session_state["default_preset"],
        disabled = not preset_bool
    )
    if preset_choice is not None:
        st.session_state['default_preset'] = list(st.session_state["presets"].keys()).index(preset_choice)

tear_options = ["None","Half","All"]

with st.form("selections"):
    with st.sidebar:
        if preset_bool:
            current_preset = st.session_state["presets"][preset_choice]
            st.session_state["yscale_slider"] = current_preset['paper size'] / 4.
            st.session_state["angle_input"] = current_preset['angle 1']
            st.session_state["tear_radio"] = tear_options[current_preset['tear 1']]
            st.session_state["yoffset_slider"] = current_preset['y-offset 1']
            st.session_state["anglep_input"] = current_preset['angle 2']
            st.session_state["yoffsetp_slider"] = current_preset['y-offset 2']
            st.session_state["tearp_radio"] = tear_options[current_preset['tear 2']]
            
        yscale = st.slider(
            "y-scale",
            min_value=0.25,
            max_value=4.00,
            step=0.25,
            disabled=preset_bool,
            key='yscale_slider'
        )
        angle = st.number_input(
            "First Angle",
            format="%.4f",
            step=1.,
            disabled=preset_bool,
            key='angle_input'
        )
        iy1 = st.select_slider(
            "First y-offset",
            options=range(len(yoffset_list)),
            format_func=lambda x: f'{yoffset_list[x][3]:6.4f}',
            disabled=preset_bool,
            key="yoffset_slider"
        )
        tear_opt = st.radio(
            "First side tear",
            options=tear_options,
            horizontal=True,
            disabled=preset_bool,
            key='tear_radio'
        )
        anglep = st.number_input(
            "Second Angle",
            format="%.4f",
            step=1.,
            disabled=preset_bool,
            key='anglep_input'
        )
        iy1p = st.select_slider(
            "Second y-offset",
            options=range(len(yoffset_list)),
            format_func=lambda x: f'{yoffset_list[x][3]:6.4f}',
            disabled=preset_bool,
            key="yoffsetp_slider"
        )
        tear_optp = st.radio(
            "Second side tear",
            options=tear_options,
            horizontal=True,
            disabled=preset_bool,
            key='tearp_radio'
        )
        
        submitted = st.form_submit_button("Draw", disabled=preset_bool)

    if not preset_bool and not submitted:
        header.write("Enter query")
    else:
        if abs(angle - anglep) < 0.01 and iy1 == iy1p and tear_opt == tear_optp:
            symm_bool = True
        else:
            symm_bool = False
        
        y1 = yoffset_list[iy1][3] * x0
        y1p = yoffset_list[iy1p][3] * x0
        ell = (yscale - (y1 + y1p) / y0)/ ell0
        if full_bool:
            if tear_opt != "None":
                guide_bool = True
            if tear_optp != "None":
                guide_bool = True
            
            if iy1:
                phi0 = 180 - math.acos(yoffset_list[iy1][0] / yoffset_list[iy1][1]) * 180 / math.pi
            else:
                phi0 = 0
            guide_bool = bool(iy1) and abs(phi0 - angle) > 1
            if iy1p:
                phi0p = 180 - math.acos(yoffset_list[iy1p][0] / yoffset_list[iy1p][1]) * 180 / math.pi
            else:
                phi0p = 0
            guide_boolp = bool(iy1p) and abs(phi0p - anglep) > 1
            inum = 0
            with cells[0][0]:
                st_plots.draw_page(yscale, y0, x0, night_mode)
                iy = int(yscale * 4)
                a = math.gcd(16, iy)
                frac = f"{iy // a}/{16 // a}"
                st.write(f"{inum}.  Fold a sheet of paper lengthwise by $1/8$ and heightwise by ${frac}$.  To achieve this height, make small creases on the side in successive halves in the order indicated to the left.")
            with cells[1 + inum // 3][inum % 3]:
                inum += 1
                st_plots.draw_initial(yscale, y0, x0, night_mode)
                st.write(f"{inum}.  Crease the paper in fourths lengthwise.")
            if guide_bool:
                with cells[1 + inum // 3][inum % 3]:
                    inum += 1
                    crease, direction = st_plots.draw_guide1(yscale, y0, x0, yoffset_list[iy1], night_mode)
                    st.write(f"{inum}.  {direction}")
                with cells[1 + inum // 3][inum % 3]:
                    inum += 1
                    st_plots.draw_guide2(yscale, y0, x0, y1, crease, night_mode)
                    st.write(f"{inum}.  Make a horizon crease going through the intersection of the crease made in step {inum - 1}.")
                    inum_yoffset = inum
            else:
                crease = None
            with cells[1 + inum // 3][inum % 3]:
                inum += 1
                st_plots.draw_angle1(yscale, angle, y1, y0, x0, crease, guide_bool, night_mode)
                if preset_bool:
                    st.write(f"{inum}.  {current_preset['fold description 1']}")
                else:
                    st.write(f"{inum}.  Fold.")
            with cells[1 + inum // 3][inum % 3]:
                inum += 1
                st_plots.draw_angle2(yscale, angle, y1, y0, x0, guide_bool, night_mode)
                st.write(f"{inum}.  Fold.")
            with cells[1 + inum // 3][inum % 3]:
                inum += 1
                st_plots.draw_angle3(yscale, angle, y1, y0, x0, guide_bool, night_mode, tear_opt, 0)
                if tear_opt == "None":
                    if symm_bool:
                        st.write(f"{inum}.  Unfold completely and rotate 180$^\circ$. Repeat steps 2 to {inum - 1}")
                    else:
                        st.write(f"{inum}.  Unfold completely and rotate 180$^\circ$.")
                else:
                    st.write(f"{inum}.  Unfold completely.")
                inum_creases = inum
            if tear_opt != "None":
                with cells[1 + inum // 3][inum % 3]:
                    inum += 1
                    if symm_bool:
                        st_plots.draw_tear(yscale, angle, y1, y0, x0, night_mode, tear_opt, 1)
                        if tear_opt == "All":
                            st.write(f"{inum}.  Tear along the fold formed in step {inum_yoffset}. Refold creases.")
                            yscale = yscale - y1 / y0
                            y1 = 0
                        else:
                            st.write(f"{inum}.  Tear horizontally half way between the bottom and the fold formed in step {inum_yoffset}. Rotate 180$^\circ$.")
                            yscale = yscale - 0.5 * y1 / y0
                            y1 /= 2
                    else:
                        st_plots.draw_tear(yscale, angle, y1, y0, x0, night_mode, tear_opt, 0)
                        if tear_opt == "All":
                            st.write(f"{inum}.  Tear along the fold formed in step {inum_yoffset}. Rotate 180$^\circ$.")
                            yscale = yscale - y1 / y0
                            y1 = 0
                        else:
                            st.write(f"{inum}.  Tear horizontally half way between the bottom and the fold formed in step {inum_yoffset}. Rotate 180$^\circ$.")
                            yscale = yscale - 0.5 * y1 / y0
                            y1 /= 2
                    if symm_bool:
                        with cells[1 + inum // 3][inum % 3]:
                            inum += 1
                            st_plots.draw_angle3(yscale, angle, y1, y0, x0, guide_bool, night_mode, tear_opt, 0)
                            st.write(f"{inum}.  Unfold completely and rotate 180$^\circ$. Repeat steps 2 to {inum - 1}")

            if symm_bool:
                if tear_opt == "All":
                    yscale = yscale - y1 / y0
                    y1p = 0
                elif tear_opt == "Half":
                    yscale = yscale - 0.5 * y1 / y0
                    y1p /= 2

            else:
                if guide_boolp:
                    with cells[1 + inum // 3][inum % 3]:
                        inum += 1
                        creasep, directionp = st_plots.draw_guide1(yscale, y0, x0, yoffset_list[iy1p], night_mode)
                        st.write(f"{inum}.  {directionp}")
                    with cells[1 + inum // 3][inum % 3]:
                        inum += 1
                        st_plots.draw_guide2(yscale, y0, x0, y1p, creasep, night_mode)
                        st.write(f"{inum}.  Make a horizon crease going through the intersection of the crease made in step {inum - 1}.")
                        inum_yoffsetp = inum
                else:
                    creasep = None
                with cells[1 + inum // 3][inum % 3]:
                    inum += 1
                    st_plots.draw_angle1(yscale, anglep, y1p, y0, x0, creasep, guide_boolp, night_mode)
                if preset_bool:
                    st.write(f"{inum}.  {current_preset['fold description 2']}")
                else:
                    st.write(f"{inum}.  Fold.")
                with cells[1 + inum // 3][inum % 3]:
                    inum += 1
                    st_plots.draw_angle2(yscale, anglep, y1p, y0, x0, guide_boolp, night_mode)
                    st.write(f"{inum}.  Fold.")
                    
                if tear_optp != "None":
                    with cells[1 + inum // 3][inum % 3]:
                        inum += 1
                        st_plots.draw_angle3(yscale, anglep, y1p, y0, x0, guide_boolp, night_mode, tear_optp, 1)
                        st.write(f"{inum}.  Unfold completely.")
                    with cells[1 + inum // 3][inum % 3]:
                        inum += 1
                        st_plots.draw_tear(yscale, anglep, y1p, y0, x0, night_mode, tear_optp, 1)
                        if tear_optp == "All":
                            st.write(f"{inum}.  Tear along the fold formed in step {inum_yoffsetp}. Refold creases.")
                            yscale = yscale - y1p / y0
                            y1p = 0
                        else:
                            st.write(f"{inum}.  Tear horizontally half way between the bottom and the fold formed in step {inum_yoffsetp}.  Refold creases.")
                            yscale = yscale - 0.5 * y1p / y0
                            y1p /= 2
            with cells[1 + inum // 3][inum % 3]:
                inum += 1
                st_plots.draw_angle3(yscale, anglep, y1p, y0, x0, guide_boolp, night_mode, "None", 1)
                st.write(f"{inum}.  Refold the right side from creases made through step {inum_creases}.")
            with cells[1 + inum // 3][inum % 3]:
                inum += 1
                st_plots.draw_final(yscale, angle, y1, anglep, y1p, y0, x0, guide_bool, guide_boolp, night_mode)
                st.write(f"{inum}.  Finished unit.  Make a crease down the center of the unit.")
        else:
            with cells[0][0]:
                st.write("Sets angle:")
            with cells[1][0]:
                st_plots.draw_fold(yscale, angle, y1, y0, x0, night_mode)
            with cells[1][1]:
                st_plots.draw_fold(yscale, anglep, y1p, y0, x0, night_mode)
            with cells[2][0]:
                st.write("Sets y-offset:")
            if iy1 != 0:
                with cells[3][0]:
                    crease, direction = st_plots.draw_guide1(yscale, y0, x0, yoffset_list[iy1], night_mode)
            if iy1p != 0:
                with cells[3][1]:
                    crease, direction = st_plots.draw_guide1(yscale, y0, x0, yoffset_list[iy1p], night_mode)

        with header:
            if preset_bool:
                st.title(preset_choice)
                st.write(f"Side length: {ell:.3f}")
                st.write(f"Angles: {angle:.1f}$^\circ$,  {anglep:.1f}$^\circ$")
                st.write(f"Units needed: {current_preset['units needed']}")
                st.write(f"Additional units: ")
                if not current_preset['additional units']:
                    st.write("N/A")
                for unit in current_preset['additional units']:
                    if st.button(unit):
                        st.session_state['default_preset'] = list(st.session_state["presets"].keys()).index(unit)
                        st.rerun()
            else:
                st.write(f"Side length: {ell:.3f}")
                st.write(f"Angles: {angle:.1f}$^\circ$,  {anglep:.1f}$^\circ$")
                


ell0 = 1. - 0.5 * x0 / y0 * math.tan(0.5 * math.acos(1. / 3.))
