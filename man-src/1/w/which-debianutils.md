---
title: "which-debianutils(1)"
name: "which-debianutils"
section: "1"
letter: "w"
url: "/docs/linux/man/1-which-debianutils/"
description: "which – locate a command"
---

<p>which &#8211; locate a command </p>
<h2>Synopsis</h2>
<p>which [-a] filename &#8230;</p>
<h2>Description</h2>
<p><code>which</code> returns the pathnames of the files (or links) which would be executed in the current environment, had its arguments been given as commands in a strictly POSIX-conformant shell. It does this by searching the PATH for executable files matching the names of the arguments. It does not canonicalize path names.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-a</code></p>
<dd>print all matching pathnames of each argument</dl>
<h2>Exit Status</h2>
<dl COMPACT>
<dt><code>0</code></p>
<dd>if all specified commands are found and executable</p>
<dt><code>1</code></p>
<dd>if one or more specified commands is nonexistent or not executable</p>
<dt><code>2</code></p>
<dd>if an invalid option is specified </p>
</dl>
