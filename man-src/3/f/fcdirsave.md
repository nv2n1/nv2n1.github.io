---
title: "fcdirsave(3)"
name: "fcdirsave"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdirsave/"
description: "FcDirSave – DEPRECATED: formerly used to save a directory cache"
---

<p>FcDirSave &#8211; DEPRECATED: formerly used to save a directory cache </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcDirSave (FcFontSet *</code><i>set</i><code>, FcStrSet *</code><i>dirs</i><code>, const FcChar8 *</code><i>dir</i><code>); </code></p>
<h2>Description</h2>
<p>This function now does nothing aside from returning FcFalse. It used to creates the per-directory cache file for <i>dir</i> and populates it with the fonts in <i>set</i> and subdirectories in <i>dirs</i>. All of this functionality is now automatically managed by FcDirCacheLoad and FcDirCacheRead.</p>
