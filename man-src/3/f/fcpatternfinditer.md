---
title: "fcpatternfinditer(3)"
name: "fcpatternfinditer"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternfinditer/"
description: "FcPatternFindIter – Set the iterator to point to the object in the pattern"
---

<p>FcPatternFindIter &#8211; Set the iterator to point to the object in the pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcPatternFindIter (const FcPattern *</code><i>p</i><code>, FcPatternIter *</code><i>iter</i><code>, const char *</code><i>object</i><code>); </code></p>
<h2>Description</h2>
<p>Set <i>iter</i> to point to <i>object</i> in <i>p</i> if any and returns FcTrue. returns FcFalse otherwise.</p>
<h2>Since</h2>
<p>version 2.13.1</p>
