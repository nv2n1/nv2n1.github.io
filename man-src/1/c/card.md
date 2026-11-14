---
title: "card(1)"
name: "card"
section: "1"
letter: "c"
url: "/docs/linux/man/1-card/"
description: "card – print reference card of program options"
---

<h2 class="name">NAME</h2>
<p> card &#8211; print reference card of program options </p>
<h2>SYNOPSIS</h2>
<p> <code>card</code> [<i>OPTION</i>]&#8230; <i>PROGRAM</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print a reference card of the PROGRAMs thanks to their inline help.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> display version information and exit</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> save the output in FILE</p>
<dt><code>-l</code>, <code>&#8211;language</code>=<i>LL</i></p>
<dd> print the help in the language LL (default: English)</p>
<dt><code>&#8211;command</code>=<i>CMD</i></p>
<dd> perform pretty-printing on the output of CMD (e.g. <code>&#8211;command=</code>&#8216;netscape <code>-help</code>&#8216;)</dl>
<p> Options for a2ps are given after `&#8211;&#8216;, for instance</p>
<dl>
<dt>
<dd> <tt>$ card -lfr a2ps -- -Pdisplay -4</tt></dl>
<p> News, updates and documentation: <a rel="nofollow" href="http://www.inf.enst.fr/~demaille/a2ps/">http://www.inf.enst.fr/~demaille/a2ps/</a></p>
<h2>AUTHOR</h2>
<p> Written by Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-a2ps [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997-99 Akim Demaille, Miguel Santana<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-a2ps/">a2ps</a></code>(1), <code><a href="/docs/linux/man/1-card/">card</a></code>(1), <code><a href="/docs/linux/man/1-fixps/">fixps</a></code>(1), <code><a href="/docs/linux/man/1-pdiff/">pdiff</a></code>(1), <code><a href="/docs/linux/man/1-psset/">psset</a></code>(1), <code><a href="/docs/linux/man/1-texi2dvi4a2ps/">texi2dvi4a2ps</a></code>(1). </p>
<p> The full documentation for <code>card</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>card</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info card</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
