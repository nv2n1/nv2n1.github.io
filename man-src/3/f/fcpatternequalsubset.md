---
title: "fcpatternequalsubset(3)"
name: "fcpatternequalsubset"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternequalsubset/"
description: "FcPatternEqualSubset – Compare portions of patterns"
---

<p>FcPatternEqualSubset &#8211; Compare portions of patterns </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcPatternEqualSubset (const FcPattern *</code><i>pa</i><code>, const FcPattern *</code><i>pb</i><code>, const FcObjectSet *</code><i>os</i><code>); </code></p>
<h2>Description</h2>
<p>Returns whether <i>pa</i> and <i>pb</i> have exactly the same values for all of the objects in <i>os</i>.</p>
