---
title: "g_trjcat(1)"
name: "g_trjcat"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_trjcat/"
description: "trjcat – concatenates trajectory files"
---

<h2>NAME</h2>
<p> trjcat &#8211; concatenates trajectory files </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>trjcat</code> <code>-f</code><i> traj.xtc </i> <code>-o</code><i> trajout.xtc </i> <code>-n</code><i> index.ndx </i> <code>-demux</code><i> remd.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-tu</code><i> enum </i> <code>-[no]xvgr</code><i></i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-prec</code><i> int </i> <code>-[no]vel</code><i></i> <code>-[no]settime</code><i></i> <code>-[no]sort</code><i></i> <code>-[no]keeplast</code><i></i> <code>-[no]cat</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> trjcat concatenates several input trajectory files in sorted order. In case of double time frames the one in the later file is used. By specifying <code> -settime</code> you will be asked for the start time of each file. The input files are taken from the command line, such that a command like <code> trjcat -o fixed.trr *.trr</code> should do the trick. Using <code> -cat</code> you can simply paste several files together without removal of frames with identical time stamps. </p>
<p> One important option is inferred when the output file is amongst the input files. In that case that particular file will be appended to which implies you do not need to store double the amount of data. Obviously the file to append to has to be the one with lowest starting time since one can only append at the end of a file. </p>
<p> If the <code> -demux</code> option is given, the N trajectories that are read, are written in another order as specified in the xvg file.The xvg file should contain something like: </p>
<p> 0 0 1 2 3 4 5 </p>
<p> 2 1 0 2 3 5 4 </p>
<p> Where the first number is the time, and subsequent numbers point to trajectory indices. The frames corresponding to the numbers present at the first line are collected into the output trajectory. If the number of frames in the trajectory does not match that in the xvg file then the program tries to be smart. Beware.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input, Mult.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-o</code><i> trajout.xtc</i> <code>Output, Mult.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-demux</code><i> remd.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-tu</code><i> enum</i><code> ps</code><br />
&nbsp;<wbr>Time unit:&nbsp;<wbr><code>&nbsp;<wbr>ps</code>,&nbsp;<wbr><code>&nbsp;<wbr>fs</code>,&nbsp;<wbr><code>&nbsp;<wbr>ns</code>,&nbsp;<wbr><code>&nbsp;<wbr>us</code>,&nbsp;<wbr><code>&nbsp;<wbr>ms</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>s</code> </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-b</code><i> time</i><code> -1 </code><br />
&nbsp;<wbr>First time to use&nbsp;<wbr>(ps) </p>
<p> <code>-e</code><i> time</i><code> -1 </code><br />
&nbsp;<wbr>Last time to use&nbsp;<wbr>(ps) </p>
<p> <code>-dt</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Only write frame when t MOD dt&nbsp;<wbr>=&nbsp;<wbr>first time&nbsp;<wbr>(ps) </p>
<p> <code>-prec</code><i> int</i><code> 3</code><br />
&nbsp;<wbr>Precision for .xtc and .gro writing in number of decimal places </p>
<p> <code>-[no]vel</code><i>yes </i><br />
&nbsp;<wbr>Read and write velocities if possible </p>
<p> <code>-[no]settime</code><i>no </i><br />
&nbsp;<wbr>Change starting time interactively </p>
<p> <code>-[no]sort</code><i>yes </i><br />
&nbsp;<wbr>Sort trajectory files&nbsp;<wbr>(not frames) </p>
<p> <code>-[no]keeplast</code><i>no </i><br />
&nbsp;<wbr>keep overlapping frames at end of trajectory </p>
<p> <code>-[no]cat</code><i>no </i><br />
&nbsp;<wbr>do not discard double time frames </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
