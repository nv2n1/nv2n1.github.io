---
title: "ofm2opl(1)"
name: "ofm2opl"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ofm2opl/"
description: "ofm2opl – convert Omega and TeX font-metric files to property-list files"
---

<h2>NAME</h2>
<p> ofm2opl &#8211; convert Omega and TeX font-metric files to property-list files </p>
<h2>SYNOPSIS</h2>
<p> <code>ofm2opl</code> [<i>options</i>] <i>ofmname</i>[<i></i><code>.ofm</code>] [<i>oplfile</i>[<i></i><code>.opl</code>]] </p>
<h2>DESCRIPTION</h2>
<p> <code>ofm2opl</code> translates a binary Omega Font Metrics file, <i>ofmname</i>, into a human-readable property-list form. The program writes to standard output (by default) or to a file specified as <i>oplfile</i>. </p>
<p> The program also works with TeX TFM files, producing TeX PL files. </p>
<h2>OPTIONS</h2>
<p> (Same as <code>ovf2ovp</code>).</p>
<dl>
<dt>
<dd>
<dt><code>-charcode-format=</code><i>type</i></p>
<dd> output character codes according to <i>type</i>, either `hex&#8217;, `octal&#8217; or `ascii&#8217;. Default is `hex&#8217;; `ascii&#8217; says to use ASCII for letters and digits, hex for all else.</p>
<dt><code>-char-format=</code><i>stype</i></p>
<dd> output character codes according to <i>stype</i>, either `num&#8217; or `ascii&#8217;. Default is `num&#8217;; `ascii&#8217; as in -charcode-format. (These two redundant options both exist only for historical compatibility.)</p>
<dt><code>-num-format=</code><i>ntype</i></p>
<dd> output numbers according to <i>ntype</i>, either `hex&#8217; or `octal&#8217;; default is hex.</p>
<dt><code>-text-format=</code><i>ttype</i></p>
<dd> output coding scheme and family according to <i>ttype</i>, either `mixed&#8217; or `upper&#8217; case; default is mixed.</p>
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
<dt><i>OFMNAME</i></p>
<dd> an Omega Font Metric file</p>
<dt><i>OPLFILE</i></p>
<dd> an Omega Property List file</dl>
<h2>BUGS</h2>
<p> Send bug reports to &lt;<a rel="nofollow" href="http://lists.tug.org/tex-k">http://lists.tug.org/tex-k</a>&gt; (mailing list); may also check if the same bug is present in <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1). General discussion of Omega (and Aleph) can take place on the &lt;<a rel="nofollow" href="http://lists.tug.org/omega">http://lists.tug.org/omega</a>&gt; mailing list. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-omega/">omega</a></code>(1), <code><a href="/docs/linux/man/1-aleph/">aleph</a></code>(1), <code><a href="/docs/linux/man/1-opl2ofm/">opl2ofm</a></code>(1), <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1), <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> According to the WEB documentation: </p>
<dl>
<dt>
<dd> The first <code>TFtoPL</code> program was designed by Leo Guibas in the summer of 1978. Contributions by Frank Liang, Doug Wyatt, and Lyle Ramshaw also had a significant effect on the evolution of the present code. </p>
<p> Extensions for an enhanced ligature mechanism were added by D.E. Knuth in 1989. </p>
<p> Extensions to handle extended font metric files (&#8220;OFM&#8221;) were added by John Plaice in December 1995 and January 1996, resulting in the new program <code>OFM2OPL</code>.</dl>
<p> <code>ofm2opl</code> is based on the WEB source code for <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1), although nowadays it is a link to <code>omfonts</code>, implemented entirely in C. </p>
<p> The primary authors of Omega are John Plaice and Yannis Haralambous. Omega (and Aleph) are now maintained as part of TeX Live. </p>
<p> This manual page was written by C.M. Connelly &lt;cmc [at] debian.org&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
