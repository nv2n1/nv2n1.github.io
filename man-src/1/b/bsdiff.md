---
title: "bsdiff(1)"
name: "bsdiff"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bsdiff/"
description: "bsdiff – generate a patch between two binary files"
---

<h2 class="name">NAME</h2>
<p> <code>bsdiff</code> &#8211; generate a patch between two binary files </p>
<h2>SYNOPSIS</h2>
<p> Ao Ar oldfile Ac Ao Ar newfile Ac Ao Ar patchfile Ac</p>
<h2>DESCRIPTION</h2>
<p> compares Ao Ar oldfile Ac to Ao Ar newfile Ac and writes to Ao Ar patchfile Ac a binary patch suitable for use by <a href="/docs/linux/man/1-bspatch/">bspatch</a>(1). When Ao Ar oldfile Ac and Ao Ar newfile Ac are two versions of an executable program, the patches produced are on average a factor of five smaller than those produced by any other binary patch tool known to the author. </p>
<p> uses memory equal to 17 times the size of Ao Ar oldfile Ac , and requires an absolute minimum working set size of 8 times the size of oldfile.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bspatch/">bspatch</a>(1)</p>
<h2>AUTHORS</h2>
<p> An Colin Percival Aq cperciva [at] freebsd.org </p>
<h2>Index</h2>
