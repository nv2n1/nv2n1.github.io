---
title: "lintianindex(3)"
name: "lintianindex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianindex/"
description: "Lintian::Index – access to collected data about the upstream (orig) sources"
---

<p>Lintian::Index &#8211; access to collected data about the upstream (orig) sources </p>
<h2>Synopsis</h2>
<pre> use Lintian::Processable;
 my $processable = Lintian::Processable::Binary-&gt;new;</pre>
<h2>Description</h2>
<p>Lintian::Processable::Orig::Index provides an interface to collected data about the upstream (orig) sources.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>catalog</dt>
<dd>Returns a reference to a hash with elements catalogued by path names.</dd>
<dt>saved_sorted_list</dt>
<dd>Returns a reference to a sorted array with path names.</dd>
<dt>&quot;basedir&quot;</dt>
<dd>Returns the base directory for file references.</dd>
<dt>&quot;anchored&quot;</dt>
<dd>
</dd><dt>&quot;allow_empty&quot;</dt>
<dd>
</dd><dt>sorted_list</dt>
<dd>
</dd><dt>lookup (<font SIZE="-1">FILE</font>)</dt>
<dd>Like &#8220;index&#8221; except orig_index is based on the &#8220;orig tarballs&#8221; of the source packages. </dd>
<p> For native packages &#8220;index&#8221; and &#8220;orig_index&#8221; are generally identical. </p>
<p> <font SIZE="-1">NB:</font> If sorted_index includes a debian packaging, it is was contained in upstream part of the source package (or the package is native). </p>
<p> Needs-Info requirements for using <i>orig_index</i>: src-orig-index</p>
<dt>resolve_path</dt>
<dd>
</dd><dt>load</dt>
<dd></dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
