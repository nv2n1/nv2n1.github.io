---
title: "npm-pack(1)"
name: "npm-pack"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-pack/"
description: "npm-pack – Create a tarball from a package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-pack</code> &#8211; Create a tarball from a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm pack[[&lt;@scope&gt; / ]&lt;pkg&gt;...][--dry - run]
</code></pre>
</dl>
<h3>Description</h3>
<p> For anything that&#8217;s installable (that is, a package folder, tarball, tarball url, name@tag, name [at] version, name, or scoped name), this command will fetch it to the cache, and then copy the tarball to the current working directory as <code>&lt;name&gt;-&lt;version&gt;.tgz</code>, and then write the filenames out to stdout. </p>
<p> If the same package is specified multiple times, then the file will be overwritten the second time. </p>
<p> If no arguments are supplied, then npm packs the current package folder. </p>
<p> The <code>&#8211;dry-run</code> argument will do everything that pack usually does without actually packing anything. Reports on what would have gone into the tarball.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help cache</p>
<dt>&bull;</p>
<dd> npm help publish</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc </p>
</dl>
</dl>
<h2>Index</h2>
