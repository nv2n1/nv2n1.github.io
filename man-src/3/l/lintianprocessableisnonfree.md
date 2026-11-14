---
title: "lintianprocessableisnonfree(3)"
name: "lintianprocessableisnonfree"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessableisnonfree/"
description: "Lintian::Processable::IsNonFree – Lintian interface to source package data collection"
---

<p>Lintian::Processable::IsNonFree &#8211; Lintian interface to source package data collection </p>
<h2>Synopsis</h2>
<pre>
    my ($name, $type, $dir) = ('foobar', 'source', '/path/to/lab-entry');
    my $collect = Lintian::Processable::IsNonFree-&gt;new($name);
    if ($collect-&gt;native) {
        print &quot;Package is native
&quot;;
    }
</pre>
<h2>Description</h2>
<p> Lintian::Processable::IsNonFree provides an interface to package data for source packages. It implements data collection methods specific to source packages. </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about source packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>is_non_free</p>
<dd> Returns a truth value if the package appears to be non-free (based on the section field; &#8220;non-free/*&#8221; and &#8220;restricted/*&#8221;)</dl>
<h2>Author</h2>
<p> Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian. Amended by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
