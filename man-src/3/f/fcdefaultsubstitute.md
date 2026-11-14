---
title: "fcdefaultsubstitute(3)"
name: "fcdefaultsubstitute"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdefaultsubstitute/"
description: "FcDefaultSubstitute – Perform default substitutions in a pattern"
---

<p>FcDefaultSubstitute &#8211; Perform default substitutions in a pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcDefaultSubstitute (FcPattern *</code><i>pattern</i><code>); </code></p>
<h2>Description</h2>
<p>Supplies default values for underspecified font patterns:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Patterns without a specified style or weight are set to Medium</p>
<dt>&bull;</p>
<dd>Patterns without a specified style or slant are set to Roman</p>
<dt>&bull;</p>
<dd>Patterns without a specified pixel size are given one computed from any specified point size (default 12), dpi (default 75) and scale (default 1). </p>
</dl>
