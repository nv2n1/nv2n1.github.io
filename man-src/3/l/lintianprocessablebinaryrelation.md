---
title: "lintianprocessablebinaryrelation(3)"
name: "lintianprocessablebinaryrelation"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablebinaryrelation/"
description: "Lintian::Processable::Binary::Relation – Lintian interface to binary package data collection"
---

<p>Lintian::Processable::Binary::Relation &#8211; Lintian interface to binary package data collection </p>
<h2>Synopsis</h2>
<pre>
    my ($name, $type, $dir) = ('foobar', 'binary', '/path/to/lab-entry');
    my $collect = Lintian::Processable::Binary::Relation-&gt;new($name);
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Binary::Relation provides an interface to package data for binary packages. It implements data collection methods specific to binary packages. </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about binary packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory. </p>
<p> Native heuristics are only available in source packages.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>relation (<font SIZE="-1">FIELD</font>)</p>
<dd> Returns a Lintian::Relation object for the specified <font SIZE="-1">FIELD,</font> which should be one of the possible relationship fields of a Debian package or one of the following special values:</p>
<dl COMPACT>
<dt>
<dd>
<dl COMPACT>
<dt>all</p>
<dd> The concatenation of Pre-Depends, Depends, Recommends, and Suggests.</p>
<dt>strong</p>
<dd> The concatenation of Pre-Depends and Depends.</p>
<dt>weak</p>
<dd> The concatenation of Recommends and Suggests.</dl>
</dl>
<dl COMPACT>
<dt>
<dd>
<p> If <font SIZE="-1">FIELD</font> isn&#8217;t present in the package, the returned Lintian::Relation object will be empty (always satisfied and implies nothing).</dl>
<dt>saved_relations</p>
<dd></dl>
<h2>Author</h2>
<p> Originally written by Frank Lichtenheld &lt;djpig [at] debian.org&gt; for Lintian. Amended by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
