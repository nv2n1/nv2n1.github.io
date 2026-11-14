---
title: "fcstrstrignorecase(3)"
name: "fcstrstrignorecase"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrstrignorecase/"
description: "FcStrStrIgnoreCase – locate UTF-8 substring ignoring ASCII case"
---

<p>FcStrStrIgnoreCase &#8211; locate UTF-8 substring ignoring ASCII case </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcStrStrIgnoreCase (const FcChar8 *</code><i>s1</i><code>, const FcChar8 *</code><i>s2</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the location of <i>s2</i> in <i>s1</i>, ignoring case. Returns NULL if <i>s2</i> is not present in <i>s1</i>. This test is case-insensitive for all proper UTF-8 encoded strings.</p>
