---
title: "ndctl-disable-region(1)"
name: "ndctl-disable-region"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndctl-disable-region/"
description: "ndctl-disable-region – disable the given region(s) and all descendant namespaces"
---

<h2 class="name">NAME</h2>
<p> ndctl-disable-region &#8211; disable the given region(s) and all descendant namespaces </p>
<h2>SYNOPSIS</h2>
<pre>
<i>ndctl disable-region</i> &lt;region&gt; [&lt;options&gt;]
</pre>
<h2>DESCRIPTION</h2>
<p> A generic REGION device is registered for each PMEM range or BLK-aperture set. LIBNVDIMM provides a built-in driver for these REGION devices. This driver is responsible for reconciling the aliased DPA mappings across all regions, parsing the LABEL, if present, and then emitting NAMESPACE devices with the resolved/exclusive DPA-boundaries for the nd_pmem or nd_blk device driver to consume.</p>
<h2>OPTIONS</h2>
<p> &lt;region&gt;</p>
<dl>
<dt>
<dd> A <i>regionX</i> device name, or a region id number. The keyword <i>all</i> can be specified to carry out the operation on every region in the system, optionally filtered by bus id (see &#8211;bus= option).</dl>
<p> -b, &#8211;bus=</p>
<dl>
<dt>
<dd> Enforce that the operation only be carried on devices that are attached to the given bus. Where <i>bus</i> can be a provider name or a bus id number.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ndctl-enable-region/">ndctl-enable-region</a></code>(1) </p>
<h2>Index</h2>
