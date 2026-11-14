---
title: "lintianprocessablebinaryclass(3)"
name: "lintianprocessablebinaryclass"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablebinaryclass/"
description: "Lintian::Processable::Binary::Class – Lintian interface to binary package data collection"
---

<p>Lintian::Processable::Binary::Class &#8211; Lintian interface to binary package data collection </p>
<h2>Synopsis</h2>
<pre> my ($name, $type, $dir) = ('foobar', 'binary', '/path/to/lab-entry');
 my $collect = Lintian::Processable::Binary::Class-&gt;new($name);</pre>
<h2>Description</h2>
<p>Lintian::Processable::Binary::Class provides an interface to package data for binary packages. It implements data collection methods specific to binary packages. </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about binary packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory. </p>
<p> Native heuristics are only available in source packages.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>is_pkg_class ([<font SIZE="-1">TYPE</font>])</p>
<dd>Returns a truth value if the package is the given <font SIZE="-1">TYPE</font> of special package. <font SIZE="-1">TYPE</font> can be one of &#8220;transitional&#8221;, &#8220;debug&#8221; or &#8220;any-meta&#8221;. If omitted it defaults to &#8220;any-meta&#8221;. The semantics for these values are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>transitional</p>
<dd>The package is (probably) a transitional package (e.g. it is probably empty, just depend on stuff will eventually disappear.) </p>
<p> Guessed from package description.</p>
<dt>any-meta</p>
<dd>This package is (probably) some kind of meta or task package. A meta package is usually empty and just depend on stuff. It will also return a truth value for &#8220;tasks&#8221; (i.e. tasksel &#8220;tasks&#8221;). </p>
<p> A transitional package will also match this. </p>
<p> Guessed from package description, section or package name.</p>
<dt>debug</p>
<dd>The package is (probably) a package containing debug symbols. </p>
<p> Guessed from the package name.</p>
<dt>auto-generated</p>
<dd>The package is (probably) a package generated automatically (e.g. a dbgsym package) </p>
<p> Guessed from the &#8220;Auto-Built-Package&#8221; field.</dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h2>Author</h2>
<p>Originally written by Frank Lichtenheld &lt;djpig [at] debian.org&gt; for Lintian. Amended by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
