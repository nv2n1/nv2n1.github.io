---
title: "lintiantagbearer(3)"
name: "lintiantagbearer"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiantagbearer/"
description: "Lintian::Tag::Bearer — Facilities for objects receiving Lintian tags"
---

<p>Lintian::Tag::Bearer &#8212; Facilities for objects receiving Lintian tags </p>
<h2>Synopsis</h2>
<pre> use Moo;
use namespace::clean;
 with('Lintian::Tag::Bearer');</pre>
<h2>Description</h2>
<p>A class for collecting Lintian tags as they are found</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>tag (<font SIZE="-1">ARGS</font>)</p>
<dd>Store found tags for later processing.</p>
<dt>tags</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
