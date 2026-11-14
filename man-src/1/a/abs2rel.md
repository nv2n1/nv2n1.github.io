---
title: "abs2rel(1)"
name: "abs2rel"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abs2rel/"
description: "abs2rel – convert absolute path to relative path"
---

<h2 class="name">NAME</h2>
<p> abs2rel &#8211; convert absolute path to relative path </p>
<h2>SYNOPSIS</h2>
<p> <code>abs2rel</code> path base</p>
<h2>DESCRIPTION</h2>
<p> The <code>abs2rel</code> command takes exactly two arguments &#8211; a destination path and a base path. It determines relative path from the base path to the destination path and prints it on standard output.</p>
<h2>EXAMPLES</h2>
<p> <code>abs2rel /1/2/3/a/b/c /1/2/3</code> will print <code>a/b/c</code> on standard output. </p>
<p> <code>abs2rel foo/bar foo/baz</code> will print <code>../bar</code> on standard output.</p>
<h2>REPORTING BUGS</h2>
<p> Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[]. </p>
<h2>Index</h2>
