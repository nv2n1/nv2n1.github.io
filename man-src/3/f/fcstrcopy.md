---
title: "fcstrcopy(3)"
name: "fcstrcopy"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrcopy/"
description: "FcStrCopy – duplicate a string"
---

<p>FcStrCopy &#8211; duplicate a string </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcStrCopy (const FcChar8 *</code><i>s</i><code>); </code></p>
<h2>Description</h2>
<p>Allocates memory, copies <i>s</i> and returns the resulting buffer. Yes, this is <code>strdup</code>, but that function isn&#8217;t available on every platform.</p>
