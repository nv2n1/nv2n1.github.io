---
title: "fcconfiggetcachedirs(3)"
name: "fcconfiggetcachedirs"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfiggetcachedirs/"
description: "FcConfigGetCacheDirs – return the list of directories searched for cache files"
---

<p>FcConfigGetCacheDirs &#8211; return the list of directories searched for cache files </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcStrList * FcConfigGetCacheDirs (const FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcConfigGetCacheDirs</code> returns a string list containing all of the directories that fontconfig will search when attempting to load a cache file for a font directory. If <i>config</i> is NULL, the current configuration is used.</p>
