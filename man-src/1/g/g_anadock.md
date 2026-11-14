---
title: "g_anadock(1)"
name: "g_anadock"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_anadock/"
description: "anadock – cluster structures from Autodock runs"
---

<h2>NAME</h2>
<p> anadock &#8211; cluster structures from Autodock runs </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>anadock</code> <code>-f</code><i> eiwit.pdb </i> <code>-ox</code><i> cluster.pdb </i> <code>-od</code><i> edocked.xvg </i> <code>-of</code><i> efree.xvg </i> <code>-g</code><i> anadock.log </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]xvgr</code><i></i> <code>-[no]free</code><i></i> <code>-[no]rms</code><i></i> <code>-cutoff</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> anadock analyses the results of an Autodock run and clusters the structures together, based on distance or RMSD. The docked energy and free energy estimates are analysed, and for each cluster the energy statistics are printed. </p>
<p> An alternative approach to this is to cluster the structures first (using <code> g_cluster</code> and then sort the clusters on either lowest energy or average energy.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> eiwit.pdb</i> <code>Input</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-ox</code><i> cluster.pdb</i> <code>Output</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-od</code><i> edocked.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-of</code><i> efree.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-g</code><i> anadock.log</i> <code>Output</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]free</code><i>no </i><br />
&nbsp;<wbr>Use Free energy estimate from autodock for sorting the classes </p>
<p> <code>-[no]rms</code><i>yes </i><br />
&nbsp;<wbr>Cluster on RMS or distance </p>
<p> <code>-cutoff</code><i> real</i><code> 0.2 </code><br />
&nbsp;<wbr>Maximum RMSD/distance for belonging to the same cluster </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
