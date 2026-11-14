---
title: "fcdircacheread(3)"
name: "fcdircacheread"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdircacheread/"
description: "FcDirCacheRead – read or construct a directory cache"
---

<p>FcDirCacheRead &#8211; read or construct a directory cache </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcCache * FcDirCacheRead (const FcChar8 *</code><i>dir</i><code>, FcBool </code><i>force</i><code>, FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>This returns a cache for <i>dir</i>. If <i>force</i> is FcFalse, then an existing, valid cache file will be used. Otherwise, a new cache will be created by scanning the directory and that returned.</p>
