---
title: "cleanlinks(1)"
name: "cleanlinks"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cleanlinks/"
description: "cleanlinks – remove dangling symbolic links and empty directories"
---

<h2>NAME</h2>
<p> cleanlinks &#8211; remove dangling symbolic links and empty directories</p>
<h2>SYNOPSIS</h2>
<p> <code>cleanlinks</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>cleanlinks</i> program searches the directory tree descended from the current directory for symbolic links whose targets do not exist, and removes them. It then removes all empty directories in that directory tree. </p>
<p> <i>cleanlinks</i> is useful for cleaning up a shadow link tree created with <code><a href="/docs/linux/man/1-lndir/">lndir</a></code>(1) after files have been removed from the real directory.</p>
<h2>DIAGNOSTICS</h2>
<p> A message will be printed upon encountering each dangling symlink and empty directory.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lndir/">lndir</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> The version of the <i>cleanlinks</i> included in this X.Org Foundation release was originally written by David Dawes wrote as a part of XFree86. </p>
<p> Colin Watson wrote this manual page, originally for the Debian Project. </p>
<h2>Index</h2>
