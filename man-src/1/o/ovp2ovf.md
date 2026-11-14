---
title: "ovp2ovf(1)"
name: "ovp2ovf"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ovp2ovf/"
description: "ovp2ovf – convert a virtual property-list file into a virtual font file and its associated font metric file"
---

<h2>NAME</h2>
<p> ovp2ovf &#8211; convert a virtual property-list file into a virtual font file and its associated font metric file </p>
<h2>SYNOPSIS</h2>
<p> <code>ovp2ovf</code> [<i>OPTIONS</i>] <i>OVPFILE</i>[<i></i><code>.ovp</code>] [<i>OVFFILE</i>[<i></i><code>.ovf</code>] [<i>OFMFILE</i>[<i></i><code>.ofm</code>]]] </p>
<h2>DESCRIPTION</h2>
<p> <code>ovp2ovf</code> translates a human-readable virtual property list (OVP) file, <i>OVPFILE</i>, into a virtual font (OVF) file, <i>OVFFILE</i> and its companion font metric (OFM) file, <i>OFMFILE</i>. </p>
<p> The program also works with TeX VP files, producing VF and TFM files. (<code>ovp2ovf</code> is based on the WEB source code for <code><a href="/docs/linux/man/1-vptovf/">vptovf</a></code>(1).) </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> display a brief summary of syntax and options</p>
<dt><code>-verbose</code></p>
<dd> display progress reports</p>
<dt><code>-version</code></p>
<dd> output version information and exit</p>
<dt>
<dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>OFMFILE</i></p>
<dd> Omega Font Metric file</p>
<dt><i>OVFFILE</i></p>
<dd> Omega Virtual Font file</p>
<dt><i>OVPFILE</i></p>
<dd> Omega Virtual Property List file</dl>
<h2>BUGS</h2>
<p> None known, but report any found to &lt;omega [at] ens.fr&gt; (mailing list). You should also check to see if the bug is in <code><a href="/docs/linux/man/1-vptovf/">vptovf</a></code>(1). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-omega/">omega</a></code>(1), <code><a href="/docs/linux/man/1-ofm2opl/">ofm2opl</a></code>(1), <code><a href="/docs/linux/man/1-ovf2ovp/">ovf2ovp</a></code>(1), <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1), <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1), <code><a href="/docs/linux/man/1-vftovp/">vftovp</a></code>(1), <code><a href="/docs/linux/man/1-vptovf/">vptovf</a></code>(1) </p>
<p> <i>Draft Manual for the Omega System</i> (<i>omega-manual.dvi</i>). </p>
<p> Web page: &lt;<a rel="nofollow" href="http://www.gutenberg.eu.org/omega/">http://www.gutenberg.eu.org/omega/</a>&gt; </p>
<h2>AUTHOR</h2>
<p> According to the WEB documentation: </p>
<dl>
<dt>
<dd> <code>VPtoVF</code> is an extended version of the program <code>PLtoTF</code>, which is part of the standard TeXware library. <code>OVP2OVF</code> is an extended version of <code>VPtoVF</code> that allows much larger fonts. The idea of a virtual font was inspired by the work of David R. Fuchs who designed a similar set of conventions in 1984 while developing a device driver for ArborText, Inc. He wrote a somewhat similar program called <code>PLFONT</code>.</dl>
<p> The primary authors of Omega are John Plaice &lt;plaice [at] cse.unsw.edu.au&gt; and Yannis Haralambous &lt;yannis [at] fluxus-virus.com&gt;. </p>
<p> This manual page was written by C.M. Connelly &lt;cmc [at] debian.org&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
