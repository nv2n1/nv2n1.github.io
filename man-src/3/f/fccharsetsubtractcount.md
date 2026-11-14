---
title: "fccharsetsubtractcount(3)"
name: "fccharsetsubtractcount"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsetsubtractcount/"
description: "FcCharSetSubtractCount – Subtract and count charsets"
---

<p>FcCharSetSubtractCount &#8211; Subtract and count charsets </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar32 FcCharSetSubtractCount (const FcCharSet *</code><i>a</i><code>, const FcCharSet *</code><i>b</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the number of chars that are in <i>a</i> but not in <i>b</i>.</p>
