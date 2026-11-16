---
title: "struct_ccw_driver(9)"
name: "struct_ccw_driver"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_ccw_driver/"
description: "struct_ccw_driver – device driver for channel attached devices"
---

<p>struct_ccw_driver &#8211; device driver for channel attached devices</p>
<h2>Synopsis</h2>
<pre><code>struct ccw_driver {
    struct ccw_device_id *ids;
    int (*probe)(struct ccw_device *);
    void (*remove)(struct ccw_device *);
    int (*set_online)(struct ccw_device *);
    int (*set_offline)(struct ccw_device *);
    int (*notify)(struct ccw_device *, int);
    void (*path_event)(struct ccw_device *, int *);
    void (*shutdown)(struct ccw_device *);
    int (*prepare)(struct ccw_device *);
    void (*complete)(struct ccw_device *);
    int (*freeze)(struct ccw_device *);
    int (*thaw)(struct ccw_device *);
    int (*restore)(struct ccw_device *);
    enum uc_todo (*uc_handler)(struct ccw_device *, struct irb *);
    struct device_driver driver;
    enum interruption_class int_class;
};</code></pre>
<h2>Members</h2>
<p>ids</p>
<dl>
<dd>ids supported by this driver</dd></dl>
<p> probe</p>
<dl>
<dd>function called on probe</dd></dl>
<p> remove</p>
<dl>
<dd>function called on remove</dd></dl>
<p> set_online</p>
<dl>
<dd>called when setting device online</dd></dl>
<p> set_offline</p>
<dl>
<dd>called when setting device offline</dd></dl>
<p> notify</p>
<dl>
<dd>notify driver of device state changes</dd></dl>
<p> path_event</p>
<dl>
<dd>notify driver of channel path events</dd></dl>
<p> shutdown</p>
<dl>
<dd>called at device shutdown</dd></dl>
<p> prepare</p>
<dl>
<dd>prepare for pm state transition</dd></dl>
<p> complete</p>
<dl>
<dd>undo work done in <i>prepare</i></dd></dl>
<p> freeze</p>
<dl>
<dd>callback for freezing during hibernation snapshotting</dd></dl>
<p> thaw</p>
<dl>
<dd>undo work done in <i>freeze</i></dd></dl>
<p> restore</p>
<dl>
<dd>callback for restoring after hibernation</dd></dl>
<p> uc_handler</p>
<dl>
<dd>callback for unit check handler</dd></dl>
<p> driver</p>
<dl>
<dd>embedded device driver structure</dd></dl>
<p> int_class</p>
<dl>
<dd>interruption class to use for accounting interrupts</dd></dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
