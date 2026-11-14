---
title: "g_filter_d(1)"
name: "g_filter_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_filter_d/"
description: "g_filter – frequency filters trajectories, useful for making smooth movies"
---

<h2>NAME</h2>
<p> g_filter &#8211; frequency filters trajectories, useful for making smooth movies </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_filter</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-ol</code><i> lowpass.xtc </i> <code>-oh</code><i> highpass.xtc </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-nf</code><i> int </i> <code>-[no]all</code><i></i> <code>-[no]nojump</code><i></i> <code>-[no]fit</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_filter performs frequency filtering on a trajectory. The filter shape is cos(pi t/A) + 1 from -A to +A, where A is given by the option <code> -nf</code> times the time step in the input trajectory. This filter reduces fluctuations with period A by 85%, with period 2*A by 50% and with period 3*A by 17% for low-pass filtering. Both a low-pass and high-pass filtered trajectory can be written. </p>
<p> Option <code> -ol</code> writes a low-pass filtered trajectory. A frame is written every <code> nf</code> input frames. This ratio of filter length and output interval ensures a good suppression of aliasing of high-frequency motion, which is useful for making smooth movies. Also averages of properties which are linear in the coordinates are preserved, since all input frames are weighted equally in the output. When all frames are needed, use the <code> -all</code> option. </p>
<p> Option <code> -oh</code> writes a high-pass filtered trajectory. The high-pass filtered coordinates are added to the coordinates from the structure file. When using high-pass filtering use <code> -fit</code> or make sure you use a trajectory which has been fitted on the coordinates in the structure file.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-ol</code><i> lowpass.xtc</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-oh</code><i> highpass.xtc</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
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
<p> <code>-nf</code><i> int</i><code> 10</code><br />
&nbsp;<wbr>Sets the filter length as well as the output interval for low-pass filtering </p>
<p> <code>-[no]all</code><i>no </i><br />
&nbsp;<wbr>Write all low-pass filtered frames </p>
<p> <code>-[no]nojump</code><i>yes </i><br />
&nbsp;<wbr>Remove jumps of atoms across the box </p>
<p> <code>-[no]fit</code><i>no </i><br />
&nbsp;<wbr>Fit all frames to a reference structure </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
