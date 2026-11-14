---
title: "nvme-get-ns-id(1)"
name: "nvme-get-ns-id"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-get-ns-id/"
---

<h2 class="name">NAME</h2>
 

 nvme-get-ns-id - Retrieves the namespace ID for an NVMe block device 

<h2>SYNOPSIS</h2>

 

 <pre>
<i>nvme get-ns-id</i> &lt;device&gt;
</pre>

<h2>DESCRIPTION</h2>

 

 Retrieves the namespace ID for an NVMe block device. The &lt;device&gt; param is mandatory and must be an NVMe block device (ex: /dev/nvme0n1).

<h2>OPTIONS</h2>

 

 None

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Shows the namespace id for the given block device: 

<dl>
<dt>
<dd> <pre>
# nvme get-ns-id /dev/nvme0n1
</pre></dl>
</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


