---
title: "npm-uninstall(1)"
name: "npm-uninstall"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-uninstall/"
description: "npm-uninstall – Remove a package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-uninstall</code> &#8211; Remove a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm uninstall[&lt;@scope&gt; / ]&lt;pkg&gt;[@&lt;version&gt;]...[-S | --save | -D | --save - dev | -O | --save - optional | --no - save] aliases : remove, rm, r, un, unlink
</code></pre>
</dl>
<h3>Description</h3>
<p> This uninstalls a package, completely removing everything npm installed on its behalf. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
npm uninstall sax
</pre>
</dl>
<p> In global mode (ie, with <code>-g</code> or <code>&#8211;global</code> appended to the command), it uninstalls the current package context as a global package. </p>
<p> <code>npm uninstall</code> takes 3 exclusive, optional flags which save or update the package version in your main package.json:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>-S, &#8211;save</code>: Package will be removed from your <code>dependencies</code>.</p>
<dt>&bull;</p>
<dd> <code>-D, &#8211;save-dev</code>: Package will be removed from your <code>devDependencies</code>.</p>
<dt>&bull;</p>
<dd> <code>-O, &#8211;save-optional</code>: Package will be removed from your <code>optionalDependencies</code>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-save</code>: Package will not be removed from your <code>package.json</code> file. </p>
</dl>
</dl>
<p> Further, if you have an <code>npm-shrinkwrap.json</code> then it will be updated as well. </p>
<p> Scope is optional and follows the usual rules for npm help <code>scope</code>. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre><code>
npm uninstall sax-- save
            npm uninstall @myorg /
        privatepackage-- save
            npm uninstall node -
    tap-- save - dev npm uninstall dtrace - provider-- save - optional npm uninstall lodash-- no - save
</code></pre>
</dl>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help prune</p>
<dt>&bull;</p>
<dd> npm help install</p>
<dt>&bull;</p>
<dd> npm help folders</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc </p>
</dl>
</dl>
<h2>Index</h2>
