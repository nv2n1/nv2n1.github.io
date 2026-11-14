---
title: "kpsewhere(1)"
name: "kpsewhere"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kpsewhere/"
description: "kpsewhere – Expanding kpsewhich to separately iterate over each texmf tree listed in $TEXMF."
---

<h2>NAME</h2>
<p> kpsewhere &#8211; Expanding <code>kpsewhich</code> to separately iterate over each texmf tree listed in $TEXMF. </p>
<h2>SYNOPSIS</h2>
<p> <code>kpsewhere </code> [ <i>kpsewhich-OPTIONS</i>&#8230; ] <i>COMMAND</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>kpsewhere</code> is an extension to <code>kpsewhich</code> (as <code>where</code> is for <code>which</code> in tcsh). The intention is to provide a way to check for conflicts/shadowed files. It will, however, only find <code>one</code> file per TEXMF tree. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h|&#8211;help</code></p>
<dd> show a short help message</p>
<dt><code>*</code></p>
<dd> all other options are directly handed to kpsewhich</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kpsewhich/">kpsewhich</a></code>(1) </p>
<p> <i>Kpathsea: A library for path searching</i> (info or DVI file) </p>
<p> Web page: &lt;<a rel="nofollow" href="http://tug.org/teTeX/">http://tug.org/teTeX/</a>&gt; </p>
<h2>BUGS</h2>
<p> None known, but report any bugs found to &lt;tetex [at] dbs.uni-hannover.de&gt; (mailing list). </p>
<h2>AUTHOR</h2>
<p> <code>kpsewhere</code> was written by Hans Fredrik Nordhaug &lt;hans.fredrik [at] nordhaug.no&gt;, additions by Thomas Esser &lt;te [at] dbs.uni-hannover.de&gt;, in 2003 and 2004. <code>kpsewhere</code> is in the public domain. </p>
<p> This manual page was written by Frank Küster &lt;frank [at] kuesterei.ch&gt;, for the Debian GNU/Linux system. It is also in the public domain and may be used and changed by others without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
