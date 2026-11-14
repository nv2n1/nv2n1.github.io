---
title: "ndctl(1)"
name: "ndctl"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndctl/"
description: "ndctl – Manage \"libnvdimm\" subsystem devices (Non-volatile Memory)"
---

<h2 class="name">NAME</h2>
<p> ndctl &#8211; Manage &quot;libnvdimm&quot; subsystem devices (Non-volatile Memory) </p>
<h2>SYNOPSIS</h2>
<pre><code>
ndctl[--version][--help][OPTIONS] COMMAND[ARGS]
</code></pre>
<h2>OPTIONS</h2>
<p> -v, &#8211;version</p>
<dl>
<dt>
<dd> Display ndctl version.</dl>
<p> -h, &#8211;help</p>
<dl>
<dt>
<dd> Run ndctl help command.</dl>
<h2>DESCRIPTION</h2>
<p> ndctl is utility for managing the &quot;libnvdimm&quot; kernel subsystem. The &quot;libnvdimm&quot; subsystem defines a kernel device model and control message interface for platform NVDIMM resources like those defined by the ACPI 6.0 NFIT (NVDIMM Firmware Interface Table). Operations supported by the tool include, provisioning capacity (namespaces), as well as enumerating/enabling/disabling the devices (dimms, regions, namspaces) associated with an NVDIMM bus.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ndctl-create-namespace/">ndctl-create-namespace</a></code>(1), <code><a href="/docs/linux/man/1-ndctl-enable-region/">ndctl-enable-region</a></code>(1), <code><a href="/docs/linux/man/1-ndctl-disable-region/">ndctl-disable-region</a></code>(1), <code><a href="/docs/linux/man/1-ndctl-enable-namespace/">ndctl-enable-namespace</a></code>(1), <code><a href="/docs/linux/man/1-ndctl-disable-namespace/">ndctl-disable-namespace</a></code>(1), m[blue]<code>LIBNVDIMM Overview</code>m[]<font SIZE="-2">[1]</font>, m[blue]<code>NVDIMM Driver Writer&#8217;s Guide</code>m[]<font SIZE="-2">[2]</font></p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> LIBNVDIMM Overview</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.kernel.org/doc/Documentation/nvdimm/nvdimm.txt">https://www.kernel.org/doc/Documentation/nvdimm/nvdimm.txt</a></dl>
<dt> 2.</p>
<dd> NVDIMM Driver Writer&#8217;s Guide</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://pmem.io/documents/NVDIMM_Driver_Writers_Guide.pdf">http://pmem.io/documents/NVDIMM_Driver_Writers_Guide.pdf</a></dl>
</dl>
<h2>Index</h2>
