---
title: "fcconfighome(3)"
name: "fcconfighome"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfighome/"
description: "FcConfigHome – return the current home directory."
---

<p>FcConfigHome &#8211; return the current home directory. </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcConfigHome (void</code><i></i><code>); </code></p>
<h2>Description</h2>
<p>Return the current user&#8217;s home directory, if it is available, and if using it is enabled, and NULL otherwise. See also <code>FcConfigEnableHome</code>).</p>
