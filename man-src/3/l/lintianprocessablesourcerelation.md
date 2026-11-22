---
title: "lintianprocessablesourcerelation(3)"
name: "lintianprocessablesourcerelation"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablesourcerelation/"
description: "Lintian::Processable::Source::Relation – Lintian interface to source package data collection"
---

<p>Lintian::Processable::Source::Relation &#8211; Lintian interface to source package data collection </p>
<h2>Synopsis</h2>
<pre> my ($name, $type, $dir) = ('foobar', 'source', '/path/to/lab-entry');
 my $collect = Lintian::Processable::Source::Relation-&gt;new($name);
 if ($collect-&gt;native) {
 print &quot;Package is native
&quot;;
 }</pre>
<h2>Description</h2>
<p>Lintian::Processable::Source::Relation provides an interface to package data for source packages. It implements data collection methods specific to source packages. </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about source packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>binary_relation (PACKAGE, FIELD)</dt>
<dd>Returns a Lintian::Relation object for the specified FIELD in the binary package PACKAGE in the <i>debian/control</i> file. FIELD should be one of the possible relationship fields of a Debian package or one of the following special values:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt>all</dt>
<dd>The concatenation of Pre-Depends, Depends, Recommends, and Suggests.</dd>
<dt>strong</dt>
<dd>The concatenation of Pre-Depends and Depends.</dd>
<dt>weak</dt>
<dd>The concatenation of Recommends and Suggests.</dd></dl>
</dl>
<dl COMPACT>
<dd>If FIELD isn&#8217;t present in the package, the returned Lintian::Relation object will be empty (always satisfied and implies nothing). </dd>
<p> Any substvars in <i>debian/control</i> will be represented in the returned relation as packages named after the substvar. </p>
<p> Needs-Info requirements for using <i>binary_relation</i>: Same as binary_field</dl>
<dt>saved_binary_relations</dt>
<dd>
</dd><dt>relation (FIELD)</dt>
<dd>Returns a Lintian::Relation object for the given build relationship field FIELD. In addition to the normal build relationship fields, the following special field names are supported:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt>build-depends-all</dt>
<dd>The concatenation of Build-Depends, Build-Depends-Arch and Build-Depends-Indep.</dd>
<dt>build-conflicts-all</dt>
<dd>The concatenation of Build-Conflicts, Build-Conflicts-Arch and Build-Conflicts-Indep.</dd></dl>
</dl>
<dl COMPACT>
<dd>If FIELD isn&#8217;t present in the package, the returned Lintian::Relation object will be empty (always satisfied and implies nothing).</dd></dl>
<dt>saved_relation</dt>
<dd>
</dd><dt>relation_noarch (FIELD)</dt>
<dd>The same as &#8220;relation (FIELD)&#8221;, but ignores architecture restrictions and build profile restrictions in the FIELD field.</dd>
<dt>saved_relations_noarch</dt>
<dd></dd></dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian. Amended by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
