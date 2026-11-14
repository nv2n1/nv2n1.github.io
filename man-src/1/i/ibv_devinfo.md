---
title: "ibv_devinfo(1)"
name: "ibv_devinfo"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibv_devinfo/"
description: "ibv_devinfo – query RDMA devices"
---

<h2 class="name">NAME</h2>
<p> ibv_devinfo &#8211; query RDMA devices</p>
<h2>SYNOPSIS</h2>
<p> <code>ibv_devinfo</code> [-d device] [-i port] [-l] [-v] </p>
<h2>DESCRIPTION</h2>
<p> Print information about RDMA devices available for use from userspace. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;ib-dev</code>=<i>DEVICE</i></p>
<dd> use IB device <i>DEVICE</i> (default first device found) </p>
<p> <code>-i</code>, <code>&#8211;ib-port</code>=<i>PORT</i> query port <i>PORT</i> (default all ports) </p>
<p> <code>-l</code>, <code>&#8211;list</code> only list names of RDMA devices </p>
<p> <code>-v</code>, <code>&#8211;verbose</code> print all available information about RDMA devices </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ibv_devices/">ibv_devices</a></code>(1) </p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak</p>
<dd> &lt;<i>dotanba [at] gmail.com</i>&gt;</p>
<dt>Roland Dreier</p>
<dd> &lt;<i>rolandd [at] cisco.com</i>&gt; </p>
</dl>
<h2>Index</h2>
