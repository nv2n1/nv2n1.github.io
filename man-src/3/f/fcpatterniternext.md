---
title: "fcpatterniternext(3)"
name: "fcpatterniternext"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatterniternext/"
description: "FcPatternIterNext –"
---

<p>FcPatternIterNext &#8211; </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcPatternIterNext (const FcPattern *</code><i>p</i><code>, FcPatternIter *</code><i>iter</i><code>); </code></p>
<h2>Description</h2>
<p>Set <i>iter</i> to point to the next object in <i>p</i> and returns FcTrue if <i>iter</i> has been changed to the next object. returns FcFalse otherwise.</p>
<h2>Since</h2>
<p>version 2.13.1</p>
