---
title: "g_rdf_d(1)"
name: "g_rdf_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_rdf_d/"
description: "g_rdf – calculates radial distribution functions"
---

<h2>NAME</h2>
<p> g_rdf &#8211; calculates radial distribution functions </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_rdf</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> rdf.xvg </i> <code>-sq</code><i> sq.xvg </i> <code>-cn</code><i> rdf_cn.xvg </i> <code>-hq</code><i> hq.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-bin</code><i> real </i> <code>-[no]com</code><i></i> <code>-rdf</code><i> enum </i> <code>-[no]pbc</code><i></i> <code>-[no]norm</code><i></i> <code>-[no]xy</code><i></i> <code>-cut</code><i> real </i> <code>-ng</code><i> int </i> <code>-fade</code><i> real </i> <code>-nlevel</code><i> int </i> <code>-startq</code><i> real </i> <code>-endq</code><i> real </i> <code>-energy</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> The structure of liquids can be studied by either neutron or X-ray scattering. The most common way to describe liquid structure is by a radial distribution function. However, this is not easy to obtain from a scattering experiment. </p>
<p> g_rdf calculates radial distribution functions in different ways. The normal method is around a (set of) particle(s), the other method is around the center of mass of a set of particles. With both methods rdf&#8217;s can also be calculated around axes parallel to the z-axis with option <code> -xy</code>. </p>
<p> The option <code> -rdf</code> sets the type of rdf to be computed. Default is for atoms or particles, but one can also select center of mass or geometry of molecules or residues. In all cases only the atoms in the index groups are taken into account. For molecules and/or the center of mass option a run input file is required. Other weighting than COM or COG can currently only be achieved by providing a run input file with different masses. Option <code> -com</code> also works in conjunction with <code> -rdf</code>. </p>
<p> If a run input file is supplied (<code> -s</code>) and <code> -rdf</code> is set to <code> atom</code>, exclusions defined in that file are taken into account when calculating the rdf. The option <code> -cut</code> is meant as an alternative way to avoid intramolecular peaks in the rdf plot. It is however better to supply a run input file with a higher number of exclusions. For eg. benzene a topology with nrexcl set to 5 would eliminate all intramolecular contributions to the rdf. Note that all atoms in the selected groups are used, also the ones that don&#8217;t have Lennard-Jones interactions. </p>
<p> Option <code> -cn</code> produces the cumulative number rdf, i.e. the average number of particles within a distance r. </p>
<p> To bridge the gap between theory and experiment structure factors can be computed (option <code> -sq</code>). The algorithm uses FFT, the gridspacing of which is determined by option <code> -grid</code>.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> rdf.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-sq</code><i> sq.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-cn</code><i> rdf_cn.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-hq</code><i> hq.xvg</i> <code>Output, Opt.</code><br />
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
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-bin</code><i> real</i><code> 0.002 </code><br />
&nbsp;<wbr>Binwidth&nbsp;<wbr>(nm) </p>
<p> <code>-[no]com</code><i>no </i><br />
&nbsp;<wbr>RDF with respect to the center of mass of first group </p>
<p> <code>-rdf</code><i> enum</i><code> atom</code><br />
&nbsp;<wbr>RDF type:&nbsp;<wbr><code>&nbsp;<wbr>atom</code>,&nbsp;<wbr><code>&nbsp;<wbr>mol_com</code>,&nbsp;<wbr><code>&nbsp;<wbr>mol_cog</code>,&nbsp;<wbr><code>&nbsp;<wbr>res_com</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>res_cog</code> </p>
<p> <code>-[no]pbc</code><i>yes </i><br />
&nbsp;<wbr>Use periodic boundary conditions for computing distances. Without PBC the maximum range will be three times the larges box edge. </p>
<p> <code>-[no]norm</code><i>yes </i><br />
&nbsp;<wbr>Normalize for volume and density </p>
<p> <code>-[no]xy</code><i>no </i><br />
&nbsp;<wbr>Use only the x and y components of the distance </p>
<p> <code>-cut</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Shortest distance&nbsp;<wbr>(nm)&nbsp;<wbr>to be considered </p>
<p> <code>-ng</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Number of secondary groups to compute RDFs around a central group </p>
<p> <code>-fade</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>From this distance onwards the RDF is tranformed by g'(r)&nbsp;<wbr>=&nbsp;<wbr>1&nbsp;<wbr>+&nbsp;<wbr>[g(r)-1]&nbsp;<wbr>exp(-(r/fade-1)2 to make it go to 1 smoothly. If fade is 0.0 nothing is done. </p>
<p> <code>-nlevel</code><i> int</i><code> 20</code><br />
&nbsp;<wbr>Number of different colors in the diffraction image </p>
<p> <code>-startq</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Starting q&nbsp;<wbr>(1/nm)&nbsp;<wbr> </p>
<p> <code>-endq</code><i> real</i><code> 60 </code><br />
&nbsp;<wbr>Ending q&nbsp;<wbr>(1/nm) </p>
<p> <code>-energy</code><i> real</i><code> 12 </code><br />
&nbsp;<wbr>Energy of the incoming X-ray&nbsp;<wbr>(keV)&nbsp;<wbr> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
