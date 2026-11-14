---
title: "g_clustsize(1)"
name: "g_clustsize"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_clustsize/"
description: "g_clustsize – calculate size distributions of atomic clusters"
---

<h2>NAME</h2>
<p> g_clustsize &#8211; calculate size distributions of atomic clusters </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_clustsize</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> csize.xpm </i> <code>-ow</code><i> csizew.xpm </i> <code>-nc</code><i> nclust.xvg </i> <code>-mc</code><i> maxclust.xvg </i> <code>-ac</code><i> avclust.xvg </i> <code>-hc</code><i> histo-clust.xvg </i> <code>-temp</code><i> temp.xvg </i> <code>-mcn</code><i> maxclust.ndx </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-cut</code><i> real </i> <code>-[no]mol</code><i></i> <code>-[no]pbc</code><i></i> <code>-nskip</code><i> int </i> <code>-nlevels</code><i> int </i> <code>-ndf</code><i> int </i> <code>-rgblo</code><i> vector </i> <code>-rgbhi</code><i> vector </i></p>
<h2>DESCRIPTION</h2>
<p> This program computes the size distributions of molecular/atomic clusters in the gas phase. The output is given in the form of a XPM file. The total number of clusters is written to a XVG file. </p>
<p> When the <code> -mol</code> option is given clusters will be made out of molecules rather than atoms, which allows clustering of large molecules. In this case an index file would still contain atom numbers or your calculcation will die with a SEGV. </p>
<p> When velocities are present in your trajectory, the temperature of the largest cluster will be printed in a separate xvg file assuming that the particles are free to move. If you are using constraints, please correct the temperature. For instance water simulated with SHAKE or SETTLE will yield a temperature that is 1.5 times too low. You can compensate for this with the -ndf option. Remember to take the removal of center of mass motion into account. </p>
<p> The <code> -mc</code> option will produce an index file containing the atom numbers of the largest cluster.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Portable xdr run input file&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> csize.xpm</i> <code>Output</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-ow</code><i> csizew.xpm</i> <code>Output</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-nc</code><i> nclust.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-mc</code><i> maxclust.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ac</code><i> avclust.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-hc</code><i> histo-clust.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-temp</code><i> temp.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-mcn</code><i> maxclust.ndx</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
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
<p> <code>-cut</code><i> real</i><code> 0.35 </code><br />
&nbsp;<wbr>Largest distance&nbsp;<wbr>(nm)&nbsp;<wbr>to be considered in a cluster </p>
<p> <code>-[no]mol</code><i>no </i><br />
&nbsp;<wbr>Cluster molecules rather than atoms&nbsp;<wbr>(needs tpr file) </p>
<p> <code>-[no]pbc</code><i>yes </i><br />
&nbsp;<wbr>Use periodic boundary conditions </p>
<p> <code>-nskip</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of frames to skip between writing </p>
<p> <code>-nlevels</code><i> int</i><code> 20</code><br />
&nbsp;<wbr>Number of levels of grey in xpm output </p>
<p> <code>-ndf</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Number of degrees of freedom of the entire system for temperature calculation. If not set the number of atoms times three is used. </p>
<p> <code>-rgblo</code><i> vector</i><code> 1 1 0</code><br />
&nbsp;<wbr>RGB values for the color of the lowest occupied cluster size </p>
<p> <code>-rgbhi</code><i> vector</i><code> 0 0 1</code><br />
&nbsp;<wbr>RGB values for the color of the highest occupied cluster size </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
