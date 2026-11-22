---

title: "psset(1)"
name: "psset"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psset/"
description: "psset – insert page device request in PostScript files"
---

<p> psset &#8211; insert page device request in PostScript files </p>
<h2>SYNOPSIS</h2>
<p> <code>psset</code> <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> Produce a version of the PostScript FILE with a protected call to the PostScript operator `setpagedevice&#8217;. Typical use is making FILE print duplex, or on the manual tray etc.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> display version information and exit</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> don&#8217;t print informational messages</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></dt>
<dd> save result in FILE. If FILE is `-&#8216;, send to stdout</dd>
<dt><code>-n</code>, <code>&#8211;no-fix</code></dt>
<dd> don&#8217;t run `fixps&#8217; to fix PS problems in FILE</dd>
<dt><code>-S</code>, <code>&#8211;setpagedevice</code>=<i>KEY[</i>:VALUE]</dt>
<dd> pass a page device definition to output. Multiple values accumulate</dd>
<dt><code>-a</code>, <code>&#8211;at</code>=<i>PAGE</i></dt>
<dd> insert the page device definitions at PAGE. Default is PAGE=0, standing for the Document&#8217;s Setup section</dd></dl>
<h3>Shortcuts:</h3>
<dl>
<dt><code>-m</code>, <code>&#8211;manualfeed</code></dt>
<dd> alias for <code>-SManualFeed</code>:true</dd>
<dt><code>-s</code>, <code>&#8211;simplex</code></dt>
<dd> alias for <code>-SDuplex</code>:false</dd>
<dt><code>-d</code>, <code>&#8211;duplex</code></dt>
<dd> alias for <code>-SDuplex</code>:true <code>-STumble</code>:false corresponds to Duplex, binding along the long edge</dd>
<dt><code>-t</code>, <code>&#8211;tumble</code></dt>
<dd> alias for <code>-SDuplex</code>:true <code>-STumble</code>:true corresponds to Duplex, binding along the short edge</dd></dl>
<p> Produced output is meant for PS level 2 printers. </p>
<p> News, updates and documentation: visit <a rel="nofollow" href="http://www.inf.enst.fr/~demaille/a2ps/">http://www.inf.enst.fr/~demaille/a2ps/</a></p>
<h2>AUTHOR</h2>
<p> Written by Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-a2ps [at] gnu.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998-1999 Akim Demaille, Miguel Santana<br/>
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-a2ps/">a2ps</a></code>(1), <code><a href="/docs/linux/man/1-card/">card</a></code>(1), <code><a href="/docs/linux/man/1-fixps/">fixps</a></code>(1), <code><a href="/docs/linux/man/1-pdiff/">pdiff</a></code>(1), <code><a href="/docs/linux/man/1-psset/">psset</a></code>(1), <code><a href="/docs/linux/man/1-texi2dvi4a2ps/">texi2dvi4a2ps</a></code>(1). </p>
<p> The full documentation for <code>psset</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>psset</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info psset</code></dd></dl>
<p> should give you access to the complete manual. </p>
