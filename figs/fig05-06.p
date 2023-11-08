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

set arrow from x0/4. + r * sin(-0.9*0.69), 0.6 * y0 + r * cos(-0.9*0.69) to x0/4. + r * sin(-0.9*0.7), 0.6 * y0 + r * cos(-0.9*0.7) size 0.1,30 fixed lc rgb 'black' lw 3

plot f(0.25 * x0, 0.25 * x0, t), f(2. / 3. * y1, y0, t) lw 3 lc rgb 'black' not,\
     f(0.94 * 0.5 * x0, 7. / 12. * x0, t), f(0.98 * (y1 / 6. + sqrt(2.) / 4. * x0), sqrt(2.) / 3. * x0, t) lw 3 lc rgb 'black' not,\
     f(0.50 * x0, 2. /  3. * x0, t), f(y1 / 3., sqrt(2.) / 6. * x0, t) lw 1 lc rgb 'black' not,\
     f(0.50 * x0, 0.50 * x0, t), f(y1 / 6. + sqrt(2.) / 4. * x0, y0, t) lw 1 lc rgb 'black' not,\
     f(0.75 * x0, 0.75 * x0, t), f(0., y0, t) lw 1 lc rgb 'black' not,\
     f(0.75 * x0, 0.97 * 0.5 * x0, t), f(0., 1.06 * y1 / 3., t) lw 3 lc rgb 'black' not,\
     f(0.94 * 0.5 * x0, 0.25 * x0, t), f(1.04 * y1 / 3., 2. / 3. * y1,t) lw 3 lc rgb 'black' not,\
     f(0.94 * 0.5 * x0, 0.94 * 0.5 * x0, t), f(1.04 * y1 / 3., 0.99 * y0, t) lw 3 lc rgb 'black' not,\
     f(0.94 * 0.5 * x0, 0.97 * 2. / 3. * x0, t), f(1.04 * y1 / 3., 1.03 * sqrt(2.) / 6. * x0, t) lw 3 lc rgb 'black' not,\
     f(x0, x0, t), f(0., y0, t) lw 3 lc rgb 'black' not,\
     f(0.75 * x0, x0, t), f(0., 0., t) lw 3 lc rgb 'black' not,\
     f(0.25 * x0, x0, t), f(y0, y0, t) lw 3 lc rgb 'black' not,\
     f(0.25 * x0, 0.94 * 0.5 * x0, t), f(y0, 0.99 * y0, t) lw 3 lc rgb 'black' not,\
     f(7. / 12. * x0, 0.75 * x0, t), f(sqrt(2.) / 3. * x0, 0., t) lw 3 lc rgb 'black' not,\
     f(7. / 12. * x0, 0.97 * 2. / 3. * x0, t), f(sqrt(2.) / 3. * x0, 1.03 * sqrt(2.) / 6. * x0, t) lw 3 lc rgb 'black' not,\
     x0/4. + r * sin(0.9*f(-0.7, 0.7, t)), 0.6 * y0 + r * cos(0.9*f(-0.7, 0.7, t)) lw 3 lc rgb 'black' not
     

set terminal x11