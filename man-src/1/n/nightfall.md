---
title: "nightfall(1)"
name: "nightfall"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nightfall/"
description: "nightfall – binary star astronomy"
---

<h2>NAME</h2>
<p> nightfall &#8211; binary star astronomy</p>
<h2>SYNOPSIS</h2>
<p> <code>nightfall </code> -h<br />
 <code>nightfall </code> -U [more options] [<i>mass_ratio</i> <i>inclination </i> <i>primary_size secondary_size </i> <i>primary_temperature </i> <i>secondary_temperature]</i><br />
 <code>nightfall </code> [-G] [-A] [more options] <i>mass_ratio inclination </i> <i>primary_size secondary_size </i> <i>primary_temperature secondary_temperature</i><br />
 <code>nightfall </code> [-G | -U] [-A] [more options] -C <i>file </i> </p>
<h2>DESCRIPTION</h2>
<p> <code>nightfall</code> is an interactive astronomy program for fun, education and science. It can generate animated views of eclipsing (or non-eclipsing) binary stars, compute light curves and radial velocity curves, and determine best-fit models for observational data. </p>
<p> In the simplest case, <code>nightfall</code> computes the light curve for a binary star system with some given <i>mass_ratio</i> (mass of secondary star/mass of primary star), <i>inclination</i> (0 = plane-on view, 90 = edge-on view of the orbital plane), stellar sizes <i>primary_size,secondary_size</i> (dimensionless, in the range 0 &#8211; 1.3), and stellar temperatures <i>primary_temperature,secondary_temperature</i> (in Kelvin), and writes the light curve to a file <i>NightfallCurve.dat</i>. </p>
<p> <code>nightfall</code> is able to show many non-trivial, and sometimes spectacular, physical effecs in binary stars, as it uses a detailed physical model rather than simply assuming the stars to be spherical. </p>
<p> The full documentation for <code>nightfall</code> is distributed only in DVI and HTML format, as it is quite big, and thus not very well suited to the &#8216;man&#8217; page format. It includes some discussion of binary stars (at a popular science level, hopefully) that you may find helpful in understanding what the program does. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h</i></p>
<dd> Print a usage message on standard output and exit successfully.</p>
<dt><i>-U</i></p>
<dd> Run in interactive mode.</p>
<dt><i>-C file</i></p>
<dd> Use binary star parameters from a configuration file instead of giving them on the command line. Sample configuration files are in <i>share/nightfall/cfg</i>.</p>
<dt><i>-G</i>[<i>P</i>|<i>S</i>|<i>1</i>|<i>2</i>]</p>
<dd> Plot a graph of the lightcurve after its computation (<i>P</i>|<i>S</i> &#8211; zoom on primary/secondary eclipse, <i>1</i>|<i>2</i> &#8211; plot 1/2 orbits).</p>
<dt><i>-A</i></p>
<dd> Generate an animated view of the binary star.</p>
<dt><i>-V</i>[<i>v</i>|<i>i</i>|<i>c</i>|<i>a</i>]</p>
<dd> Visualize the geometry of the binary star system (<i>v</i> &#8211; view of the stars, <i>i</i> &#8211; image of the potential, <i>c </i> &#8211; contour plot of the potential, <i>a</i> &#8211; all of them).</p>
<dt><i>-H</i></p>
<dd> Send plot to a postscript file. If the postscript file exists, it will be overwritten.</p>
<dt><i>-B[U|B|V|I|R|J|H|K|u|v|b|y|1|2]</i></p>
<dd> Select the filter/bandpass for which the lightcurve should be plotted. <i>U</i>&#8211;<i>K</i> range from ultraviolett to infrared, best match to the human eye is V. <i>u</i>&#8211;<i>y</i> are narrow-band filters. <i>1</i>|<i>2</i> will select radial velocity curves instead of a light curve.</p>
<dt><i>-fP/-fS value</i></p>
<dd> By default, <code>nightfall </code> assumes synchroneous rotation, which means that the stars are rotating with the orbital period, and thus show each other always the same &#8216;side&#8217;. With this option, you can set the ratio of stellar rotation frequency to orbital frequency to some <i>value </i> different from one, seperately for the primary <i>P</i> and the secondary <i>S</i>.</p>
<dt><i>-e eccentricity periastron_length</i></p>
<dd> By default, <code>nightfall </code> assumes the orbit to be circular. With this option, you can set the <i>eccentricity</i> of the orbit (0 is circular, maximum is less than 1), and the <i>periastron length</i>, which is the point of closest approach of the two stars in their orbit (0 &#8211; 360 degree).</p>
<dt><i>-sP/-sS longitude latitude radius dimfactor</i></p>
<dd> Place a spot on the primary (<i>P</i>) or secondary (<i>S</i>). The spot parameters are the location of the spot (<i>longitude</i>,<i>latitude</i>), its <i>radius</i>, and the <i>dimfactor</i> by which the temperature is reduced (or increased) within the spot area.</p>
<dt><i>-tP/-tM/-tD value</i></p>
<dd> Set the absolute value for the orbital period <i>P</i> (in days), the total mass <i>M</i> (in units of solar masses), and/or the orbital separation <i>D </i> (in solar radii) of the system. Any two of these are independent, the third is then calculated from Kepler&#8217;s laws (i.e., you should set only two of these).</p>
<dt><i>-I file</i></p>
<dd> Read in observational data from a data file. Sample data files are in <i>share/nightfall/data</i>.</p>
<dt><i>-D[vwb]</i></p>
<dd> Diagnostic output (<i>v</i> &#8211; verbose, <i>w</i> &#8211; warnings, <i>b</i> &#8211; status messages).</dl>
<h2>NOTES</h2>
<p> The definition of primary/secondary is inverse to the usual convention in astronomy. </p>
<p> Obviously, the size of a star in a binary system is limited by the orbital separation of the two stars. Instead of having to calculate the maximum useful stellar size herself, the user simply gives the desired stellar size as a fraction (0.001-1.3) of the maximum <i>polar</i> radius of the star (which is calculated by the program). In the output file <i>NightfallCurve.dat</i>, you will then find the &#8216;real&#8217; size of the star(s). </p>
<p> If no absolute values for total mass and orbital period/separation are given, the program will use some default values (mass = two solar masses, orbital separation = distance earth-sun). In this case, <i>sizes/masses/velocities given in absolute units</i> (e.g. kg, m, m/s, solar masses/radii) are <i>fictuous</i> only &#8211; they would be valid only for a system with the assumed default values of total mass and orbital separation. </p>
<p> The newest version of <code>nightfall</code> can be found on <i><a href="ftp://metalab.unc.edu/pub/Linux/science/astronomy">ftp://metalab.unc.edu/pub/Linux/science/astronomy</a></i>, and on the homepage <i><a rel="nofollow" href="http://www.lsw.uni-heidelberg.de/~rwichman/Nightfall.html">http://www.lsw.uni-heidelberg.de/~rwichman/Nightfall.html</a></i>. </p>
<p> To subscribe to the nightfall mailing list, send mail to <i>majordomo [at] seul.org</i> with a body of <i>subscribe </i> <i>nightfall-l</i>. </p>
<h2>AUTHOR</h2>
<p> Rainer Wichmann (rwichmann [at] hs.uni-hamburg.de) </p>
<h2>BUG REPORTS</h2>
<p> If you find a bug in <code>nightfall</code>, please send electronic mail to <i>rwichmann [at] hs.uni-hamburg.de</i>. Please include your operating system and its revision, the version of <code>nightfall</code>, what C compiler you used to compile it, and the output from &#8216;configure&#8217;. </p>
<h2>Index</h2>
