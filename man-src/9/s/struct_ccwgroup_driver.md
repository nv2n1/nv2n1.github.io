---
title: "struct_ccwgroup_driver(9)"
name: "struct_ccwgroup_driver"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_ccwgroup_driver/"
description: "struct_ccwgroup_driver – driver for ccw group devices"
---

<p>struct_ccwgroup_driver &#8211; driver for ccw group devices</p>
<h2>Synopsis</h2>
<pre><code>struct ccwgroup_driver {
    int (*setup)(struct ccwgroup_device *);
    void (*remove)(struct ccwgroup_device *);
    int (*set_online)(struct ccwgroup_device *);
    int (*set_offline)(struct ccwgroup_device *);
    void (*shutdown)(struct ccwgroup_device *);
    int (*prepare)(struct ccwgroup_device *);
    void (*complete)(struct ccwgroup_device *);
    int (*freeze)(struct ccwgroup_device *);
    int (*thaw)(struct ccwgroup_device *);
    int (*restore)(struct ccwgroup_device *);
    struct device_driver driver;
};</code></pre>
<h2>Members</h2>
<p>setup</p>
<dl>
<dd>function called during device creation to setup the device</dl>
<p> remove</p>
<dl>
<dd>function called on remove</dl>
<p> set_online</p>
<dl>
<dd>function called when device is set online</dl>
<p> set_offline</p>
<dl>
<dd>function called when device is set offline</dl>
<p> shutdown</p>
<dl>
<dd>function called when device is shut down</dl>
<p> prepare</p>
<dl>
<dd>prepare for pm state transition</dl>
<p> complete</p>
<dl>
<dd>undo work done in <i>prepare</i></dl>
<p> freeze</p>
<dl>
<dd>callback for freezing during hibernation snapshotting</dl>
<p> thaw</p>
<dl>
<dd>undo work done in <i>freeze</i></dl>
<p> restore</p>
<dl>
<dd>callback for restoring after hibernation</dl>
<p> driver</p>
<dl>
<dd>embedded driver structure</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
