---
title: "lintianprocessablesource(3)"
name: "lintianprocessablesource"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablesource/"
description: "Lintian::Processable::Source — A dsc source package Lintian can process"
---

<p>Lintian::Processable::Source &#8212; A dsc source package Lintian can process </p>
<h2>Synopsis</h2>
<pre> use Lintian::Processable::Source;
 my $processable = Lintian::Processable::Source-&gt;new;
 $processable-&gt;init('path');</pre>
<h2>Description</h2>
<p>This class represents a &#8216;dsc&#8217; file that Lintian can process. Objects of this kind are often part of a Lintian::Group, which represents all the files in a changes or buildinfo file.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>init (<font SIZE="-1">FILE</font>)</p>
<dd>Initializes a new object from <font SIZE="-1">FILE.</font></p>
<dt>unpack</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1) </p>
<p> Lintian::Processable</p>
