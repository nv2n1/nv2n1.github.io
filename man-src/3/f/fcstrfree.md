---
title: "fcstrfree(3)"
name: "fcstrfree"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrfree/"
description: "FcStrFree – free a string"
---

<p>FcStrFree &#8211; free a string </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcStrFree (FcChar8 *</code><i>s</i><code>); </code></p>
<h2>Description</h2>
<p>This is just a wrapper around <a href="/docs/linux/man/3-free/">free</a>(3) which helps track memory usage of strings within the fontconfig library.</p>
