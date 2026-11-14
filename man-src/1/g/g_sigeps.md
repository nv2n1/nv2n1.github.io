---
title: "g_sigeps(1)"
name: "g_sigeps"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_sigeps/"
description: "sigeps – convert c6/12 or c6/cn combinations to and from sigma/epsilon"
---

<h2>NAME</h2>
<p> sigeps &#8211; convert c6/12 or c6/cn combinations to and from sigma/epsilon </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>sigeps</code> <code>-o</code><i> potje.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-c6</code><i> real </i> <code>-cn</code><i> real </i> <code>-pow</code><i> int </i> <code>-sig</code><i> real </i> <code>-eps</code><i> real </i> <code>-A</code><i> real </i> <code>-B</code><i> real </i> <code>-C</code><i> real </i> <code>-qi</code><i> real </i> <code>-qj</code><i> real </i> <code>-sigfac</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> Sigeps is a simple utility that converts c6/c12 or c6/cn combinations to sigma and epsilon, or vice versa. It can also plot the potential in file. In addition it makes an approximation of a Buckingham potential to a Lennard Jones potential.</p>
<h2>FILES</h2>
<p> <code>-o</code><i> potje.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-c6</code><i> real</i><code> 0.001 </code><br />
&nbsp;<wbr>c6 </p>
<p> <code>-cn</code><i> real</i><code> 1e-06 </code><br />
&nbsp;<wbr>constant for repulsion </p>
<p> <code>-pow</code><i> int</i><code> 12</code><br />
&nbsp;<wbr>power of the repulsion term </p>
<p> <code>-sig</code><i> real</i><code> 0.3 </code><br />
&nbsp;<wbr>sig </p>
<p> <code>-eps</code><i> real</i><code> 1 </code><br />
&nbsp;<wbr>eps </p>
<p> <code>-A</code><i> real</i><code> 100000</code><br />
&nbsp;<wbr>Buckingham A </p>
<p> <code>-B</code><i> real</i><code> 32 </code><br />
&nbsp;<wbr>Buckingham B </p>
<p> <code>-C</code><i> real</i><code> 0.001 </code><br />
&nbsp;<wbr>Buckingham C </p>
<p> <code>-qi</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>qi </p>
<p> <code>-qj</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>qj </p>
<p> <code>-sigfac</code><i> real</i><code> 0.7 </code><br />
&nbsp;<wbr>Factor in front of sigma for starting the plot </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
