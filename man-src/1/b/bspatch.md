---
title: "bspatch(1)"
name: "bspatch"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bspatch/"
description: "bspatch – apply a patch built with"
---

<h2 class="name">NAME</h2>
<p> <code>bspatch</code> &#8211; apply a patch built with </p>
<p><a href="/docs/linux/man/1-bsdiff/">bsdiff</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> Ao Ar oldfile Ac Ao Ar newfile Ac Ao Ar patchfile Ac</p>
<h2>DESCRIPTION</h2>
<p> generates Ao Ar newfile Ac from Ao Ar oldfile Ac and Ao Ar patchfile Ac where Ao Ar patchfile Ac is a binary patch built by <a href="/docs/linux/man/1-bsdiff/">bsdiff</a>(1). </p>
<p> uses memory equal to the size of Ao Ar oldfile Ac plus the size of Ao Ar newfile Ac , but can tolerate a very small working set without a dramatic loss of performance.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bsdiff/">bsdiff</a>(1)</p>
<h2>AUTHORS</h2>
<p> An Colin Percival Aq cperciva [at] freebsd.org </p>
<h2>Index</h2>
