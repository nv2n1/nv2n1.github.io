---
title: "beagle-build-index(8)"
name: "beagle-build-index"
section: "8"
letter: "b"
url: "/docs/linux/man/8-beagle-build-index/"
description: "beagle-build-index"
---

<p>beagle-build-index</p>
<h2>Synopsis</h2>
<p><code>beagle-build-index</code> [<i>options</i>] &lt;<i>index_path</i>&gt; &lt;<i>path</i>&gt; [<i>path path path</i>]</p>
<h2>Description</h2>
<p><code>beagle-build-index</code>, is a tool designed for building static indexes outside of the Beagle daemon. </p>
<p> Running <code>beagle-build-index</code> by hand is of use for those wishing to create and build static indexes used by the Beagle daemon. The static indexes can be helpful in many cases but most notably used as system-wide indexes shared by all users, and as a way for system-administrators to run indexing on a central server in a network environment. </p>
<p> <code>beagle-build-index</code> will index the data specified by the <i>path</i> arguments and create an index in the <i>index_path</i> directory. If a suitable index is found in the index directory, it will automatically append data to the index if the file at hand has been modified since it was last indexed. If it can&#8217;t find a suitable index (non-existant or version-mismatch) is will purge the directory recursively. </p>
<p> The <code>beagle-build-index</code> tool is not intended to be invoked by the standard user.</p>
<h2>Options</h2>
<p><code>beagle-build-index</code> takes the following options</p>
<dl>
<dt><code>&#8211;recursive</code></p>
<dd>If specified, do recursive crawling on the paths specified<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;debug</code></p>
<dd>If specified, echo verbose debugging information</p>
<dt><code>&#8211;cache-text</code></p>
<dd>If specified, build text-cache of documents used for snippets</p>
<dt><code>&#8211;allow-pattern [pattern]</code></p>
<dd>Only allow files that match the pattern to be indexed.</p>
<dt><code>&#8211;deny-pattern [pattern]</code></p>
<dd>Keep any files that match the pattern from being indexed.</p>
<dt><code>&#8211;remap </code>[<i>path1</i>:<i>path2</i>]</p>
<dd>If specified, remap the target path by prefix. <i>path1</i> will be replaced with <i>path2</i>. This option is intended to be used when generating pre-built indexes, where the final path will be differ from the current one.</dl>
<h2>Author</h2>
<p>Novell, Inc.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dashboard-hackers [at] gnome.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2005 Novell, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-beagled/">beagled</a></code>(1), <code><a href="/docs/linux/man/8-beagle-manage-index/">beagle-manage-index</a></code>(8) </p>
