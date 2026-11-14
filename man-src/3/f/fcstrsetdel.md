---
title: "fcstrsetdel(3)"
name: "fcstrsetdel"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrsetdel/"
description: "FcStrSetDel – delete from a string set"
---

<p>FcStrSetDel &#8211; delete from a string set </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcStrSetDel (FcStrSet *</code><i>set</i><code>, const FcChar8 *</code><i>s</i><code>); </code></p>
<h2>Description</h2>
<p>Removes <i>s</i> from <i>set</i>, returning FcTrue if <i>s</i> was a member else FcFalse.</p>
