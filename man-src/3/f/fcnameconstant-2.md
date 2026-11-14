---
title: "fcnameconstant-2(3)"
name: "fcnameconstant-2"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcnameconstant-2/"
description: "FcNameConstant – Get the value for a symbolic constant"
---

<p>FcNameConstant &#8211; Get the value for a symbolic constant </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcNameConstant (FcChar8 *</code><i>string</i><code>, int *</code><i>result</i><code>); </code></p>
<h2>Description</h2>
<p>Returns whether a symbolic constant with name <i>string</i> is registered, placing the value of the constant in <i>result</i> if present.</p>
