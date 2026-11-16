---
title: "npm-deprecate(3)"
name: "npm-deprecate"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-deprecate/"
description: "npm-deprecate — Deprecate a version of a package"
---

<p><code>npm-deprecate</code> &#8212; Deprecate a version of a package</p>
<h2>Synopsis</h2>
<pre>npm.commands.deprecate(args, callback)</pre>
<h2>Description</h2>
<p>This command will update the npm registry entry for a package, providing a deprecation warning to all who attempt to install it. </p>
<p> The &#8216;args&#8217; parameter must have exactly two elements:</p>
<dl>
<dt>&bull;</dt>
<dd><code>package[@version]</code></dd>
<dd>The <code>version</code> portion is optional, and may be either a range, or a specific version, or a tag.</dd>
<dt>&bull;</dt>
<dd><code>message</code></dd>
<dd>The warning message that will be printed whenever a user attempts to install the package.</dd>
<dd></dd></dl>
<p> Note that you must be the package owner to deprecate something. See the <code>owner</code> and <code>adduser</code> help topics. </p>
<p> To un-deprecate a package, specify an empty string (<code>&quot;&quot;</code>) for the <code>message</code> argument.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</dt>
<dd>npm apihelp publish</dd>
<dt>&bull;</dt>
<dd>npm apihelp unpublish</dd>
<dt>&bull;</dt>
<dd>npm help registry</dd>
<dd>
</dd></dl>