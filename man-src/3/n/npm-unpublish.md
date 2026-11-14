---
title: "npm-unpublish(3)"
name: "npm-unpublish"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-unpublish/"
description: "npm-unpublish — Remove a package from the registry"
---

<p><code>npm-unpublish</code> &#8212; Remove a package from the registry</p>
<h2>Synopsis</h2>
<pre>npm.commands.unpublish(package, callback)</pre>
<h2>Description</h2>
<p>This removes a package version from the registry, deleting its entry and removing the tarball. The package parameter must be defined. Only the first element in the package parameter is used. If there is no first element, then npm assumes that the package at the current working directory is what is meant. If no version is specified, or if all versions are removed then the root package entry is removed from the registry entirely. </p>
