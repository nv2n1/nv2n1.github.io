---
title: "g32pbm(1)"
name: "g32pbm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g32pbm/"
description: "g32pbm – convert a Group 3 fax file into a portable bitmap"
---

<h2 class="name">NAME</h2>
<p> g32pbm &#8211; convert a Group 3 fax file into a portable bitmap </p>
<h2>SYNOPSIS</h2>
<p> <code>g32pbm</code> [<code>-reversebits</code>] [<code>-stretch</code>] [<i>g3file</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a Group 3 fax file (raw or digifax) as input. If no filename is given, stdin is used. Produces a portable bitmap as output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code></p>
<dd> Tells <i>g32pbm</i> to interpret bits least-significant first, instead of the default most-significant first (&quot;-reversebits&quot;). Some fax modems do it one way and others do it the other way. If you get a whole bunch of &quot;invalid code&quot; messages (nearly one per line), try using this flag.</p>
<dt><code>-s</code></p>
<dd> Double each horizontal row of the fax file in the pbm file (&quot;-stretch)&quot;. You can use this to adjust the aspect ratio of a &quot;normal resolution&quot; fax file to match that of a &quot;fine resolution&quot; fax file. This might not seem like it belongs here, but it&#8217;s <i>much</i> faster than using pnmscale|pgmtopbm later. <code>-s </code> is activated automatically if the file is specified on the command line and its name starts with &quot;fn&#8230;&quot; (fax/normal).</p>
<dt><code>-l(aserjet)</code></p>
<dd> Instead of a portable bitmap (PBM), output HP laserjet files, suitable for direct printing on a HP laserjet or desjket.</p>
<dt><code>-d &lt;dpi&gt;</code></p>
<dd> Scale output to &lt;dpi&gt; dots per inch before printing. Normal FAX resolution is 204&#215;196 dpi (fine mode), or 204&#215;98 dpi (normal mode). In LaerJet mode, only the values 75, 150 and 300 are allowed for &lt;dpi&gt;.</p>
<dt><code>-t</code></p>
<dd> turn image by 90 degrees clockwise. Multiple -t commands increase angle, that is, -t -t will turn it upside down, and so on.</p>
<dt><code>-?</code></p>
<dd> Print a short command syntax.</dl>
<h2>REFERENCES</h2>
<p> The standard for Group 3 fax is defined in CCITT Recommendation T.4.</p>
<h2>BUGS</h2>
<p> <i>g32pbm</i> could be smarter about the image width, at the moment, the maximum width is 1728 pixels, and the maximum height is 4300 lines. Everything bigger is just cut off. </p>
<p> Only &#8216;raw&#8217; pbm files are created. </p>
<p> Scaling is too slow. </p>
<p> Turning is too slow (and not yet fully implemented either).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pbm2g3/">pbm2g3</a>(1), <a href="/docs/linux/man/5-pbm/">pbm</a>(5), <a href="/docs/linux/man/1-g3cat/">g3cat</a>(1), <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8), <a href="/docs/linux/man/1-mgetty/">mgetty</a>(1)</p>
<h2>AUTHOR</h2>
<p> <i>g32pbm</i> is Copyright (C) 1993 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;. It is similar to the <i>g3topbm</i> program in Jef Poskanzers <i>pbmplus</i> package, but it&#8217;s a complete re-write. No code is copied. </p>
<h2>Index</h2>
