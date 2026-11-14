---
title: "lintianindexpatched(3)"
name: "lintianindexpatched"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianindexpatched/"
description: "Lintian::Index::Patched — An index of a patched file set"
---

<p>Lintian::Index::Patched &#8212; An index of a patched file set </p>
<h2>Synopsis</h2>
<pre> use Lintian::Index::Patched;
 # Instantiate via Lintian::Index::Patched
 my $orig = Lintian::Index::Patched-&gt;new;</pre>
<h2>Description</h2>
<p>Instances of this perl class are objects that hold file indices of patched file sets. The origins of this class can be found in part in the collections scripts used previously.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>collect</p>
<dd>
<dt>unpack</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian. Substantial portions adapted from code written by Russ Allbery, Niels Thykier, and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1) </p>
<p> Lintian::Index</p>
