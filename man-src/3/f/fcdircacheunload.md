---
title: "fcdircacheunload(3)"
name: "fcdircacheunload"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdircacheunload/"
description: "FcDirCacheUnload – unload a cache file"
---

<p>FcDirCacheUnload &#8211; unload a cache file </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcDirCacheUnload (FcCache *</code><i>cache</i><code>); </code></p>
<h2>Description</h2>
<p>This function dereferences <i>cache</i>. When no other references to it remain, all memory associated with the cache will be freed.</p>
