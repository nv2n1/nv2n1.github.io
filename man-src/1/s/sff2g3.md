---
title: "sff2g3(1)"
name: "sff2g3"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sff2g3/"
description: "sff2g3 – convert CAPI SFF fax files into G3 fax files"
---

<h2 class="name">NAME</h2>
<p> sff2g3 &#8211; convert CAPI SFF fax files into G3 fax files </p>
<h2>SYNOPSIS</h2>
<p> <code>sff2g3</code> [<code>-r</code>] [<code>-d</code>] [<code>-v</code>] <code>input.SFF output.%03d.g3 </code></p>
<h2>DESCRIPTION</h2>
<p> Reads a Common ISDN API (CAPI) structured file format (SFF) input file, and converts every fax page contained in it to a raw G3 fax file. </p>
<p> The input SFF files typically come from fax reception programs using CAPI on active ISDN cards (isdn4linux, AVM or DIVA cards) or similar. The output G3 files are in the &#8220;native&#8221; format that all other G3 utilites in the mgetty+sendfax package use. </p>
<p> If the input file name is &#8220;-&#8221;, <code>sff2g3</code> will read from stdin. </p>
<p> The output file name should contain a &#8220;%d&#8221; or &#8220;%03d&#8221; part. It will be replaced with the current page number. If there is no page number field, only the last page in the SFF file will be saved.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code></p>
<dd> reverse the bit order in the bytes of the output G3 file. The input bit order is fixed.</p>
<dt><code>-d</code></p>
<dd> will one day make sff2g3 prepend a digifax header to the page.</p>
<dt><code>-v</code></p>
<dd> verbose mode &#8211; show what&#8217;s going on. Multiple <code>-v</code> arguments increase debug output level. </p>
</dl>
<h2>REFERENCES</h2>
<p> The standard for Group 3 fax is defined in CCITT Recommendation T.4. The SFF file format is specified in the CAPI specs (<a rel="nofollow" href="http://www.capi.org">http://www.capi.org</a>).</p>
<h2>BUGS</h2>
<p> The -d option isn&#8217;t implemented yet. </p>
<p> The output file name is not yet robust against format string attacks.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-g32pbm/">g32pbm</a>(1), <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> <i>sff2g3</i> is Copyright (C) 2004 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;. </p>
<h2>Index</h2>
