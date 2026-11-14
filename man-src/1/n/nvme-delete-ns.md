---
title: "nvme-delete-ns(1)"
name: "nvme-delete-ns"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-delete-ns/"
---

<h2 class="name">NAME</h2>
 

 nvme-delete-ns - Send NVMe Namespace Management delete namespace command, return result. 

<h2>SYNOPSIS</h2>

 

 <pre>
<i>nvme delete-ns</i> &lt;device&gt; [--namespace-id=&lt;nsid&gt; | -n &lt;nsid&gt;]
</pre>

<h2>DESCRIPTION</h2>

 

 For the NVMe device given, sends an nvme namespace management command to delete the requested namespace and provides the result. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). The '--namespace-id' option is mandatory.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> The namespace identifier to delete.</dl>

<h2>EXAMPLES</h2>

 

 No examples yet.

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


