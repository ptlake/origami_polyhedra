import glob
import json
import math

import streamlit as st

@st.cache_data
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

@st.cache_data
def read_presets():
    presets = {}
    for fname in glob.glob("presets/*.json"):
        f = open(fname)
        data = json.load(f)
        f.close()
        for unit in data['units']:
            presets[unit['name']] = unit
    return presets
