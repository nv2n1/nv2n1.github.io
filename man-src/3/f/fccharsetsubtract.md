---
title: "fccharsetsubtract(3)"
name: "fccharsetsubtract"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsetsubtract/"
description: "FcCharSetSubtract – Subtract charsets"
---

<p>FcCharSetSubtract &#8211; Subtract charsets </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcCharSet * FcCharSetSubtract (const FcCharSet *</code><i>a</i><code>, const FcCharSet *</code><i>b</i><code>); </code></p>
<h2>Description</h2>
<p>Returns a set including only those chars found in <i>a</i> but not <i>b</i>.</p>
