---
title: "tk_gethinstance(3)"
name: "tk_gethinstance"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_gethinstance/"
description: "Tk_GetHINSTANCE – retrieve the global application instance handle"
---

<p>Tk_GetHINSTANCE &#8211; retrieve the global application instance handle </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tkPlatDecls.h&gt;</code>
HINSTANCE
<code>Tk_GetHINSTANCE</code>()
<br>
<hr></pre>
<h2>Description</h2>
<p><code>Tk_GetHINSTANCE</code> returns the Windows application instance handle for the Tk application. This function is only available on Windows platforms.</p>
<h2>Keywords</h2>
<p>identifier, instance</p>
