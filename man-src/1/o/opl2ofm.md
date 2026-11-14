---
title: "opl2ofm(1)"
name: "opl2ofm"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opl2ofm/"
description: "opl2ofm – convert Omega and TeX property-list files to font-metric files"
---

<h2>NAME</h2>
<p> opl2ofm &#8211; convert Omega and TeX property-list files to font-metric files </p>
<h2>SYNOPSIS</h2>
<p> <code>opl2ofm</code> [<i>OPTIONS</i>] <i>OPLFILE</i>[<i></i><code>.opl</code>] [<i>OFMFILE</i>[<i></i><code>.ofm</code>]] </p>
<h2>DESCRIPTION</h2>
<p> <code>opl2ofm</code> translates a property-list format file, <i>OPLFILE</i>, into the binary Omega Font Metric format. The program writes to standard output (by default) or to a file specified as <i>OFMFILE</i>. </p>
<p> The program also works with TeX PL files, producing TeX TFM files. (<code>opl2ofm</code> is based on the WEB source code for <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1).) </p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd>
<dt><code>-help</code></p>
<dd> display a brief summary of syntax and options</p>
<dt><code>-verbose</code></p>
<dd> display progress reports</p>
<dt><code>-version</code></p>
<dd> output version information and exit</p>
<dt>
<dd></dl>
<h2>BUGS</h2>
<p> None known, but report any found to &lt;omega [at] ens.fr&gt; (mailing list). You should also check to see if the bug is present in <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-omega/">omega</a></code>(1), <code><a href="/docs/linux/man/1-ofm2opl/">ofm2opl</a></code>(1), <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1), <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1). </p>
<p> <i>Draft Manual for the Omega System</i> (<i>omega-manual.dvi</i>). </p>
<p> Web page: &lt;<a rel="nofollow" href="http://www.gutenberg.eu.org/omega/">http://www.gutenberg.eu.org/omega/</a>&gt; </p>
<h2>AUTHOR</h2>
<p> According to the WEB documentation: </p>
<dl>
<dt>
<dd> The first <code>PLtoTF</code> program was designed by Leo Guibas in the summer of 1978. Contributions by Frank Liang, Doug Wyatt, and Lyle Ramshaw also had a significant effect on the evolution of the present code. </p>
<p> Extensions for an enhanced ligature mechanism were added by D.E. Knuth in 1989. </p>
<p> Extensions to handle extended font metric files (&#8220;OFM&#8221;) were added by John Plaice in December 1995 and January 1996, resulting in the new program <code>OPL2OFM</code>.</dl>
<p> The primary authors of Omega are John Plaice &lt;plaice [at] cse.unsw.edu.au&gt; and Yannis Haralambous &lt;yannis [at] fluxus-virus.com&gt;. </p>
<p> This manual page was written by C.M. Connelly &lt;cmc [at] debian.org&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
