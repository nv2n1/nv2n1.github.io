---
title: "ibsrpdm(1)"
name: "ibsrpdm"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibsrpdm/"
description: "ibsrpdm – Discover SRP targets on an InfiniBand Fabric"
---

<h2 class="name">NAME</h2>
<p> ibsrpdm &#8211; Discover SRP targets on an InfiniBand Fabric</p>
<h2>SYNOPSIS</h2>
<p> <code>ibsrpdm [</code><i>OPTIONS</i><code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> List InfiniBand SCSI RDMA Protocol (SRP) targets on an IB fabric. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Generate output suitable for piping directly to a /sys/class/infiniband_srp/srp-&lt;device&gt;-&lt;port&gt;/add_target file</p>
<dt><code>-d</code> <i>DEVICE</i></p>
<dd> Use device file <i>DEVICE</i> (default /dev/infiniband/umad0)</p>
<dt><code>-k</code> <i>P_KEY</i></p>
<dd> Use InfiniBand partition key <i>P_KEY</i> (default 0xffff)</p>
<dt><code>-v</code></p>
<dd> Print more verbose output </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-srp_daemon/">srp_daemon</a></code>(1) </p>
<h2>AUTHORS</h2>
<dl>
<dt>Roland Dreier</p>
<dd> &lt;<i>roland [at] kernel.org</i>&gt; </p>
</dl>
<h2>Index</h2>
