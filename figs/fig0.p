set output "test.tex"
set terminal epslatex

set para
set tr [0:1]
set size ratio -1

unset border
unset tic

plot 11.7/8., 8.3 * t lw 1 lc rgb 'black' not,\
     11.7/4., 8.3 * t lw 1 lc rgb 'black' not,\
     3. * 11.7/8., 8.3 * t lw 1 lc rgb 'black' not,\
     11.7/2., 8.3 * t lw 1 lc rgb 'black' not,\
     5. * 11.7/8., 8.3 * t lw 1 lc rgb 'black' not,\
     3. * 11.7/4., 8.3 * t lw 1 lc rgb 'black' not,\
     7. * 11.7 / 8., 8.3 / 4. * (1. + 3. * t) lw 1 lc rgb 'black' not,\
     11.7 * t, 3. * 8.3 / 4. lw 1 lc rgb 'black' not,\
     11.7 * t, 8.3 / 2. lw 1 lc rgb 'black' not,\
     7. * 11.7 / 8. * t, 8.3 / 4. lw 1 lc rgb 'black' not,\
     0, 8.3 * t lw 3 lc rgb 'black' not,\
     11.7, 8.3 / 4. * (1. + 3. * t) lw 3 lc rgb 'black' not,\
     7. * 11.7 / 8., 8.3 / 4. * t lw 3 lc rgb 'black' not,\
     7. * 11.7 / 8. * t,0 lw 3 lc rgb 'black' not,\
     11.7 / 8. * (7. + t), 8.3 / 4. lw 3 lc rgb 'black' not,\
     11.7 * t,8.3 lw 3 lc rgb 'black' not,\
     11.7 / 8. * (7. + t) + 0.25, -0.25 lw 3 lc rgb 'black' not,\
     11.7 / 8. * (7. + t) + 0.25, 8.3 / 4. - 0.25 lw 3 lc rgb 'black' not,\
     7. * 11.7 / 8. + 0.25 , 8.3 / 4. * t - 0.25 lw 3 lc rgb 'black' not,\
     11.7 + 0.25, 8.3 / 4. * t - 0.25 lw 3 lc rgb 'black' not

     

set terminal x11
