---
title: "npm-scope(7)"
name: "npm-scope"
section: "7"
letter: "n"
url: "/docs/linux/man/7-npm-scope/"
description: "npm-scope – Scoped packages"
---

<p><code>npm-scope</code> &#8211; Scoped packages</p>
<h2>Description</h2>
<p>All npm packages have a name. Some package names also have a scope. A scope follows the usual rules for package names (url-safe characters, no leading dots or underscores). When used in package names, preceded by an @-symbol and followed by a slash, e.g.</p>
<dl>
<dd>
<pre>@somescope/somepackagename</pre>
<dd></dl>
<p> Scopes are a way of grouping related packages together, and also affect a few things about the way npm treats the package. </p>
<p> Scoped packages are supported by the public npm registry. The npm client is backwards-compatible with un-scoped registries, so it can be used to work with scoped and un-scoped registries at the same time.</p>
<h2>Installing scoped packages</h2>
<p>Scoped packages are installed to a sub-folder of the regular installation folder, e.g. if your other packages are installed in <code>node_modules/packagename</code>, scoped modules will be in <code>node_modules/@myorg/packagename</code>. The scope folder (<code>@myorg</code>) is simply the name of the scope preceded by an @-symbol, and can contain any number of scoped packages. </p>
<p> A scoped package is installed by referencing it by name, preceded by an @-symbol, in <code>npm install</code>:</p>
<dl>
<dd>
<pre>npm install @myorg/mypackage</pre>
<dd></dl>
<p> Or in <code>package.json</code>:</p>
<dl>
<dd>
<pre>&quot;dependencies&quot;: {
 &quot;@myorg/mypackage&quot;: &quot;^1.3.0&quot;
}</pre>
<dd></dl>
<p> Note that if the @-symbol is omitted in either case npm will instead attempt to install from GitHub; see npm help <code>npm-install</code>.</p>
<h2>Requiring scoped packages</h2>
<p>Because scoped packages are installed into a scope folder, you have to include the name of the scope when requiring them in your code, e.g.</p>
<dl>
<dd>
<pre>require('@myorg/mypackage')</pre>
<dd></dl>
<p> There is nothing special about the way Node treats scope folders, this is just specifying to require the module <code>mypackage</code> in the folder called <code>@myorg</code>.</p>
<h2>Publishing scoped packages</h2>
<p>Scoped packages can be published to any registry that supports them, including the public npm registry. </p>
<p> (As of 2015-04-19, the public npm registry <code>does</code> support scoped packages) </p>
<p> If you wish, you may associate a scope with a registry; see below.</p>
<h3>Publishing public scoped packages to the public npm registry</h3>
<p>To publish a public scoped package, you must specify <code>&#8211;access public</code> with the initial publication. This will publish the package and set access to <code>public</code> as if you had run <code>npm access public</code> after publishing.</p>
<h3>Publishing private scoped packages to the npm registry</h3>
<p>To publish a private scoped package to the npm registry, you must have an npm Private Modules <i><a rel="nofollow" href="https://www.npmjs.com/private-modules">https://www.npmjs.com/private-modules</a></i> account. </p>
<p> You can then publish the module with <code>npm publish</code> or <code>npm publish &#8211;access restricted</code>, and it will be present in the npm registry, with restricted access. You can then change the access permissions, if desired, with <code>npm access</code> or on the npmjs.com website.</p>
<h2>Associating a scope with a registry</h2>
<p>Scopes can be associated with a separate registry. This allows you to seamlessly use a mix of packages from the public npm registry and one or more private registries, such as npm Enterprise. </p>
<p> You can associate a scope with a registry at login, e.g.</p>
<dl>
<dd>
<pre>npm login --registry=<a rel="nofollow" href="http://reg.example.com">http://reg.example.com</a> --scope=@myco</pre>
<dd></dl>
<p> Scopes have a many-to-one relationship with registries: one registry can host multiple scopes, but a scope only ever points to one registry. </p>
<p> You can also associate a scope with a registry using <code>npm config</code>:</p>
<dl>
<dd>
<pre>npm config set @myco:registry <a rel="nofollow" href="http://reg.example.com">http://reg.example.com</a></pre>
<dd></dl>
<p> Once a scope is associated with a registry, any <code>npm install</code> for a package with that scope will request packages from that registry instead. Any <code>npm publish</code> for a package name that contains the scope will be published to that registry instead.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help install</p>
<dt>&bull;</p>
<dd>npm help publish</p>
<dt>&bull;</p>
<dd>npm help access</p>
<dd>
