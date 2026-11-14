---
title: "struct_ccw_dev_id(9)"
name: "struct_ccw_dev_id"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_ccw_dev_id/"
description: "struct_ccw_dev_id – unique identifier for ccw devices"
---

<p>struct_ccw_dev_id &#8211; unique identifier for ccw devices</p>
<h2>Synopsis</h2>
<pre><code>struct ccw_dev_id {
    u8 ssid;
    u16 devno;
};</code></pre>
<h2>Members</h2>
<p>ssid</p>
<dl>
<dd>subchannel set id</dl>
<p> devno</p>
<dl>
<dd>device number</dl>
<h2>Description</h2>
<p>This structure is not directly based on any hardware structure. The hardware identifies a device by its device number and its subchannel, which is in turn identified by its id. In order to get a unique identifier for ccw devices across subchannel sets, <i>struct</i> ccw_dev_id has been introduced.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
