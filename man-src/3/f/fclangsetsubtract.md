---
title: "fclangsetsubtract(3)"
name: "fclangsetsubtract"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fclangsetsubtract/"
description: "FcLangSetSubtract – Subtract langsets"
---

<p>FcLangSetSubtract &#8211; Subtract langsets </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcLangSet * FcLangSetSubtract (const FcLangSet *</code><i>ls_a</i><code>, const FcLangSet *</code><i>ls_b</i><code>); </code></p>
<h2>Description</h2>
<p>Returns a set including only those languages found in <i>ls_a</i> but not in <i>ls_b</i>.</p>
<h2>Since</h2>
<p>version 2.9.0</p>
