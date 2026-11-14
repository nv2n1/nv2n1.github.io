---
title: "misc_register(9)"
name: "misc_register"
section: "9"
letter: "m"
url: "/docs/linux/man/9-misc_register/"
description: "misc_register – register a miscellaneous device"
---

<p>misc_register &#8211; register a miscellaneous device</p>
<h2>Synopsis</h2>
<pre><code>int misc_register(struct miscdevice *misc);</code></pre>
<h2>Arguments</h2>
<p><i>misc</i></p>
<dl>
<dd>
<dd>device structure</dl>
<h2>Description</h2>
<p>Register a miscellaneous device with the kernel. If the minor number is set to <code>MISC_DYNAMIC_MINOR</code> a minor number is assigned and placed in the minor field of the structure. For other cases the minor number requested is used. </p>
<p> The structure passed is linked into the kernel and may not be destroyed until it has been unregistered. By default, an <code>open</code> syscall to the device sets file-&gt;private_data to point to the structure. Drivers don&#8217;t need open in fops for this. </p>
<p> A zero is returned on success and a negative errno code for failure.</p>
<h2>Copyright</h2>
