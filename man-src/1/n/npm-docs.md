---
title: "npm-docs(1)"
name: "npm-docs"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-docs/"
description: "npm-docs – Docs for a package in a web browser maybe"
---

<h2 class="name">NAME</h2>
<p> <code>npm-docs</code> &#8211; Docs for a package in a web browser maybe </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm docs[&lt;pkgname&gt;[&lt;pkgname&gt;...]] npm docs.npm home[&lt;pkgname&gt;[&lt;pkgname&gt;...]] npm home.
</code></pre>
</dl>
<h3>Description</h3>
<p> This command tries to guess at the likely location of a package&#8217;s documentation URL, and then tries to open it using the <code>&#8211;browser</code> config param. You can pass multiple package names at once. If no package name is provided, it will search for a <code>package.json</code> in the current folder and use the <code>name</code> property.</p>
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
<p> The browser that is called by the <code>npm docs</code> command to open websites.</p>
<h3>registry</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: <a rel="nofollow" href="https://registry.npmjs.org/">https://registry.npmjs.org/</a></p>
<dt>&bull;</p>
<dd> Type: url </p>
</dl>
</dl>
<p> The base URL of the npm package registry.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help view</p>
<dt>&bull;</p>
<dd> npm help publish</p>
<dt>&bull;</p>
<dd> npm help registry</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc</p>
<dt>&bull;</p>
<dd> npm help package.json </p>
</dl>
</dl>
<h2>Index</h2>
