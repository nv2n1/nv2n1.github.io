---
title: "fcdircacheloadfile(3)"
name: "fcdircacheloadfile"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdircacheloadfile/"
description: "FcDirCacheLoadFile – load a cache file"
---

<p>FcDirCacheLoadFile &#8211; load a cache file </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcCache * FcDirCacheLoadFile (const FcChar8 *</code><i>cache_file</i><code>, struct stat *</code><i>file_stat</i><code>); </code></p>
<h2>Description</h2>
<p>This function loads a directory cache from <i>cache_file</i>. If <i>file_stat</i> is non-NULL, it will be filled with the results of <a href="/docs/linux/man/2-stat/">stat</a>(2) on the cache file.</p>
