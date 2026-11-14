---
title: "fcdircacheload(3)"
name: "fcdircacheload"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdircacheload/"
description: "FcDirCacheLoad – load a directory cache"
---

<p>FcDirCacheLoad &#8211; load a directory cache </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcCache * FcDirCacheLoad (const FcChar8 *</code><i>dir</i><code>, FcConfig *</code><i>config</i><code>, FcChar8 **</code><i>cache_file</i><code>); </code></p>
<h2>Description</h2>
<p>Loads the cache related to <i>dir</i>. If no cache file exists, returns NULL. The name of the cache file is returned in <i>cache_file</i>, unless that is NULL. See also FcDirCacheRead.</p>
