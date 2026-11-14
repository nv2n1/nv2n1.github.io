---
title: "fcstrcmpignorecase(3)"
name: "fcstrcmpignorecase"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrcmpignorecase/"
description: "FcStrCmpIgnoreCase – compare UTF-8 strings ignoring case"
---

<p>FcStrCmpIgnoreCase &#8211; compare UTF-8 strings ignoring case </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> int FcStrCmpIgnoreCase (const FcChar8 *</code><i>s1</i><code>, const FcChar8 *</code><i>s2</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the usual &lt;0, 0, &gt;0 result of comparing <i>s1</i> and <i>s2</i>. This test is case-insensitive for all proper UTF-8 encoded strings.</p>
