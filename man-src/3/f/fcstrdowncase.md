---
title: "fcstrdowncase(3)"
name: "fcstrdowncase"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrdowncase/"
description: "FcStrDowncase – create a lower case translation of a string"
---

<p>FcStrDowncase &#8211; create a lower case translation of a string </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcStrDowncase (const FcChar8 *</code><i>s</i><code>); </code></p>
<h2>Description</h2>
<p>Allocates memory, copies <i>s</i>, converting upper case letters to lower case and returns the allocated buffer.</p>
