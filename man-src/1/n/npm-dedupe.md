---
title: "npm-dedupe(1)"
name: "npm-dedupe"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-dedupe/"
description: "npm-dedupe – Reduce duplication"
---

<h2 class="name">NAME</h2>
<p> <code>npm-dedupe</code> &#8211; Reduce duplication </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm dedupe
npm ddp
aliases: find-dupes, ddp
</pre>
</dl>
<h3>Description</h3>
<p> Searches the local package tree and attempts to simplify the overall structure by moving dependencies further up the tree, where they can be more effectively shared by multiple dependent packages. </p>
<p> For example, consider this dependency graph: </p>
<dl>
<dt>
<dd>
<pre><code>
a + --b &lt; --depends on c @1.0.x |   `--c @1.0.3
`--d &lt; --depends on c @~1.0.9
    `--c @1.0.10
</code></pre>
</dl>
<p> In this case, <code>npm dedupe</code> will transform the tree to: </p>
<dl>
<dt>
<dd>
<pre>
a
+-- b
+-- d
`-- c@1.0.10
</pre>
</dl>
<p> Because of the hierarchical nature of node&#8217;s module lookup, b and d will both get their dependency met by the single c package at the root level of the tree. </p>
<p> The deduplication algorithm walks the tree, moving each dependency as far up in the tree as possible, even if duplicates are not found. This will result in both a flat and deduplicated tree. </p>
<p> If a suitable version exists at the target location in the tree already, then it will be left untouched, but the other duplicates will be deleted. </p>
<p> Arguments are ignored. Dedupe always acts on the entire tree. </p>
<p> Modules </p>
<p> Note that this operation transforms the dependency tree, but will never result in new modules being installed.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help ls</p>
<dt>&bull;</p>
<dd> npm help update</p>
<dt>&bull;</p>
<dd> npm help install </p>
</dl>
</dl>
<h2>Index</h2>
