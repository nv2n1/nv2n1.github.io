---
title: "fcdircacheclean(3)"
name: "fcdircacheclean"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdircacheclean/"
description: "FcDirCacheClean – Clean up a cache directory"
---

<p>FcDirCacheClean &#8211; Clean up a cache directory </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcDirCacheClean (const FcChar8 *</code><i>cache_dir</i><code>, FcBool</code><i>verbose</i><code>); </code></p>
<h2>Description</h2>
<p>This tries to clean up the cache directory of <i>cache_dir</i>. This returns FcTrue if the operation is successfully complete. otherwise FcFalse.</p>
<h2>Since</h2>
<p>version 2.9.91</p>
