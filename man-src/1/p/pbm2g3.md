---
title: "pbm2g3(1)"
name: "pbm2g3"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbm2g3/"
description: "pbm2g3 – convert portable bitmaps (PBM) into G3 fax files"
---

<h2 class="name">NAME</h2>
<p> pbm2g3 &#8211; convert portable bitmaps (PBM) into G3 fax files </p>
<h2>SYNOPSIS</h2>
<p> <code>pbm2g3</code> [<code>-r</code>] [<code>-w</code>&lt;page<code>width&gt;</code>] [<code>-h</code>&lt;blank<code>lines&gt;</code>] [<code>-d</code>] [<code>-a</code>] [<i>pbmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable bitmap as input, converting it into a G3 fax file on stdout. That file is suitable for faxing it with <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8) or queueing it for faxing with <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1) (provided that it gets a &#8220;.g3&#8221; suffix). </p>
<p> <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1) uses <a href="/docs/linux/man/1-pbm2g3/">pbm2g3</a>(1) internally to convert various bitmap formats into fax g3 format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> byte-aligns the end-of-line codes, inserting padding bits as necessary.</p>
<dt><code>-w &lt;page width&gt;</code></p>
<dd> sets the width of the resulting G3 page. Default is 1728. If you want to be able to fax it with sendfax, don&#8217;t use anything else. For other fax programs, 2048, 2432, 864 and 1216 may be useful. For other purposes, use what you like. </p>
<p> If you set it to 0, the width of the pbm file will be used.</p>
<dt><code>-h &lt;blank lines&gt;</code></p>
<dd> specifies the number of blank lines <i>pbm2g3</i> should prepend to each page. Default is 0. </p>
<p> To produce identical output as pbmplus&#8217; pbm2g3 program (with my patch!) does, use &#8220;-h 4&#8221;.</p>
<dt><code>-r</code></p>
<dd> reverse the bit order in the bytes.</p>
<dt><code>-d</code></p>
<dd> will one day make pbm2g3 prepend a digifax header to the page. </p>
</dl>
<h2>REFERENCES</h2>
<p> The standard for Group 3 fax is defined in CCITT Recommendation T.4.</p>
<h2>BUGS</h2>
<p> The -d option isn&#8217;t implemented yet. </p>
<p> If a raw pbm file is converted, and the width of the g3 file is smaller than the width of the pbm file, the former is rounded up to the next multiple of 8.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-g32pbm/">g32pbm</a>(1), <a href="/docs/linux/man/5-pbm/">pbm</a>(5), <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8)</p>
<h2>AUTHOR</h2>
<p> <i>pbm2g3</i> is Copyright (C) 1993 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;. It is similar to the <i>pbmtog3</i> program in Jef Poskanzers <i>pbmplus</i> package, but it&#8217;s a complete re-write. No code is copied. </p>
<h2>Index</h2>
