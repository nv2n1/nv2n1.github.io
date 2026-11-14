---
title: "upscli_cleanup(3)"
name: "upscli_cleanup"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_cleanup/"
description: "upscli_cleanup – Clean-up upsclient module after usage."
---

<p>upscli_cleanup &#8211; Clean-up upsclient module after usage.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
int upscli_cleanup();</code></pre>
<h2>Description</h2>
<p>The <code>upscli_cleanup()</code> function flushes SSL caches and frees memory used internally in upsclient module.</p>
<h2>Return Value</h2>
<p>The <code>upscli_cleanup()</code> function returns 1 on success, or -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_init/">upscli_init</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
