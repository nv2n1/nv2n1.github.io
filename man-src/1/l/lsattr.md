---
title: "lsattr(1)"
name: "lsattr"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsattr/"
description: "lsattr – list file attributes on a Linux second extended file system"
---

<h2 class="name">NAME</h2>
<p> lsattr &#8211; list file attributes on a Linux second extended file system </p>
<h2>SYNOPSIS</h2>
<p> <code>lsattr</code> [ <code>-RVadlpv</code> ] [ <i>files&#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lsattr</code> lists the file attributes on a second extended file system. See <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) for a description of the attributes and what they mean.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-R</code></p>
<dd> Recursively list attributes of directories and their contents.</p>
<dt><code>-V</code></p>
<dd> Display the program version.</p>
<dt><code>-a</code></p>
<dd> List all files in directories, including files that start with `.&#8217;.</p>
<dt><code>-d</code></p>
<dd> List directories like other files, rather than listing their contents.</p>
<dt><code>-l</code></p>
<dd> Print the options using long names instead of single character abbreviations.</p>
<dt><code>-p</code></p>
<dd> List the file&#8217;s project number.</p>
<dt><code>-v</code></p>
<dd> List the file&#8217;s version/generation number.</dl>
<h2>AUTHOR</h2>
<p> <code>lsattr</code> was written by Remy Card &lt;Remy.Card [at] linux.org&gt;. It is currently being maintained by Theodore Ts&#8217;o &lt;tytso [at] alum.mit.edu&gt;.</p>
<h2>BUGS</h2>
<p> There are none :-).</p>
<h2>AVAILABILITY</h2>
<p> <code>lsattr</code> is part of the e2fsprogs package and is available from <a rel="nofollow" href="http://e2fsprogs.sourceforge.net.">http://e2fsprogs.sourceforge.net.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) </p>
<h2>Index</h2>
