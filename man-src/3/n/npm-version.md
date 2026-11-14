---
title: "npm-version(3)"
name: "npm-version"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-version/"
description: "npm-version — Bump a package version"
---

<p><code>npm-version</code> &#8212; Bump a package version</p>
<h2>Synopsis</h2>
<pre>npm.commands.version(newversion, callback)</pre>
<h2>Description</h2>
<p>Run this in a package directory to bump the version and write the new data back to the package.json file. If run in a git repo, it will also create a version commit and tag, and fail if the repo is not clean. Like all other commands, this function takes a string array as its first parameter. The difference, however, is this function will fail if it does not have exactly one element. The only element should be a version number. </p>
