---
title: "fcatomiccreate(3)"
name: "fcatomiccreate"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcatomiccreate/"
description: "FcAtomicCreate – create an FcAtomic object"
---

<p>FcAtomicCreate &#8211; create an FcAtomic object </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcAtomic * FcAtomicCreate (const FcChar8 *</code><i>file</i><code>); </code></p>
<h2>Description</h2>
<p>Creates a data structure containing data needed to control access to <i>file</i>. Writing is done to a separate file. Once that file is complete, the original configuration file is atomically replaced so that reading process always see a consistent and complete file without the need to lock for reading.</p>
