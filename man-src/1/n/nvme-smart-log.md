---
title: "nvme-smart-log(1)"
name: "nvme-smart-log"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-smart-log/"
---

<h2 class="name">NAME</h2>
 

 nvme-smart-log - Send NVMe SMART log page request, returns result and log 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme smart - log&lt;device&gt;[--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
                        [--raw - binary | -b]
</code></pre>

<h2>DESCRIPTION</h2>

 

 Retrieves the NVMe SMART log page from an NVMe device and provides the retuned structure. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). 

 On success, the returned f/w log structure may be returned in one of several ways depending on the option flags; the structure may parsed by the program and printed in a readable format or the raw buffer may be printed to stdout for another program to parse.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Retrieve the SMART log for the given nsid. This is optional and its success may depend on the device's capabilities to provide this log on a per-namespace basis (see the NVMe Identify Controller for this capability). The default nsid to use is 0xffffffff for the device global SMART log.</dl>
 

 -b, --raw-binary
<dl>
<dt>
<dd> Print the raw SMART log buffer to stdout.</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Print the SMART log page in a human readable format: 

<dl>
<dt>
<dd> <pre>
# nvme smart-log /dev/nvme0
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; Print the raw SMART log to a file: 

<dl>
<dt>
<dd> <pre>
# nvme smart-log /dev/nvme0 --raw-binary &gt; fw_log.raw
</pre></dl>
 

 It is probably a bad idea to not redirect stdout when using this mode.</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


