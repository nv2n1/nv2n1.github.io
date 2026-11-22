---
title: "lintianrelationversion(3)"
name: "lintianrelationversion"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianrelationversion/"
description: "Lintian::Relation::Version – Comparison operators on Debian versions"
---

<p>Lintian::Relation::Version &#8211; Comparison operators on Debian versions </p>
<h2>Synopsis</h2>
<pre> print &quot;yes
&quot; if versions_equal('1.0', '1.00');
 print &quot;yes
&quot; if versions_gte('1.1', '1.0');
 print &quot;no
&quot; if versions_lte('1.1', '1.0');
 print &quot;yes
&quot; if versions_gt('1.1', '1.0');
 print &quot;no
&quot; if versions_lt('1.1', '1.1');
 print &quot;yes
&quot; if versions_compare('1.1', '&lt;=', '1.1');</pre>
<h2>Description</h2>
<p>This module provides five functions for comparing version numbers. The underlying implementation uses <tt>&quot;libapt-pkg-perl&quot;</tt> to ensure that the results match what dpkg will expect.</p>
<h2>Functions</h2>
<dl COMPACT>
<dt>versions_equal(A, B)</dt>
<dd>Returns true if A is equal to B (<tt>&quot;=&quot;</tt>) and false otherwise.</dd>
<dt>versions_lte(A, B)</dt>
<dd>Returns true if A is less than or equal (<tt>&quot;&lt;=&quot;</tt>) to B and false otherwise.</dd>
<dt>versions_gte(A, B)</dt>
<dd>Returns true if A is greater than or equal (<tt>&quot;&gt;=&quot;</tt>) to B and false otherwise.</dd>
<dt>versions_lt(A, B)</dt>
<dd>Returns true if A is less than (<tt>&quot;&lt;&lt;&quot;</tt>) B and false otherwise.</dd>
<dt>versions_gt(A, B)</dt>
<dd>Returns true if A is greater than (<tt>&quot;&gt;&gt;&quot;</tt>) B and false otherwise.</dd>
<dt>versions_compare(A, OP, B)</dt>
<dd>Returns true if A OP B, where OP is one of <tt>&quot;=&quot;</tt>, <tt>&quot;&lt;=&quot;</tt>, <tt>&quot;&gt;=&quot;</tt>, <tt>&quot;&lt;&lt;&quot;</tt>, or <tt>&quot;&gt;&gt;&quot;</tt>, and false otherwise.</dd>
<dt>versions_comparator (A, B)</dt>
<dd>Returns -1, 0 or 1 if the version A is (respectively) less than, equal to or greater than B. This is useful for (e.g.) sorting a list of versions: </dd>
<pre> foreach my $version (sort versions_comparator @versions) {
 ...
 }</pre>
</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian and adapted to use libapt-pkg-perl by Adam D. Barratt &lt;adam [at] adam-barratt-org.uk&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
