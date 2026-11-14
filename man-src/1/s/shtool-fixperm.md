---
title: "shtool-fixperm(1)"
name: "shtool-fixperm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-fixperm/"
description: "shtool fixperm – GNU shtool file permission fixing command"
---

<h2 class="name">NAME</h2>
<p> shtool fixperm &#8211; GNU shtool file permission fixing command </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool fixperm</code> [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-t</code>|<code>&#8211;trace</code>] <i>path</i> [<i>path</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>shtool fixperm</code> fixes file permissions inside a source tree under <i>path</i> by cleaning up the permission bits. It determines the cleaned up permission from the already set bits. It is intended to be run before a tarball is rolled (usually with <code>shtool tarball</code>) out of a source tree. The trick is that this is more convenient than having to set the permissions manually or by using a large file list.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display some processing information.</p>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd> Enable the output of the essential shell commands which are executed.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   Makefile.in
 dist:
     shtool fixperm -v *
     ...
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>fixperm</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1996 for <i></i><font SIZE="-1"><i>OSSP</i></font><i> eperl</i>. It was later taken over into <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1). </p>
<h2>Index</h2>
