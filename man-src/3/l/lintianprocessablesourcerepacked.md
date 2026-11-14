---
title: "lintianprocessablesourcerepacked(3)"
name: "lintianprocessablesourcerepacked"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablesourcerepacked/"
description: "Lintian::Processable::Source::Repacked – Lintian interface to source package data collection"
---

<p>Lintian::Processable::Source::Repacked &#8211; Lintian interface to source package data collection </p>
<h2>Synopsis</h2>
<pre> my ($name, $type, $dir) = ('foobar', 'source', '/path/to/lab-entry');
 my $collect = Lintian::Processable::Source::Repacked-&gt;new($name);
 if ($collect-&gt;native) {
 print &quot;Package is native
&quot;;
 }</pre>
<h2>Description</h2>
<p>Lintian::Processable::Source::Repacked provides an interface to package data for source packages. It implements data collection methods specific to source packages. </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about source packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>repacked</p>
<dd>Returns true if the source package has been &#8220;repacked&#8221; and false otherwise. This is determined from the version name containing &#8220;dfsg&#8221; or similar.</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian. Amended by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
