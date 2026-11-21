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
</dt><dd>
<pre><code>
npm uninstall[&lt;@scope&gt; / ]&lt;pkg&gt;[@&lt;version&gt;]...[-S | --save | -D | --save - dev | -O | --save - optional | --no - save] aliases : remove, rm, r, un, unlink
</code></pre>
</dd></dl>
<h3>Description</h3>
<p> This uninstalls a package, completely removing everything npm installed on its behalf. </p>
<p> Example: </p>
<dl>
<dt>
</dt><dd>
<pre>
npm uninstall sax
</pre>
</dd></dl>
<p> In global mode (ie, with <code>-g</code> or <code>&#8211;global</code> appended to the command), it uninstalls the current package context as a global package. </p>
<p> <code>npm uninstall</code> takes 3 exclusive, optional flags which save or update the package version in your main package.json:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <code>-S, &#8211;save</code>: Package will be removed from your <code>dependencies</code>.</dd>
<dt>&bull;</dt>
<dd> <code>-D, &#8211;save-dev</code>: Package will be removed from your <code>devDependencies</code>.</dd>
<dt>&bull;</dt>
<dd> <code>-O, &#8211;save-optional</code>: Package will be removed from your <code>optionalDependencies</code>.</dd>
<dt>&bull;</dt>
<dd> <code>&#8211;no-save</code>: Package will not be removed from your <code>package.json</code> file. </dd>
</dl>
</dl>
<p> Further, if you have an <code>npm-shrinkwrap.json</code> then it will be updated as well. </p>
<p> Scope is optional and follows the usual rules for npm help <code>scope</code>. </p>
<p> Examples: </p>
<dl>
<dt>
</dt><dd>
<pre><code>
npm uninstall sax-- save
            npm uninstall @myorg /
        privatepackage-- save
            npm uninstall node -
    tap-- save - dev npm uninstall dtrace - provider-- save - optional npm uninstall lodash-- no - save
</code></pre>
</dd></dl>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help prune</dd>
<dt>&bull;</dt>
<dd> npm help install</dd>
<dt>&bull;</dt>
<dd> npm help folders</dd>
<dt>&bull;</dt>
<dd> npm help config</dd>
<dt>&bull;</dt>
<dd> npm help npmrc </dd>
</dl>
</dl>
