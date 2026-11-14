---
title: "fccharsetmerge(3)"
name: "fccharsetmerge"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsetmerge/"
description: "FcCharSetMerge – Merge charsets"
---

<p>FcCharSetMerge &#8211; Merge charsets </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcCharSetMerge (FcCharSet *</code><i>a</i><code>, const FcCharSet *</code><i>b</i><code>, FcBool *</code><i>changed</i><code>); </code></p>
<h2>Description</h2>
<p>Adds all chars in <i>b</i> to <i>a</i>. In other words, this is an in-place version of FcCharSetUnion. If <i>changed</i> is not NULL, then it returns whether any new chars from <i>b</i> were added to <i>a</i>. Returns FcFalse on failure, either when <i>a</i> is a constant set or from running out of memory.</p>
