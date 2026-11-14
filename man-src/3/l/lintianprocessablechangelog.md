---
title: "lintianprocessablechangelog(3)"
name: "lintianprocessablechangelog"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablechangelog/"
description: "Lintian::Processable::Changelog – access to collected changelog data"
---

<p>Lintian::Processable::Changelog &#8211; access to collected changelog data </p>
<h2>Synopsis</h2>
<pre>
    use Lintian::Processable;
    my $processable = Lintian::Processable::Binary-&gt;new;
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Changelog provides an interface to changelog data.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>changelog</p>
<dd> For binary: </p>
<p> Returns the changelog of the binary package as a Parse::DebianChangelog object, or undef if the changelog doesn&#8217;t exist. The changelog-file collection script must have been run to create the changelog file, which this method expects to find in <i>changelog</i>. </p>
<p> Needs-Info requirements for using <i>changelog</i>: changelog-file </p>
<p> For source: </p>
<p> Returns the changelog of the source package as a Parse::DebianChangelog object, or <tt>&quot;undef&quot;</tt> if the changelog cannot be resolved safely.</p>
<dt>saved_changelog</p>
<dd> Returns the cached changelog information.</dl>
<h2>Author</h2>
<p> Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
