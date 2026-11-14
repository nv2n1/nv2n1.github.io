---
title: "lintianprocessablesourcefields(3)"
name: "lintianprocessablesourcefields"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablesourcefields/"
description: "Lintian::Processable::Source::Fields – Lintian interface to source package data collection"
---

<p>Lintian::Processable::Source::Fields &#8211; Lintian interface to source package data collection </p>
<h2>Synopsis</h2>
<pre> my ($name, $type, $dir) = ('foobar', 'source', '/path/to/lab-entry');
 my $collect = Lintian::Processable::Source::Fields-&gt;new($name);
 if ($collect-&gt;native) {
 print &quot;Package is native
&quot;;
 }</pre>
<h2>Description</h2>
<p>Lintian::Processable::Source::Fields provides an interface to package data for source packages. It implements data collection methods specific to source packages. </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about source packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>binaries</p>
<dd>Returns a list of the binary and udeb packages listed in the <i>debian/control</i>. Package names appear the same order in the returned list as they do in the control file. </p>
<p> <i>Note</i>: Package names that are not valid are silently ignored. </p>
<p> Needs-Info requirements for using <i>binaries</i>: Same as binary_package_type</p>
<dt>binary_package_type (<font SIZE="-1">BINARY</font>)</p>
<dd>Returns package type based on value of the Package-Type (or if absent, X-Package-Type) field. If the field is omitted, the default value &#8220;deb&#8221; is used. </p>
<p> If the <font SIZE="-1">BINARY</font> is not a binary listed in the source packages <i>debian/control</i> file, this method return <tt>&quot;undef&quot;</tt>. </p>
<p> Needs-Info requirements for using <i>binary_package_type</i>: Same as binary_field</p>
<dt>source_field([FIELD[, <font SIZE="-1">DEFAULT</font>]])</p>
<dd>Returns the content of the field <font SIZE="-1">FIELD</font> from source package paragraph of the <i>debian/control</i> file, or <font SIZE="-1">DEFAULT</font> (defaulting to <tt>&quot;undef&quot;</tt>) if the field is not present. Only the literal value of the field is returned. </p>
<p> If <font SIZE="-1">FIELD</font> is not given, return a hashref mapping field names to their values (in this case <font SIZE="-1">DEFAULT</font> is ignored). This hashref should not be modified. </p>
<p> <font SIZE="-1">NB:</font> If a field from the &#8220;dsc&#8221; file itself is desired, please use field instead.</p>
<dt>binary_field (PACKAGE[, FIELD[, <font SIZE="-1">DEFAULT</font>]])</p>
<dd>Returns the content of the field <font SIZE="-1">FIELD</font> for the binary package <font SIZE="-1">PACKAGE</font> in the <i>debian/control</i> file, or <font SIZE="-1">DEFAULT</font> (defaulting to <tt>&quot;undef&quot;</tt>) if the field is not present. Inheritance of field values from the source section of the control file is not implemented. Only the literal value of the field is returned. </p>
<p> If <font SIZE="-1">FIELD</font> is not given, return a hashref mapping field names to their values (in this case, <font SIZE="-1">DEFAULT</font> is ignored). This hashref should not be modified. </p>
<p> If <font SIZE="-1">PACKAGE</font> is not a binary built from this source, this returns <font SIZE="-1">DEFAULT.</font></p>
<dt>load_debian_control</p>
<dd>
<dt>binaries_data =item binary_names =item binary_fields =item source_fields</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian. Amended by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
