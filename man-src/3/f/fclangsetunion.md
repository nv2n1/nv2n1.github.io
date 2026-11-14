---
title: "fclangsetunion(3)"
name: "fclangsetunion"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fclangsetunion/"
description: "FcLangSetUnion – Add langsets"
---

<p>FcLangSetUnion &#8211; Add langsets </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcLangSet * FcLangSetUnion (const FcLangSet *</code><i>ls_a</i><code>, const FcLangSet *</code><i>ls_b</i><code>); </code></p>
<h2>Description</h2>
<p>Returns a set including only those languages found in either <i>ls_a</i> or <i>ls_b</i>.</p>
<h2>Since</h2>
<p>version 2.9.0</p>
