---
title: "struct_ccwgroup_device(9)"
name: "struct_ccwgroup_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_ccwgroup_device/"
description: "struct_ccwgroup_device – ccw group device"
---

<p>struct_ccwgroup_device &#8211; ccw group device</p>
<h2>Synopsis</h2>
<pre><code>struct ccwgroup_device {
    enum state;
    unsigned int count;
    struct device dev;
    struct work_struct ungroup_work;
    struct ccw_device *cdev[0];
};</code></pre>
<h2>Members</h2>
<p>state</p>
<dl>
<dd>online/offline state</dl>
<p> count</p>
<dl>
<dd>number of attached slave devices</dl>
<p> dev</p>
<dl>
<dd>embedded device structure</dl>
<p> ungroup_work</p>
<dl>
<dd>work to be done when a ccwgroup notifier has action type <code>BUS_NOTIFY_UNBIND_DRIVER</code></dl>
<p> cdev[0]</p>
<dl>
<dd>variable number of slave devices, allocated as needed</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
