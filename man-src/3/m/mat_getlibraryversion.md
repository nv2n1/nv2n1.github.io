---
title: "mat_getlibraryversion(3)"
name: "mat_getlibraryversion"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_getlibraryversion/"
description: "Mat_GetLibraryVersion – Get the version of the matio library"
---

<p><code>Mat_GetLibraryVersion</code> &#8211; Get the version of the matio library</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft void Fo Mat_GetLibraryVersion Fa int *major Fa int *minor Fa int *release Fc</p>
<h2>Description</h2>
<p>The Fn Mat_GetLibraryVersion function returns the major, minor, and release version numbers of the library. These can be used to check that the version specified in the header by <code>MATIO_MAJOR_VERSION,</code> <code>MATIO_MINOR_VERSION,</code> and <code>MATIO_RELEASE_LEVEL.</code></p>
