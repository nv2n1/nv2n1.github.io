---
title: "psmandup(1)"
name: "psmandup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psmandup/"
description: "psmandup – print duplex on non duplex printers"
---

<h2 class="name">NAME</h2>
<p> psmandup &#8211; print duplex on non duplex printers </p>
<h2>SYNOPSIS</h2>
<p> <code>psmandup</code> <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> Tries to produce a version of the PostScript FILE to print in manual Duplex.</p>
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
<dt><code>-n</code>, <code>&#8211;no-fix</code></p>
<dd> don&#8217;t call fixps to fix PS problems in FILE</p>
<dt><code>-f</code>, <code>&#8211;front</code></p>
<dd> output only the front pages (recto) on the regular tray</p>
<dt><code>-b</code>, <code>&#8211;back</code></p>
<dd> output only the back pages (verso) on the manual feed tray</dl>
<p> Produced output is meant for PS level 2 printers which don&#8217;t support Duplex printing, but support Manual Feed. Once the first set of pages is printed (odd pages), manual feed is asked: introduce the odd pages to print the even pages on the other side. </p>
<p> Because there is usually a short time out for manually fed jobs, you should really be next to the printer. If ever the time out expired, use the option <code>-b</code> to send only the missing part. </p>
<p> Environment variables FIXPS, PSSELECT and PSSET, if defined, are used to find the tools. </p>
<p> News, updates and documentation: <a rel="nofollow" href="http://www.inf.enst.fr/~demaille/a2ps/">http://www.inf.enst.fr/~demaille/a2ps/</a></p>
<h2>AUTHOR</h2>
<p> Written by Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-a2ps [at] gnu.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998-1999 Akim Demaille, Miguel Santana<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-a2ps/">a2ps</a></code>(1), <code><a href="/docs/linux/man/1-card/">card</a></code>(1), <code><a href="/docs/linux/man/1-fixps/">fixps</a></code>(1), <code><a href="/docs/linux/man/1-pdiff/">pdiff</a></code>(1), <code><a href="/docs/linux/man/1-psset/">psset</a></code>(1), <code><a href="/docs/linux/man/1-texi2dvi4a2ps/">texi2dvi4a2ps</a></code>(1). </p>
<p> The full documentation for <code>psmandup</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>psmandup</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info psmandup</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
