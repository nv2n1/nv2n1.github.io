---
title: "which(1)"
name: "which"
section: "1"
letter: "w"
url: "/docs/linux/man/1-which/"
description: "which – locate a command"
---

<h2 class="name">NAME</h2>
<p> which &#8211; locate a command </p>
<h2>SYNOPSIS</h2>
<p> which [-a] filename &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>which</code> returns the pathnames of the files (or links) which would be executed in the current environment, had its arguments been given as commands in a strictly POSIX-conformant shell. It does this by searching the PATH for executable files matching the names of the arguments. It does not canonicalize path names.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> print all matching pathnames of each argument</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> if all specified commands are found and executable</p>
<dt><code>1</code></p>
<dd> if one or more specified commands is nonexistent or not executable</p>
<dt><code>2</code></p>
<dd> if an invalid option is specified </p>
</dl>
<h2>Index</h2>
