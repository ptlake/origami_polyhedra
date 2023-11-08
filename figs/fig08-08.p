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

phi = -0.5 * (asin(0.25 * x0 / sqrt(y1**2 / 9. + x0**2 / 4.)) - atan(3. * x0 / 2. / y1))

y2 = y1 / 3. + tan(phi) * 0.5 * x0
x2 = y2 / tan(phi)

f(x1,x2,t) = x1 + (x2 - x1) * t

r = 0.5
dr = 0.5 * x0
th = pi/2. - 2.*phi
dth = asin(dr/2./r)
xc = 0.25 * x0 + y2 * (x2 - 0.25 * x0) / x2 * sin(2. * phi) + sqrt(r**2 - 0.25 * dr**2) * cos(th)
yc = 2. * y2 * (x2 - 0.25 * x0) / x2 * cos(phi)**2 + sqrt(r**2 - 0.25 * dr**2) * sin(th)

plot f(0.50 * x0, 1.06 * 0.50 * x0, t), f(y2 * (x2 - 0.50 * x0) / x2, 1.19 * y2 * (x2 - 0.50 * x0) / x2, t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.97 * 0.50 * x0, t), f(y1 / 3., 1.08 * y1 / 3., t) lw 1 lc rgb 'black' not,\
     f(0.96 * 0.5 * x0, 1.06 * 0.5 * x0, t), f(1.045 * y1 / 3., 0.935 * y1 / 3., t) lw 3 lc rgb 'black' not,\
     f(1.5 * x0 - x2, 0.75 * x0, t), f(-0.02, tan(phi) * (x2 - 0.75 * x0), t) lw 3 lc rgb 'black' not,\
     f(1.06 * 0.5 * x0, 0.94 * 0.5 * x0, t), f(0.94 * (2. * y2 * cos(phi)**2 * (x2 - 0.50 * x0) / (x2 - 0.25 * x0)), 1.07 * (2. * y2 * cos(phi)**2 * (x2 - 0.50 * x0) / (x2 - 0.25 * x0)), t) lw 4 lc rgb 'black' not,\
     f(0.25 * x0, 0.94 * 0.50 * x0, t), f(y2 * (x2 - 0.25 * x0) / x2, y2 * (x2 - 0.50 * x0) / x2, t) lw 3 lc rgb 'black' not,\
     f(1.06 * 0.5 * x0, 0.94 * 0.5 * x0, t), f(0.9 * (2. * y2 * cos(phi)**2 * (x2 - 0.50 * x0) / (x2 - 0.25 * x0)), 1.05 * (2. * y2 * cos(phi)**2 * (x2 - 0.50 * x0) / (x2 - 0.25 * x0)), t) lw 3 lc rgb 'black' not,\
     f(1.06 * 0.5 * x0, 0.94 * 0.5 * x0, t), f(1.36 * y2 * (x2 - 0.50 * x0) / x2, y2 * (x2 - 0.50 * x0) / x2, t) lw 3 lc rgb 'black' not,\
f(0.50 * x0, 0.50 * x0, t), f(y1 / 3., 0.6 * y0, t) lw 4 lc rgb 'black' dt 6 not,\
     f(0.75 * x0, 1.06 * 0.5 * x0, t), f(y1 / 3., y1 / 3. -0.01 * y0, t) lw 1 lc rgb 'black' not,\
     f(0.25 * x0, 0.25 * x0, t), f(y2 * (x2 - 0.25 * x0) / x2, 0.6 * y0 + 0.09, t) lw 3 lc rgb 'black' not,\
     f(0.94 * 0.5 * x0, 0.94 * 0.5 * x0, t), f(y1 / 3., 0.6 * y0 + 0.035, t) lw 3 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0, t), f(tan(phi) * (x2 - 0.75 * x0), 0.6 * y0 - 0.1, t) lw 3 lc rgb 'black' not,\
     f(1.06 * 0.5 * x0, 1.06 * 0.5 * x0, t), f(0.6 * y0 - 0.01, -0.01 * y0, t) lw 3 lc rgb 'black' not,\
     f(1.06 * 0.5 * x0, 1.5 * x0 - x2, t), f(-0.01 * y0, -0.02, t) lw 3 lc rgb 'black' not,\
     f(0.1 * x0, 0.9 * x0, t), 0.6 * y0 + 0.1 * sin(6.*t) lw 4 lc rgb 'black' not
     

set terminal x11
