---
title: "beagle-dump-index(8)"
name: "beagle-dump-index"
section: "8"
letter: "b"
url: "/docs/linux/man/8-beagle-dump-index/"
description: "beagle-dump-index"
---

<p>beagle-dump-index</p>
<h2>Synopsis</h2>
<p><code>beagle-dump-index</code> [<i>options</i>] [[file or URI to match] &#8230;]</p>
<h2>Description</h2>
<p><code>beagle-dump-index</code> is a low-level tool for examining data indexed by the Beagle search system. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;uris</code></dt>
<dd>Dump all Uris (default)</dd>
<dt><code>&#8211;properties</code></dt>
<dd>Dump all properties</dd>
<dt><code>&#8211;term-frequencies</code></dt>
<dd>Dump term frequencies</dd>
<dt><code>&#8211;fields</code></dt>
<dd>Dump all fields</dd>
<dt><code>&#8211;show-counts</code></dt>
<dd>Show index count totals (default)</dd>
<dt><code>&#8211;hide-counts</code></dt>
<dd>Hide index count totals</dd>
<dt><code>&#8211;index=&lt;index name&gt;</code></dt>
<dd>Limit results to an index by name. May be used multiple times.</dd>
<dt><code>&#8211;indexdir=&lt;directory&gt;</code></dt>
<dd>Limit results to an index specified by absolute path. May be used multiple times. Example path /home/user/.beagle/Indexes/FileSystemIndex</dd>
<dt><code>file or URI to match</code></dt>
<dd>Get information in index about one or more files or URIs. Note this doesn&#8217;t make sense with and will cause an error.</dd></dl>
<h2>Author</h2>
<p>Novell, Inc.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugzilla.gnome.org">http://bugzilla.gnome.org</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2007 Novell, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-beagled/">beagled</a></code>(1), <code><a rel="nofollow" href="http://beagle-project.org">http://beagle-project.org</a></code> </p>
