---

title: "npm-bugs(1)"
name: "npm-bugs"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-bugs/"
description: "npm-bugs – Bugs for a package in a web browser maybe"
---

<p> <code>npm-bugs</code> &#8211; Bugs for a package in a web browser maybe </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre>
npm bugs [&lt;pkgname&gt;]
aliases: issues
</pre>
</dd></dl>
<h3>Description</h3>
<p> This command tries to guess at the likely location of a package&#8217;s bug tracker URL, and then tries to open it using the <code>&#8211;browser</code> config param. If no package name is provided, it will search for a <code>package.json</code> in the current folder and use the <code>name</code> property.</p>
<h3>Configuration</h3>
<h3>browser</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: OS X: <code>&quot;open&quot;</code>, Windows: <code>&quot;start&quot;</code>, Others: <code>&quot;xdg-open&quot;</code></dd>
<dt>&bull;</dt>
<dd> Type: String </dd>
</dl>
</dl>
<p> The browser that is called by the <code>npm bugs</code> command to open websites.</p>
<h3>registry</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: <a rel="nofollow" href="https://registry.npmjs.org/">https://registry.npmjs.org/</a></dd>
<dt>&bull;</dt>
<dd> Type: url </dd>
</dl>
</dl>
<p> The base URL of the npm package registry.</p>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help docs</dd>
<dt>&bull;</dt>
<dd> npm help view</dd>
<dt>&bull;</dt>
<dd> npm help publish</dd>
<dt>&bull;</dt>
<dd> npm help registry</dd>
<dt>&bull;</dt>
<dd> npm help config</dd>
<dt>&bull;</dt>
<dd> npm help npmrc</dd>
<dt>&bull;</dt>
<dd> npm help package.json </dd>
</dl>
</dl>
