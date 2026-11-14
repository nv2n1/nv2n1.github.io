---
title: "pskc_get_device_manufacturer(3)"
name: "pskc_get_device_manufacturer"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_get_device_manufacturer/"
description: "pskc_get_device_manufacturer – API function"
---

<p>pskc_get_device_manufacturer &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
const char *pskc_get_device_manufacturer(pskc_key_t *key);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_key_t * key</p>
<dd>a <code>pskc_key_t</code> handle, from <code>pskc_get_keypackage()</code>.</dl>
<h2>Description</h2>
<p>Get the PSKC KeyPackage DeviceInfo Manufacturer value. This element indicates the manufacturer of the device.</p>
<h2>Returns</h2>
<p>a constant string (must not be deallocated) holding the content, or NULL if not set.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
