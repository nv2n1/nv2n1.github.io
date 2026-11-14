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
<dt>binary_relation (<font SIZE="-1">PACKAGE, FIELD</font>)</p>
<dd>Returns a Lintian::Relation object for the specified <font SIZE="-1">FIELD</font> in the binary package <font SIZE="-1">PACKAGE</font> in the <i>debian/control</i> file. <font SIZE="-1">FIELD</font> should be one of the possible relationship fields of a Debian package or one of the following special values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>all</p>
<dd>The concatenation of Pre-Depends, Depends, Recommends, and Suggests.</p>
<dt>strong</p>
<dd>The concatenation of Pre-Depends and Depends.</p>
<dt>weak</p>
<dd>The concatenation of Recommends and Suggests.</dl>
</dl>
<dl COMPACT>
<dd>If <font SIZE="-1">FIELD</font> isn&#8217;t present in the package, the returned Lintian::Relation object will be empty (always satisfied and implies nothing). </p>
<p> Any substvars in <i>debian/control</i> will be represented in the returned relation as packages named after the substvar. </p>
<p> Needs-Info requirements for using <i>binary_relation</i>: Same as binary_field</dl>
<dt>saved_binary_relations</p>
<dd>
<dt>relation (<font SIZE="-1">FIELD</font>)</p>
<dd>Returns a Lintian::Relation object for the given build relationship field <font SIZE="-1">FIELD.</font> In addition to the normal build relationship fields, the following special field names are supported:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>build-depends-all</p>
<dd>The concatenation of Build-Depends, Build-Depends-Arch and Build-Depends-Indep.</p>
<dt>build-conflicts-all</p>
<dd>The concatenation of Build-Conflicts, Build-Conflicts-Arch and Build-Conflicts-Indep.</dl>
</dl>
<dl COMPACT>
<dd>If <font SIZE="-1">FIELD</font> isn&#8217;t present in the package, the returned Lintian::Relation object will be empty (always satisfied and implies nothing).</dl>
<dt>saved_relation</p>
<dd>
<dt>relation_noarch (<font SIZE="-1">FIELD</font>)</p>
<dd>The same as &#8220;relation (<font SIZE="-1">FIELD</font>)&#8221;, but ignores architecture restrictions and build profile restrictions in the <font SIZE="-1">FIELD</font> field.</p>
<dt>saved_relations_noarch</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian. Amended by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
