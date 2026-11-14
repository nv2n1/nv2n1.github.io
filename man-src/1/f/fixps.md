---
title: "fixps(1)"
name: "fixps"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fixps/"
description: "fixps – sanitize PostScript files"
---

<h2 class="name">NAME</h2>
<p> fixps &#8211; sanitize PostScript files </p>
<h2>SYNOPSIS</h2>
<p> <code>fixps</code> [<i>OPTIONS</i>] <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> Try to fix common PostScript problems that break postprocessing.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> display version information and exit</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> don&#8217;t print informational messages</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> save result in FILE. If FILE is `-&#8216;, send to stdout</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> force full rewrite by ghostscript</p>
<dt><code>-n</code>, <code>&#8211;no-fix</code></p>
<dd> don&#8217;t fix the FILE, but still honor `-o&#8217;</p>
<dt><code>-c</code>, <code>&#8211;check</code>, <code>&#8211;dry-run</code></p>
<dd> don&#8217;t perform any action</dl>
<h3>Fixes:</h3>
<dl>
<dt>
<dd> &#8211; Remove junk before and after PostScript content &#8211; Use only Unix end of lines (</dl>
<p> )</p>
<dl>
<dt>
<dd> &#8211; Remove empty lines &#8211; Fix Apple prologue (fixmacps) &#8211; Fix FrameMaker prologue (fixfmps) &#8211; Fix CorelDraw prologue (fixnt) &#8211; Fix Windows NT 3.5/4.0 prologue (fixnt) &#8211; Fix Windows 95 prologue &#8211; Ensure there is a `%%BeginSetup/%%EndSetup&#8217; section &#8211; Removes Canvas&#8217; extraneaous `%%EndDocument:&#8217; comments &#8211; Split too long lines</dl>
<p> If the FILE seems really in a bad state, ghostscript may be used to perform a full rewrite. The output might then be significantly bigger, but much safer.</p>
<h2>AUTHOR</h2>
<p> Written by Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-a2ps [at] gnu.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998-2000 Akim Demaille, Miguel Santana<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-a2ps/">a2ps</a></code>(1), <code><a href="/docs/linux/man/1-card/">card</a></code>(1), <code><a href="/docs/linux/man/1-fixps/">fixps</a></code>(1), <code><a href="/docs/linux/man/1-pdiff/">pdiff</a></code>(1), <code><a href="/docs/linux/man/1-psset/">psset</a></code>(1), <code><a href="/docs/linux/man/1-texi2dvi4a2ps/">texi2dvi4a2ps</a></code>(1). </p>
<p> The full documentation for <code>fixps</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>fixps</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info fixps</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
