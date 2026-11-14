---
title: "nvme-flush(1)"
name: "nvme-flush"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-flush/"
---

<h2 class="name">NAME</h2>
 

 nvme-flush - Flush command. 

<h2>SYNOPSIS</h2>

 

 <pre>
<i>nvme flush</i> &lt;device&gt; [--namespace-id=&lt;nsid&gt; | -n &lt;nsid&gt;]
</pre>

<h2>DESCRIPTION</h2>

 

 The Flush command shall commit data and metadata associated with the specified namespace(s) to nonvolatile media. The flush applies to all commands completed prior to the submission of the Flush command. The controller may also flush additional data and/or metadata from any namespace.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Specify the optional namespace id for this command. Defaults to 0xffffffff, indicating flush for all namespaces.</dl>

<h2>EXAMPLES</h2>

 

 No examples yet.

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


