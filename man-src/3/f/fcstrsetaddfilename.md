---
title: "fcstrsetaddfilename(3)"
name: "fcstrsetaddfilename"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrsetaddfilename/"
description: "FcStrSetAddFilename – add a filename to a string set"
---

<p>FcStrSetAddFilename &#8211; add a filename to a string set </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcStrSetAddFilename (FcStrSet *</code><i>set</i><code>, const FcChar8 *</code><i>s</i><code>); </code></p>
<h2>Description</h2>
<p>Adds a copy <i>s</i> to <i>set</i>, The copy is created with FcStrCopyFilename so that leading &#8216;~&#8217; values are replaced with the value of the HOME environment variable.</p>
