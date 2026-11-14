---
title: "fclangsetcompare(3)"
name: "fclangsetcompare"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fclangsetcompare/"
description: "FcLangSetCompare – compare language sets"
---

<p>FcLangSetCompare &#8211; compare language sets </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcLangResult FcLangSetCompare (const FcLangSet *</code><i>ls_a</i><code>, const FcLangSet *</code><i>ls_b</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcLangSetCompare</code> compares language coverage for <i>ls_a</i> and <i>ls_b</i>. If they share any language and territory pair, this function returns FcLangEqual. If they share a language but differ in which territory that language is for, this function returns FcLangDifferentTerritory. If they share no languages in common, this function returns FcLangDifferentLang.</p>
