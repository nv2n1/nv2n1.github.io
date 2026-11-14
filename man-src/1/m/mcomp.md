---
title: "mcomp(1)"
name: "mcomp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcomp/"
description: "mcomp – Compares two files using mtools"
---

<h2 class="name">NAME</h2>
<p> mcomp &#8211; Compares two files using mtools </p>
<h2>SYNOPSIS</h2>
<p> <code>mcomp</code> <i>file-on-floppy</i> <i>local-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mcomp</code> compares two files, the first one must be on a floppy disk so it can be accessed via <code>mtools</code>. It is not strictly necessary on Debian GNU/Linux, because the diffutils <code><a href="/docs/linux/man/1-cmp/">cmp</a></code>(1) program provides the same capability after copying the file locally with </p>
<p> <code>mcopy</code> <i>file</i> <i>destination</i> </p>
<p> but this utility is provided in the mtools package for other platforms and is retained here for completeness. </p>
<h2>AUTHOR</h2>
<p> Luis Bustamante &lt;luferbu [at] fluidsignal.com&gt; wrote this page for the <i>Debian/GNU</i> mtools package. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mtools/">mtools</a></code>(1), <code><a href="/docs/linux/man/1-cmp/">cmp</a></code>(1), <code><a href="/docs/linux/man/1-mcopy/">mcopy</a></code>(1) </p>
<h2>Index</h2>
