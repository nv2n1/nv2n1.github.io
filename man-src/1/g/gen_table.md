---
title: "gen_table(1)"
name: "gen_table"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gen_table/"
description: "gen_table – generate tables for use by mdrun"
---

<h2>NAME</h2>
<p> gen_table &#8211; generate tables for use by mdrun </p>
<p> <code>VERSION 4.0_rc1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>gen_table</code> <code>-o</code><i> table.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-el</code><i> enum </i> <code>-rc</code><i> real </i> <code>-rtol</code><i> real </i> <code>-xi</code><i> real </i> <code>-xir</code><i> real </i> <code>-z1</code><i> real </i> <code>-z2</code><i> real </i> <code>-nrow1</code><i> int </i> <code>-nrow2</code><i> int </i> <code>-m</code><i> enum </i> <code>-resol</code><i> int </i> <code>-delta</code><i> real </i> <code>-efac</code><i> real </i> <code>-nrep</code><i> int </i> <code>-ndisp</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> gen_table generates tables for mdrun for use with the USER defined potentials. Note that the format has been update for higher accuracy in the forces starting with version 4.0. Using older tables with 4.0 will silently crash your simulations, as will using new tables with an older GROMACS version. This is because in the old version the second derevative of the potential was specified whereas in the new version the first derivative of the potential is used instead. </p>
<p> For Slater interactions four parameters must be passed: the 1/Width and the row number of the element. The interactions are computed analytically which may be slow due to the fact that arbitraray precision arithmetic is needed. If the width of one of the Slater is zero a Nucleus-Slater interaction will be generated.</p>
<h2>FILES</h2>
<p> <code>-o</code><i> table.xvg</i> <code>Output</code><br />
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
<p> <code>-el</code><i> enum</i><code> cut</code><br />
&nbsp;<wbr>Electrostatics type: cut, rf or pme:&nbsp;<wbr> <code>cut</code> , <code>rf</code> or <code>pme</code> </p>
<p> <code>-rc</code><i> real</i><code> 0.9 </code><br />
&nbsp;<wbr>Cut-off required for rf or pme </p>
<p> <code>-rtol</code><i> real</i><code> 1e-05 </code><br />
&nbsp;<wbr>Ewald tolerance required for pme </p>
<p> <code>-xi</code><i> real</i><code> 0.15 </code><br />
&nbsp;<wbr>Width of the Gaussian diffuse charge of the G&amp;G model </p>
<p> <code>-xir</code><i> real</i><code> 0.0615</code><br />
&nbsp;<wbr>Width of erfc(z)/z repulsion of the G&amp;G model&nbsp;<wbr>(z=0.5 rOO/xir) </p>
<p> <code>-z1</code><i> real</i><code> 20 </code><br />
&nbsp;<wbr>1/Width of the first Slater charge&nbsp;<wbr>(unit 1/nm) </p>
<p> <code>-z2</code><i> real</i><code> 20 </code><br />
&nbsp;<wbr>1/Width of the second Slater charge&nbsp;<wbr>(unit 1/nm) </p>
<p> <code>-nrow1</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Row number for the first Slater charge </p>
<p> <code>-nrow2</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Row number for the first Slater charge </p>
<p> <code>-m</code><i> enum</i><code> ljc</code><br />
&nbsp;<wbr>Model for the tables:&nbsp;<wbr> <code>ljc</code> , <code>gg</code> , <code>guillot2001a</code> or <code>slater</code> </p>
<p> <code>-resol</code><i> int</i><code> 500</code><br />
&nbsp;<wbr>Resolution of the table&nbsp;<wbr>(points per nm) </p>
<p> <code>-delta</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Displacement in the Coulomb functions&nbsp;<wbr>(nm), used as 1/(r+delta). Only for hard wall potential. </p>
<p> <code>-efac</code><i> real</i><code> 500 </code><br />
&nbsp;<wbr>Number indicating the steepness of the hardwall potential. </p>
<p> <code>-nrep</code><i> int</i><code> 12</code><br />
&nbsp;<wbr>Power for the repulsion potential&nbsp;<wbr>(with model AB1 or maaren) </p>
<p> <code>-ndisp</code><i> int</i><code> 6</code><br />
&nbsp;<wbr>Power for the dispersion potential&nbsp;<wbr>(with model AB1 or maaren) </p>
<h2>Index</h2>
