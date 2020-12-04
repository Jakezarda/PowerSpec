reset

set size 0.75,0.75
set multiplot

#top panel
set size 1,0.75
set origin 0,0.25
set logscale y 10
set xrange [0.01:0.2]
unset xtics
plot 'averagePowerSpectrum.dat' w point pointtype 7 title "Average Power Spectrum", 'averagePowerSpectrum.dat' notitle w errorbars, 'inputPowerSpectrum.dat' title "Input Power Spectrum" w lines


#bottom panel
set xtics
unset logscale
set size 1,0.25
set origin 0,0
set xrange[0.01:0.2]
plot 'normalizedDifference.dat' title "Normalized Difference" w point pointtype 7, 'normalizedDifference.dat' notitle w errorbars

unset multiplot
