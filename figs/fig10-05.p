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

phi = atan2(y1 / 3., x0 / 2.)

y2 = y1 / 3. + tan(phi) * 0.5 * x0
x2 = y2 / tan(phi)

f(x1,x2,t) = x1 + (x2 - x1) * t

r = 1.5
dr = 1.5 * y2
th = -phi
dth = asin(dr/2./r)
xc = 0.125 * x0 + sqrt(r**2 - 0.25 * dr**2) * cos(th)
yc = y1 / 3. + 0.375 * x0 * tan(phi) + sqrt(r**2 - 0.25 * dr**2) * sin(th)

set arrow from xc - r * cos(th - 0.92 * dth), yc - r * sin(th - 0.92 * dth) to xc - r * cos(th - 0.95 * dth), yc - r * sin(th - 0.95 * dth) size 0.1,30 fixed lc rgb 'black' lw 3

plot f(0.25 * x0, 0.25 * x0, t), f(0., y0, t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.50 * x0, t), f(0., y0, t) lw 1 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0, t), f(0., y0, t) lw 1 lc rgb 'black' not,\
     f( 2. / 3. * 0.75 * x0 + 0.1 * x0 * 0.75 / y1, 2. / 3. * 0.75 * x0 - 0.1 * 0.75 * x0 / y1, t), f(y1 / 3. - 0.1, y1 / 3. + 0.1, t) lw 1 lc rgb 'black' not,\
f(0., x0, t), f(y2, 2. * y1 / 3. - y2, t) lw 4 lc rgb 'black' dt 6 not,\
     f(0., x0, t), f(y1 / 3., y1 / 3., t) lw 1 lc rgb 'black' not,\
     f(0., 0., t), f(0., y0, t) lw 3 lc rgb 'black' not,\
     f(x0, x0, t), f(0., y0, t) lw 3 lc rgb 'black' not,\
     f(0., x0, t), f(0., 0., t) lw 3 lc rgb 'black' not,\
     f(0., x0, t), f(y0, y0, t) lw 3 lc rgb 'black' not,\
     xc - r * cos(th + 0.95*f(-dth, dth, t)), yc - r * sin(th + 0.95*f(-dth, dth, t)) lw 3 lc rgb 'black' not
     
#f(0., y2 * cos(0.5 * pi - 2. * phi), t), f(y2, y2 + y2 * sin(0.5 * pi - 2. * phi), t) lw 4 lc rgb 'black' not,\

set terminal x11
