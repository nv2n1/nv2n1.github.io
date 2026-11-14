---
title: "rpmdb(8)"
name: "rpmdb"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpmdb/"
description: "rpmdb – RPM Database Tool"
---

<p>rpmdb &#8211; RPM Database Tool</p>
<h2>Synopsis</h2>
<p><code>rpm</code> {<code>&#8211;initdb|&#8211;rebuilddb</code>} </p>
<h2>Description</h2>
<p>The general form of an rpm rebuild database command is <code>rpm</code> {<code>&#8211;initdb|&#8211;rebuilddb</code>} [<code>-v</code>] [<code>&#8211;dbpath </code><i>DIRECTORY</i>] [<code>&#8211;root </code><i>DIRECTORY</i>] Use <code>&#8211;initdb</code> to create a new database if one doesn&#8217;t already exist (existing database is not overwritten), use <code>&#8211;rebuilddb</code> to rebuild the database indices from the installed package headers. </p>
<h2>See Also</h2>
<pre><code><a href="//www.systutorials.com/docs/linux/man/3-popt/">popt</a></code>(3),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm/">rpm</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmkeys/">rpmkeys</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmsign/">rpmsign</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm2cpio/">rpm2cpio</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmbuild/">rpmbuild</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmspec/">rpmspec</a></code>(8),</pre>
<p><code>rpm &#8211;help</code> &#8211; as rpm supports customizing the options via popt aliases it&#8217;s impossible to guarantee that what&#8217;s described in the manual matches what&#8217;s available. </p>
<p> <code><a rel="nofollow" href="http://www.rpm.org/">http://www.rpm.org/</a> &lt;URL:<a href="http://www.rpm.org/">http://www.rpm.org/</a>&gt; </code></p>
<h2>Authors</h2>
<pre>Marc Ewing &lt;marc [at] redhat.com&gt;
Jeff Johnson &lt;jbj [at] redhat.com&gt;
Erik Troan &lt;ewt [at] redhat.com&gt;
Panu Matilainen &lt;pmatilai [at] redhat.com&gt;</pre>
