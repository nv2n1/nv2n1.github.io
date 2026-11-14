---
title: "g_current(1)"
name: "g_current"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_current/"
description: "g_current – calculates dielectric constants for charged systems"
---

<h2>NAME</h2>
<p> g_current &#8211; calculates dielectric constants for charged systems </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_current</code> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-f</code><i> traj.xtc </i> <code>-o</code><i> current.xvg </i> <code>-caf</code><i> caf.xvg </i> <code>-dsp</code><i> dsp.xvg </i> <code>-md</code><i> md.xvg </i> <code>-mj</code><i> mj.xvg </i> <code>-mc</code><i> mc.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-sh</code><i> int </i> <code>-[no]nojump</code><i></i> <code>-eps</code><i> real </i> <code>-bfit</code><i> real </i> <code>-efit</code><i> real </i> <code>-bvit</code><i> real </i> <code>-evit</code><i> real </i> <code>-tr</code><i> real </i> <code>-temp</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> This is a tool for calculating the current autocorrelation function, the correlation of the rotational and translational dipole moment of the system, and the resulting static dielectric constant. To obtain a reasonable result the index group has to be neutral. Furthermore the routine is capable of extracting the static conductivity from the current autocorrelation function, if velocities are given. Additionally an Einstein-Helfand fit also allows to get the static conductivity. </p>
<p> The flag <code> -caf</code> is for the output of the current autocorrelation function and <code> -mc</code> writes the correlation of the rotational and translational part of the dipole moment in the corresponding file. However this option is only available for trajectories containing velocities.Options <code> -sh</code> and <code> -tr</code> are responsible for the averaging and integration of the autocorrelation functions. Since averaging proceeds by shifting the starting point through the trajectory, the shift can be modified with <code> -sh</code> to enable the choice of uncorrelated starting points. Towards the end, statistical inaccuracy grows and integrating the correlation function only yields reliable values until a certain point, depending on the number of frames. The option <code> -tr</code> controls the region of the integral taken into account for calculating the static dielectric constant. </p>
<p> Option <code> -temp</code> sets the temperature required for the computation of the static dielectric constant. </p>
<p> Option <code> -eps</code> controls the dielectric constant of the surrounding medium for simulations using a Reaction Field or dipole corrections of the Ewald summation (eps=0 corresponds to tin-foil boundary conditions). </p>
<p> <code> -[no]nojump</code> unfolds the coordinates to allow free diffusion. This is required to get a continuous translational dipole moment, required for the Einstein-Helfand fit. The resuls from the fit allow to determine the dielectric constant for system of charged molecules. However it is also possible to extract the dielectric constant from the fluctuations of the total dipole moment in folded coordinates. But this options has to be used with care, since only very short time spans fulfill the approximation, that the density of the molecules is approximately constant and the averages are already converged. To be on the safe side, the dielectric constant should be calculated with the help of the Einstein-Helfand method for the translational part of the dielectric constant.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-o</code><i> current.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-caf</code><i> caf.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dsp</code><i> dsp.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-md</code><i> md.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-mj</code><i> mj.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-mc</code><i> mc.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
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
<p> <code>-sh</code><i> int</i><code> 1000</code><br />
&nbsp;<wbr>Shift of the frames for averaging the correlation functions and the mean-square displacement. </p>
<p> <code>-[no]nojump</code><i>yes </i><br />
&nbsp;<wbr>Removes jumps of atoms across the box. </p>
<p> <code>-eps</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Dielectric constant of the surrounding medium. eps=0.0 corresponds to eps=infinity&nbsp;<wbr>(thinfoil boundary conditions). </p>
<p> <code>-bfit</code><i> real</i><code> 100 </code><br />
&nbsp;<wbr>Begin of the fit of the straight line to the MSD of the translational fraction of the dipole moment. </p>
<p> <code>-efit</code><i> real</i><code> 400 </code><br />
&nbsp;<wbr>End of the fit of the straight line to the MSD of the translational fraction of the dipole moment. </p>
<p> <code>-bvit</code><i> real</i><code> 0.5 </code><br />
&nbsp;<wbr>Begin of the fit of the current autocorrelation function to a*tb. </p>
<p> <code>-evit</code><i> real</i><code> 5 </code><br />
&nbsp;<wbr>End of the fit of the current autocorrelation function to a*tb. </p>
<p> <code>-tr</code><i> real</i><code> 0.25 </code><br />
&nbsp;<wbr>Fraction of the trajectory taken into account for the integral. </p>
<p> <code>-temp</code><i> real</i><code> 300 </code><br />
&nbsp;<wbr>Temperature for calculating epsilon. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
