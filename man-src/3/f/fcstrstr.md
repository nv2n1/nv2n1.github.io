---
title: "fcstrstr(3)"
name: "fcstrstr"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrstr/"
description: "FcStrStr – locate UTF-8 substring"
---

<p>FcStrStr &#8211; locate UTF-8 substring </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcStrStr (const FcChar8 *</code><i>s1</i><code>, const FcChar8 *</code><i>s2</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the location of <i>s2</i> in <i>s1</i>. Returns NULL if <i>s2</i> is not present in <i>s1</i>. This test will operate properly with UTF8 encoded strings.</p>
