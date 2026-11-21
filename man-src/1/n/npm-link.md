---
title: "npm-link(1)"
name: "npm-link"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-link/"
description: "npm-link – Symlink a package folder"
---

<h2 class="name">NAME</h2>
<p> <code>npm-link</code> &#8211; Symlink a package folder </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre><code>
npm link(in package dir)
    npm link[&lt;@scope&gt; / ]&lt;pkg&gt;[@&lt;version&gt;] alias : npm ln
</code></pre>
</dd></dl>
<h3>Description</h3>
<p> Package linking is a two-step process. </p>
<p> First, <code>npm link</code> in a package folder will create a symlink in the global folder <code>{prefix}/lib/node_modules/&lt;package&gt;</code> that links to the package where the <code>npm link</code> command was executed. It will also link any bins in the package to <code>{prefix}/bin/{name}</code>. Note that <code>npm link</code> uses the global prefix (see <code>npm prefix -g</code> for its value). </p>
<p> Next, in some other location, <code>npm link package-name</code> will create a symbolic link from globally-installed <code>package-name</code> to <code>node_modules/</code> of the current folder. </p>
<p> Note that <code>package-name</code> is taken from <code>package.json</code>, not from directory name. </p>
<p> The package name can be optionally prefixed with a scope. See npm help <code>scope</code>. The scope must be preceded by an @-symbol and followed by a slash. </p>
<p> When creating tarballs for <code>npm publish</code>, the linked packages are &quot;snapshotted&quot; to their current state by resolving the symbolic links. </p>
<p> This is handy for installing your own stuff, so that you can work on it and test it iteratively without having to continually rebuild. </p>
<p> For example: </p>
<dl>
<dt>
</dt><dd>
<pre>
    cd ~/projects/node-redis    # go into the package directory
    npm link                    # creates global link
    cd ~/projects/node-bloggy   # go into some other package directory.
    npm link redis              # link-install the package
</pre>
</dd></dl>
<p> Now, any changes to ~/projects/node-redis will be reflected in ~/projects/node-bloggy/node_modules/node-redis/. Note that the link should be to the package name, not the directory name for that package. </p>
<p> You may also shortcut the two steps in one. For example, to do the above use-case in a shorter way: </p>
<dl>
<dt>
</dt><dd>
<pre>
cd ~/projects/node-bloggy  # go into the dir of your main project
npm link ../node-redis     # link the dir of your dependency
</pre>
</dd></dl>
<p> The second line is the equivalent of doing: </p>
<dl>
<dt>
</dt><dd>
<pre>
(cd ../node-redis; npm link)
npm link redis
</pre>
</dd></dl>
<p> That is, it first creates a global link, and then links the global installation target into your project&#8217;s <code>node_modules</code> folder. </p>
<p> Note that in this case, you are referring to the directory name, <code>node-redis</code>, rather than the package name <code>redis</code>. </p>
<p> If your linked package is scoped (see npm help <code>scope</code>) your link command must include that scope, e.g. </p>
<dl>
<dt>
</dt><dd>
<pre>
npm link @myorg/privatepackage
</pre>
</dd></dl>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help developers</dd>
<dt>&bull;</dt>
<dd> npm help package.json</dd>
<dt>&bull;</dt>
<dd> npm help npm- nstall</dd>
<dt>&bull;</dt>
<dd> npm help folders</dd>
<dt>&bull;</dt>
<dd> npm help config</dd>
<dt>&bull;</dt>
<dd> npm help npmrc </dd>
</dl>
</dl>
