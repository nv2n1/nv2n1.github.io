---
title: "fcstrdirname(3)"
name: "fcstrdirname"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrdirname/"
description: "FcStrDirname – directory part of filename"
---

<p>FcStrDirname &#8211; directory part of filename </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcStrDirname (const FcChar8 *</code><i>file</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the directory containing <i>file</i>. This is returned in newly allocated storage which should be freed when no longer needed.</p>
