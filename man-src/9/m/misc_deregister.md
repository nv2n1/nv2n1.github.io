---
title: "misc_deregister(9)"
name: "misc_deregister"
section: "9"
letter: "m"
url: "/docs/linux/man/9-misc_deregister/"
description: "misc_deregister – unregister a miscellaneous device"
---

<p>misc_deregister &#8211; unregister a miscellaneous device</p>
<h2>Synopsis</h2>
<pre><code>void misc_deregister(struct miscdevice *misc);</code></pre>
<h2>Arguments</h2>
<p><i>misc</i></p>
<dl>
<dd>
<dd>device to unregister</dl>
<h2>Description</h2>
<p>Unregister a miscellaneous device that was previously successfully registered with <code>misc_register</code>.</p>
<h2>Copyright</h2>
