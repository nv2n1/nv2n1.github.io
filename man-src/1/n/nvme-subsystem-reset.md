---
title: "nvme-subsystem-reset(1)"
name: "nvme-subsystem-reset"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-subsystem-reset/"
---

<h2 class="name">NAME</h2>
 

 nvme-subsystem-reset - Reset the nvme subsystem. 

<h2>SYNOPSIS</h2>

 

 <pre>
<i>nvme subsystem-reset</i> &lt;device&gt;
</pre>

<h2>DESCRIPTION</h2>

 

 Requests NVMe subsystem reset. The &lt;device&gt; param is mandatory and must be an NVMe character device (ex: /dev/nvme0).

<h2>OPTIONS</h2>

 

 None

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Resets the subsystem. 

<dl>
<dt>
<dd> <pre>
# nvme subsystem-reset /dev/nvme0
</pre></dl>
</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


