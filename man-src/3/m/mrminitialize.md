---
title: "mrminitialize(3)"
name: "mrminitialize"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrminitialize/"
description: "MrmInitialize — Prepares an application to use MRM widget-fetching facilities"
---

<p><code>MrmInitialize</code> &#8212; Prepares an application to use MRM widget-fetching facilities</p>
<h2>Synopsis</h2>
<pre><code>void MrmInitialize</code>(<code>void</code>)</pre>
<h2>Description</h2>
<p>The <code>MrmInitialize</code> function must be called to prepare an application to use MRM widget-fetching facilities. You must call this function prior to fetching a widget. However, it is good programming practice to call <code>MrmInitialize</code> prior to performing any MRM operations. </p>
<p> <code>MrmInitialize</code> initializes the internal data structures that MRM needs to successfully perform type conversion on arguments and to successfully access widget creation facilities. An application must call <code>MrmInitialize</code> before it uses other MRM functions.</p>
