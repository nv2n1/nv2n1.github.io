---
title: "psset(1)"
name: "psset"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psset/"
description: "psset – insert page device request in PostScript files"
---

<h2 class="name">NAME</h2>
<p> psset &#8211; insert page device request in PostScript files </p>
<h2>SYNOPSIS</h2>
<p> <code>psset</code> <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> Produce a version of the PostScript FILE with a protected call to the PostScript operator `setpagedevice&#8217;. Typical use is making FILE print duplex, or on the manual tray etc.</p>
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
<dd> don&#8217;t run `fixps&#8217; to fix PS problems in FILE</p>
<dt><code>-S</code>, <code>&#8211;setpagedevice</code>=<i>KEY[</i>:VALUE]</p>
<dd> pass a page device definition to output. Multiple values accumulate</p>
<dt><code>-a</code>, <code>&#8211;at</code>=<i>PAGE</i></p>
<dd> insert the page device definitions at PAGE. Default is PAGE=0, standing for the Document&#8217;s Setup section</dl>
<h3>Shortcuts:</h3>
<dl>
<dt><code>-m</code>, <code>&#8211;manualfeed</code></p>
<dd> alias for <code>-SManualFeed</code>:true</p>
<dt><code>-s</code>, <code>&#8211;simplex</code></p>
<dd> alias for <code>-SDuplex</code>:false</p>
<dt><code>-d</code>, <code>&#8211;duplex</code></p>
<dd> alias for <code>-SDuplex</code>:true <code>-STumble</code>:false corresponds to Duplex, binding along the long edge</p>
<dt><code>-t</code>, <code>&#8211;tumble</code></p>
<dd> alias for <code>-SDuplex</code>:true <code>-STumble</code>:true corresponds to Duplex, binding along the short edge</dl>
<p> Produced output is meant for PS level 2 printers. </p>
<p> News, updates and documentation: visit <a rel="nofollow" href="http://www.inf.enst.fr/~demaille/a2ps/">http://www.inf.enst.fr/~demaille/a2ps/</a></p>
<h2>AUTHOR</h2>
<p> Written by Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-a2ps [at] gnu.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998-1999 Akim Demaille, Miguel Santana<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-a2ps/">a2ps</a></code>(1), <code><a href="/docs/linux/man/1-card/">card</a></code>(1), <code><a href="/docs/linux/man/1-fixps/">fixps</a></code>(1), <code><a href="/docs/linux/man/1-pdiff/">pdiff</a></code>(1), <code><a href="/docs/linux/man/1-psset/">psset</a></code>(1), <code><a href="/docs/linux/man/1-texi2dvi4a2ps/">texi2dvi4a2ps</a></code>(1). </p>
<p> The full documentation for <code>psset</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>psset</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info psset</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
