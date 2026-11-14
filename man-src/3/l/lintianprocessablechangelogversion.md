---
title: "lintianprocessablechangelogversion(3)"
name: "lintianprocessablechangelogversion"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablechangelogversion/"
description: "Lintian::Processable::Changelog::Version – Lintian interface to source package data collection"
---

<p>Lintian::Processable::Changelog::Version &#8211; Lintian interface to source package data collection </p>
<h2>Synopsis</h2>
<pre>
    my ($name, $type, $dir) = ('foobar', 'source', '/path/to/lab-entry');
    my $collect = Lintian::Processable::Changelog::Version-&gt;new($name);
    if ($collect-&gt;native) {
        print &quot;Package is native
&quot;;
    }
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Changelog::Version provides an interface to package data for source packages. It implements data collection methods specific to source packages. </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about source packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>changelog_version</p>
<dd> Returns a fully parsed Lintian::Inspect::Changelog::Version for the source package&#8217;s version string.</dl>
<h2>Author</h2>
<p> Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian. Amended by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
