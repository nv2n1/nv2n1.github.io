---
title: "fcpatternadd(3)"
name: "fcpatternadd"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternadd/"
description: "FcPatternAdd – Add a value to a pattern"
---

<p>FcPatternAdd &#8211; Add a value to a pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcPatternAdd (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, FcValue </code><i>value</i><code>, FcBool </code><i>append</i><code>); </code></p>
<h2>Description</h2>
<p>Adds a single value to the list of values associated with the property named `object<i>. If `append</i> is FcTrue, the value is added at the end of any existing list, otherwise it is inserted at the beginning. `value&#8217; is saved (with FcValueSave) when inserted into the pattern so that the library retains no reference to any application-supplied data structure.</p>
