---
title: "linux-version(1)"
name: "linux-version"
section: "1"
letter: "l"
url: "/docs/linux/man/1-linux-version/"
description: "linux-version – operate on Linux kernel version strings"
---

<h2 class="name">NAME</h2>
<p> linux-version &#8211; operate on Linux kernel version strings </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>linux-version compare</code><i>&nbsp;VERSION1 OP VERSION2</i></p>
<dt> <code>linux-version sort</code>&nbsp;[<code>&#8211;reverse</code>] [<i>VERSION1 VERSION2</i>&nbsp;&#8230;]</p>
<dt> <code>linux-version list</code>&nbsp;[<code>&#8211;paths</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>linux-version</code> operates on Linux kernel version strings as</p>
<dd>reported by <code>uname -r</code> and used in file and directory names. These version strings do not follow the same rules as Debian package version strings and should not be compared as such or as arbitrary strings.</p>
<dl>
<dt><code>compare</code><i>&nbsp;VERSION1 OP VERSION2</i></p>
<dd> Compare version strings, where <i>OP</i> is a binary operator. <code>linux-version</code> returns success (zero result) if the specified condition is satisfied, and failure (nonzero result) otherwise. The valid operators are: <code>lt le eq ne ge gt</code></p>
<dt><code>sort</code> [<code>&#8211;reverse</code>] [<i>VERSION1 VERSION2</i> &#8230;]</p>
<dd> Sort the given version strings and print them in order from lowest to highest. If the <code>&#8211;reverse</code> option is used, print them in order from highest to lowest.</p>
<dl>
<dt>
<dd>
<p> If no version strings are given as arguments, the version strings will instead be read from standard input, one per line. They may be suffixed by arbitrary text after a space, which will be included in the output. This means that, for example: </p>
<p> linux-version list &#8211;paths | linux-version sort &#8211;reverse </p>
<p> will list the installed versions and corresponding paths in order from highest to lowest version.</dl>
<dt><code>list</code> [<code>&#8211;paths</code>]</p>
<dd> List kernel versions installed in the customary location. If the <code>&#8211;paths</code> option, show the corresponding path for each version.</dl>
<h2>AUTHOR</h2>
<p> <code>linux-version</code> and this manual page were written by Ben Hutchings as part of the Debian <code>linux-base</code> package. </p>
<h2>Index</h2>
