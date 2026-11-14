---
title: "fclangsetadd(3)"
name: "fclangsetadd"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fclangsetadd/"
description: "FcLangSetAdd – add a language to a langset"
---

<p>FcLangSetAdd &#8211; add a language to a langset </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcLangSetAdd (FcLangSet *</code><i>ls</i><code>, const FcChar8 *</code><i>lang</i><code>); </code></p>
<h2>Description</h2>
<p><i>lang</i> is added to <i>ls</i>. <i>lang</i> should be of the form Ll-Tt where Ll is a two or three letter language from ISO 639 and Tt is a territory from ISO 3166.</p>
