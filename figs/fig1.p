set output "test.tex"
set terminal epslatex

set para
set tr [0:1]
set size ratio -1

unset border
unset tic

x0 = 11.7 / 8.
y0 = 8.3 / 4.

f(x1,x2,t) = x1 + (x2 - x1) * t

plot f(0.25 * x0, 0.25 * x0, t), f(0., y0, t) lw 4 lc rgb 'black' dt 6 not,\
     f(0.50 * x0, 0.50 * x0, t), f(0., y0, t) lw 4 lc rgb 'black' dt 6 not,\
     f(0.75 * x0, 0.75 * x0, t), f(0., y0, t) lw 4 lc rgb 'black' dt 6 not,\
     f(0., 0., t), f(0., y0, t) lw 3 lc rgb 'black' not,\
     f(x0, x0, t), f(0., y0, t) lw 3 lc rgb 'black' not,\
     f(0., x0, t), f(0., 0., t) lw 3 lc rgb 'black' not,\
     f(0., x0, t), f(y0, y0, t) lw 3 lc rgb 'black' not
     

set terminal x11
