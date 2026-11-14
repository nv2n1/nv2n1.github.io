---
title: "ovf2ovp(1)"
name: "ovf2ovp"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ovf2ovp/"
description: "ovf2ovp – convert virtual font file and associated font metrics to property-list format"
---

<h2>NAME</h2>
<p> ovf2ovp &#8211; convert virtual font file and associated font metrics to property-list format </p>
<h2>SYNOPSIS</h2>
<p> <code>ovf2ovp</code> [<i>options</i>] <i>ovfname</i>[<i></i><code>.ovf</code>] [<i>ofmname</i>[<i></i><code>.ofm</code>] [<i>ovpfile</i>[<i></i><code>.ovp</code>]]] </p>
<h2>DESCRIPTION</h2>
<p> <code>ovf2ovp</code> translates a virtual font (OVF) file, <i>ovfname</i>, and its companion font metric (OFM) file, <i>ofmname</i>, into a human-readable property-list format. The program writes to standard output (by default) or to a file specified as <i>ovpname</i>. </p>
<p> The program also works with TeX VF and TFM files, producing TeX VPL files. </p>
<h2>OPTIONS</h2>
<p> (Same as <code>ofm2opl</code>).</p>
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
<dt><i>ovpfile</i></p>
<dd> Omega Virtual Property List file</p>
<dt><i>ofmname</i></p>
<dd> Omega Font Metric file</p>
<dt><i>ovfname</i></p>
<dd> Omega Virtual Font file</dl>
<h2>BUGS</h2>
<p> Send bug reports to &lt;<a rel="nofollow" href="http://lists.tug.org/tex-k">http://lists.tug.org/tex-k</a>&gt; (mailing list); may also check if the same bug is present in <code><a href="/docs/linux/man/1-vftovp/">vftovp</a></code>(1). General discussion of Omega (and Aleph) can take place on the &lt;<a rel="nofollow" href="http://lists.tug.org/omega">http://lists.tug.org/omega</a>&gt; mailing list. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-omega/">omega</a></code>(1), <code><a href="/docs/linux/man/1-aleph/">aleph</a></code>(1), <code><a href="/docs/linux/man/1-ofm2opl/">ofm2opl</a></code>(1), <code><a href="/docs/linux/man/1-ovp2ovf/">ovp2ovf</a></code>(1), <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1), <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1), <code><a href="/docs/linux/man/1-vftovp/">vftovp</a></code>(1), <code><a href="/docs/linux/man/1-vptovf/">vptovf</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> According to the WEB documentation: </p>
<dl>
<dt>
<dd> <code>VFtoVP</code> is an extended version of the program <code>TFtoPL</code>, which is part of the standard TeXware library. The idea of a virtual font was inspired by the work of David R. Fuchs who designed a similar set of conventions in 1984 while developing a device driver for ArborText, Inc. He wrote a somewhat similar program called <code>AMFtoXPL</code>.</dl>
<p> Thus, <code>ovf2ovp</code> is based on the WEB source code for <code><a href="/docs/linux/man/1-vftovp/">vftovp</a></code>(1), although nowadays it is a link to <code>omfonts</code>, implemented entirely in C. </p>
<p> The primary authors of Omega are John Plaice and Yannis Haralambous. Omega (and Aleph) are now maintained as part of TeX Live. </p>
<p> This manual page was written by C.M. Connelly &lt;cmc [at] debian.org&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
