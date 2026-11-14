---
title: "fcdircacherescan(3)"
name: "fcdircacherescan"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdircacherescan/"
description: "FcDirCacheRescan – Re-scan a directory cache"
---

<p>FcDirCacheRescan &#8211; Re-scan a directory cache </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcCache * FcDirCacheRescan (const FcChar8 *</code><i>dir</i><code>, FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Re-scan directories only at <i>dir</i> and update the cache. returns NULL if failed.</p>
<h2>Since</h2>
<p>version 2.11.1</p>
