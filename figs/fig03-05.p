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

r = 0.5
dr = y1 / 2.
th = pi/2.
dth = asin(dr/2./r)
xc = x0 / 8. + sqrt(r**2 - 0.25 * dr**2) * sin(th)
yc = y1 / 3. - sqrt(r**2 - 0.25 * dr**2) * cos(th)

set label at -0.15, y1 / 3. - 0.025 * y0 "{\\Huge \\ding{34}}"

plot f(0.25 * x0, 0.25 * x0, t), f(y1 / 3., y0, t) lw 1 lc rgb 'black' not,\
     f(0.25 * x0, 0.25 * x0, t), f(-0.05 * y0, y1 / 3. - 0.05 * y0, t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.50 * x0, t), f(y1 / 3., y0, t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.50 * x0, t), f(-0.05 * y0, y1 / 3. - 0.05 * y0, t) lw 1 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0, t), f(y1 / 3., y0, t) lw 1 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0, t), f(-0.05 * y0, y1 / 3. - 0.05 * y0, t) lw 1 lc rgb 'black' not,\
     f( 2. / 3. * 0.75 * x0 + 0.1 * x0 * 0.75 / y1, 2. / 3. * 0.75 * x0, t), f(y1 / 3. - 0.1 - 0.05 * y0, y1 / 3. - 0.05 * y0, t) lw 1 lc rgb 'black' not,\
     f( 2. / 3. * 0.75 * x0, 2. / 3. * 0.75 * x0 - 0.1 * 0.75 * x0 / y1, t), f(y1 / 3., y1 / 3. + 0.1, t) lw 1 lc rgb 'black' not,\
     f(0., x0, t), f(y1 / 3., y1 / 3., t) lw 3 lc rgb 'black' not,\
     f(0., x0, t), f(y1 / 3. - 0.05 * y0, y1 / 3. - 0.05 * y0, t) lw 3 lc rgb 'black' not,\
     f(0., 0., t), f(y1 / 3., y0, t) lw 3 lc rgb 'black' not,\
     f(0., 0., t), f(-0.05 * y0, y1 / 3. - 0.05 * y0, t) lw 3 lc rgb 'black' not,\
     f(x0, x0, t), f(y1 / 3., y0, t) lw 3 lc rgb 'black' not,\
     f(x0, x0, t), f(-0.05 * y0, y1 / 3. - 0.05 * y0, t) lw 3 lc rgb 'black' not,\
     f(0., x0, t), f(-0.05 * y0,-0.05 * y0, t) lw 3 lc rgb 'black' not,\
     f(0., x0, t), f(y0, y0, t) lw 3 lc rgb 'black' not     

set terminal x11
