---
title: "ibsrpdm(1)"
name: "ibsrpdm"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibsrpdm/"
description: "ibsrpdm – Discover SRP targets on an InfiniBand Fabric"
---

<h2>SYNOPSIS</h2>
<p> <code>ibsrpdm [</code><i>OPTIONS</i><code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> List InfiniBand SCSI RDMA Protocol (SRP) targets on an IB fabric. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></dt>
<dd> Generate output suitable for piping directly to a /sys/class/infiniband_srp/srp-&lt;device&gt;-&lt;port&gt;/add_target file</dd>
<dt><code>-d</code> <i>DEVICE</i></dt>
<dd> Use device file <i>DEVICE</i> (default /dev/infiniband/umad0)</dd>
<dt><code>-k</code> <i>P_KEY</i></dt>
<dd> Use InfiniBand partition key <i>P_KEY</i> (default 0xffff)</dd>
<dt><code>-v</code></dt>
<dd> Print more verbose output </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-srp_daemon/">srp_daemon</a></code>(1) </p>
<h2>AUTHORS</h2>
<dl>
<dt>Roland Dreier</dt>
<dd> &lt;<i>roland [at] kernel.org</i>&gt; </dd>
</dl>
