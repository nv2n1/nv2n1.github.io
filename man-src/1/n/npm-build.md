---
title: "npm-build(1)"
name: "npm-build"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-build/"
description: "npm-build – Build a package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-build</code> &#8211; Build a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm build [&lt;package-folder&gt;]
</pre>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>&lt;package-folder&gt;</code>: A folder containing a <code>package.json</code> file in its root. </p>
</dl>
</dl>
<h3>Description</h3>
<p> This is the plumbing command called by <code>npm link</code> and <code>npm install</code>. </p>
<p> It should generally be called during installation, but if you need to run it directly, run: </p>
<dl>
<dt>
<dd>
<pre>
    npm run-script build
</pre>
</dl>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help install</p>
<dt>&bull;</p>
<dd> npm help link</p>
<dt>&bull;</p>
<dd> npm help scripts</p>
<dt>&bull;</p>
<dd> npm help package.json </p>
</dl>
</dl>
<h2>Index</h2>
