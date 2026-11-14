---
title: "g_vanhove(1)"
name: "g_vanhove"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_vanhove/"
description: "g_vanhove – calculates Van Hove displacement functions"
---

<h2>NAME</h2>
<p> g_vanhove &#8211; calculates Van Hove displacement functions </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_vanhove</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-om</code><i> vanhove.xpm </i> <code>-or</code><i> vanhove_r.xvg </i> <code>-ot</code><i> vanhove_t.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-sqrt</code><i> real </i> <code>-fm</code><i> int </i> <code>-rmax</code><i> real </i> <code>-rbin</code><i> real </i> <code>-mmax</code><i> real </i> <code>-nlevels</code><i> int </i> <code>-nr</code><i> int </i> <code>-fr</code><i> int </i> <code>-rt</code><i> real </i> <code>-ft</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> g_vanhove computes the Van Hove correlation function. The Van Hove G(r,t) is the probability that a particle that is at r0 at time zero can be found at position r0+r at time t. g_vanhove determines G not for a vector r, but for the length of r. Thus it gives the probability that a particle moves a distance of r in time t. Jumps across the periodic boundaries are removed. Corrections are made for scaling due to isotropic or anisotropic pressure coupling. </p>
<p> With option <code> -om</code> the whole matrix can be written as a function of t and r or as a function of sqrt(t) and r (option <code> -sqrt</code>). </p>
<p> With option <code> -or</code> the Van Hove function is plotted for one or more values of t. Option <code> -nr</code> sets the number of times, option <code> -fr</code> the number spacing between the times. The binwidth is set with option <code> -rbin</code>. The number of bins is determined automatically. </p>
<p> With option <code> -ot</code> the integral up to a certain distance (option <code> -rt</code>) is plotted as a function of time. </p>
<p> For all frames that are read the coordinates of the selected particles are stored in memory. Therefore the program may use a lot of memory. For options <code> -om</code> and <code> -ot</code> the program may be slow. This is because the calculation scales as the number of frames times <code> -fm</code> or <code> -ft</code>. Note that with the <code> -dt</code> option the memory usage and calculation time can be reduced.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-om</code><i> vanhove.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-or</code><i> vanhove_r.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ot</code><i> vanhove_t.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-b</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>First frame&nbsp;<wbr>(ps)&nbsp;<wbr>to read from trajectory </p>
<p> <code>-e</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Last frame&nbsp;<wbr>(ps)&nbsp;<wbr>to read from trajectory </p>
<p> <code>-dt</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Only use frame when t MOD dt&nbsp;<wbr>=&nbsp;<wbr>first time&nbsp;<wbr>(ps) </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-sqrt</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Use sqrt(t)&nbsp;<wbr>on the matrix axis which binspacing&nbsp;<wbr>&nbsp;<wbr>in sqrt(ps) </p>
<p> <code>-fm</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of frames in the matrix, 0 is plot all </p>
<p> <code>-rmax</code><i> real</i><code> 2 </code><br />
&nbsp;<wbr>Maximum r in the matrix&nbsp;<wbr>(nm) </p>
<p> <code>-rbin</code><i> real</i><code> 0.01 </code><br />
&nbsp;<wbr>Binwidth in the matrix and for -or&nbsp;<wbr>(nm) </p>
<p> <code>-mmax</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum density in the matrix, 0 is calculate&nbsp;<wbr>(1/nm) </p>
<p> <code>-nlevels</code><i> int</i><code> 81</code><br />
&nbsp;<wbr>Number of levels in the matrix </p>
<p> <code>-nr</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Number of curves for the -or output </p>
<p> <code>-fr</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Frame spacing for the -or output </p>
<p> <code>-rt</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Integration limit for the -ot output&nbsp;<wbr>(nm) </p>
<p> <code>-ft</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of frames in the -ot output, 0 is plot all </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
