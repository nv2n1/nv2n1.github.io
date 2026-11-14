---
title: "fcpatternduplicate(3)"
name: "fcpatternduplicate"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternduplicate/"
description: "FcPatternDuplicate – Copy a pattern"
---

<p>FcPatternDuplicate &#8211; Copy a pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcPattern * FcPatternDuplicate (const FcPattern *</code><i>p</i><code>); </code></p>
<h2>Description</h2>
<p>Copy a pattern, returning a new pattern that matches <i>p</i>. Each pattern may be modified without affecting the other.</p>
