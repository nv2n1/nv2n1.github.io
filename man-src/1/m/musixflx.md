---
title: "musixflx(1)"
name: "musixflx"
section: "1"
letter: "m"
url: "/docs/linux/man/1-musixflx/"
description: "musixflx – process mx1 files (the second pass of 3-pass MusiXTeX typesetting)"
---

<h2 class="name">NAME</h2>
<p> musixflx &#8211; process mx1 files (the second pass of 3-pass MusiXTeX typesetting)</p>
<h2>SYNOPSIS</h2>
<p> [ texlua ] <code>musixflx[.lua]</code> <i>jobname </i> [ .mx1 | .tex ] [ <i>debugmode </i> ] </p>
<p> where <i>debugmode </i> can be<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>output debugging information to the screen</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>m<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>output line numbers to the screen</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>f<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>output debugging information to jobname.mxl (not mx1)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>s<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>output computed lines to the screen</p>
<h2>DESCRIPTION</h2>
<p> Musixflx processes mx1 files (the second pass of 3-pass MusiXTeX typesetting) </p>
<p> To allow for ease of use with a batch file, <code> musixflx.lua</code> can be fed with either <i> jobname.mx1</i>, <i> jobname.tex</i>, or just <i> jobname</i>, any of which open <i> jobname.mx1</i> and create <i> jobname.mx2</i>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-musixtex/">musixtex</a></code>(1)<br />
 musixdoc.pdf </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Andreas Tille &lt;tille [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). Corrections to the synopsis were pointed out by Peter Breitenlohner &lt;peb [at] mppmu.mpg.de&gt; and implemented by Bob Tennent &lt;rdt [at] cs.queensu.ca&gt;. </p>
<h2>Index</h2>
