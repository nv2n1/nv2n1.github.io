---
title: "dmi_find_device(9)"
name: "dmi_find_device"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dmi_find_device/"
description: "dmi_find_device – find onboard device by type/name"
---

<p>dmi_find_device &#8211; find onboard device by type/name</p>
<h2>Synopsis</h2>
<pre><code>const struct dmi_device *dmi_find_device(int type, const char *name, const struct dmi_device *from);</code></pre>
<h2>Arguments</h2>
<p><i>type</i></p>
<dl>
<dd>
<dd>device type or <code>DMI_DEV_TYPE_ANY</code> to match all device types</dl>
<p> <i>name</i></p>
<dl>
<dd>device name string or <code>NULL</code> to match all</dl>
<p> <i>from</i></p>
<dl>
<dd>previous device found in search, or <code>NULL</code> for new search.</dl>
<h2>Description</h2>
<p>Iterates through the list of known onboard devices. If a device is found with a matching <i>type</i> and <i>name</i>, a pointer to its device structure is returned. Otherwise, <code>NULL</code> is returned. A new search is initiated by passing <code>NULL</code> as the <i>from</i> argument. If <i>from</i> is not <code>NULL</code>, searches continue from next device.</p>
<h2>Copyright</h2>
