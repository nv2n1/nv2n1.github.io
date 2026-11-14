---
title: "xkbgetdeviceinfochanges(3)"
name: "xkbgetdeviceinfochanges"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetdeviceinfochanges/"
description: "XkbGetDeviceInfoChanges – Query the changes that have occurred in the button actions or indicator names and indicator maps associated with an input extension device"
---

<p>XkbGetDeviceInfoChanges &#8211; Query the changes that have occurred in the button actions or indicator names and indicator maps associated with an input extension device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetDeviceInfoChanges</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDeviceInfoPtr </code><i>device_info</i><code>,</code> <code>XkbDeviceChangesPtr </code><i>changes</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_info</i></p>
<dd>structure to update with results</p>
<dt><i>&#8211; changes</i></p>
<dd>contains notes of changes that have occurred</dl>
<h2>Description</h2>
<p>The <i>changes-&gt;changed </i> field indicates which attributes of the device specified in <i>changes-&gt;device </i> have changed. The parameters describing the changes are contained in the other fields of <i>changes. XkbGetDeviceInfoChanges </i> uses that information to call <i>XkbGetDeviceInfo </i> to obtain the current status of those attributes that have changed. It then updates the local description of the device in <i>device_info </i> with the new information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetdeviceinfo/">XkbGetDeviceInfo</a></code>(3)</p>
