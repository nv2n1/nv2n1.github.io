---
title: "fclangsethaslang(3)"
name: "fclangsethaslang"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fclangsethaslang/"
description: "FcLangSetHasLang – test langset for language support"
---

<p>FcLangSetHasLang &#8211; test langset for language support </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcLangResult FcLangSetHasLang (const FcLangSet *</code><i>ls</i><code>, const FcChar8 *</code><i>lang</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcLangSetHasLang</code> checks whether <i>ls</i> supports <i>lang</i>. If <i>ls</i> has a matching language and territory pair, this function returns FcLangEqual. If <i>ls</i> has a matching language but differs in which territory that language is for, this function returns FcLangDifferentTerritory. If <i>ls</i> has no matching language, this function returns FcLangDifferentLang.</p>
