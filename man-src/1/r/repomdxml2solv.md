---
title: "repomdxml2solv(1)"
name: "repomdxml2solv"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repomdxml2solv/"
description: "repomdxml2solv – convert a repomd.xml file into a solv file"
---

<h2 class="name">NAME</h2>
<p> repomdxml2solv &#8211; convert a repomd.xml file into a solv file </p>
<h2>SYNOPSIS</h2>
<p> <code>repomdxml2solv</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The repomd.xml file is the index file of a rpm-md repository, containing references to all data file with checksums. The repomdxml2solv tool reads the repomd.xml file from stdin and writes the parsed data as solv file to standard output. The data is stored as meta attributes in the result. </p>
<p> <code>-q</code> <i>WHAT</i></p>
<dl>
<dt>
<dd> Data query mode: instead of writing a solv file, select the <i>WHAT</i> element in the input data and write it to standard output. Examples for <i>WHAT</i> are <code>type</code> to get a list of all types, and <code>primary:location</code> to get the location of the element with type <code>primary</code>.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rpmmd2solv/">rpmmd2solv</a>(1), <a href="/docs/linux/man/1-mergesolv/">mergesolv</a>(1), <a href="/docs/linux/man/8-createrepo/">createrepo</a>(8)</p>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
