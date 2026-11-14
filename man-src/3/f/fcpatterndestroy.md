---
title: "fcpatterndestroy(3)"
name: "fcpatterndestroy"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatterndestroy/"
description: "FcPatternDestroy – Destroy a pattern"
---

<p>FcPatternDestroy &#8211; Destroy a pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcPatternDestroy (FcPattern *</code><i>p</i><code>); </code></p>
<h2>Description</h2>
<p>Decrement the pattern reference count. If all references are gone, destroys the pattern, in the process destroying all related values.</p>
