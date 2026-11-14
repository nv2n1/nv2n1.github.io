---
title: "g_tpbconv_d(1)"
name: "g_tpbconv_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_tpbconv_d/"
description: "tpbconv – makes a run input file for restarting a crashed run"
---

<h2>NAME</h2>
<p> tpbconv &#8211; makes a run input file for restarting a crashed run </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>tpbconv</code> <code>-s</code><i> topol.tpr </i> <code>-f</code><i> traj.trr </i> <code>-e</code><i> ener.edr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> tpxout.tpr </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-nsteps</code><i> int </i> <code>-runtime</code><i> real </i> <code>-time</code><i> real </i> <code>-extend</code><i> real </i> <code>-until</code><i> real </i> <code>-[no]zeroq</code><i></i> <code>-[no]cont</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> tpbconv can edit run input files in four ways. </p>
<p> <code> 1st.</code> by modifying the number of steps in a run input file with option <code> -nsteps</code> or option <code> -runtime</code>. </p>
<p> <code> 2st.</code> (OBSOLETE) by creating a run input file for a continuation run when your simulation has crashed due to e.g. a full disk, or by making a continuation run input file. This option is obsolete, since mdrun now writes and reads checkpoint files. Note that a frame with coordinates and velocities is needed. When pressure and/or Nose-Hoover temperature coupling is used an energy file can be supplied to get an exact continuation of the original run. </p>
<p> <code> 3nd.</code> by creating a tpx file for a subset of your original tpx file, which is useful when you want to remove the solvent from your tpx file, or when you want to make e.g. a pure Ca tpx file. <code> WARNING: this tpx file is not fully functional</code>. <code> 4rd.</code> by setting the charges of a specified group to zero. This is useful when doing free energy estimates using the LIE (Linear Interaction Energy) method.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.trr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<p> <code>-e</code><i> ener.edr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> tpxout.tpr</i> <code>Output</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-nsteps</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Change the number of steps </p>
<p> <code>-runtime</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Set the run time&nbsp;<wbr>(ps) </p>
<p> <code>-time</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Continue from frame at this time&nbsp;<wbr>(ps)&nbsp;<wbr>instead of the last frame </p>
<p> <code>-extend</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Extend runtime by this amount&nbsp;<wbr>(ps) </p>
<p> <code>-until</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Extend runtime until this ending time&nbsp;<wbr>(ps) </p>
<p> <code>-[no]zeroq</code><i>no </i><br />
&nbsp;<wbr>Set the charges of a group&nbsp;<wbr>(from the index)&nbsp;<wbr>to zero </p>
<p> <code>-[no]cont</code><i>yes </i><br />
&nbsp;<wbr>For exact continuation, the constraints should not be solved before the first step </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
