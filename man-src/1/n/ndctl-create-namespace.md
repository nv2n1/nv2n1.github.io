---
title: "ndctl-create-namespace(1)"
name: "ndctl-create-namespace"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndctl-create-namespace/"
description: "ndctl-create-namespace – provision or reconfigure a namespace"
---

<h2 class="name">NAME</h2>
<p> ndctl-create-namespace &#8211; provision or reconfigure a namespace </p>
<h2>SYNOPSIS</h2>
<pre>
<i>ndctl create-namespace</i> [&lt;options&gt;]
</pre>
<h2>DESCRIPTION</h2>
<p> A REGION, after resolving DPA aliasing and LABEL specified boundaries, surfaces one or more &quot;namespace&quot; devices. The arrival of a &quot;namespace&quot; device currently triggers either the nd_blk or nd_pmem driver to load and register a disk/block device.</p>
<h2>EXAMPLES</h2>
<p> Create a maximally sized pmem namespace in <i>memory</i> mode </p>
<dl>
<dt>
<dd>
<pre>
ndctl create-namespace
</pre>
</dl>
<p> Convert namespace0.0 to <i>sector</i> mode </p>
<dl>
<dt>
<dd>
<pre>
ndctl create-namespace -f -e namespace0.0 --mode=sector
</pre>
</dl>
<h2>OPTIONS</h2>
<p> -t, &#8211;type=</p>
<dl>
<dt>
<dd> Create a <i>pmem</i> or <i>blk</i> namespace (subject to available capacity). A pmem namespace supports the DAX (direct access) capability to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) persistent memory directly into a process address space. A blk namespace access persistent memory through a block-window-aperture. Compared to pmem it supports a traditional storage error model (EIO on error rather than a cpu exception on a bad memory access), but it does not support DAX.</dl>
<p> -m, &#8211;mode=</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; &quot;raw&quot;: expose the namespace capacity directly with some limitations. Neither a raw pmem namepace nor raw blk namespace support sector atomicity by default (see &quot;sector&quot; mode below). A raw pmem namespace may have limited support for passing a DAX mapping to other syscalls. I.e. direct-I/O to/from a DAX buffer may fail for a pmem namespace in raw mode.</dl>
<dl>
<dt>
<dd> &bull; &quot;sector&quot; or &quot;safe&quot;: persistent memory, given that it is byte addressable, does not support sector atomicity. The problematic aspect of sector tearing is that most applications do not know they have a atomic sector update dependency. At least a disk rarely ever tears sectors and if it does it almost certainly returns a checksum error on access. Persistent memory devices will always tear and always silently. Until an application is audited to be robust in the presence of sector-tearing &quot;safe&quot; mode is recommended. This imposes some performance overhead and disables the DAX capability.</dl>
<dl>
<dt>
<dd> &bull; &quot;memory&quot;: A pmem namespace in this mode supports direct I/O to/from DAX mappings. Depending on the kernel this mode may come at the cost of allocating per-pmem-page metadata. If that allocation is required the capacity can be allocated from &quot;System RAM&quot; or from a reserved portion of pmem (see the &#8211;map= option).</dl>
<dl>
<dt>
<dd> &bull; &quot;dax&quot;: Device DAX is the device-centric analogue of Filesystem DAX (CONFIG_FS_DAX). It allows memory ranges to be allocated and mapped without need of an intervening file system. Device DAX is strict, precise and predictable. Specifically this interface: </p>
<dl>
<dt>
<dd> &bull; Guarantees fault granularity with respect to a given page size (pte, pmd, or pud) set at configuration time.</dl>
<dl>
<dt>
<dd> &bull; Enforces deterministic behavior by being strict about what fault scenarios are supported.</dl>
</dl>
</dl>
<p> -s, &#8211;size=</p>
<dl>
<dt>
<dd> For NVDIMM devices that support namespace labels, set the namespace size. Otherwise it defaults to the maximum size specified by platform firmware.</dl>
<p> -e, &#8211;reconfig=</p>
<dl>
<dt>
<dd> Reconfigure an existing namespace (change the mode, sector size, etc&#8230;). All namespace parameters, save uuid, default to the current attributes of the specified namespace. The namespace is then re-created with the specified modifications. The uuid is refreshed to a new value by default whenever the data layout of a namespace is changed, see &#8211;uuid= to set a specific uuid.</dl>
<p> -u, &#8211;uuid=</p>
<dl>
<dt>
<dd> This option is not recommended as a new uuid should be generated every time a namespace is (re-)created. For recovery scenarios however the uuid may be specified.</dl>
<p> -n, &#8211;name=</p>
<dl>
<dt>
<dd> For NVDIMM devices that support namespace labels, specify a human friendly name for a namespace. This name is available as device attribute for use in udev rules or elsewhere.</dl>
<p> -l, &#8211;sector-size</p>
<dl>
<dt>
<dd> Specify the logical sector size (LBA size) of the block storage device associated with a namespace.</dl>
<p> -M, &#8211;map=</p>
<dl>
<dt>
<dd> A pmem namespace in &quot;memory&quot; mode may require allocation of per-page metadata. The allocation can be drawn from either: </p>
<dl>
<dt>
<dd> &bull; &quot;mem&quot;: typical system memory</dl>
<dl>
<dt>
<dd> &bull; &quot;dev&quot;: persistent memory reserved from the namespace</dl>
</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Unless this option is specified a <i>reconfigure namespace</i> operation will fail if the namespace is presently active. Specifying &#8211;force causes the namespace to be disabled before reconfiguring.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Emit debug messages for the namespace creation process</dl>
<p> -r, &#8211;region=</p>
<dl>
<dt>
<dd> A <i>regionX</i> device name, or a region id number. The keyword <i>all</i> can be specified to carry out the operation on every region in the system, optionally filtered by bus id (see &#8211;bus= option).</dl>
<p> -b, &#8211;bus=</p>
<dl>
<dt>
<dd> Enforce that the operation only be carried on devices that are attached to the given bus. Where <i>bus</i> can be a provider name or a bus id number.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ndctl-zero-labels/">ndctl-zero-labels</a></code>(1), <code><a href="/docs/linux/man/1-ndctl-disable-namespace/">ndctl-disable-namespace</a></code>(1), <code><a href="/docs/linux/man/1-ndctl-enable-namespace/">ndctl-enable-namespace</a></code>(1), m[blue]<code>NVDIMM Namespace Specification</code>m[]<font SIZE="-2">[1]</font></p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> NVDIMM Namespace Specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://pmem.io/documents/NVDIMM_Namespace_Spec.pdf">http://pmem.io/documents/NVDIMM_Namespace_Spec.pdf</a></dl>
</dl>
<h2>Index</h2>
