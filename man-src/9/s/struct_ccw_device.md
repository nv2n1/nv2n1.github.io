---
title: "struct_ccw_device(9)"
name: "struct_ccw_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_ccw_device/"
description: "struct_ccw_device – channel attached device"
---

<p>struct_ccw_device &#8211; channel attached device</p>
<h2>Synopsis</h2>
<pre><code>struct ccw_device {
    spinlock_t *ccwlock;
    struct ccw_device_id id;
    struct ccw_driver *drv;
    struct device dev;
    int online;
    void (*handler)(struct ccw_device *, unsigned long, struct irb *);
};</code></pre>
<h2>Members</h2>
<p>ccwlock</p>
<dl>
<dd>pointer to device lock</dl>
<p> id</p>
<dl>
<dd>id of this device</dl>
<p> drv</p>
<dl>
<dd>ccw driver for this device</dl>
<p> dev</p>
<dl>
<dd>embedded device structure</dl>
<p> online</p>
<dl>
<dd>online status of device</dl>
<p> handler</p>
<dl>
<dd>interrupt handler</dl>
<h2>Description</h2>
<p><i>handler</i> is a member of the device rather than the driver since a driver can have different interrupt handlers for different ccw devices (multi-subchannel drivers).</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
