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
<dt>new ()</p>
<dd>Creates a new Lintian::Inspect::Changelog::Version object.</dl>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>set (<font SIZE="-1">LITERAL, NATIVE</font>)</p>
<dd>Set the various members in the Lintian::Inspect::Changelog::Version object using the <font SIZE="-1">LITERAL</font> version string and the <font SIZE="-1">NATIVE</font> boolean selector.</p>
<dt>literal</p>
<dd>
<dt>epoch</p>
<dd>
<dt>no_epoch</p>
<dd>
<dt>upstream</p>
<dd>
<dt>maintainer_revision</p>
<dd>
<dt>debian_source</p>
<dd>
<dt>debian_no_epoch</p>
<dd>
<dt>source_nmu</p>
<dd>
<dt>binary_nmu</p>
<dd>
<dt>without_source_nmu</p>
<dd>
<dt>debian_without_backport</p>
<dd>
<dt>backport_release</p>
<dd>
<dt>backport_revision</p>
<dd>
<dt>without_backport</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
