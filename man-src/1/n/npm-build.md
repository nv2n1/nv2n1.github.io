---

title: "npm-build(1)"
name: "npm-build"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-build/"
description: "npm-build – Build a package"
---

<p> <code>npm-build</code> &#8211; Build a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre>
npm build [&lt;package-folder&gt;]
</pre>
</dd></dl>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <code>&lt;package-folder&gt;</code>: A folder containing a <code>package.json</code> file in its root. </dd>
</dl>
</dl>
<h3>Description</h3>
<p> This is the plumbing command called by <code>npm link</code> and <code>npm install</code>. </p>
<p> It should generally be called during installation, but if you need to run it directly, run: </p>
<dl>
<dt>
</dt><dd>
<pre>
    npm run-script build
</pre>
</dd></dl>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help install</dd>
<dt>&bull;</dt>
<dd> npm help link</dd>
<dt>&bull;</dt>
<dd> npm help scripts</dd>
<dt>&bull;</dt>
<dd> npm help package.json </dd>
</dl>
</dl>
