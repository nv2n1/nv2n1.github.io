---
title: "fcdircacheunlink(3)"
name: "fcdircacheunlink"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdircacheunlink/"
description: "FcDirCacheUnlink – Remove all caches related to dir"
---

<p>FcDirCacheUnlink &#8211; Remove all caches related to dir </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcDirCacheUnlink (const FcChar8 *</code><i>dir</i><code>, FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Scans the cache directories in <i>config</i>, removing any instances of the cache file for <i>dir</i>. Returns FcFalse when some internal error occurs (out of memory, etc). Errors actually unlinking any files are ignored.</p>
