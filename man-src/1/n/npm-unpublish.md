---

title: "npm-unpublish(1)"
name: "npm-unpublish"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-unpublish/"
description: "npm-unpublish – Remove a package from the registry"
---

<p> <code>npm-unpublish</code> &#8211; Remove a package from the registry </p>
<h3>Synopsis</h3>
<h3>Unpublishing a single version of a package</h3>
<dl>
<dt>
</dt><dd>
<pre>
npm unpublish [&lt;@scope&gt;/]&lt;pkg&gt;@&lt;version&gt;
</pre>
</dd></dl>
<h3>Unpublishing an entire package</h3>
<dl>
<dt>
</dt><dd>
<pre>
npm unpublish [&lt;@scope&gt;/]&lt;pkg&gt; --force
</pre>
</dd></dl>
<h3>Warning</h3>
<p> Consider using the <code>deprecate</code> command instead, if your intent is to encourage users to upgrade, or if you no longer want to maintain a package.</p>
<h3>Description</h3>
<p> This removes a package version from the registry, deleting its entry and removing the tarball. </p>
<p> If no version is specified, or if all versions are removed then the root package entry is removed from the registry entirely. </p>
<p> Even if a package version is unpublished, that specific name and version combination can never be reused. In order to publish the package again, a new version number must be used. If you unpublish the entire package, you may not publish any new versions of that package until 24 hours have passed. </p>
<p> To learn more about how unpublish is treated on the npm registry, see our &lt;a href=&quot;<a rel="nofollow" href="https://www.npmjs.com/policies/unpublish">https://www.npmjs.com/policies/unpublish</a>&quot; target=&quot;_blank&quot; rel=&quot;noopener noreferrer&quot;&gt; unpublish policies&lt;/a&gt;.</p>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help deprecate</dd>
<dt>&bull;</dt>
<dd> npm help publish</dd>
<dt>&bull;</dt>
<dd> npm help registry</dd>
<dt>&bull;</dt>
<dd> npm help adduser</dd>
<dt>&bull;</dt>
<dd> npm help owner </dd>
</dl>
</dl>
