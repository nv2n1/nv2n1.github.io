---
title: "fclangsetdel(3)"
name: "fclangsetdel"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fclangsetdel/"
description: "FcLangSetDel – delete a language from a langset"
---

<p>FcLangSetDel &#8211; delete a language from a langset </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcLangSetDel (FcLangSet *</code><i>ls</i><code>, const FcChar8 *</code><i>lang</i><code>); </code></p>
<h2>Description</h2>
<p><i>lang</i> is removed from <i>ls</i>. <i>lang</i> should be of the form Ll-Tt where Ll is a two or three letter language from ISO 639 and Tt is a territory from ISO 3166.</p>
<h2>Since</h2>
<p>version 2.9.0</p>
