---
title: "rpmmd2solv(1)"
name: "rpmmd2solv"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmmd2solv/"
description: "rpmmd2solv – convert files in rpm-md format into a solv file"
---

<h2 class="name">NAME</h2>
<p> rpmmd2solv &#8211; convert files in rpm-md format into a solv file </p>
<h2>SYNOPSIS</h2>
<p> <code>rpmmd2solv</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The rpmmd2solv tool reads rpm-md xml data from stdin, and writes it as solv file to standard output. It understands the <code>primary</code>, <code>filelist</code>, <code>other</code>, and <code>susedata</code> format. </p>
<p> <code>-X</code></p>
<dl>
<dt>
<dd> Autoexpand SUSE pattern and product provides into packages.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-repomdxml2solv/">repomdxml2solv</a>(1), <a href="/docs/linux/man/1-mergesolv/">mergesolv</a>(1), <a href="/docs/linux/man/8-createrepo/">createrepo</a>(8)</p>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
