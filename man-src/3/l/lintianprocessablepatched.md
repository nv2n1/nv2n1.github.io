---
title: "lintianprocessablepatched(3)"
name: "lintianprocessablepatched"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablepatched/"
description: "Lintian::Processable::Patched – access to sources with Debian patches applied"
---

<p>Lintian::Processable::Patched &#8211; access to sources with Debian patches applied </p>
<h2>Synopsis</h2>
<pre>
    use Lintian::Processable;
    my $processable = Lintian::Processable::Binary-&gt;new;
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Patched provides an interface to collected data about patched sources.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>patched</p>
<dd> Returns a index object representing a patched source tree.</p>
<dt>index (<font SIZE="-1">FILE</font>)</p>
<dd> The index of a source package is not very well defined for non-native source packages. This method gives the index of the &#8220;unpacked&#8221; package (with 3.0 (quilt), this implies patches have been applied). </p>
<p> If you want the index of what is listed in the upstream orig tarballs, then there is &#8220;orig_index&#8221;. </p>
<p> For native packages, the two indices are generally the same as they only have one tarball and their debian packaging is included in that tarball. </p>
<p> <font SIZE="-1">IMPLEMENTATION DETAIL/CAVEAT:</font> Lintian currently (2.5.11) generates this by running &#8220;<code><a href="/docs/linux/man/1-find/">find</a></code>(1)&#8221; after unpacking the source package. This has three consequences. </p>
<p> First it means that (original) owner/group data is lost; Lintian inserts &#8220;root/root&#8221; here. This is usually not a problem as owner/group information for source packages do not really follow any standards. </p>
<p> Secondly, permissions are modified by A) umask and B) laboratory set{g,u}id bits (the laboratory on lintian.d.o has setgid). This is *not* corrected/altered. Note Lintian (usually) breaks if any of the &#8220;user&#8221; bits are set in the umask, so that part of the permission bit <i>should</i> be reliable. </p>
<p> Again, this shouldn&#8217;t be a problem as permissions in source packages are usually not important. Though if accuracy is needed here, &#8220;orig_index&#8221; may used instead (assuming it has the file in question). </p>
<p> Third, hardlinking information is lost and no attempt has been made to restore it. </p>
<p> Needs-Info requirements for using <i>index</i>: unpacked</p>
<dt>sorted_index</p>
<dd> Returns a sorted array of file names listed in the package. The names will not have a leading slash (or &#8220;./&#8221;) and can be passed to &#8220;unpacked ([<font SIZE="-1">FILE</font>])&#8221; or &#8220;index (<font SIZE="-1">FILE</font>)&#8221; as is. </p>
<p> The array will not contain the entry for the &#8220;root&#8221; of the package.</p>
<dt>index_resolved_path(<font SIZE="-1">PATH</font>)</p>
<dd> Resolve <font SIZE="-1">PATH</font> (relative to the root of the package) and return the entry denoting the resolved path. </p>
<p> The resolution is done using resolve_path.</dl>
<h2>Author</h2>
<p> Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
