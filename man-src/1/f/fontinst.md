---
title: "fontinst(1)"
name: "fontinst"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fontinst/"
description: "fontinst – utility to run TeX as fontinst"
---

<h2>NAME</h2>
<p> fontinst &#8211; utility to run TeX as fontinst </p>
<h2>SYNOPSIS</h2>
<p> <code>fontinst</code> <i>package</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>fontinst</code> runs <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) with the <code>&#8211;progname</code> flag set to pretend to be the program fontinst (affecting Karl Berry paths). </p>
<p> Typing </p>
<p> <tt>fontinst fontinst.sty</tt> </p>
<p> will start <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) and give the user an interactive prompt (<tt>*</tt>) where fontinst commands can be typed (such as <tt>\latinfamily{ptm}{}ye</tt>). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) </p>
<p> The fontinst manual, <i>fontinst.tex</i>. </p>
<p> Web page: &lt;<a rel="nofollow" href="http://tug.org/applications/fontinst/">http://tug.org/applications/fontinst/</a>&gt; </p>
<h2>BUGS</h2>
<p> None known, but report any bugs found to tex-fonts [at] tug.org (mailing list). </p>
<h2>AUTHOR</h2>
<p> Thomas Esser &lt;te [at] dbs.uni-hannover.de&gt; </p>
<p> This manual page was written by C.M. Connelly &lt;c@eskimo.com&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
