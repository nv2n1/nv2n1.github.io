---
title: "g_bundle(1)"
name: "g_bundle"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_bundle/"
description: "g_bundle – analyzes bundles of axes, e.g. helices"
---

<h2>NAME</h2>
<p> g_bundle &#8211; analyzes bundles of axes, e.g. helices </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_bundle</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-ol</code><i> bun_len.xvg </i> <code>-od</code><i> bun_dist.xvg </i> <code>-oz</code><i> bun_z.xvg </i> <code>-ot</code><i> bun_tilt.xvg </i> <code>-otr</code><i> bun_tiltr.xvg </i> <code>-otl</code><i> bun_tiltl.xvg </i> <code>-ok</code><i> bun_kink.xvg </i> <code>-okr</code><i> bun_kinkr.xvg </i> <code>-okl</code><i> bun_kinkl.xvg </i> <code>-oa</code><i> axes.pdb </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]xvgr</code><i></i> <code>-na</code><i> int </i> <code>-[no]z</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_bundle analyzes bundles of axes. The axes can be for instance helix axes. The program reads two index groups and divides both of them in <code> -na</code> parts. The centers of mass of these parts define the tops and bottoms of the axes. Several quantities are written to file: the axis length, the distance and the z-shift of the axis mid-points with respect to the average center of all axes, the total tilt, the radial tilt and the lateral tilt with respect to the average axis. </p>
<p> With options <code> -ok</code>, <code> -okr</code> and <code> -okl</code> the total, radial and lateral kinks of the axes are plotted. An extra index group of kink atoms is required, which is also divided into <code> -na</code> parts. The kink angle is defined as the angle between the kink-top and the bottom-kink vectors. </p>
<p> With option <code> -oa</code> the top, mid (or kink when <code> -ok</code> is set) and bottom points of each axis are written to a pdb file each frame. The residue numbers correspond to the axis numbers. When viewing this file with <code> rasmol</code>, use the command line option <code> -nmrpdb</code>, and type <code> set axis true</code> to display the reference axis.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-ol</code><i> bun_len.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-od</code><i> bun_dist.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oz</code><i> bun_z.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ot</code><i> bun_tilt.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-otr</code><i> bun_tiltr.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-otl</code><i> bun_tiltl.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ok</code><i> bun_kink.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-okr</code><i> bun_kinkr.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-okl</code><i> bun_kinkl.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oa</code><i> axes.pdb</i> <code>Output, Opt.</code><br />
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
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-na</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of axes </p>
<p> <code>-[no]z</code><i>no </i><br />
&nbsp;<wbr>Use the Z-axis as reference iso the average axis </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
