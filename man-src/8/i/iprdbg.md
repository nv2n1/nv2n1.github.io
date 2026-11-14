---
title: "iprdbg(8)"
name: "iprdbg"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iprdbg/"
description: "iprdbg – IBM Power RAID storage adapter debug utility"
---

<p>iprdbg &#8211; IBM Power RAID storage adapter debug utility</p>
<h2>Synopsis</h2>
<p>This executable is part of the package &#8216;iprutils&#8217;: Utilities for the IBM Power Linux RAID Adapters</p>
<h2>Description</h2>
<p><code>iprdbg</code> is used to debug IBM Power RAID storage adapters.</p>
<h2>Exit Status</h2>
<dl>
<dt>-EINVAL</p>
<dd>Invalid input.</p>
<dt>-ENXIO</p>
<dd>No IOA devices. </p>
<p> Or an exit status of specified command.</dl>
<h2>Files</h2>
<dl>
<dt>/etc/iprdbg.conf</p>
<dd>
<dt>/var/log/iprdbg</p>
<dd></dl>
<h2>Notes</h2>
<p>iprdbg is part of iprutils package</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iprconfig/">iprconfig</a>(8),</code> <code><a href="/docs/linux/man/8-iprdump/">iprdump</a></code>(8), <code><a href="/docs/linux/man/8-iprinit/">iprinit</a></code>(8), <code><a href="/docs/linux/man/8-iprupdate/">iprupdate</a></code>(8)</p>
<h2>Author</h2>
<p>Wayne Boyer &lt;wayneb [at] linux.vnet.ibm.com&gt;</p>
