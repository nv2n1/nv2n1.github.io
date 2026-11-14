---
title: "npm-prune(1)"
name: "npm-prune"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-prune/"
description: "npm-prune – Remove extraneous packages"
---

<h2 class="name">NAME</h2>
<p> <code>npm-prune</code> &#8211; Remove extraneous packages </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm prune[[&lt;@scope&gt; / ]&lt;pkg&gt;...][--production][--dry - run][--json]
</code></pre>
</dl>
<h3>Description</h3>
<p> This command removes &quot;extraneous&quot; packages. If a package name is provided, then only packages matching one of the supplied names are removed. </p>
<p> Extraneous packages are packages that are not listed on the parent package&#8217;s dependencies list. </p>
<p> If the <code>&#8211;production</code> flag is specified or the <code>NODE_ENV</code> environment variable is set to <code>production</code>, this command will remove the packages specified in your <code>devDependencies</code>. Setting <code>&#8211;no-production</code> will negate <code>NODE_ENV</code> being set to <code>production</code>. </p>
<p> If the <code>&#8211;dry-run</code> flag is used then no changes will actually be made. </p>
<p> If the <code>&#8211;json</code> flag is used then the changes <code>npm prune</code> made (or would have made with <code>&#8211;dry-run</code>) are printed as a JSON object. </p>
<p> In normal operation with package-locks enabled, extraneous modules are pruned automatically when modules are installed and you&#8217;ll only need this command with the <code>&#8211;production</code> flag. </p>
<p> If you&#8217;ve disabled package-locks then extraneous modules will not be removed and it&#8217;s up to you to run <code>npm prune</code> from time-to-time to remove them.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help uninstall</p>
<dt>&bull;</p>
<dd> npm help folders</p>
<dt>&bull;</p>
<dd> npm help ls </p>
</dl>
</dl>
<h2>Index</h2>
