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

f(x1,x2,t) = x1 + (x2 - x1) * t

r = 1.5
dr = x0 * sqrt(0.75)
th = atan(sqrt(2.))
dth = asin(dr/2./r)
xc = 0.25 * x0 + sqrt(r**2 - 0.25 * dr**2) * sin(th)
yc = 0.25 * sqrt(2.) * x0 - sqrt(r**2 - 0.25 * dr**2) * cos(th)

set arrow from xc - r * sin(th - 0.94 * dth), yc + r * cos(th - 0.94 * dth) to xc - r * sin(th - 0.95 * dth), yc + r * cos(th - 0.95 * dth) size 0.1,30 fixed lc rgb 'black' lw 3
set arrow from x0 - (xc - r * sin(th - 0.94 * dth)), y0 - (yc + r * cos(th - 0.94 * dth)) to x0 - (xc - r * sin(th - 0.95 * dth)), y0 - (yc + r * cos(th - 0.95 * dth)) size 0.1,30 fixed lc rgb 'black' lw 3

plot f(0.25 * x0, 0.25 * x0, t), f(0., y0, t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.50 * x0, t), f(0., y0, t) lw 1 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0, t), f(0., y0, t) lw 1 lc rgb 'black' not,\
     f( 2. / 3. * 0.75 * x0 + 0.1 * x0 * 0.75 / y1, 2. / 3. * 0.75 * x0 - 0.1 * 0.75 * x0 / y1, t), f(y1 / 3. - 0.1, y1 / 3. + 0.1, t) lw 4 lc rgb 'black' dt 6 not,\
     f(0.75 * x0, 2. / 3. * 0.75 * x0 + 0.1 * x0 * 0.75 / y1,t), f(0., y1 / 3. - 0.1, t) lw 1 lc rgb 'black'  not,\
     f(2. / 3. * 0.75 * x0 - 0.1 * x0 * 0.75 / y1, 0.,t), f(y1 / 3. + 0.1, y1, t) lw 1 lc rgb 'black' not,\
     f( x0 - (2. / 3. * 0.75 * x0 + 0.1 * x0 * 0.75 / y1), x0 - (2. / 3. * 0.75 * x0 - 0.1 * 0.75 * x0 / y1), t), f(y0 - (y1 / 3. - 0.1), y0 - (y1 / 3. + 0.1), t) lw 4 lc rgb 'black' dt 6 not,\
     f(x0 - (0.75 * x0), x0 - (2. / 3. * 0.75 * x0 + 0.1 * x0 * 0.75 / y1),t), f(y0, y0 - (y1 / 3. - 0.1), t) lw 1 lc rgb 'black'  not,\
     f(x0 - (2. / 3. * 0.75 * x0 - 0.1 * x0 * 0.75 / y1), x0,t), f(y0 - (y1 / 3. + 0.1), y0 - y1, t) lw 1 lc rgb 'black' not,\
     f(0., 0., t), f(0., y0, t) lw 3 lc rgb 'black' not,\
     f(x0, x0, t), f(0., y0, t) lw 3 lc rgb 'black' not,\
     f(0., x0, t), f(0., 0., t) lw 3 lc rgb 'black' not,\
     f(0., x0, t), f(y0, y0, t) lw 3 lc rgb 'black' not,\
     x0 - (xc - r * sin(th + 0.95*f(-dth, dth, t))), y0 - (yc + r * cos(th + 0.95*f(-dth, dth, t))) lw 3 lc rgb 'black' not,\
     xc - r * sin(th + 0.95*f(-dth, dth, t)), yc + r * cos(th + 0.95*f(-dth, dth, t)) lw 3 lc rgb 'black' not
     

set terminal x11
