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

y2 = y1 / 3. + 0.5 * x0

f(x1,x2,t) = x1 + (x2 - x1) * t

r = 0.5
dr = 0.5 * x0
th = -pi/2.
dth = asin(dr/2./r)
xc = y2 - sqrt(r**2 - 0.25 * dr**2) * sin(th)
yc = y2 - 0.25 * x0 + sqrt(r**2 - 0.25 * dr**2) * cos(th)

set arrow from xc + r * sin(th + 0.89 * dth), yc - r * cos(th + 0.89 * dth) to xc + r * sin(th + 0.9 * dth), yc - r * cos(th + 0.9 * dth) size 0.1,30 fixed lc rgb 'black' lw 3
set arrow from x0/4. + r * sin(0.9*0.69), 0.6 * y0 + r * cos(0.9*0.69) to x0/4. + r * sin(0.9*0.7), 0.6 * y0 + r * cos(0.9*0.7) size 0.1,30 fixed lc rgb 'black' lw 3

plot f(0.50 * x0, y2, t), f(y2 - x0 / 2., y2 - x0 / 2., t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.5 * x0, t), f(y2 - x0 / 2., y2, t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.50 * x0, t), f(y2, y0, t) lw 1 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0, t), f(0., y0, t) lw 1 lc rgb 'black' not,\
     f(0., y2, t), f(y2, 0., t) lw 3 lc rgb 'black' not,\
     f(y2, x0, t), f(y1 / 3., y1 / 3., t) lw 1 lc rgb 'black' not,\
     f(0.25 * x0, y2, t), f(y2 - x0 / 4., y2 - x0 / 4., t) lw 4 lc rgb 'black' dt 6 not,\
     f(0.25 * x0, 0.25 * x0, t), f(y2, y0, t) lw 4 lc rgb 'black' dt 6 not,\
     f(0.25 * x0, 0.5 * x0, t), f(y2 - x0 / 4., y2, t) lw 4 lc rgb 'black' dt 4 not,\
     f(0., 0., t), f(y2, y0, t) lw 3 lc rgb 'black' not,\
     f(0., y2, t), f(y2, y2, t) lw 3 lc rgb 'black' not,\
     f(x0, x0, t), f(0., y0, t) lw 3 lc rgb 'black' not,\
     f(y2, x0, t), f(0., 0., t) lw 3 lc rgb 'black' not,\
     f(y2, y2, t), f(0., y2, t) lw 3 lc rgb 'black' not,\
     f(0., x0, t), f(y0, y0, t) lw 3 lc rgb 'black' not,\
     xc + r * sin(th + 0.9*f(-dth, dth, t)), yc - r * cos(th + 0.9*f(-dth, dth, t)) lw 3 lc rgb 'black' not,\
     x0/4. + r * sin(0.9*f(-0.7, 0.7, t)), 0.6 * y0 + r * cos(0.9*f(-0.7, 0.7, t)) lw 3 lc rgb 'black' not
     

set terminal x11
