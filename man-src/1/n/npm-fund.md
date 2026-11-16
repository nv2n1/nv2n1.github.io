---
title: "npm-fund(1)"
name: "npm-fund"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-fund/"
description: "npm-fund – Retrieve funding information"
---

<h2 class="name">NAME</h2>
<p> <code>npm-fund</code> &#8211; Retrieve funding information </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre>
    npm fund [&lt;pkg&gt;]
</pre>
</dd></dl>
<h3>Description</h3>
<p> This command retrieves information on how to fund the dependencies of a given project. If no package name is provided, it will list all dependencies that are looking for funding in a tree-structure in which are listed the type of funding and the url to visit. If a package name is provided then it tries to open its funding url using the <code>&#8211;browser</code> config param; if there are multiple funding sources for the package, the user will be instructed to pass the <code>&#8211;which</code> command to disambiguate. </p>
<p> The list will avoid duplicated entries and will stack all packages that share the same type/url as a single entry. Given this nature the list is not going to have the same shape of the output from <code>npm ls</code>.</p>
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
<p> The browser that is called by the <code>npm fund</code> command to open websites.</p>
<h3>json</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Type: Boolean</dd>
<dt>&bull;</dt>
<dd> Default: false </dd>
</dl>
</dl>
<p> Show information in JSON format.</p>
<h3>unicode</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Type: Boolean</dd>
<dt>&bull;</dt>
<dd> Default: true </dd>
</dl>
</dl>
<p> Whether to represent the tree structure using unicode characters. Set it to <code>false</code> in order to use all-ansi output.</p>
<h3>which</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Type: Number</dd>
<dt>&bull;</dt>
<dd> Default: undefined </dd>
</dl>
</dl>
<p> If there are multiple funding sources, which 1-indexed source URL to open.</p>
<h2>See Also</h2>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help docs</dd>
<dt>&bull;</dt>
<dd> npm help config</dd>
<dt>&bull;</dt>
<dd> npm help install</dd>
<dt>&bull;</dt>
<dd> npm help ls </dd>
</dl>
</dl>
<h2>Index</h2>
