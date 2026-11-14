---
title: "fccharsetaddchar(3)"
name: "fccharsetaddchar"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsetaddchar/"
description: "FcCharSetAddChar – Add a character to a charset"
---

<p>FcCharSetAddChar &#8211; Add a character to a charset </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcCharSetAddChar (FcCharSet *</code><i>fcs</i><code>, FcChar32 </code><i>ucs4</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcCharSetAddChar</code> adds a single Unicode char to the set, returning FcFalse on failure, either as a result of a constant set or from running out of memory.</p>
