---
title: "fccachesubdir(3)"
name: "fccachesubdir"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccachesubdir/"
description: "FcCacheSubdir – Return the i’th subdirectory."
---

<p>FcCacheSubdir &#8211; Return the i&#8217;th subdirectory. </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> const FcChar8 * FcCacheSubdir (const FcCache *</code><i>cache</i><code>, int</code><i>i</i><code>); </code></p>
<h2>Description</h2>
<p>The set of subdirectories stored in a cache file are indexed by this function, <i>i</i> should range from 0 to <i>n</i>-1, where <i>n</i> is the return value from FcCacheNumSubdir.</p>
