---
title: "lintianindexinstalled(3)"
name: "lintianindexinstalled"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianindexinstalled/"
description: "Lintian::Index::Installed — An index of an installed file set"
---

<p>Lintian::Index::Installed &#8212; An index of an installed file set </p>
<h2>Synopsis</h2>
<pre> use Lintian::Index::Installed;
 # Instantiate via Lintian::Index::Installed
 my $orig = Lintian::Index::Installed-&gt;new;</pre>
<h2>Description</h2>
<p>Instances of this perl class are objects that hold file indices of installed file sets. The origins of this class can be found in part in the collections scripts used previously.</p>
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
