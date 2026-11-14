---
title: "g_msd(1)"
name: "g_msd"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_msd/"
description: "g_msd – calculates mean square displacements"
---

<h2>NAME</h2>
<p> g_msd &#8211; calculates mean square displacements </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_msd</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> msd.xvg </i> <code>-mol</code><i> diff_mol.xvg </i> <code>-pdb</code><i> diff_mol.pdb </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-type</code><i> enum </i> <code>-lateral</code><i> enum </i> <code>-[no]ten</code><i></i> <code>-ngroup</code><i> int </i> <code>-[no]mw</code><i></i> <code>-[no]rmcomm</code><i></i> <code>-tpdb</code><i> time </i> <code>-trestart</code><i> time </i> <code>-beginfit</code><i> time </i> <code>-endfit</code><i> time </i></p>
<h2>DESCRIPTION</h2>
<p> g_msd computes the mean square displacement (MSD) of atoms from their initial positions. This provides an easy way to compute the diffusion constant using the Einstein relation. The time between additional starting points for the MSD calculation is set with <code> -trestart</code>. The diffusion constant is calculated by least squares fitting a straight line through the MSD from <code> -beginfit</code> to <code> -endfit</code>. An error estimate given, which is the difference of the diffusion coefficients obtained from fits over the two halfs of the fit interval. </p>
<p> There are three, mutually exclusive, options to determine different types of mean square displacement: <code> -type</code>, <code> -lateral</code> and <code> -ten</code>. Option <code> -ten</code> writes the full MSD tensor for each group, the order in the output is: trace xx yy zz yx zx zy. </p>
<p> Option <code> -mol</code> plots the MSD for molecules, this implies With option <code> -rmcomm</code> center of mass motion can be removed. For trajectories produced with GROMACS this is usually not necessary as mdrun usually already removes the center of mass motion. When you use this option be sure that the whole system is stored in the trajectory file. </p>
<p> <code> -mw</code>, i.e. for each inidividual molecule an diffusion constant is computed for its center of mass. The chosen index group will be split into molecules. The diffusion coefficient is determined by linear regression of the MSD, where, unlike for the normal output of D, the times are weighted according to the number of restart point, i.e. short times have a higher weight. Also when <code> -beginfit</code>=-1,fitting starts at 0 and when <code> -endfit</code>=-1, fitting goes to the end. Using this option one also gets an accurate error estimate based on the statistics between individual molecules. Note that this diffusion coefficient and error estimate are only accurate when the MSD is completely linear between <code> -beginfit</code> and <code> -endfit</code>. </p>
<p> Option <code> -pdb</code> writes a pdb file with the coordinates of the frame at time <code> -tpdb</code> with in the B-factor field the square root of the diffusion coefficient of the molecule. This option implies option <code> -mol</code>.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> msd.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-mol</code><i> diff_mol.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-pdb</code><i> diff_mol.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
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
<p> <code>-tu</code><i> enum</i><code> ps</code><br />
&nbsp;<wbr>Time unit:&nbsp;<wbr><code>&nbsp;<wbr>ps</code>,&nbsp;<wbr><code>&nbsp;<wbr>fs</code>,&nbsp;<wbr><code>&nbsp;<wbr>ns</code>,&nbsp;<wbr><code>&nbsp;<wbr>us</code>,&nbsp;<wbr><code>&nbsp;<wbr>ms</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>s</code> </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-type</code><i> enum</i><code> no</code><br />
&nbsp;<wbr>Compute diffusion coefficient in one direction:&nbsp;<wbr><code>&nbsp;<wbr>no</code>,&nbsp;<wbr><code>&nbsp;<wbr>x</code>,&nbsp;<wbr><code>&nbsp;<wbr>y</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>z</code> </p>
<p> <code>-lateral</code><i> enum</i><code> no</code><br />
&nbsp;<wbr>Calculate the lateral diffusion in a plane perpendicular to:&nbsp;<wbr><code>&nbsp;<wbr>no</code>,&nbsp;<wbr><code>&nbsp;<wbr>x</code>,&nbsp;<wbr><code>&nbsp;<wbr>y</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>z</code> </p>
<p> <code>-[no]ten</code><i>no </i><br />
&nbsp;<wbr>Calculate the full tensor </p>
<p> <code>-ngroup</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Number of groups to calculate MSD for </p>
<p> <code>-[no]mw</code><i>yes </i><br />
&nbsp;<wbr>Mass weighted MSD </p>
<p> <code>-[no]rmcomm</code><i>no </i><br />
&nbsp;<wbr>Remove center of mass motion </p>
<p> <code>-tpdb</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>The frame to use for option -pdb&nbsp;<wbr>(ps) </p>
<p> <code>-trestart</code><i> time</i><code> 10 </code><br />
&nbsp;<wbr>Time between restarting points in trajectory&nbsp;<wbr>(ps) </p>
<p> <code>-beginfit</code><i> time</i><code> -1 </code><br />
&nbsp;<wbr>Start time for fitting the MSD&nbsp;<wbr>(ps), -1 is 10% </p>
<p> <code>-endfit</code><i> time</i><code> -1 </code><br />
&nbsp;<wbr>End time for fitting the MSD&nbsp;<wbr>(ps), -1 is 90% </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
