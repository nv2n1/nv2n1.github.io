---
title: "lintianprocessablebinary(3)"
name: "lintianprocessablebinary"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablebinary/"
description: "Lintian::Processable::Binary — A deb installation package Lintian can process"
---

<p>Lintian::Processable::Binary &#8212; A deb installation package Lintian can process </p>
<h2>Synopsis</h2>
<pre> use Lintian::Processable::Binary;
 my $processable = Lintian::Processable::Binary-&gt;new;
 $processable-&gt;init('path');</pre>
<h2>Description</h2>
<p>This class represents a &#8216;deb&#8217; file that Lintian can process. Objects of this kind are often part of a Lintian::Group, which represents all the files in a changes or buildinfo file.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>init (<font SIZE="-1">FILE</font>)</p>
<dd>Initializes a new object from <font SIZE="-1">FILE.</font></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1) </p>
<p> Lintian::Processable</p>
