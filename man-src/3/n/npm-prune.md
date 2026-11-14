---
title: "npm-prune(3)"
name: "npm-prune"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-prune/"
description: "npm-prune — Remove extraneous packages"
---

<p><code>npm-prune</code> &#8212; Remove extraneous packages</p>
<h2>Synopsis</h2>
<pre>npm.commands.prune([packages,] callback)</pre>
<h2>Description</h2>
<p>This command removes &quot;extraneous&quot; packages. The first parameter is optional, and it specifies packages to be removed. No packages are specified, then all packages will be checked. Extraneous packages are packages that are not listed on the parent package&#8217;s dependencies list. </p>
