---
title: "fccharsetdelchar(3)"
name: "fccharsetdelchar"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsetdelchar/"
description: "FcCharSetDelChar – Add a character to a charset"
---

<p>FcCharSetDelChar &#8211; Add a character to a charset </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcCharSetDelChar (FcCharSet *</code><i>fcs</i><code>, FcChar32 </code><i>ucs4</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcCharSetDelChar</code> deletes a single Unicode char from the set, returning FcFalse on failure, either as a result of a constant set or from running out of memory.</p>
<h2>Since</h2>
<p>version 2.9.0</p>
