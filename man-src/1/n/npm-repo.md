---
title: "npm-repo(1)"
name: "npm-repo"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-repo/"
description: "npm-repo – Open package repository page in the browser"
---

<h2 class="name">NAME</h2>
<p> <code>npm-repo</code> &#8211; Open package repository page in the browser </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm repo [&lt;pkg&gt;]
</pre>
</dl>
<h3>Description</h3>
<p> This command tries to guess at the likely location of a package&#8217;s repository URL, and then tries to open it using the <code>&#8211;browser</code> config param. If no package name is provided, it will search for a <code>package.json</code> in the current folder and use the <code>name</code> property.</p>
<h3>Configuration</h3>
<h3>browser</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: OS X: <code>&quot;open&quot;</code>, Windows: <code>&quot;start&quot;</code>, Others: <code>&quot;xdg-open&quot;</code></p>
<dt>&bull;</p>
<dd> Type: String </p>
</dl>
</dl>
<p> The browser that is called by the <code>npm repo</code> command to open websites.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help docs</p>
<dt>&bull;</p>
<dd> npm help config </p>
</dl>
</dl>
<h2>Index</h2>
