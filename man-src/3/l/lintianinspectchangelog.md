---
title: "lintianinspectchangelog(3)"
name: "lintianinspectchangelog"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianinspectchangelog/"
description: "Lintian::Inspect::Changelog — Parse a literal version string into its constituents"
---

<p>Lintian::Inspect::Changelog &#8212; Parse a literal version string into its constituents </p>
<h2>Synopsis</h2>
<pre> use Lintian::Inspect::Changelog;
 my $version = Lintian::Inspect::Changelog-&gt;new;
 $version-&gt;set('1.2.3-4', undef);</pre>
<h2>Description</h2>
<p>A class for parsing literal version strings</p>
<h2>Class Methods</h2>
<dl COMPACT>
<dt>new ()</p>
<dd>Creates a new Lintian::Inspect::Changelog object.</p>
<dt>find_closes</p>
<dd>Takes one string as argument and finds &#8220;Closes: #123456, #654321&#8221; statements as supported by the Debian Archive software in it. Returns all closed bug numbers in an array reference.</dl>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>parse (<font SIZE="-1">STRING</font>)</p>
<dd>Parses <font SIZE="-1">STRING</font> as the content of a debian/changelog file.</p>
<dt>errors</p>
<dd>
<dt>entries</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
