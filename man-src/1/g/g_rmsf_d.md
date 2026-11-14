---
title: "g_rmsf_d(1)"
name: "g_rmsf_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_rmsf_d/"
description: "g_rmsf – calculates atomic fluctuations"
---

<h2>NAME</h2>
<p> g_rmsf &#8211; calculates atomic fluctuations </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_rmsf</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-q</code><i> eiwit.pdb </i> <code>-oq</code><i> bfac.pdb </i> <code>-ox</code><i> xaver.pdb </i> <code>-o</code><i> rmsf.xvg </i> <code>-od</code><i> rmsdev.xvg </i> <code>-oc</code><i> correl.xvg </i> <code>-dir</code><i> rmsf.log </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]res</code><i></i> <code>-[no]aniso</code><i></i> <code>-[no]fit</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_rmsf computes the root mean square fluctuation (RMSF, i.e. standard deviation) of atomic positions after (optionally) fitting to a reference frame. </p>
<p> With option <code> -oq</code> the RMSF values are converted to B-factor values, which are written to a pdb file with the coordinates, of the structure file, or of a pdb file when <code> -q</code> is specified. Option <code> -ox</code> writes the B-factors to a file with the average coordinates. </p>
<p> With the option <code> -od</code> the root mean square deviation with respect to the reference structure is calculated. </p>
<p> With the option <code> aniso</code> g_rmsf will compute anisotropic temperature factors and then it will also output average coordinates and a pdb file with ANISOU records (corresonding to the <code> -oq</code> or <code> -ox</code> option). Please note that the U values are orientation dependent, so before comparison with experimental data you should verify that you fit to the experimental coordinates. </p>
<p> When a pdb input file is passed to the program and the <code> -aniso</code> flag is set a correlation plot of the Uij will be created, if any anisotropic temperature factors are present in the pdb file. </p>
<p> With option <code> -dir</code> the average MSF (3&#215;3) matrix is diagonalized. This shows the directions in which the atoms fluctuate the most and the least.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-q</code><i> eiwit.pdb</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-oq</code><i> bfac.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-ox</code><i> xaver.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-o</code><i> rmsf.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-od</code><i> rmsdev.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oc</code><i> correl.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dir</code><i> rmsf.log</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
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
<p> <code>-[no]res</code><i>no </i><br />
&nbsp;<wbr>Calculate averages for each residue </p>
<p> <code>-[no]aniso</code><i>no </i><br />
&nbsp;<wbr>Compute anisotropic termperature factors </p>
<p> <code>-[no]fit</code><i>yes </i><br />
&nbsp;<wbr>Do a least squares superposition before computing RMSF. Without this you must make sure that the reference structure and the trajectory match. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
