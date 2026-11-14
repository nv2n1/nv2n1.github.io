---
title: "fcdirscan(3)"
name: "fcdirscan"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdirscan/"
description: "FcDirScan – scan a font directory without caching it"
---

<p>FcDirScan &#8211; scan a font directory without caching it </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcDirScan (FcFontSet *</code><i>set</i><code>, FcStrSet *</code><i>dirs</i><code>, FcFileCache *</code><i>cache</i><code>, FcBlanks *</code><i>blanks</i><code>, const FcChar8 *</code><i>dir</i><code>, FcBool </code><i>force</i><code>); </code></p>
<h2>Description</h2>
<p>If <i>cache</i> is not zero or if <i>force</i> is FcFalse, this function currently returns FcFalse. Otherwise, it scans an entire directory and adds all fonts found to <i>set</i>. Any subdirectories found are added to <i>dirs</i>. Calling this function does not create any cache files. Use FcDirCacheRead() if caching is desired.</p>
