---
title: "lintianindexorig(3)"
name: "lintianindexorig"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianindexorig/"
description: "Lintian::Index::Orig — An index of an upstream (orig) file set"
---

<p>Lintian::Index::Orig &#8212; An index of an upstream (orig) file set </p>
<h2>Synopsis</h2>
<pre> use Lintian::Index::Orig;
 # Instantiate via Lintian::Index::Orig
 my $orig = Lintian::Index::Orig-&gt;new;</pre>
<h2>Description</h2>
<p>Instances of this perl class are objects that hold file indices of upstream file sets. The origins of this class can be found in part in the collections scripts used previously.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>collect</p>
<dd>
<dt>create</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian. Substantial portions adapted from code written by Russ Allbery, Niels Thykier, and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1) </p>
<p> Lintian::Index</p>
