---
title: "nvme-list-ns(1)"
name: "nvme-list-ns"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-list-ns/"
---

<h2 class="name">NAME</h2>
 

 nvme-list-ns - Send NVMe Identify List Namespaces, return result and structure 

<h2>SYNOPSIS</h2>

 

 <pre>
<i>nvme list-ns</i> &lt;device&gt; [--namespace-id=&lt;nsid&gt; | -n &lt;nsid&gt;]
</pre>

<h2>DESCRIPTION</h2>

 

 For the NVMe device given, sends an identify command for namespace list and provides the result and returned structure. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). If the starting namespace in the list always begins with 0 unless the '--namespace-id' option is given to override. 

 On success, the namespace array is printed for each index and nsid for a valid nsid.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Retrieve the identify list structure starting with the given nsid.</dl>

<h2>EXAMPLES</h2>

 

 No examples yet.

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


