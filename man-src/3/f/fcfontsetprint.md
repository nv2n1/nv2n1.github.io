---
title: "fcfontsetprint(3)"
name: "fcfontsetprint"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfontsetprint/"
description: "FcFontSetPrint – Print a set of patterns to stdout"
---

<p>FcFontSetPrint &#8211; Print a set of patterns to stdout </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcFontSetPrint (FcFontSet *</code><i>set</i><code>); </code></p>
<h2>Description</h2>
<p>This function is useful for diagnosing font related issues, printing the complete contents of every pattern in <i>set</i>. The format of the output is designed to be of help to users and developers, and may change at any time.</p>
