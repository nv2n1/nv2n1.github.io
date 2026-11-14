---
title: "npm-link(3)"
name: "npm-link"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-link/"
description: "npm-link — Symlink a package folder"
---

<p><code>npm-link</code> &#8212; Symlink a package folder</p>
<h2>Synopsis</h2>
<pre>npm.command.link(callback)
npm.command.link(packages, callback)</pre>
<h2>Description</h2>
<p>Package linking is a two-step process. Without parameters, link will create a globally-installed symbolic link from <code>prefix/package-name</code> to the current folder. With a parameters, link will create a symlink from the local <code>node_modules</code> folder to the global symlink. When creating tarballs for <code>npm publish</code>, the linked packages are &quot;snapshotted&quot; to their current state by resolving the symbolic links. This is handy for installing your own stuff, so that you can work on it and test it iteratively without having to continually rebuild. For example:</p>
<dl>
<dd>
<pre>npm.commands.link(cb) # creates global link from the cwd
 # (say redis package)
npm.commands.link('redis', cb) # link-install the package</pre>
<dd></dl>
<p> Now, any changes to the redis package will be reflected in the package in the current working directory </p>
