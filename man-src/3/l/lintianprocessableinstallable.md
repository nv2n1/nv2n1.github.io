---
title: "lintianprocessableinstallable(3)"
name: "lintianprocessableinstallable"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessableinstallable/"
description: "Lintian::Processable::Installable – Lintian interface to binary package data collection"
---

<p>Lintian::Processable::Installable &#8211; Lintian interface to binary package data collection </p>
<h2>Synopsis</h2>
<pre>
    my ($name, $type, $dir) = ('foobar', 'binary', '/path/to/lab-entry');
    my $collect = Lintian::Processable::Installable-&gt;new($name);
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Installable provides an interface to package data for binary packages. It implements data collection methods specific to binary packages. </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about binary packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory. </p>
<p> Native heuristics are only available in source packages.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>unpack</p>
<dd></dl>
<h2>Author</h2>
<p> Originally written by Frank Lichtenheld &lt;djpig [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
