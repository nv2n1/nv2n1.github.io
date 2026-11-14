---
title: "ares_version(3)"
name: "ares_version"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_version/"
description: "ares_version – Get the version number of the library"
---

<h2>NAME</h2>
<p> ares_version &#8211; Get the version number of the library</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
const char *ares_version(int *version)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_version</code> function gets the library version as a string and optionally as an integer stored in the <i>version</i>, argument. If you pass a NULL, no integer is attempted to be returned. </p>
<p> The integer is built up as 24bit number, with 8 separate bits used for major number, minor number and patch number. This makes a version string such as 1.2.3 will be returned as the hexadecimal number 0x010203 (decimal 66051).</p>
<h2>NOTES</h2>
<p> This function is not compatible with ares.</p>
<h2>AUTHOR</h2>
<p> Daniel Stenberg </p>
<h2>Index</h2>
