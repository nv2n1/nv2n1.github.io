---
title: "g_helix_d(1)"
name: "g_helix_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_helix_d/"
description: "g_helix – calculates basic properties of alpha helices"
---

<h2>NAME</h2>
<p> g_helix &#8211; calculates basic properties of alpha helices </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_helix</code> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-f</code><i> traj.xtc </i> <code>-to</code><i> gtraj.g87 </i> <code>-cz</code><i> zconf.gro </i> <code>-co</code><i> waver.gro </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-r0</code><i> int </i> <code>-[no]q</code><i></i> <code>-[no]F</code><i></i> <code>-[no]db</code><i></i> <code>-prop</code><i> enum </i> <code>-[no]ev</code><i></i> <code>-ahxstart</code><i> int </i> <code>-ahxend</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> g_helix computes all kind of helix properties. First, the peptide is checked to find the longest helical part. This is determined by Hydrogen bonds and Phi/Psi angles. That bit is fitted to an ideal helix around the Z-axis and centered around the origin. Then the following properties are computed: </p>
<p> <code> 1.</code> Helix radius (file radius.xvg). This is merely the RMS deviation in two dimensions for all Calpha atoms. it is calced as sqrt((SUM i(x2(i)+y2(i)))/N), where N is the number of backbone atoms. For an ideal helix the radius is 0.23 nm </p>
<p> <code> 2.</code> Twist (file twist.xvg). The average helical angle per residue is calculated. For alpha helix it is 100 degrees, for 3-10 helices it will be smaller, for 5-helices it will be larger. </p>
<p> <code> 3.</code> Rise per residue (file rise.xvg). The helical rise per residue is plotted as the difference in Z-coordinate between Ca atoms. For an ideal helix this is 0.15 nm </p>
<p> <code> 4.</code> Total helix length (file len-ahx.xvg). The total length of the helix in nm. This is simply the average rise (see above) times the number of helical residues (see below). </p>
<p> <code> 5.</code> Number of helical residues (file n-ahx.xvg). The title says it all. </p>
<p> <code> 6.</code> Helix Dipole, backbone only (file dip-ahx.xvg). </p>
<p> <code> 7.</code> RMS deviation from ideal helix, calculated for the Calpha atoms only (file rms-ahx.xvg). </p>
<p> <code> 8.</code> Average Calpha-Calpha dihedral angle (file phi-ahx.xvg). </p>
<p> <code> 9.</code> Average Phi and Psi angles (file phipsi.xvg). </p>
<p> <code> 10.</code> Ellipticity at 222 nm according to <i> Hirst and Brooks</i> </p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-to</code><i> gtraj.g87</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Gromos-87 ASCII trajectory format&nbsp;<wbr> </p>
<p> <code>-cz</code><i> zconf.gro</i> <code>Output</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-co</code><i> waver.gro</i> <code>Output</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
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
<p> <code>-r0</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>The first residue number in the sequence </p>
<p> <code>-[no]q</code><i>no </i><br />
&nbsp;<wbr>Check at every step which part of the sequence is helical </p>
<p> <code>-[no]F</code><i>yes </i><br />
&nbsp;<wbr>Toggle fit to a perfect helix </p>
<p> <code>-[no]db</code><i>no </i><br />
&nbsp;<wbr>Print debug info </p>
<p> <code>-prop</code><i> enum</i><code> RAD</code><br />
&nbsp;<wbr>Select property to weight eigenvectors with. WARNING experimental stuff:&nbsp;<wbr><code>&nbsp;<wbr>RAD</code>,&nbsp;<wbr><code>&nbsp;<wbr>TWIST</code>,&nbsp;<wbr><code>&nbsp;<wbr>RISE</code>,&nbsp;<wbr><code>&nbsp;<wbr>LEN</code>,&nbsp;<wbr><code>&nbsp;<wbr>NHX</code>,&nbsp;<wbr><code>&nbsp;<wbr>DIP</code>,&nbsp;<wbr><code>&nbsp;<wbr>RMS</code>,&nbsp;<wbr><code>&nbsp;<wbr>CPHI</code>,&nbsp;<wbr><code>&nbsp;<wbr>RMSA</code>,&nbsp;<wbr><code>&nbsp;<wbr>PHI</code>,&nbsp;<wbr><code>&nbsp;<wbr>PSI</code>,&nbsp;<wbr><code>&nbsp;<wbr>HB3</code>,&nbsp;<wbr><code>&nbsp;<wbr>HB4</code>,&nbsp;<wbr><code>&nbsp;<wbr>HB5</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>CD222</code> </p>
<p> <code>-[no]ev</code><i>no </i><br />
&nbsp;<wbr>Write a new&nbsp;<wbr>&#8216;trajectory&#8217;&nbsp;<wbr>file for ED </p>
<p> <code>-ahxstart</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>First residue in helix </p>
<p> <code>-ahxend</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Last residue in helix </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
