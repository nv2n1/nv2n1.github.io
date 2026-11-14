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
<dt>catalog</p>
<dd>Returns a reference to a hash with elements catalogued by path names.</p>
<dt>saved_sorted_list</p>
<dd>Returns a reference to a sorted array with path names.</p>
<dt>&quot;basedir&quot;</p>
<dd>Returns the base directory for file references.</p>
<dt>&quot;anchored&quot;</p>
<dd>
<dt>&quot;allow_empty&quot;</p>
<dd>
<dt>sorted_list</p>
<dd>
<dt>lookup (<font SIZE="-1">FILE</font>)</p>
<dd>Like &#8220;index&#8221; except orig_index is based on the &#8220;orig tarballs&#8221; of the source packages. </p>
<p> For native packages &#8220;index&#8221; and &#8220;orig_index&#8221; are generally identical. </p>
<p> <font SIZE="-1">NB:</font> If sorted_index includes a debian packaging, it is was contained in upstream part of the source package (or the package is native). </p>
<p> Needs-Info requirements for using <i>orig_index</i>: src-orig-index</p>
<dt>resolve_path</p>
<dd>
<dt>load</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
