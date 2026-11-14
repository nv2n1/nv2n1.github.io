---
title: "fcvaluedestroy(3)"
name: "fcvaluedestroy"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcvaluedestroy/"
description: "FcValueDestroy – Free a value"
---

<p>FcValueDestroy &#8211; Free a value </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcValueDestroy (FcValue </code><i>v</i><code>); </code></p>
<h2>Description</h2>
<p>Frees any memory referenced by <i>v</i>. Values of type FcTypeString, FcTypeMatrix and FcTypeCharSet reference memory, the other types do not.</p>
