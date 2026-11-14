---
title: "fcstrplus(3)"
name: "fcstrplus"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrplus/"
description: "FcStrPlus – concatenate two strings"
---

<p>FcStrPlus &#8211; concatenate two strings </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcStrPlus (const FcChar8 *</code><i>s1</i><code>, const FcChar8 *</code><i>s2</i><code>); </code></p>
<h2>Description</h2>
<p>This function allocates new storage and places the concatenation of <i>s1</i> and <i>s2</i> there, returning the new string.</p>
