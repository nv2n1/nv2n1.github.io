---
title: "fcstrbasename(3)"
name: "fcstrbasename"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrbasename/"
description: "FcStrBasename – last component of filename"
---

<p>FcStrBasename &#8211; last component of filename </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcStrBasename (const FcChar8 *</code><i>file</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the filename of <i>file</i> stripped of any leading directory names. This is returned in newly allocated storage which should be freed when no longer needed.</p>
