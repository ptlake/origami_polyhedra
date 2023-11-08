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
y2 = sqrt(3.) / 2. * x0

f(x1,x2,t) = x1 + (x2 - x1) * t

r = 0.5
dr = 0.5 * x0
th = atan2(y2, x0/2.)
dth = asin(dr/2./r)
xc = 5. * x0 / 8. + sqrt(3.) * y1 / 6. + sqrt(r**2 - 0.25 * dr**2) * sin(th)
yc = y2 / 4. + y1 / 6. - sqrt(r**2 - 0.25 * dr**2) * cos(th)

plot f(0.50 * x0, 0.50 * x0, t), f(y1 / 3., 0.6 * y0, t) lw 4 lc rgb 'black' dt 6 not,\
     f(0.75 * x0, 1.06 * 0.5 * x0, t), f(y1 / 3., 0.95 * y1 / 3., t) lw 1 lc rgb 'black' not,\
     f(0.25 * x0, 0.25 * x0, t), f(y2 / 2. + y1 / 3., 0.6 * y0 + 0.09, t) lw 3 lc rgb 'black' not,\
     f(0.94 * 0.50 * x0, 1.06 * 0.5 * x0, t), f(1.03 * (y2 / 3. + y1 / 3.), 0.955 * (y2 / 3. + y1 / 3.), t) lw 3 lc rgb 'black' not,\
     f(0.25 * x0, 0.94 * 0.50 * x0, t), f(y2 / 2. + y1 / 3., y1 / 3., t) lw 3 lc rgb 'black' not,\
     f(1.06 * 0.5 * x0, 0.94 * 0.5 * x0, t), f(0.79 * y1 / 3., y1 / 3., t) lw 3 lc rgb 'black' not,\
     f(0.94 * 0.5 * x0, 0.94 * 0.5 * x0, t), f(y1 / 3., 0.6 * y0 + 0.035, t) lw 3 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0, t), f(0., 0.6 * y0 - 0.1, t) lw 3 lc rgb 'black' not,\
     f(1.06 * 0.5 * x0, 1.06 * 0.5 * x0, t), f(0.6 * y0 - 0.01, -0.01 * y0, t) lw 3 lc rgb 'black' not,\
     f(1.06 * 0.5 * x0, 0.75 * x0, t), f(-0.01 * y0, 0., t) lw 3 lc rgb 'black' not,\
     f(0.1 * x0, 0.9 * x0, t), 0.6 * y0 + 0.1 * sin(6.*t) lw 4 lc rgb 'black' not

set terminal x11
