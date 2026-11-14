---
title: "fcpatternaddweak(3)"
name: "fcpatternaddweak"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternaddweak/"
description: "FcPatternAddWeak – Add a value to a pattern with weak binding"
---

<p>FcPatternAddWeak &#8211; Add a value to a pattern with weak binding </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcPatternAddWeak (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, FcValue </code><i>value</i><code>, FcBool </code><i>append</i><code>); </code></p>
<h2>Description</h2>
<p>FcPatternAddWeak is essentially the same as FcPatternAdd except that any values added to the list have binding <i>weak</i> instead of <i>strong</i>.</p>
