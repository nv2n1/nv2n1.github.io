---

title: "pdiff(1)"
name: "pdiff"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdiff/"
description: "pdiff – produce a pretty comparison between files"
---

<p> pdiff &#8211; produce a pretty comparison between files </p>
<h2>SYNOPSIS</h2>
<p> <code>pdiff</code> <i>FILE1 FILE2 </i>[<i>&#8212; A2PS-OPTIONS</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Pretty print the differences between FILE1 and FILE2.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> display version information and exit</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> don&#8217;t print informational messages</dd>
<dt><code>-l</code>, <code>&#8211;lines</code></dt>
<dd> search for line differences (`diff&#8217;)</dd>
<dt><code>-w</code>, <code>&#8211;words</code></dt>
<dd> search for word differences (`wdiff&#8217;)</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></dt>
<dd> save the output in FILE</dd></dl>
<p> Options for a2ps are given after `&#8211;&#8216;, for instance</p>
<dl>
<dt>
</dt><dd> <tt>$ pdiff COPYING COPYING.LIB -- -Pdisplay</tt></dd></dl>
<p> News, updates and documentation: <a rel="nofollow" href="http://www.inf.enst.fr/~demaille/a2ps/.">http://www.inf.enst.fr/~demaille/a2ps/.</a></p>
<h2>AUTHOR</h2>
<p> Written by Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-a2ps [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997-1999 Akim Demaille, Miguel Santana<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-a2ps/">a2ps</a></code>(1), <code><a href="/docs/linux/man/1-card/">card</a></code>(1), <code><a href="/docs/linux/man/1-fixps/">fixps</a></code>(1), <code><a href="/docs/linux/man/1-pdiff/">pdiff</a></code>(1), <code><a href="/docs/linux/man/1-psset/">psset</a></code>(1), <code><a href="/docs/linux/man/1-texi2dvi4a2ps/">texi2dvi4a2ps</a></code>(1). </p>
<p> The full documentation for <code>pdiff</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>pdiff</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info pdiff</code></dd></dl>
<p> should give you access to the complete manual. </p>
