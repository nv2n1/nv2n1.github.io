---
title: "diffindex-rred(1)"
name: "diffindex-rred"
section: "1"
letter: "d"
url: "/docs/linux/man/1-diffindex-rred/"
description: "diffindex-rred – Restricted restricted ed"
---

<h2 class="name">NAME</h2>
<p> diffindex-rred &#8211; Restricted restricted ed </p>
<h2>SYNOPSIS</h2>
<p> <code>diffindex-rred</code> <code>diff1</code><i> &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>diffindex-rred</code> is a command line tool for applying <code>diff &#8211;ed</code> style patches, as used in APT&#8217;s diff/Index format. It can efficiently apply several patches in one run and does not need to read the whole source file into memory. </p>
<p> The source file is taken from stdin. The patched file is written to stdout. Compressed patch files are decompressed automatically if they have the proper .gz, .bz2, or .lzo extension. </p>
<p> <code>diffindex-rred</code> is used by <code>diffindex-download</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apt-file/">apt-file</a></code>(1), <code><a href="/docs/linux/man/1-diffindex-download/">diffindex-download</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>diffindex-rred</code> was written by Stefan Fritsch &lt;sf [at] debian.org&gt;. </p>
<h2>Index</h2>
