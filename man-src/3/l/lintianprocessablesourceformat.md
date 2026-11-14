---
title: "lintianprocessablesourceformat(3)"
name: "lintianprocessablesourceformat"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablesourceformat/"
description: "Lintian::Processable::Source::Format – Lintian interface to source format"
---

<p>Lintian::Processable::Source::Format &#8211; Lintian interface to source format </p>
<h2>Synopsis</h2>
<pre> my $collect = Lintian::Processable::Source::Format-&gt;new;</pre>
<h2>Description</h2>
<p>Lintian::Processable::Source::Format provides an interface to source format information.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>source_format</p>
<dd>
<dt>native</p>
<dd>Returns true if the source package is native and false otherwise. This is generally determined from the source format, though in the 1.0 case the nativeness is determined by looking for the diff.gz (using the name of the source package and its version). </p>
<p> If the source format is 1.0 and the version number is absent, this will return false (as native packages are a lot rarer than non-native ones). </p>
<p> Note if the source format is missing, it is assumed to be a 1.0 package.</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian. Amended by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1), <code><a href="/docs/linux/man/3-lintian--relation/">Lintian::Relation</a></code>(3)</p>
