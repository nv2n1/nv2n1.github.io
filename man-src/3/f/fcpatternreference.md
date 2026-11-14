---
title: "fcpatternreference(3)"
name: "fcpatternreference"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternreference/"
description: "FcPatternReference – Increment pattern reference count"
---

<p>FcPatternReference &#8211; Increment pattern reference count </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcPatternReference (FcPattern *</code><i>p</i><code>); </code></p>
<h2>Description</h2>
<p>Add another reference to <i>p</i>. Patterns are freed only when the reference count reaches zero.</p>
