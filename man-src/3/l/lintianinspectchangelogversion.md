---
title: "lintianinspectchangelogversion(3)"
name: "lintianinspectchangelogversion"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianinspectchangelogversion/"
description: "Lintian::Inspect::Changelog::Version — Parse a literal version string into its constituents"
---

<p>Lintian::Inspect::Changelog::Version &#8212; Parse a literal version string into its constituents </p>
<h2>Synopsis</h2>
<pre> use Lintian::Inspect::Changelog::Version;
 my $version = Lintian::Inspect::Changelog::Version-&gt;new;
 $version-&gt;set('1.2.3-4', undef);</pre>
<h2>Description</h2>
<p>A class for parsing literal version strings</p>
<h2>Class Methods</h2>
<dl COMPACT>
<dt>new ()</dt>
<dd>Creates a new Lintian::Inspect::Changelog::Version object.</dd></dl>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>set (<font SIZE="-1">LITERAL, NATIVE</font>)</dt>
<dd>Set the various members in the Lintian::Inspect::Changelog::Version object using the <font SIZE="-1">LITERAL</font> version string and the <font SIZE="-1">NATIVE</font> boolean selector.</dd>
<dt>literal</dt>
<dd>
</dd><dt>epoch</dt>
<dd>
</dd><dt>no_epoch</dt>
<dd>
</dd><dt>upstream</dt>
<dd>
</dd><dt>maintainer_revision</dt>
<dd>
</dd><dt>debian_source</dt>
<dd>
</dd><dt>debian_no_epoch</dt>
<dd>
</dd><dt>source_nmu</dt>
<dd>
</dd><dt>binary_nmu</dt>
<dd>
</dd><dt>without_source_nmu</dt>
<dd>
</dd><dt>debian_without_backport</dt>
<dd>
</dd><dt>backport_release</dt>
<dd>
</dd><dt>backport_revision</dt>
<dd>
</dd><dt>without_backport</dt>
<dd></dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
