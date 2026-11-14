---
title: "bbox(1)"
name: "bbox"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bbox/"
description: "bbox – prints out the bounding box of a rawppm or rawpbm image"
---

<h2 class="name">NAME</h2>
<p> bbox &#8211; prints out the bounding box of a rawppm or rawpbm image </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bbox</code> [<code>-l</code>] [<code>-r</code>] [<code>-h</code>] [<code>-V</code>] [<i>rawpbmfile</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>bbox</code></p>
<dd>reads a rawppm or rawpbm file and prints out the bounding box of the image (as postscript comment and in postscript points, i.e. 1/72dpi) as well as the high resolution bounding box. Input is read from standard input if no filename is specified. Example output: </p>
<dl>
<dt>
<dd>
<pre>
          %%BoundingBox: 12 253 829 837
          %%HiResBoundingBox: 12.500000 253.000000 828.500000 837.00000
          
</pre>
</dl>
<p> <code>bbox</code> has only very limited memory requirements as it reads the input line by line and thus needs to store only one picture line in memory.</p>
<h2>OPTIONS</h2>
<p> <code>-h | &#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Show version of program.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> resolution of picture in dpi</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> loose bounding box (integer bounding box is expanded by 1 point, hires bounding box is expanded by 0.5 points)</dl>
<h2>SEE ALSO</h2>
<p> ps2eps (1)</p>
<h2>AUTHOR</h2>
<p> <code>bbox</code> was written by Roland Bless.</p>
<h3>ACKNOWLEDGMENTS</h3>
<p> Special thanks goes to Michael Sharpe from UCSD who suggested a lot of improvements for bbox to become more precise and robust, especially for small drawings. </p>
<p> An earlier version of this manual page was originally written by Rafael Laboissiere &lt;rafael [at] debian.org&gt; for the Debian system. Thank you Rafael! Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
<h2>BUGS</h2>
<p> Though the code is quite small and the probability for bugs is now small, there may be some left somewhere between the lines. In case you find one, please send a short description with <code>bbox</code> version number to &lt;roland [at] bless.de&gt; (please allow some time to reply).</p>
<h2>AUTHOR</h2>
<p> <code>Roland Bless</code></p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003 Roland Bless </p>
<h2>Index</h2>
