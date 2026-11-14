---
title: "g_wheel(1)"
name: "g_wheel"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_wheel/"
description: "wheel – plots helical wheels"
---

<h2>NAME</h2>
<p> wheel &#8211; plots helical wheels </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>wheel</code> <code>-f</code><i> nnnice.dat </i> <code>-o</code><i> plot.eps </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-r0</code><i> int </i> <code>-rot0</code><i> real </i> <code>-T</code><i> string </i> <code>-[no]nn</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> wheel plots a helical wheel representation of your sequence.The input sequence is in the .dat file where the first line contains the number of residues and each consecutive line contains a residuename.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> nnnice.dat</i> <code>Input</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-o</code><i> plot.eps</i> <code>Output</code><br />
&nbsp;<wbr>Encapsulated PostScript&nbsp;<wbr>(tm)&nbsp;<wbr>file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-r0</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>The first residue number in the sequence </p>
<p> <code>-rot0</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Rotate around an angle initially&nbsp;<wbr>(90 degrees makes sense) </p>
<p> <code>-T</code><i> string</i><br />
&nbsp;<wbr>Plot a title in the center of the wheel&nbsp;<wbr>(must be shorter than 10 characters, or it will overwrite the wheel) </p>
<p> <code>-[no]nn</code><i>yes </i><br />
&nbsp;<wbr>Toggle numbers </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
