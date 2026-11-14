---
title: "g_traj_d(1)"
name: "g_traj_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_traj_d/"
description: "g_traj – plots x, v and f of selected atoms/groups (and more) from a trajectory"
---

<h2>NAME</h2>
<p> g_traj &#8211; plots x, v and f of selected atoms/groups (and more) from a trajectory </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_traj</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-ox</code><i> coord.xvg </i> <code>-oxt</code><i> coord.xtc </i> <code>-ov</code><i> veloc.xvg </i> <code>-of</code><i> force.xvg </i> <code>-ob</code><i> box.xvg </i> <code>-ot</code><i> temp.xvg </i> <code>-ekt</code><i> ektrans.xvg </i> <code>-ekr</code><i> ekrot.xvg </i> <code>-vd</code><i> veldist.xvg </i> <code>-cv</code><i> veloc.pdb </i> <code>-cf</code><i> force.pdb </i> <code>-av</code><i> all_veloc.xvg </i> <code>-af</code><i> all_force.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]com</code><i></i> <code>-[no]mol</code><i></i> <code>-[no]nojump</code><i></i> <code>-[no]x</code><i></i> <code>-[no]y</code><i></i> <code>-[no]z</code><i></i> <code>-ng</code><i> int </i> <code>-[no]len</code><i></i> <code>-bin</code><i> real </i> <code>-scale</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_traj plots coordinates, velocities, forces and/or the box. With <code> -com</code> the coordinates, velocities and forces are calculated for the center of mass of each group. When <code> -mol</code> is set, the numbers in the index file are interpreted as molecule numbers and the same procedure as with <code> -com</code> is used for each molecule. </p>
<p> Option <code> -ot</code> plots the temperature of each group, provided velocities are present in the trajectory file. No corrections are made for constrained degrees of freedom! This implies <code> -com</code>. </p>
<p> Options <code> -ekt</code> and <code> -ekr</code> plot the translational and rotational kinetic energy of each group, provided velocities are present in the trajectory file. This implies <code> -com</code>. </p>
<p> Options <code> -cv</code> and <code> -cf</code> write the average velocities and average forces as temperature factors to a pdb file with the average coordinates. The temperature factors are scaled such that the maximum is 10. The scaling can be changed with the option <code> -scale</code>. To get the velocities or forces of one frame set both <code> -b</code> and <code> -e</code> to the time of desired frame. When averaging over frames you might need to use the <code> -nojump</code> option to obtain the correct average coordinates. If you select either of these option the average force and velocity for each atom are written to an xvg file as well (specified with <code> -av</code> or <code> -af</code>). </p>
<p> Option <code> -vd</code> computes a velocity distribution, i.e. the norm of the vector is plotted. In addition in the same graph the kinetic energy distribution is given.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-ox</code><i> coord.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oxt</code><i> coord.xtc</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-ov</code><i> veloc.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-of</code><i> force.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ob</code><i> box.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ot</code><i> temp.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ekt</code><i> ektrans.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ekr</code><i> ekrot.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-vd</code><i> veldist.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-cv</code><i> veloc.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-cf</code><i> force.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-av</code><i> all_veloc.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-af</code><i> all_force.xvg</i> <code>Output, Opt.</code><br />
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
<p> <code>-tu</code><i> enum</i><code> ps</code><br />
&nbsp;<wbr>Time unit:&nbsp;<wbr><code>&nbsp;<wbr>ps</code>,&nbsp;<wbr><code>&nbsp;<wbr>fs</code>,&nbsp;<wbr><code>&nbsp;<wbr>ns</code>,&nbsp;<wbr><code>&nbsp;<wbr>us</code>,&nbsp;<wbr><code>&nbsp;<wbr>ms</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>s</code> </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]com</code><i>no </i><br />
&nbsp;<wbr>Plot data for the com of each group </p>
<p> <code>-[no]mol</code><i>no </i><br />
&nbsp;<wbr>Index contains molecule numbers iso atom numbers </p>
<p> <code>-[no]nojump</code><i>no </i><br />
&nbsp;<wbr>Remove jumps of atoms across the box </p>
<p> <code>-[no]x</code><i>yes </i><br />
&nbsp;<wbr>Plot X-component </p>
<p> <code>-[no]y</code><i>yes </i><br />
&nbsp;<wbr>Plot Y-component </p>
<p> <code>-[no]z</code><i>yes </i><br />
&nbsp;<wbr>Plot Z-component </p>
<p> <code>-ng</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Number of groups to consider </p>
<p> <code>-[no]len</code><i>no </i><br />
&nbsp;<wbr>Plot vector length </p>
<p> <code>-bin</code><i> real</i><code> 1 </code><br />
&nbsp;<wbr>Binwidth for velocity histogram&nbsp;<wbr>(nm/ps) </p>
<p> <code>-scale</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Scale factor for pdb output, 0 is autoscale </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
