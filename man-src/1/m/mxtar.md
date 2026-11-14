---
title: "mxtar(1)"
name: "mxtar"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mxtar/"
description: "mxtar – Wrapper for using GNU tar directly from a floppy disk"
---

<h2 class="name">NAME</h2>
<p> mxtar &#8211; Wrapper for using GNU tar directly from a floppy disk </p>
<h2>SYNOPSIS</h2>
<p> <code>mxtar </code> [ <code>&#8211;</code> ] <i>[ tar-options ]</i> <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mxtar</code> let you use GNU <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) on a floppy disk without mounting it using <code><a href="/docs/linux/man/1-mtools/">mtools</a></code>(1). It is not strictly necessary on Debian GNU/Linux, because the GNU <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) program provides the same capability after copying the file locally with </p>
<p> <code>mcopy</code> <i>file</i> <i>destination</i> </p>
<p> but this utility is provided in the mtools package for other platforms and is retained here for completeness. </p>
<h2>AUTHOR</h2>
<p> Luis Bustamante &lt;luferbu [at] fluidsignal.com&gt; wrote this page for the <i>Debian/GNU</i> mtools package. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mtools/">mtools</a></code>(1), <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), <code><a href="/docs/linux/man/1-mcopy/">mcopy</a></code>(1) </p>
<h2>Index</h2>
