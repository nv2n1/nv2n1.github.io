---
title: "npm-ls(1)"
name: "npm-ls"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-ls/"
description: "npm-ls – List installed packages"
---

<h2 class="name">NAME</h2>
<p> <code>npm-ls</code> &#8211; List installed packages </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm ls[[&lt;@scope&gt; / ]&lt;pkg&gt;...] aliases : list, la, ll
</code></pre>
</dl>
<h3>Description</h3>
<p> This command will print to stdout all the versions of packages that are installed, as well as their dependencies, in a tree-structure. </p>
<p> Positional arguments are <code>name [at] version-range</code> identifiers, which will limit the results to only the paths to the packages named. Note that nested packages will <i>also</i> show the paths to the specified packages. For example, running <code>npm ls promzard</code> in npm&#8217;s source tree will show: </p>
<dl>
<dt>
<dd>
<pre><code>
npm[at] 6.14.4 / path / to / npm
    └─┬ init - package - json[at] 0.0.4
      └── promzard[at] 0.1.5
</code></pre>
</dl>
<p> It will print out extraneous, missing, and invalid packages. </p>
<p> If a project specifies git urls for dependencies these are shown in parentheses after the name [at] version to make it easier for users to recognize potential forks of a project. </p>
<p> The tree shown is the logical dependency tree, based on package dependencies, not the physical layout of your node_modules folder. </p>
<p> When run as <code>ll</code> or <code>la</code>, it shows extended information by default.</p>
<h3>Configuration</h3>
<h3>json</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: false</p>
<dt>&bull;</p>
<dd> Type: Boolean </p>
</dl>
</dl>
<p> Show information in JSON format.</p>
<h3>long</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: false</p>
<dt>&bull;</p>
<dd> Type: Boolean </p>
</dl>
</dl>
<p> Show extended information.</p>
<h3>parseable</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: false</p>
<dt>&bull;</p>
<dd> Type: Boolean </p>
</dl>
</dl>
<p> Show parseable output instead of tree view.</p>
<h3>global</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: false</p>
<dt>&bull;</p>
<dd> Type: Boolean </p>
</dl>
</dl>
<p> List packages in the global install prefix instead of in the current project.</p>
<h3>depth</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Type: Int </p>
</dl>
</dl>
<p> Max display depth of the dependency tree.</p>
<h3>prod / production</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Type: Boolean</p>
<dt>&bull;</p>
<dd> Default: false </p>
</dl>
</dl>
<p> Display only the dependency tree for packages in <code>dependencies</code>.</p>
<h3>dev / development</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Type: Boolean</p>
<dt>&bull;</p>
<dd> Default: false </p>
</dl>
</dl>
<p> Display only the dependency tree for packages in <code>devDependencies</code>.</p>
<h3>only</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Type: String </p>
</dl>
</dl>
<p> When &quot;dev&quot; or &quot;development&quot;, is an alias to <code>dev</code>. </p>
<p> When &quot;prod&quot; or &quot;production&quot;, is an alias to <code>production</code>.</p>
<h3>link</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Type: Boolean</p>
<dt>&bull;</p>
<dd> Default: false </p>
</dl>
</dl>
<p> Display only dependencies which are linked</p>
<h3>unicode</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Type: Boolean</p>
<dt>&bull;</p>
<dd> Default: true </p>
</dl>
</dl>
<p> Whether to represent the tree structure using unicode characters. Set it to false in order to use all-ansi output.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc</p>
<dt>&bull;</p>
<dd> npm help folders</p>
<dt>&bull;</p>
<dd> npm help install</p>
<dt>&bull;</p>
<dd> npm help link</p>
<dt>&bull;</p>
<dd> npm help prune</p>
<dt>&bull;</p>
<dd> npm help outdated</p>
<dt>&bull;</p>
<dd> npm help update </p>
</dl>
</dl>
<h2>Index</h2>
