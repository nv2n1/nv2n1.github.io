---
title: "rpmspec(8)"
name: "rpmspec"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpmspec/"
description: "rpmspec – RPM Spec Tool"
---

<p>rpmspec &#8211; RPM Spec Tool</p>
<h2>Synopsis</h2>
<h3>Querying Spec Files:</h3>
<p><code>rpmspec</code> {<code>-q|&#8211;query</code>} [<code>select-options</code>] [<code>query-options</code>] <i>SPEC_FILE</i><i> &#8230;</i></p>
<h3>select-options</h3>
<p>&nbsp;<wbr>[<code>&#8211;rpms</code>]<br />
&nbsp;<wbr>[<code>&#8211;srpms</code>]</p>
<h3>query-options</h3>
<p>&nbsp;<wbr>[<code>&#8211;qf,&#8211;queryformat&nbsp;<wbr></code><i>QUERYFMT</i>]<br />
&nbsp;<wbr>[<code>&#8211;target&nbsp;<wbr></code><i>TARGET_PLATFORM</i>]<br />
&nbsp;<wbr></p>
<h3>Query Options</h3>
<p>The general form of an rpm spec query command is <code>rpm</code> {<code>-q|&#8211;query</code>} [<code>select-options</code>] [<code>query-options</code>] You may specify the format that the information should be printed in. To do this, you use the<br />
&nbsp;<wbr><code>&#8211;qf|&#8211;queryformat</code>&nbsp;<wbr><i>QUERYFMT</i> option, followed by the <i>QUERYFMT</i> format string. See <code><a href="/docs/linux/man/8-rpm/">rpm</a>(8)</code> for details.</p>
<h3>Select Options</h3>
<p>&nbsp;<wbr><code>&#8211;rpms</code> Operate on the binary package header(s).<br />
&nbsp;<wbr><code>&#8211;srpm</code> Operate on the source package header(s). </p>
<h2>See Also</h2>
<pre><code><a href="//www.systutorials.com/docs/linux/man/3-popt/">popt</a></code>(3),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm/">rpm</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmdb/">rpmdb</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmkeys/">rpmkeys</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmsign/">rpmsign</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm2cpio/">rpm2cpio</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmbuild/">rpmbuild</a></code>(8),</pre>
<p><code>rpmspec &#8211;help</code> &#8211; as rpm supports customizing the options via popt aliases it&#8217;s impossible to guarantee that what&#8217;s described in the manual matches what&#8217;s available. </p>
<p> <code><a rel="nofollow" href="http://www.rpm.org/">http://www.rpm.org/</a> &lt;URL:<a href="http://www.rpm.org/">http://www.rpm.org/</a>&gt; </code></p>
<h2>Authors</h2>
<pre>Marc Ewing &lt;marc [at] redhat.com&gt;
Jeff Johnson &lt;jbj [at] redhat.com&gt;
Erik Troan &lt;ewt [at] redhat.com&gt;
Panu Matilainen &lt;pmatilai [at] redhat.com&gt;</pre>
