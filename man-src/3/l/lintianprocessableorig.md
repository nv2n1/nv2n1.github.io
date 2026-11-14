---
title: "lintianprocessableorig(3)"
name: "lintianprocessableorig"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessableorig/"
description: "Lintian::Processable::Orig – access to collected data about the upstream (orig) sources"
---

<p>Lintian::Processable::Orig &#8211; access to collected data about the upstream (orig) sources </p>
<h2>Synopsis</h2>
<pre>
    use Lintian::Processable;
    my $processable = Lintian::Processable::Binary-&gt;new;
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Orig provides an interface to collected data about the upstream (orig) sources.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>orig</p>
<dd> Returns the index for orig.tar.gz.</p>
<dt>orig_index (<font SIZE="-1">FILE</font>)</p>
<dd> Like &#8220;index&#8221; except orig_index is based on the &#8220;orig tarballs&#8221; of the source packages. </p>
<p> For native packages &#8220;index&#8221; and &#8220;orig_index&#8221; are generally identical. </p>
<p> <font SIZE="-1">NB:</font> If sorted_index includes a debian packaging, it is was contained in upstream part of the source package (or the package is native). </p>
<p> Needs-Info requirements for using <i>orig_index</i>: src-orig-index</p>
<dt>sorted_orig_index</p>
<dd>
<dt>orig_index_resolved_path(<font SIZE="-1">PATH</font>)</p>
<dd> Resolve <font SIZE="-1">PATH</font> (relative to the root of the package) and return the entry denoting the resolved path. </p>
<p> The resolution is done using resolve_path. </p>
<p> <font SIZE="-1">NB:</font> If orig_index_resolved_path includes a debian packaging, it is was contained in upstream part of the source package (or the package is native). </p>
<p> Needs-Info requirements for using <i>orig_index_resolved_path</i>: Same as orig_index</dl>
<h2>Author</h2>
<p> Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
