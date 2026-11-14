---
title: "ccw_device_get_path_mask(9)"
name: "ccw_device_get_path_mask"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_get_path_mask/"
description: "ccw_device_get_path_mask – get currently available paths"
---

<p>ccw_device_get_path_mask &#8211; get currently available paths</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>__u8 ccw_device_get_path_mask(struct ccw_device&nbsp;<wbr>*&nbsp;<wbr></code><i>cdev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>ccw device to be queried</dl>
<h2>Return</h2>
<p><code>0</code> if no subchannel for the device is available, else the mask of currently available paths for the ccw device&#8217;s subchannel.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
