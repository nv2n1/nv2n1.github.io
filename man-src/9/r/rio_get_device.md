---
title: "rio_get_device(9)"
name: "rio_get_device"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_get_device/"
description: "rio_get_device – Begin or continue searching for a RIO device by vid/did"
---

<p>rio_get_device &#8211; Begin or continue searching for a RIO device by vid/did</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>struct rio_dev * rio_get_device(u16&nbsp;<wbr></code><i>vid</i><code>, u16&nbsp;<wbr></code><i>did</i><code>, struct rio_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>from</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>vid</i></p>
<dl>
<dd>
<dd>RIO vid to match or <code>RIO_ANY_ID</code> to match all vids</dl>
<p> <i>did</i></p>
<dl>
<dd>RIO did to match or <code>RIO_ANY_ID</code> to match all dids</dl>
<p> <i>from</i></p>
<dl>
<dd>Previous RIO device found in search, or <code>NULL</code> for new search</dl>
<h2>Description</h2>
<p>Iterates through the list of known RIO devices. If a RIO device is found with a matching <i>vid</i> and <i>did</i>, the reference count to the device is incrememted and a pointer to its device structure is returned. Otherwise, <code>NULL</code> is returned. A new search is initiated by passing <code>NULL</code> to the <i>from</i> argument. Otherwise, if <i>from</i> is not <code>NULL</code>, searches continue from next device on the global list. The reference count for <i>from</i> is always decremented if it is not <code>NULL</code>.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
