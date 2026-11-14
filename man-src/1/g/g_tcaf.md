---
title: "g_tcaf(1)"
name: "g_tcaf"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_tcaf/"
description: "g_tcaf – calculates viscosities of liquids"
---

<h2>NAME</h2>
<p> g_tcaf &#8211; calculates viscosities of liquids </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_tcaf</code> <code>-f</code><i> traj.trr </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-ot</code><i> transcur.xvg </i> <code>-oa</code><i> tcaf_all.xvg </i> <code>-o</code><i> tcaf.xvg </i> <code>-of</code><i> tcaf_fit.xvg </i> <code>-oc</code><i> tcaf_cub.xvg </i> <code>-ov</code><i> visc_k.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]mol</code><i></i> <code>-[no]k34</code><i></i> <code>-wt</code><i> real </i> <code>-acflen</code><i> int </i> <code>-[no]normalize</code><i></i> <code>-P</code><i> enum </i> <code>-fitfn</code><i> enum </i> <code>-ncskip</code><i> int </i> <code>-beginfit</code><i> real </i> <code>-endfit</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_tcaf computes tranverse current autocorrelations. These are used to estimate the shear viscosity eta. For details see: Palmer, JCP 49 (1994) pp 359-366. </p>
<p> Transverse currents are calculated using the k-vectors (1,0,0) and (2,0,0) each also in the y- and z-direction, (1,1,0) and (1,-1,0) each also in the 2 other plains (these vectors are not independent) and (1,1,1) and the 3 other box diagonals (also not independent). For each k-vector the sine and cosine are used, in combination with the velocity in 2 perpendicular directions. This gives a total of 16*2*2=64 transverse currents. One autocorrelation is calculated fitted for each k-vector, which gives 16 tcaf&#8217;s. Each of these tcaf&#8217;s is fitted to f(t) = exp(-v)(cosh(Wv) + 1/W sinh(Wv)), v = -t/(2 tau), W = sqrt(1 &#8211; 4 tau eta/rho k2), which gives 16 tau&#8217;s and eta&#8217;s. The fit weights decay with time as exp(-t/wt), the tcaf and fit are calculated up to time 5*wt. The eta&#8217;s should be fitted to 1 &#8211; a eta(k) k2, from which one can estimate the shear viscosity at k=0. </p>
<p> When the box is cubic, one can use the option <code> -oc</code>, which averages the tcaf&#8217;s over all k-vectors with the same length. This results in more accurate tcaf&#8217;s. Both the cubic tcaf&#8217;s and fits are written to <code> -oc</code> The cubic eta estimates are also written to <code> -ov</code>. </p>
<p> With option <code> -mol</code> the transverse current is determined of molecules instead of atoms. In this case the index group should consist of molecule numbers instead of atom numbers. </p>
<p> The k-dependent viscosities in the <code> -ov</code> file should be fitted to eta(k) = eta0 (1 &#8211; a k2) to obtain the viscosity at infinite wavelength. </p>
<p> NOTE: make sure you write coordinates and velocities often enough. The initial, non-exponential, part of the autocorrelation function is very important for obtaining a good fit.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.trr</i> <code>Input</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-ot</code><i> transcur.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oa</code><i> tcaf_all.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-o</code><i> tcaf.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-of</code><i> tcaf_fit.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oc</code><i> tcaf_cub.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ov</code><i> visc_k.xvg</i> <code>Output</code><br />
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
<p> <code>-[no]mol</code><i>no </i><br />
&nbsp;<wbr>Calculate tcaf of molecules </p>
<p> <code>-[no]k34</code><i>no </i><br />
&nbsp;<wbr>Also use k=(3,0,0)&nbsp;<wbr>and k=(4,0,0) </p>
<p> <code>-wt</code><i> real</i><code> 5 </code><br />
&nbsp;<wbr>Exponential decay time for the TCAF fit weights </p>
<p> <code>-acflen</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Length of the ACF, default is half the number of frames </p>
<p> <code>-[no]normalize</code><i>yes </i><br />
&nbsp;<wbr>Normalize ACF </p>
<p> <code>-P</code><i> enum</i><code> 0</code><br />
&nbsp;<wbr>Order of Legendre polynomial for ACF&nbsp;<wbr>(0 indicates none):&nbsp;<wbr><code>&nbsp;<wbr>0</code>,&nbsp;<wbr><code>&nbsp;<wbr>1</code>,&nbsp;<wbr><code>&nbsp;<wbr>2</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>3</code> </p>
<p> <code>-fitfn</code><i> enum</i><code> none</code><br />
&nbsp;<wbr>Fit function:&nbsp;<wbr><code>&nbsp;<wbr>none</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp</code>,&nbsp;<wbr><code>&nbsp;<wbr>aexp</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp_exp</code>,&nbsp;<wbr><code>&nbsp;<wbr>vac</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp5</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp7</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>exp9</code> </p>
<p> <code>-ncskip</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Skip N points in the output file of correlation functions </p>
<p> <code>-beginfit</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Time where to begin the exponential fit of the correlation function </p>
<p> <code>-endfit</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Time where to end the exponential fit of the correlation function, -1 is till the end </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
