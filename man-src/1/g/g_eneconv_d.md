---
title: "g_eneconv_d(1)"
name: "g_eneconv_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_eneconv_d/"
description: "eneconv – converts energy files"
---

<h2>NAME</h2>
<p> eneconv &#8211; converts energy files </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>eneconv</code> <code>-f</code><i> ener.edr </i> <code>-o</code><i> fixed.edr </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> real </i> <code>-e</code><i> real </i> <code>-dt</code><i> real </i> <code>-offset</code><i> real </i> <code>-[no]settime</code><i></i> <code>-[no]sort</code><i></i> <code>-scalefac</code><i> real </i> <code>-[no]error</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> With <i> multiple files</i> specified for the <code> -f</code> option: </p>
<p> Concatenates several energy files in sorted order. In case of double time frames the one in the later file is used. By specifying <code> -settime</code> you will be asked for the start time of each file. The input files are taken from the command line, such that the command <code> eneconv -o fixed.edr *.edr</code> should do the trick. </p>
<p> With <i> one file</i> specified for <code> -f</code>: </p>
<p> Reads one energy file and writes another, applying the <code> -dt</code>, <code> -offset</code>, <code> -t0</code> and <code> -settime</code> options and converting to a different format if necessary (indicated by file extentions). </p>
<p> <code> -settime</code> is applied first, then <code> -dt</code>/<code> -offset</code> followed by <code> -b</code> and <code> -e</code> to select which frames to write.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> ener.edr</i> <code>Input, Mult.</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-o</code><i> fixed.edr</i> <code>Output</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-b</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>First time to use </p>
<p> <code>-e</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Last time to use </p>
<p> <code>-dt</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Only write out frame when t MOD dt&nbsp;<wbr>=&nbsp;<wbr>offset </p>
<p> <code>-offset</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Time offset for -dt option </p>
<p> <code>-[no]settime</code><i>no </i><br />
&nbsp;<wbr>Change starting time interactively </p>
<p> <code>-[no]sort</code><i>yes </i><br />
&nbsp;<wbr>Sort energy files&nbsp;<wbr>(not frames) </p>
<p> <code>-scalefac</code><i> real</i><code> 1 </code><br />
&nbsp;<wbr>Multiply energy component by this factor </p>
<p> <code>-[no]error</code><i>yes </i><br />
&nbsp;<wbr>Stop on errors in the file </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; When combining trajectories the sigma and E2 (necessary for statistics) are not updated correctly. Only the actual energy is correct. One thus has to compute statistics in another way. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
