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

set arrow from x0/4. - r * sin(0.9*0.69), 0.6 * y0 + r * cos(0.9*0.69) to x0/4. - r * sin(0.9*0.7), 0.6 * y0 + r * cos(0.9*0.7) size 0.1,30 fixed lc rgb 'black' lw 3

plot f(0.50 * x0, 0.50 * x0, t), f(2. * y2 * cos(phi)**2 * (x2 - 0.50 * x0) / (x2 - 0.25 * x0), y0, t) lw 1 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0, t), f(2. * y2 * cos(phi)**2 * (x2 - 0.75 * x0) / (x2 - 0.25 * x0), y0, t) lw 1 lc rgb 'black' not,\
     f(0.25 * x0 + (x2 - 0.25 * x0) * (1. - y1 / (6. * y2 * cos(phi)**2)), x0, t), f(y1 / 3., y1 / 3., t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.50 * x0 + y2 * (x2 - 0.50 * x0) / x2 * sin(2. * phi), t), f(y2 * (x2 - 0.50 * x0) / x2, 2. * y2 * (x2 - 0.50 * x0) / x2 * cos(phi)**2, t) lw 1 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0 + y2 * (x2 - 0.75 * x0) / x2 * sin(2. * phi), t), f(y2 * (x2 - 0.75 * x0) / x2, 2. * y2 * (x2 - 0.75 * x0) / x2 * cos(phi)**2, t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.97 * 0.50 * x0, t), f(y1 / 3., 1.08 * y1 / 3., t) lw 1 lc rgb 'black' not,\
     f(0.96 * 0.5 * x0, x2, t), f(1.045 * y1 / 3., 0., t) lw 3 lc rgb 'black' not,\
     f(0.94 * 0.5 * x0, 0.94 * 0.5 * x0, t), f(y2 * (x2 - 0.50 * x0) / x2, 0.99 * y0, t) lw 3 lc rgb 'black' not,\
     f(x0, x0, t), f(0., y0, t) lw 3 lc rgb 'black' not,\
     f(x2, x0, t), f(0., 0., t) lw 3 lc rgb 'black' not,\
     f(0.25 * x0, x0, t), f(y0, y0, t) lw 3 lc rgb 'black' not,\
     f(0.25 * x0, 0.94 * 0.5 * x0, t), f(y0, 0.99 * y0, t) lw 3 lc rgb 'black' not,\
     f(x2, 0.94 * 0.5 * x0, t), f(0., 1.07 * (2. * y2 * cos(phi)**2 * (x2 - 0.50 * x0) / (x2 - 0.25 * x0)), t) lw 4 lc rgb 'black' not,\
     f(0.25 * x0, 0.25 * x0, t), f(y2 * (x2 - 0.25 * x0) / x2, y0, t) lw 3 lc rgb 'black' not,\
     f(0.25 * x0, 0.94 * 0.50 * x0, t), f(y2 * (x2 - 0.25 * x0) / x2, y2 * (x2 - 0.50 * x0) / x2, t) lw 3 lc rgb 'black' not,\
     f(0.96 * (0.50 * x0 + y2 * (x2 - 0.50 * x0) / x2 * sin(2. * phi)), 0.94 * 0.5 * x0, t), f(2. * y2 * (x2 - 0.50 * x0) / x2 * cos(phi)**2, 1.05 * (2. * y2 * cos(phi)**2 * (x2 - 0.50 * x0) / (x2 - 0.25 * x0)), t) lw 3 lc rgb 'black' not,\
f(0.96 * (0.50 * x0 + y2 * (x2 - 0.50 * x0) / x2 * sin(2. * phi)), 0.94 * 0.5 * x0, t), f(2. * y2 * (x2 - 0.50 * x0) / x2 * cos(phi)**2, y2 * (x2 - 0.50 * x0) / x2, t) lw 3 lc rgb 'black' not,\
     x0/4. + r * sin(0.9*f(-0.7, 0.7, t)), 0.6 * y0 + r * cos(0.9*f(-0.7, 0.7, t)) lw 3 lc rgb 'black' not
     

set terminal x11
