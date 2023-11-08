set output "test.tex"
set terminal epslatex

set para
set tr [0:1]
set size ratio -1

unset border
unset tic

x0 = 11.7 / 8.
y0 = 8.3 / 4.

y1 = 0.75 * x0 * tan(0.5 * acos(1. / 3.))

y2 = y1 / 3. + sqrt(3.) / 6. * x0
y2h = y1 / 3. + sqrt(3.) / 12. * x0

f(x1,x2,t) = x1 + (x2 - x1) * t

r = 0.5
dr = 0.5 * x0
th = 2. * pi / 3.
dth = asin(dr/2./r)
xc = 0.125 * x0 + sqrt(3.) * y2 / 2. + sqrt(r**2 - 0.25 * dr**2) * sin(th)
yc = y1 / 2. + sqrt(3.) * x0 / 8. - sqrt(r**2 - 0.25 * dr**2) * cos(th)


plot f(0.50 * x0, 1.06 * 0.5 * x0, t), f(y1 / 3., 1.1 * y1 / 3., t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.985 * 0.5 * x0, t), f(y1 / 3., 1.08 * y1 / 3., t) lw 1 lc rgb 'black' not,\
     f(0.94 * 0.5 * x0, 0.125 * x0 + sqrt(3.) * y2 / 2., t), f(((0.94 * 0.5 * x0 - 0.125 * x0 - sqrt(3.) * y2 / 2.)) / sqrt(3.) + y1 / 2. + sqrt(3.) * x0 / 8., y1 / 2. + sqrt(3.) * x0 / 8., t) lw 3 lc rgb 'black' not,\
     f(0.25 * x0, 0.94 * 0.5 * x0, t), f(y1 / 3. + sqrt(3.) / 12. * x0, y1 / 3., t) lw 3 lc rgb 'black' not,\
     f(0.97 * 0.5 * x0, 1.06 * 0.5 * x0, t), f(1.04 * y1 / 3., 0.9 * y1 / 3., t) lw 3 lc rgb 'black' not,\
     f(0.75 * x0, 1.5 * x0 - sqrt(3.) * y2, t), f(0.047, -0.005, t) lw 3 lc rgb 'black' not,\
     f(0.94 * 0.5 * x0, 1.06 * 0.50 * x0, t), f(y1 / 3., 1.19 * y1 / 3., t) lw 3 lc rgb 'black' not,\
f(0.50 * x0, 0.50 * x0, t), f(y1 / 3., 0.6 * y0, t) lw 4 lc rgb 'black' dt 6 not,\
     f(0.75 * x0, 1.06 * 0.5 * x0, t), f(y1 / 3., y1 / 3. - 0.01 * y0, t) lw 1 lc rgb 'black' not,\
     f(0.25 * x0, 0.25 * x0, t), f(y1 / 3. + sqrt(3.) / 12. * x0, 0.6 * y0 + 0.09, t) lw 3 lc rgb 'black' not,\
     f(0.94 * 0.5 * x0, 0.94 * 0.5 * x0, t), f(y1 / 3., 0.6 * y0 + 0.035, t) lw 3 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0, t), f(0.047, 0.6 * y0 - 0.1, t) lw 3 lc rgb 'black' not,\
     f(1.06 * 0.5 * x0, 1.06 * 0.5 * x0, t), f(0.6 * y0 - 0.01, -0.01 * y0, t) lw 3 lc rgb 'black' not,\
     f(1.06 * 0.5 * x0, 1.5 * x0 - sqrt(3.) * y2, t), f(-0.01 * y0, -0.005, t) lw 3 lc rgb 'black' not,\
     f(0.1 * x0, 0.9 * x0, t), 0.6 * y0 + 0.1 * sin(6.*t) lw 4 lc rgb 'black' not
     

set terminal x11
